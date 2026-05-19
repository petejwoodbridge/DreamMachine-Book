"""Rebuild the PDF whenever any source file in Book/ changes.

Uses Python's stdlib only — no extra installs. Polls modification times every
second and rebuilds whenever something changes. Debounces multi-file saves so a
batch edit produces one rebuild, not ten.

Run:
    python Book/watch_book.py

Stop with Ctrl-C.
"""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILD_SCRIPT = ROOT / "build_book.py"

# What we watch — every .md, .css, and .png under Book/ except the generated outputs
def collect_sources() -> dict[Path, float]:
    snapshot: dict[Path, float] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if "build" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".css", ".png", ".py"}:
            continue
        if path.name == "watch_book.py":
            continue
        try:
            snapshot[path] = path.stat().st_mtime
        except OSError:
            pass
    return snapshot


def build_once() -> bool:
    result = subprocess.run([sys.executable, str(BUILD_SCRIPT)])
    return result.returncode == 0


DEBOUNCE_SECONDS = 1.0
POLL_INTERVAL = 1.0


def main() -> int:
    print(f">> Watching {ROOT} for changes (Ctrl-C to stop).")
    print(">> Initial build...")
    build_once()

    last_snapshot = collect_sources()
    last_change_at: float | None = None

    while True:
        try:
            time.sleep(POLL_INTERVAL)
            snapshot = collect_sources()
            changed = []
            for path, mtime in snapshot.items():
                if last_snapshot.get(path) != mtime:
                    changed.append(path)
            for path in set(last_snapshot) - set(snapshot):
                changed.append(path)

            if changed:
                last_change_at = time.time()
                last_snapshot = snapshot
                names = ", ".join(p.name for p in changed[:3])
                more = "" if len(changed) <= 3 else f" (+{len(changed)-3} more)"
                print(f">> Change detected: {names}{more}")

            if last_change_at is not None and (time.time() - last_change_at) >= DEBOUNCE_SECONDS:
                last_change_at = None
                print(">> Rebuilding...")
                ok = build_once()
                print(">> Done." if ok else ">> Build failed.")

        except KeyboardInterrupt:
            print("\n>> Stopped watching.")
            return 0


if __name__ == "__main__":
    sys.exit(main())
