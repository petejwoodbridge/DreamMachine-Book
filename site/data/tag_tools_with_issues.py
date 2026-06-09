#!/usr/bin/env python3
"""
tag_tools_with_issues.py
Reads all Dream Machine newsletter issues, extracts tool mentions from
Tool Spotlight sections and inline tool news, then tags each tool in
tools.json with the issue numbers it was mentioned in.

Strategy:
  - For issues with explicit "Tool Spotlight" sections (1-5, 30-32):
    extract **Bold** tool names and match against tools.json.
  - For ALL issues: scan link text and bold text for DISTINCTIVE tool name
    strings. "Distinctive" = the full primary name (before first "/") must
    appear as a phrase, OR a vendor+product pair must both appear.
  - Generic words ("music", "video", "google", "adobe", "ai", "studio",
    "model", etc.) are never used as standalone match tokens.

Run from the repo root:
    python site/data/tag_tools_with_issues.py
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent.parent
ISSUES_DIR = REPO_ROOT / "Dream Machine MD"
TOOLS_JSON = Path(__file__).parent / "tools.json"

# ---------------------------------------------------------------------------
# Generic / stop words that should never be a standalone match signal
# ---------------------------------------------------------------------------
STOP_WORDS = {
    "ai", "video", "music", "audio", "image", "model", "studio", "app",
    "tool", "platform", "google", "apple", "meta", "nvidia", "adobe",
    "microsoft", "sony", "amazon", "tencent", "open", "system", "new",
    "base", "pro", "plus", "lite", "free", "fast", "real", "live", "gen",
    "labs", "deep", "clip", "film", "game", "games", "media", "data",
    "voice", "flow", "work", "node", "edit", "film", "face", "head",
    "world", "scene", "code", "space", "text", "film", "team", "agent",
    "plugin", "maker", "chat", "cloud", "flux", "snap", "play", "cast",
    "byte", "link", "hub", "kit", "net", "set", "lab", "run", "mix",
}

# ---------------------------------------------------------------------------
# Load tools
# ---------------------------------------------------------------------------
with open(TOOLS_JSON, encoding="utf-8") as f:
    tools = json.load(f)

# ---------------------------------------------------------------------------
# For each tool, build a list of "primary match phrases" – the part of the
# name BEFORE the first "/" separator, stripped of vendor/parenthetical.
# Only phrases that contain at least one non-stop distinctive word.
# ---------------------------------------------------------------------------

def clean_phrase(s):
    """Lowercase, strip version numbers and parentheticals, trim."""
    s = s.lower().strip()
    # Remove parenthetical vendor: "(openai)" etc.
    s = re.sub(r"\s*\([^)]*\)", "", s)
    # Remove version numbers like "2.0", "v3", "3.1 flash"
    s = re.sub(r"\s+v?\d+(\.\d+)*\b", "", s)
    return s.strip()

def is_distinctive(phrase):
    """True if the phrase has at least one non-stop-word token >= 3 chars."""
    tokens = re.split(r"[\s\-/]", phrase)
    for t in tokens:
        t = t.strip().lower()
        if len(t) >= 3 and t not in STOP_WORDS:
            return True
    return False

# Build primary_phrases: list of (tool_index, phrase) sorted by phrase length
# (longest first for greedy matching)
primary_phrases = []  # (tool_idx, phrase, min_len)
for i, t in enumerate(tools):
    name = t["name"]
    # Primary phrase = first variant before "/"
    primary = re.split(r"\s*/\s*", name)[0]
    phrase = clean_phrase(primary)
    if phrase and is_distinctive(phrase) and len(phrase) >= 4:
        primary_phrases.append((i, phrase))

    # Also add additional distinctive variants (not the first)
    for variant in re.split(r"\s*/\s*", name)[1:]:
        vphrase = clean_phrase(variant)
        if vphrase and is_distinctive(vphrase) and len(vphrase) >= 5:
            primary_phrases.append((i, vphrase))

# Sort longest first so "Runway Gen-4.5" matches before "Runway"
primary_phrases.sort(key=lambda x: -len(x[1]))

# Build a fast lookup: first distinctive token -> list of (tool_idx, phrase)
token_to_entries = defaultdict(list)
for tidx, phrase in primary_phrases:
    tokens = [t for t in re.split(r"[\s\-/]", phrase) if len(t) >= 3 and t not in STOP_WORDS]
    if tokens:
        token_to_entries[tokens[0]].append((tidx, phrase))

# ---------------------------------------------------------------------------
# Tool Spotlight extraction: parse **Bold text** from a Spotlight section.
# ---------------------------------------------------------------------------

def spotlight_names_from_section(text):
    """Extract tool names (lowercased, before '—') from a Spotlight block."""
    names = []
    for m in re.finditer(r"\*\*([^*]+)\*\*", text):
        raw = m.group(1).strip()
        raw = re.split(r"\s*[—–\-]\s*", raw)[0].strip()
        raw = re.sub(r"\s*\([^)]*\)", "", raw)  # strip vendor
        raw = raw.lower().strip()
        if raw and len(raw) >= 3:
            names.append(raw)
    # Also capture lines starting with a word followed by newline+link pattern
    for m in re.finditer(r"^\*([^*\n]+)\*\s*$", text, re.MULTILINE):
        raw = m.group(1).strip().lower()
        if raw and len(raw) >= 3:
            names.append(raw)
    return names

def match_name_to_tool(name):
    """Try to match a spotlight name string to a tool index. Returns idx or None."""
    name_lc = name.lower()
    # 1. Exact substring: does this name appear in any tool's primary phrase?
    for tidx, phrase in primary_phrases:
        if name_lc == phrase:
            return tidx
        if name_lc in phrase or phrase in name_lc:
            return tidx
    # 2. Token overlap: at least 2 non-stop tokens in common
    name_tokens = {t for t in re.split(r"[\s\-/]", name_lc) if len(t) >= 3 and t not in STOP_WORDS}
    best = (0, None)
    for tidx, phrase in primary_phrases:
        phrase_tokens = {t for t in re.split(r"[\s\-/]", phrase) if len(t) >= 3 and t not in STOP_WORDS}
        overlap = len(name_tokens & phrase_tokens)
        if overlap > best[0]:
            best = (overlap, tidx)
    if best[0] >= 2:
        return best[1]
    if best[0] == 1 and name_tokens:
        # Single distinctive token match – only trust if that token is >= 5 chars
        shared = name_tokens & {t for t in re.split(r"[\s\-/]", primary_phrases[0][1]) if t not in STOP_WORDS}
        for tidx, phrase in primary_phrases:
            phrase_tokens = {t for t in re.split(r"[\s\-/]", phrase) if len(t) >= 3 and t not in STOP_WORDS}
            common = name_tokens & phrase_tokens
            if common and max(len(w) for w in common) >= 6:
                return tidx
    return None

# ---------------------------------------------------------------------------
# Inline text matching: find tool phrases appearing in a body of text.
# Uses phrase-level matching (not keyword-level) for precision.
# ---------------------------------------------------------------------------

def find_tools_in_text(text):
    """Return set of tool indices whose primary phrase appears in text."""
    text_lc = text.lower()
    found = set()
    # Get all distinctive first tokens present in the text
    candidate_tokens = {tok for tok in token_to_entries if tok in text_lc}
    for tok in candidate_tokens:
        for tidx, phrase in token_to_entries[tok]:
            # Check the full phrase appears in text (with word boundary on both ends)
            escaped = re.escape(phrase)
            if re.search(r"(?<!\w)" + escaped + r"(?!\w)", text_lc):
                found.add(tidx)
    return found

# ---------------------------------------------------------------------------
# Process each issue file
# ---------------------------------------------------------------------------

issue_tool_map = defaultdict(set)

for issue_num in range(1, 33):
    md_path = ISSUES_DIR / f"{issue_num}.md"
    if not md_path.exists():
        print(f"  [WARN] {md_path} not found, skipping")
        continue

    with open(md_path, encoding="utf-8") as f:
        content = f.read()

    # -----------------------------------------------------------------------
    # Strategy 1: Explicit Tool Spotlight section
    # -----------------------------------------------------------------------
    spotlight_match = re.search(
        r"(?:##+ )?Tool Spotlight(.*?)(?:^(?:##|\Z))",
        content,
        flags=re.IGNORECASE | re.DOTALL | re.MULTILINE,
    )
    if spotlight_match:
        stext = spotlight_match.group(1)
        for sname in spotlight_names_from_section(stext):
            idx = match_name_to_tool(sname)
            if idx is not None:
                issue_tool_map[issue_num].add(idx)
        # Also run inline matching on the spotlight section itself
        issue_tool_map[issue_num].update(find_tools_in_text(stext))

    # -----------------------------------------------------------------------
    # Strategy 2: Inline matching across ALL issues on link text + bold text
    # (these are the "Tool" mentions embedded in the newsletter body)
    # -----------------------------------------------------------------------
    link_texts = re.findall(r"\[([^\]]{4,80})\]\(", content)
    bold_texts = re.findall(r"\*\*([^*]{4,80})\*\*", content)
    combined = " ".join(link_texts + bold_texts)
    issue_tool_map[issue_num].update(find_tools_in_text(combined))

    print(f"Issue {issue_num:2d}: {len(issue_tool_map[issue_num]):3d} tools matched")

# ---------------------------------------------------------------------------
# Write issue numbers back into tools.json
# ---------------------------------------------------------------------------

tool_issues = defaultdict(set)
for issue_num, tool_indices in issue_tool_map.items():
    for tidx in tool_indices:
        tool_issues[tidx].add(issue_num)

matched_tools = 0
for i, t in enumerate(tools):
    if i in tool_issues:
        t["issues"] = sorted(tool_issues[i])
        matched_tools += 1
    else:
        t["issues"] = []

    # Rebuild the _s search index
    issue_str = " ".join(f"issue{n}" for n in t["issues"])
    t["_s"] = " ".join(filter(None, [
        t["name"].lower(),
        (t.get("vendor") or "").lower(),
        (t.get("blurb") or "").lower(),
        (t.get("category") or "").lower(),
        (t.get("layer") or "").lower(),
        " ".join(d.lower() for d in (t.get("disciplines") or [])),
        issue_str,
    ]))

print(f"\nTagged {matched_tools}/{len(tools)} tools with at least one issue reference.")

with open(TOOLS_JSON, "w", encoding="utf-8") as f:
    json.dump(tools, f, ensure_ascii=False, indent=2)

print(f"Written to {TOOLS_JSON}")

# Regenerate bundle.js from all JSON files on disk so it reflects tagged tools
BUNDLE_JS = TOOLS_JSON.parent / "bundle.js"
JSON_NAMES = [
    "tools", "categories", "issues", "editions",
    "use-cases", "chapters", "issues-and-challenges", "site",
]
bundle_data = {}
for name in JSON_NAMES:
    p = TOOLS_JSON.parent / f"{name}.json"
    if p.exists():
        bundle_data[name] = json.loads(p.read_text(encoding="utf-8"))

bundle_js = "// Auto-generated by build_site.py / tag_tools_with_issues.py — do not edit\n"
bundle_js += "window.DM_DATA = " + json.dumps(bundle_data, ensure_ascii=False) + ";\n"
BUNDLE_JS.write_text(bundle_js, encoding="utf-8")
print(f"Regenerated bundle.js ({round(len(bundle_js.encode()) / 1024)} KB)")

print("\nTop 30 tools by issue count:")
top = sorted(
    [(len(t["issues"]), t["name"]) for t in tools if t["issues"]],
    reverse=True,
)[:30]
for cnt, name in top:
    print(f"  {cnt:2d}  {name[:65]}")

print(f"\nDistribution:")
from collections import Counter
dist = Counter(len(t["issues"]) for t in tools)
for k in sorted(dist):
    print(f"  {k:2d} issues: {dist[k]:3d} tools")

