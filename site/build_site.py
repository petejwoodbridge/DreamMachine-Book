"""Build the Dream Machine website data.

Parses:
  * Book/16_The_Tools.md             -> data/tools.json, data/categories.json
  * Dream Machine MD/*.md            -> data/issues.json, data/editions.json
  * Book/00a_Reader_Paths.md         -> data/use-cases.json
  * Book/0..18 chapter files         -> data/chapters.json, data/issues_topics.json
  * Book/build_book.py (EDITION_SLUG)-> data/site.json (latest edition pointer)

Writes the JSON catalogs under site/data/ so the static HTML/JS in site/ can
render the toolkit, use-cases, issues & challenges and newsletter archive.

Run:
    python site/build_site.py

Idempotent. Safe to run on every book rebuild.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DATA = SITE / "data"
BOOK = ROOT / "Book"
ISSUES_MD = ROOT / "Dream Machine MD"

DATA.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

URL_RE = re.compile(r"https?://[^\s<>)\]]+")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_LEAD_RE = re.compile(r"^\s*[-*]\s*\*\*(?P<name>[^*]+?)\*\*\s*(?P<rest>.*)$")
SUB_BULLET_RE = re.compile(r"^\s{2,}[-*]\s*\*\*(?P<name>[^*]+?)\*\*\s*(?P<rest>.*)$")
H4_RE = re.compile(r"^####\s+(?P<title>.+?)\s*$")
H3_RE = re.compile(r"^###\s+(?P<title>.+?)\s*$")


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "untitled"


def clean_blurb(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^[—–\-:\s]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_first_url(text: str) -> str | None:
    # Prefer markdown link target; fall back to bare URL
    m = MD_LINK_RE.search(text)
    if m:
        return m.group(2)
    m = URL_RE.search(text)
    if m:
        return m.group(0).rstrip(".,;:)")
    return None


# ---------------------------------------------------------------------------
# Chapter 16 -> tools.json
# ---------------------------------------------------------------------------

# Map raw "#### Header" categories from Chapter 16 to display-facing
# categories and the broader discipline tags we want on each tool.
CATEGORY_MAP: dict[str, dict] = {
    "Foundation models / LLMs": {
        "slug": "foundation",
        "layer": "Foundation",
        "disciplines": ["All"],
        "icon": "brain",
    },
    "AI video models": {
        "slug": "video",
        "layer": "Modality",
        "disciplines": ["Film", "Marketing", "Animation"],
        "icon": "video",
    },
    "AI image models / tools": {
        "slug": "image",
        "layer": "Modality",
        "disciplines": ["Design", "Marketing", "Film", "Animation"],
        "icon": "image",
    },
    "AI music / audio tools": {
        "slug": "music-audio",
        "layer": "Modality",
        "disciplines": ["Music"],
        "icon": "music",
    },
    "3D, world models and spatial": {
        "slug": "3d-world",
        "layer": "Modality",
        "disciplines": ["Games", "Film", "Animation", "Immersive"],
        "icon": "cube",
    },
    "Voice, avatar, digital human": {
        "slug": "voice-avatar",
        "layer": "Modality",
        "disciplines": ["Film", "Marketing", "Music"],
        "icon": "face",
    },
    "Agent platforms and orchestration": {
        "slug": "agents",
        "layer": "Agent",
        "disciplines": ["All"],
        "icon": "bolt",
    },
    "Legacy creative software, AI-augmented": {
        "slug": "legacy",
        "layer": "Legacy software",
        "disciplines": ["All"],
        "icon": "layers",
    },
    "AI-native creative studios and apps": {
        "slug": "studios",
        "layer": "Studios & apps",
        "disciplines": ["Film", "Animation"],
        "icon": "studio",
    },
    "Games-development AI": {
        "slug": "games",
        "layer": "Modality",
        "disciplines": ["Games"],
        "icon": "joystick",
    },
    "Marketing and advertising AI": {
        "slug": "marketing",
        "layer": "Native",
        "disciplines": ["Marketing"],
        "icon": "megaphone",
    },
    "Open-source ecosystem and infrastructure": {
        "slug": "open-source",
        "layer": "Open source",
        "disciplines": ["All"],
        "icon": "code",
    },
    "ComfyUI ecosystem — nodes, extensions and workflows": {
        "slug": "comfyui",
        "layer": "Open source",
        "disciplines": ["All"],
        "icon": "nodes",
    },
    "LoRAs, fine-tuning and training": {
        "slug": "loras",
        "layer": "Open source",
        "disciplines": ["All"],
        "icon": "spark",
    },
    "Provenance, watermarking and detection": {
        "slug": "provenance",
        "layer": "Infrastructure",
        "disciplines": ["All"],
        "icon": "shield",
    },
    "Consumer surfaces and distribution platforms": {
        "slug": "consumer",
        "layer": "Consumer",
        "disciplines": ["All"],
        "icon": "phone",
    },
    "Studios, programmes, festivals and institutional infrastructure": {
        "slug": "institutions",
        "layer": "Institutions",
        "disciplines": ["All"],
        "icon": "building",
    },
    "Techniques, methods and recurring workflows": {
        "slug": "techniques",
        "layer": "Technique",
        "disciplines": ["All"],
        "icon": "compass",
    },
}


def parse_tools_chapter() -> tuple[list[dict], list[dict]]:
    text = (BOOK / "16_The_Tools.md").read_text(encoding="utf-8")
    lines = text.splitlines()

    tools: list[dict] = []
    categories: list[dict] = []

    # Only consume the catalogued section. The chapter starts the reference
    # inventory under "### The complete toolchain: a categorised reference".
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("### The complete toolchain"):
            start_idx = i
            break
    if start_idx is None:
        print("WARN: could not find reference inventory section in 16_The_Tools.md")
        return tools, categories

    current_cat = None
    current_cat_meta = None
    pending_parent = None  # For Adobe Sneaks-style sub-bullets

    for raw in lines[start_idx:]:
        # Closing section ("### How to build a toolchain you can defend").
        # Use strict "### " match so we don't false-trigger on "####".
        if raw.startswith("### ") and "The complete toolchain" not in raw:
            break

        h4 = H4_RE.match(raw)
        if h4:
            current_cat = h4.group("title").strip()
            meta = CATEGORY_MAP.get(current_cat)
            if meta is None:
                # Fall back: infer
                meta = {
                    "slug": slugify(current_cat),
                    "layer": "Other",
                    "disciplines": ["All"],
                    "icon": "dot",
                }
            current_cat_meta = meta
            categories.append({
                "name": current_cat,
                "slug": meta["slug"],
                "layer": meta["layer"],
                "disciplines": meta["disciplines"],
                "icon": meta["icon"],
                "count": 0,
            })
            pending_parent = None
            continue

        # Sub-bullet (indented) of an Adobe-Sneaks-style nested entry
        sb = SUB_BULLET_RE.match(raw)
        if sb and current_cat_meta and pending_parent:
            name = sb.group("name").strip()
            rest = clean_blurb(sb.group("rest"))
            url = extract_first_url(rest)
            tool = {
                "name": name,
                "blurb": rest,
                "category": current_cat,
                "category_slug": current_cat_meta["slug"],
                "layer": current_cat_meta["layer"],
                "disciplines": current_cat_meta["disciplines"],
                "url": url,
                "parent": pending_parent,
            }
            tools.append(tool)
            categories[-1]["count"] += 1
            continue

        m = BOLD_LEAD_RE.match(raw)
        if m and current_cat_meta:
            name = m.group("name").strip()
            rest = clean_blurb(m.group("rest"))
            url = extract_first_url(rest)
            # If this bullet ends with a colon (or its rest is empty/short),
            # it's the parent of indented sub-bullets (Adobe Sneaks).
            pending_parent = name if rest.endswith(":") or len(rest) < 4 else None
            tool = {
                "name": name,
                "blurb": rest,
                "category": current_cat,
                "category_slug": current_cat_meta["slug"],
                "layer": current_cat_meta["layer"],
                "disciplines": current_cat_meta["disciplines"],
                "url": url,
                "parent": None,
            }
            tools.append(tool)
            categories[-1]["count"] += 1
            continue

    # Build a clean disciplines facet by expanding "All" into the full set
    all_disciplines = ["Film", "TV", "Music", "Games", "Animation",
                       "Design", "Marketing", "Immersive"]
    for t in tools:
        if t["disciplines"] == ["All"]:
            t["disciplines"] = all_disciplines.copy()

    return tools, categories


# ---------------------------------------------------------------------------
# Newsletter issues -> issues.json, editions.json
# ---------------------------------------------------------------------------

# Map raw issue section headers (#### Film, TV...) to our discipline taxonomy
NEWS_SECTION_MAP: dict[str, list[str]] = {
    "film": ["Film", "TV", "Animation"],
    "tv": ["TV", "Film"],
    "broadcast": ["TV", "Film"],
    "animation": ["Animation"],
    "games": ["Games"],
    "immersive": ["Immersive", "Games"],
    "interactive": ["Games", "Immersive"],
    "music": ["Music"],
    "sound": ["Music"],
    "audio": ["Music"],
    "marketing": ["Marketing"],
    "advertising": ["Marketing"],
    "tools": ["Tools"],
    "tool spotlight": ["Tools"],
    "tool": ["Tools"],
    "other": ["Other"],
    "general": ["Other"],
}


def map_news_section(header: str) -> list[str]:
    h = header.lower()
    tags: set[str] = set()
    for keyword, mapped in NEWS_SECTION_MAP.items():
        if keyword in h:
            for m in mapped:
                tags.add(m)
    return sorted(tags) or ["Other"]


def parse_issue_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    issue_num = int(path.stem)
    title = ""
    date_str = ""
    sections: list[dict] = []
    tool_spotlight: list[dict] = []
    all_urls: list[str] = []

    # Extract title (first non-empty after `# Dream Machine — Issue N`)
    for line in lines:
        if line.strip().startswith("DREAM MACHINE") and "{" in line:
            # e.g. "DREAM MACHINE | Creative AI News & Insight { May 2026 - Issue 30 }"
            m = re.search(r"\{\s*([^}]+?)\s*\}", line)
            if m:
                title = m.group(1).strip()
            break

    # Extract date from typical "21/05/2026, 06:48" pattern
    for line in lines:
        m = re.search(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b", line)
        if m:
            d, mo, y = m.groups()
            try:
                date_str = datetime(int(y), int(mo), int(d)).strftime("%Y-%m-%d")
            except ValueError:
                pass
            break

    # Walk H3/H4 sections to bucket bullet news items by topic
    current_section: dict | None = None
    in_spotlight = False
    in_url_dump = False

    for raw in lines:
        stripped = raw.strip()
        if stripped.startswith("## All embedded URLs"):
            in_url_dump = True
            continue
        if in_url_dump:
            if stripped.startswith("- "):
                url = stripped[2:].strip()
                if url.startswith("http"):
                    all_urls.append(url)
            continue

        # H3 ("News this Week" / "Tool Spotlight" group headers)
        if H3_RE.match(stripped):
            h = H3_RE.match(stripped).group("title").lower()
            in_spotlight = "tool" in h or "spotlight" in h
            continue

        # H4 (Film/Games/Music/etc.)
        h4 = H4_RE.match(stripped)
        if h4:
            title4 = h4.group("title").strip()
            tags = map_news_section(title4)
            current_section = {
                "heading": title4,
                "tags": tags,
                "items": [],
            }
            sections.append(current_section)
            continue

        # Bullets — extract news items
        if stripped.startswith("- "):
            line_text = stripped[2:].strip()
            url = extract_first_url(line_text)
            # Strip the [LINK](url) suffix if present for cleaner reading
            text_clean = re.sub(r"\s*\[LINK\]\([^)]+\)\s*$", "", line_text)
            text_clean = MD_LINK_RE.sub(r"\1", text_clean).strip()
            text_clean = re.sub(r"\s+", " ", text_clean)
            item = {"text": text_clean, "url": url}
            if in_spotlight:
                tool_spotlight.append(item)
            elif current_section is not None:
                current_section["items"].append(item)

    # Compute total counts
    news_count = sum(len(s["items"]) for s in sections)

    return {
        "issue": issue_num,
        "title": title or f"Dream Machine — Issue {issue_num}",
        "date": date_str,
        "sections": sections,
        "tool_spotlight": tool_spotlight,
        "all_urls": all_urls,
        "news_count": news_count,
        "spotlight_count": len(tool_spotlight),
        "path": f"Dream Machine MD/{path.name}",
    }


def parse_all_issues() -> list[dict]:
    files = sorted(
        ISSUES_MD.glob("*.md"),
        key=lambda p: int(p.stem) if p.stem.isdigit() else 0,
    )
    return [parse_issue_file(p) for p in files]


# ---------------------------------------------------------------------------
# Reader Paths -> use-cases.json
# ---------------------------------------------------------------------------

# Curated icons + colour accents per persona. The persona slug/headline is
# derived from the H3 in 00a_Reader_Paths.md so it stays in sync if the
# book is rewritten.
PERSONA_ACCENTS = {
    "working creative": {"icon": "user", "accent": "pink"},
    "studio": {"icon": "building", "accent": "cyan"},
    "policy": {"icon": "scale", "accent": "purple"},
    "music industry": {"icon": "music", "accent": "pink"},
    "film": {"icon": "film", "accent": "cyan"},
    "class": {"icon": "book", "accent": "green"},
}


def parse_reader_paths() -> list[dict]:
    text = (BOOK / "00a_Reader_Paths.md").read_text(encoding="utf-8")
    paths: list[dict] = []

    # Split on H3 sections, each one is a persona
    blocks = re.split(r"\n###\s+", "\n" + text)
    for block in blocks[1:]:
        head, _, body = block.partition("\n")
        headline = head.strip()
        body = body.strip()
        # Find chapter references like **Chapter 7 (Title)**
        chapter_refs = re.findall(
            r"\*\*(Chapter\s+\d+[^*]*?|Foreword|Epilogue|Appendix\s+[^*]+?)\*\*",
            body,
        )
        # De-dupe preserving order
        seen, ch_list = set(), []
        for c in chapter_refs:
            key = c.strip()
            if key not in seen:
                seen.add(key)
                ch_list.append(key)

        # Pick an accent based on keywords
        meta = {"icon": "spark", "accent": "pink"}
        for k, v in PERSONA_ACCENTS.items():
            if k in headline.lower():
                meta = v
                break

        paths.append({
            "headline": headline,
            "slug": slugify(headline)[:60],
            "icon": meta["icon"],
            "accent": meta["accent"],
            # Light cleanup: collapse double spaces, drop markdown bold
            "body": re.sub(r"\*\*([^*]+)\*\*", r"\1", body).strip(),
            "chapters": ch_list,
        })

    return paths


# ---------------------------------------------------------------------------
# Chapters -> chapters.json + curated Issues & Challenges
# ---------------------------------------------------------------------------

# The structural "issues & challenges" the book argues are reshaping the
# field. Each one is anchored to the chapter that makes the case and the
# tags it overlaps with in the news/tool data. Curated (not auto-derived)
# because the framing is editorial — but the chapter file is the source of
# truth for the descriptive blurb, which we pull from each chapter's lead.
ISSUES_CATALOG = [
    {
        "slug": "sora-day",
        "title": "The Day Sora Landed",
        "chapter": "01_The_Day_Sora_Landed.md",
        "blurb": "The Sept 2025 Sora 2 launch as the watershed moment that opens the period — and the first stress test of the new audience contract.",
        "tags": ["Film", "Tools", "Consumer"],
        "accent": "pink",
        "icon": "rocket",
    },
    {
        "slug": "history-of-resistance",
        "title": "A History of Resistance",
        "chapter": "02_A_History_of_Resistance.md",
        "blurb": "Every prior technological re-platforming of the creative industries — and the historical pattern this transition is inside.",
        "tags": ["Strategy"],
        "accent": "cyan",
        "icon": "compass",
    },
    {
        "slug": "agency-continuum",
        "title": "The Human–AI Agency Continuum",
        "chapter": "03_The_Human_AI_Agency_Continuum.md",
        "blurb": "A practitioner's framework for where a piece of creative work sits on the line from fully-human to fully-machine, and why that choice is now an explicit one.",
        "tags": ["Strategy", "Craft"],
        "accent": "purple",
        "icon": "scale",
    },
    {
        "slug": "dead-internet-living-web",
        "title": "Dead Internet, Living Web",
        "chapter": "04_Dead_Internet_Living_Web.md",
        "blurb": "The split between the synthetic-content layer eating the public web and the human-verified layer being rebuilt underneath it.",
        "tags": ["Audience", "Platforms"],
        "accent": "pink",
        "icon": "globe",
    },
    {
        "slug": "slop-ceiling",
        "title": "The Slop Ceiling",
        "chapter": "05_The_Slop_Ceiling.md",
        "blurb": "Why undifferentiated AI output asymptotes to a quality plateau the audience already discounts — and what sits above it.",
        "tags": ["Music", "Audience"],
        "accent": "cyan",
        "icon": "ceiling",
    },
    {
        "slug": "the-88-percent",
        "title": "The 88% — The Copyright Crisis",
        "chapter": "06_The_88_Percent.md",
        "blurb": "The UK consultation, the Petrillo-template levy mechanism, and the rights-and-licensing fight that will define the legal layer of the transition.",
        "tags": ["Policy", "Music", "Legal"],
        "accent": "purple",
        "icon": "scale",
    },
    {
        "slug": "studios-decide",
        "title": "The Studios Decide",
        "chapter": "07_The_Studios_Decide.md",
        "blurb": "The four strategic positions the studios, labels and agencies have chosen between — and the trap the legacy industries built for themselves.",
        "tags": ["Strategy", "Film", "TV"],
        "accent": "cyan",
        "icon": "building",
    },
    {
        "slug": "worlds-not-pictures",
        "title": "Worlds, Not Pictures",
        "chapter": "08_Worlds_Not_Pictures.md",
        "blurb": "World models replacing flat video as the default creative medium of the next decade — and the spatial pipeline that is already shipping.",
        "tags": ["Games", "Immersive", "Film"],
        "accent": "pink",
        "icon": "cube",
    },
    {
        "slug": "ai-in-everything",
        "title": "AI in Everything, Everywhere",
        "chapter": "09_AI_In_Everything.md",
        "blurb": "The absorption pattern: how the legacy creative-software vendors quietly became the dominant AI-creative platforms by burying capability inside the apps people already used.",
        "tags": ["Platforms", "Tools"],
        "accent": "cyan",
        "icon": "layers",
    },
    {
        "slug": "newly-possible",
        "title": "What Is Newly Possible",
        "chapter": "10_What_Is_Newly_Possible.md",
        "blurb": "The new categories of creative work the transition has opened up — what you can build now that you literally could not in 2024.",
        "tags": ["Craft", "Tools"],
        "accent": "purple",
        "icon": "spark",
    },
    {
        "slug": "the-orchestrator",
        "title": "The Orchestrator",
        "chapter": "11_The_Orchestrator.md",
        "blurb": "The new working role of the period — briefing, allocating, judging and integrating across an agent fleet — and the AI Literacy Premium.",
        "tags": ["Craft", "Agents"],
        "accent": "pink",
        "icon": "bolt",
    },
    {
        "slug": "authenticity-premium",
        "title": "Authenticity as the New Scarcity",
        "chapter": "12_Authenticity_New_Scarcity.md",
        "blurb": "Why verifiably-human, verifiably-provenanced creative work commands a structural premium — and how the provenance stack is being built.",
        "tags": ["Provenance", "Audience"],
        "accent": "cyan",
        "icon": "shield",
    },
    {
        "slug": "coordination-collapse",
        "title": "Coordination Collapse",
        "chapter": "13_Coordination_Collapse.md",
        "blurb": "Why traditional collective bargaining, industry standards and inter-studio coordination are failing under the speed of the transition — and what organisations should do.",
        "tags": ["Labour", "Policy", "Strategy"],
        "accent": "purple",
        "icon": "scale",
    },
    {
        "slug": "new-jobs",
        "title": "The New Jobs",
        "chapter": "14_The_New_Jobs.md",
        "blurb": "The labour-market evidence: which jobs are appearing, which are restructuring, which are vanishing, and the policy frame the data demands.",
        "tags": ["Labour", "Policy"],
        "accent": "pink",
        "icon": "user",
    },
    {
        "slug": "choosing-the-future",
        "title": "Choosing the Future",
        "chapter": "15_Choosing_the_Future.md",
        "blurb": "The four principles the book argues for, and what working creatives should do on Monday morning.",
        "tags": ["Strategy", "Craft"],
        "accent": "cyan",
        "icon": "compass",
    },
    {
        "slug": "five-years",
        "title": "Five Years Inside the Dream Machine",
        "chapter": "17_Five_Years_Inside_the_Dream_Machine.md",
        "blurb": "A speculative future-cast: what the creative economy looks like in 2031 if the current trajectory holds, and the off-ramps that are still available.",
        "tags": ["Strategy", "Future"],
        "accent": "purple",
        "icon": "rocket",
    },
]


def parse_chapters() -> list[dict]:
    chapter_files = [
        "00_Foreword.md", "00a_Reader_Paths.md",
        "01_The_Day_Sora_Landed.md", "02_A_History_of_Resistance.md",
        "03_The_Human_AI_Agency_Continuum.md", "04_Dead_Internet_Living_Web.md",
        "05_The_Slop_Ceiling.md", "06_The_88_Percent.md",
        "07_The_Studios_Decide.md", "08_Worlds_Not_Pictures.md",
        "09_AI_In_Everything.md", "10_What_Is_Newly_Possible.md",
        "11_The_Orchestrator.md", "12_Authenticity_New_Scarcity.md",
        "13_Coordination_Collapse.md", "14_The_New_Jobs.md",
        "15_Choosing_the_Future.md", "16_The_Tools.md",
        "17_Five_Years_Inside_the_Dream_Machine.md", "18_Epilogue.md",
    ]
    appendices = [
        "A1_Appendix_Quantitative_Anatomy.md", "A2_Glossary.md",
        "A3_Bibliography_by_Topic.md", "A4_Deep_Dive_Shadow_AI.md",
        "A5_Deep_Dive_Adoption_Dynamics.md", "A6_Deep_Dive_AI_Stigma.md",
        "A7_Deep_Dive_AI_Intent.md", "A8_Source_Index.md",
    ]
    out = []
    for name in chapter_files + appendices:
        p = BOOK / name
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        # Extract H1 title and (optional) H2 subtitle
        title = ""
        subtitle = ""
        for line in lines:
            if line.startswith("# ") and not title:
                title = line[2:].strip()
            elif line.startswith("## ") and title and not subtitle:
                subtitle = line[3:].strip()
                break
        out.append({
            "file": name,
            "title": title,
            "subtitle": subtitle,
            "path": f"Book/{name}",
            "is_appendix": name.startswith("A") and "_" in name,
        })
    return out


# ---------------------------------------------------------------------------
# Edition pointer (from build_book.py)
# ---------------------------------------------------------------------------

def extract_edition_slug() -> tuple[str, str]:
    text = (BOOK / "build_book.py").read_text(encoding="utf-8")
    slug = ""
    date_human = ""
    m = re.search(r'EDITION_SLUG\s*=\s*"([^"]+)"', text)
    if m:
        slug = m.group(1)
    m = re.search(r'DATE\s*=\s*"([^"]+)"', text)
    if m:
        date_human = m.group(1)
    return slug, date_human


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

VENDOR_LEAD_RE = re.compile(r"^\(([^)]+)\)\s*[—\-:]?\s*")


DOMAIN_RE = re.compile(r"https?://(?:www\.)?([^/\s]+)")
# Strip common suffixes when we use the domain as a search key
DOMAIN_SUFFIXES = (".com", ".org", ".net", ".io", ".ai", ".co", ".uk",
                   ".dev", ".app", ".ml", ".tv", ".tech", ".studio", ".tools")


def domain_stem(url: str) -> str | None:
    m = DOMAIN_RE.match(url or "")
    if not m:
        return None
    host = m.group(1).lower()
    parts = host.split(".")
    # Skip if it's a news site or generic media host - we want product domains
    skip_hosts = {"linkedin", "twitter", "youtube", "github", "medium",
                  "techcrunch", "variety", "billboard", "rollingstone",
                  "bloomberg", "forbes", "hollywoodreporter", "wired",
                  "theguardian", "nytimes", "wsj", "bbc", "verge",
                  "businessinsider", "siliconangle", "musictech",
                  "musically", "musicbusinessworldwide", "thedrum",
                  "macrumors", "kotaku", "pcgamer", "gamesindustry",
                  "videogameschronicle", "yougov", "fortune", "cartoonbrew",
                  "huggingface", "newsroom"}
    # Use the second-to-last label as the brand (e.g. tamber.ai -> tamber)
    if len(parts) >= 2:
        brand = parts[-2] if parts[-1] in [s.lstrip(".") for s in DOMAIN_SUFFIXES] else parts[0]
        # blog.google -> google ; deepmind.google -> deepmind
        if brand in skip_hosts:
            return None
        return brand
    return None


def enrich_tools(tools: list[dict], issues: list[dict]) -> None:
    """Mutate tools in place: split vendor out of the blurb, attach a URL
    cross-referenced from newsletter URLs whose domain matches the tool name,
    and add a lowercase searchable blob.
    """
    # Build domain-stem -> URL map from EVERY URL across all issues
    # (including the per-issue "All embedded URLs" footer dump)
    stem_to_url: dict[str, str] = {}

    def harvest(url: str) -> None:
        stem = domain_stem(url)
        if stem and stem not in stem_to_url:
            stem_to_url[stem] = url

    # Build a single concatenated lowercase text blob per issue for tagging
    issue_text: dict[int, str] = {}

    for issue in issues:
        chunks: list[str] = []
        for url in issue.get("all_urls", []):
            harvest(url)
        for item in issue.get("tool_spotlight", []):
            chunks.append(item.get("text", ""))
            if item.get("url"):
                harvest(item["url"])
        for sec in issue.get("sections", []):
            for item in sec.get("items", []):
                chunks.append(item.get("text", ""))
                if item.get("url"):
                    harvest(item["url"])
        issue_text[issue["issue"]] = " ".join(chunks).lower()

    for t in tools:
        blurb = t["blurb"]
        vendor = None
        vm = VENDOR_LEAD_RE.match(blurb)
        if vm:
            vendor = vm.group(1).strip()
            blurb = blurb[vm.end():]
        blurb = re.sub(r"^[—\-]\s*", "", blurb).strip()
        t["vendor"] = vendor
        t["blurb"] = blurb

        # Cross-reference URL by domain stem
        name_words = re.findall(r"[A-Za-z][A-Za-z0-9]{2,}", t["name"])
        if not t.get("url"):
            for w in name_words:
                key = w.lower()
                if key in stem_to_url:
                    t["url"] = stem_to_url[key]
                    break

        # Tag which newsletter issues mention this tool. Use the longest
        # name token (the most distinctive part) as the lookup key.
        primary = max(name_words, key=len) if name_words else t["name"]
        primary = primary.lower()
        if len(primary) >= 4:  # avoid noisy short tokens
            mentioned_in = [iss_num for iss_num, txt in issue_text.items()
                            if primary in txt]
            t["issues"] = sorted(mentioned_in)
        else:
            t["issues"] = []

        # Searchable blob (lowercase) used by client-side filter
        t["_s"] = " ".join([
            t["name"], t.get("vendor") or "", t["blurb"], t["category"],
            t["layer"], " ".join(t["disciplines"])
        ]).lower()


def main() -> int:
    print(">> Parsing newsletter issues -> issues.json + editions.json")
    issues = parse_all_issues()
    print(f"   {len(issues)} issues")

    print(">> Parsing Chapter 16 -> tools.json + categories.json")
    tools, categories = parse_tools_chapter()
    enrich_tools(tools, issues)
    enriched_url_count = sum(1 for t in tools if t.get("url"))
    print(f"   {len(tools)} tools across {len(categories)} categories ({enriched_url_count} with URLs)")
    (DATA / "tools.json").write_text(
        json.dumps(tools, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (DATA / "categories.json").write_text(
        json.dumps(categories, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    (DATA / "issues.json").write_text(
        json.dumps(issues, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    editions = [{
        "issue": i["issue"],
        "title": i["title"],
        "date": i["date"],
        "news_count": i["news_count"],
        "spotlight_count": i["spotlight_count"],
    } for i in issues]
    editions.sort(key=lambda x: x["issue"], reverse=True)
    (DATA / "editions.json").write_text(
        json.dumps(editions, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(">> Parsing Reader Paths -> use-cases.json")
    use_cases = parse_reader_paths()
    (DATA / "use-cases.json").write_text(
        json.dumps(use_cases, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(">> Parsing chapters -> chapters.json + issues-and-challenges.json")
    chapters = parse_chapters()
    (DATA / "chapters.json").write_text(
        json.dumps(chapters, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (DATA / "issues-and-challenges.json").write_text(
        json.dumps(ISSUES_CATALOG, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(">> Writing site metadata")
    slug, date_human = extract_edition_slug()
    site_meta = {
        "title": "DREAM MACHINE",
        "tagline": "A creative's guide to AI",
        "edition_slug": slug,
        "edition_date": date_human,
        "edition_pdf": f"Book/build/Dream_Machine_{slug}.pdf" if slug else None,
        "newsletter_url": "https://www.linkedin.com/newsletters/dream-machine-creative-ai-7379776527871381505/",
        "podcast_url": "https://open.spotify.com/show/2ptbLwVWeyO7ooPGHoYTqk",
        "studio_url": "https://dreamlab.org.uk/",
        "github_url": "https://github.com/petejwoodbridge",
        "totals": {
            "tools": len(tools),
            "categories": len(categories),
            "issues": len(issues),
            "use_cases": len(use_cases),
            "challenges": len(ISSUES_CATALOG),
            "news_items": sum(i["news_count"] for i in issues),
        },
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    (DATA / "site.json").write_text(
        json.dumps(site_meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"\nDone. Site data written to: {DATA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
