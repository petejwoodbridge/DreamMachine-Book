"""Build a deduplicated, categorized index of substantive URLs across all 29 newsletters.

Filters out LinkedIn UI chrome, profile links, and duplicates. Categorizes the
remainder by domain bucket so we can dispatch research agents in parallel.
"""
import os
import re
import json
from collections import defaultdict
from urllib.parse import urlparse

MD_DIR = r"d:/VSCODE PROJECTS/DreamMachine Book/Dream Machine MD"
OUT_PATH = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/url_index.json"

URL_RE = re.compile(r"https?://[^\s)\]]+")

# Junk we never want to research
JUNK_HOSTS = {
    "linkedin.com",  # we handle linkedin selectively below
}

JUNK_PATH_PATTERNS = [
    r"^/feed/",
    r"^/mynetwork/",
    r"^/jobs/",
    r"^/messaging/",
    r"^/notifications",
    r"^/campaignmanager",
    r"^/article/edit/",
    r"^/analytics/",
    r"^/in/",  # profile URLs
    r"^/company/",  # company landing pages
    r"^/news/story/",  # auto-aggregated
    r"^/pulse/",  # other people's LinkedIn articles (cited later if needed)
    r"^/showcase/",
]

# Substantive content buckets keyed by domain
BUCKETS = {
    "primary_press": {
        "hosts": [
            "theguardian.com", "nytimes.com", "wsj.com", "bbc.co.uk", "bbc.com",
            "ft.com", "economist.com", "reuters.com", "bloomberg.com", "wired.com",
            "theverge.com", "nature.com", "scientificamerican.com", "newscientist.com",
            "ap.org", "thetimes.co.uk", "atlantic.com", "newyorker.com", "vanityfair.com",
            "vox.com", "fastcompany.com", "thedrum.com", "axios.com", "project-syndicate.org",
        ],
    },
    "industry_trade": {
        "hosts": [
            "hollywoodreporter.com", "variety.com", "deadline.com", "indiewire.com",
            "broadcastnow.co.uk", "broadcastprome.com", "tvbeurope.com", "tvtechnology.com",
            "advanced-television.com", "screendaily.com", "tvnewscheck.com",
            "ibc.org", "campaignlive.co.uk", "campaignbrief.com", "marketingweek.com",
            "adage.com", "adweek.com", "digiday.com", "martech.org", "martechseries.com",
            "thedrum.com", "the-grocer.co.uk", "thegrocer.co.uk",
        ],
    },
    "games_industry": {
        "hosts": [
            "gamesindustry.biz", "gamedeveloper.com", "pcgamer.com", "pocketgamer.biz",
            "videogameschronicle.com", "polygon.com", "ign.com", "eurogamer.net",
            "gamesradar.com", "gamesbeat.com", "gamespot.com", "80.lv", "nichegamer.com",
            "thegamepost.com", "decrypt.co", "techspot.com", "uploadvr.com", "roadtovr.com",
        ],
    },
    "music_industry": {
        "hosts": [
            "musically.com", "musictech.com", "musicradar.com", "musicbusinessworldwide.com",
            "musicbusinessresearch.wordpress.com", "billboard.com", "rollingstone.com",
            "rollingstone.co.uk", "completemusicupdate.com", "digitalmusicnews.com",
            "hypebot.com", "soundonsound.com", "cdm.link", "edm.com", "stereogum.com",
            "happymag.tv", "nme.com", "djmag.com", "routenote.com", "soultracks.com",
            "press.dittomusic.com", "newsroom.spotify.com", "blog.spotify.com",
        ],
    },
    "tech_press": {
        "hosts": [
            "techcrunch.com", "engadget.com", "cnet.com", "zdnet.com", "tomshardware.com",
            "siliconangle.com", "venturebeat.com", "arstechnica.com", "theinformation.com",
            "futurism.com", "businessinsider.com", "cnbc.com", "forbes.com", "techradar.com",
            "mashable.com", "pymnts.com", "marketingdive.com", "digiday.com",
            "edtechinnovationhub.com", "artificialintelligence-news.com", "creativeboom.com",
            "creativebloq.com", "techbullion.com", "webpronews.com",
        ],
    },
    "research_policy": {
        "hosts": [
            "reutersinstitute.politics.ox.ac.uk", "deloitte.com", "mckinsey.com",
            "gov.uk", "europa.eu", "ec.europa.eu", "grandviewresearch.com",
            "youthmusic.org.uk", "equity.org.uk", "prsformusic.com", "wipo.int",
            "imperva.com", "bain.com", "dayforce.com", "ana.net", "humanityai.ai",
            "ofcom.org.uk", "ada.cam.ac.uk",
        ],
    },
    "company_blog": {
        "hosts": [
            "openai.com", "anthropic.com", "deepmind.google", "blog.google",
            "news.adobe.com", "blog.adobe.com", "stability.ai", "runwayml.com",
            "blog.cloudflare.com", "research.nvidia.com", "magenta.withgoogle.com",
            "worldlabs.ai", "spaitial.ai", "decart.ai", "udio.com", "kling.ai",
            "comfy.org", "blog.comfy.org", "bfl.ai",
        ],
    },
    "academic": {
        "hosts": [
            "arxiv.org", "huggingface.co", "github.com",
        ],
    },
    "blog_essay": {
        "hosts": [
            "thereader.mitpress.mit.edu", "medium.com", "substack.com",
            "newsletter.smartbrief.com", "en.wikipedia.org",
        ],
    },
}

HOST_TO_BUCKET = {}
for bucket, cfg in BUCKETS.items():
    for h in cfg["hosts"]:
        HOST_TO_BUCKET[h] = bucket


def host_of(url):
    try:
        h = urlparse(url).hostname or ""
        return h.lower().lstrip(".").replace("www.", "")
    except Exception:
        return ""


def is_junk(url):
    h = host_of(url)
    if not h:
        return True
    if h.endswith("linkedin.com"):
        p = urlparse(url).path
        for pat in JUNK_PATH_PATTERNS:
            if re.match(pat, p):
                return True
        # Skip /feed/update/, /posts/* (people's posts), /pulse/ (other articles).
        if "/feed/update/" in url or "/posts/" in url:
            return True
        return False  # keep useful linkedin company pages if substantive
    # Skip auto-translated/aggregator nonsense
    if h in {"l.facebook.com", "youtu.be"}:
        return False
    return False


def bucket_for(url):
    h = host_of(url)
    if h in HOST_TO_BUCKET:
        return HOST_TO_BUCKET[h]
    # parent-host match
    for known, bucket in HOST_TO_BUCKET.items():
        if h.endswith("." + known) or h == known:
            return bucket
    return "other"


def main():
    seen = set()
    by_issue = defaultdict(list)
    by_bucket = defaultdict(list)
    junk_count = 0

    files = sorted(
        [f for f in os.listdir(MD_DIR) if f.endswith(".md")],
        key=lambda x: int(x.split(".")[0]),
    )
    for f in files:
        issue = int(f.split(".")[0])
        text = open(os.path.join(MD_DIR, f), encoding="utf-8").read()
        urls = URL_RE.findall(text)
        for u in urls:
            u = u.rstrip(".,);]")
            if is_junk(u):
                junk_count += 1
                continue
            if u in seen:
                continue
            seen.add(u)
            bucket = bucket_for(u)
            entry = {"url": u, "issue": issue, "bucket": bucket}
            by_issue[issue].append(entry)
            by_bucket[bucket].append(entry)

    print(f"Total unique substantive URLs: {len(seen)}")
    print(f"Filtered out as junk: {junk_count}")
    print("\nBy bucket:")
    for b in sorted(by_bucket, key=lambda x: -len(by_bucket[x])):
        print(f"  {b:>18}: {len(by_bucket[b])}")

    out = {
        "total": len(seen),
        "by_bucket": {b: by_bucket[b] for b in by_bucket},
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
