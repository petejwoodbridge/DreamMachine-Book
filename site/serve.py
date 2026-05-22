"""Tiny local preview server for the Dream Machine site.

The site is fully static, but it loads JSON via fetch() which needs an HTTP
origin (most browsers refuse file:// fetch). This serves the project root
on http://localhost:8765 so you can open http://localhost:8765/site/.

Run:
    python site/serve.py
"""
from __future__ import annotations

import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

PORT = 8765
ROOT = Path(__file__).resolve().parent.parent  # project root, so we can serve Book/build/*.pdf too


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):  # quiet
        sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))


def main() -> int:
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/site/"
        print(f">> Serving Dream Machine site at {url}")
        print(">> Ctrl-C to stop.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n>> Stopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
