#!/usr/bin/env python3
"""Check the curated videos in lms/videos.json.

    python lms/check_videos.py --schema   # offline: structure and rules only (run by check_repo.py)
    python lms/check_videos.py --quick    # online: each video still exists and allows embedding
    python lms/check_videos.py            # online: also English audio, English captions, length

Standard library only. --quick uses YouTube's oEmbed endpoint, which also works from CI.
The full check reads each public watch page; YouTube sometimes blocks that from cloud IPs,
so run it on your own machine when adding or reviewing videos.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "lms" / "videos.json"
UA = {"User-Agent": "Mozilla/5.0 (fde-zero-to-hired video check)", "Accept-Language": "en-US,en;q=0.9"}
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
MAX_WEEKLY_MINUTES = 30.5


def videos(data: dict):
    """Yield (where, video, optional) for every video in the file."""
    for p in data["phases"]:
        for w in p["weeks"]:
            for v in w["videos"]:
                yield f"phase {p['phase']} week {w['week']}", v, False
        for v in p.get("optional", []):
            yield f"phase {p['phase']} optional", v, True


def check_schema(data: dict) -> list[str]:
    problems, seen = [], {}
    for key in ("about", "checked", "phases"):
        if key not in data:
            problems.append(f"missing top-level key '{key}'")
    for where, v, optional in videos(data):
        for key in ("id", "title", "channel", "minutes", "published", "why"):
            if key not in v:
                problems.append(f"{where}: {v.get('id', '?')} missing '{key}'")
        vid = v.get("id", "")
        if not ID_RE.match(vid):
            problems.append(f"{where}: bad video id '{vid}'")
        if not optional and float(v.get("minutes", 0)) > MAX_WEEKLY_MINUTES:
            problems.append(f"{where}: {vid} is {v['minutes']} min; weekly videos must be under 30 (move it to 'optional')")
        if vid in seen and seen[vid] != where:
            problems.append(f"{where}: {vid} also listed in {seen[vid]}")
        seen.setdefault(vid, where)
    return problems


def get(url: str) -> str:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        return r.read().decode("utf-8", "replace")


def check_online(vid: str, full: bool) -> list[str]:
    issues = []
    try:
        get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json")
    except urllib.error.HTTPError as e:
        return [{401: "embedding disabled", 403: "embedding disabled", 404: "removed or private"}.get(e.code, f"oEmbed HTTP {e.code}")]
    except Exception as e:  # noqa: BLE001
        return [f"oEmbed failed: {e}"]
    if not full:
        return issues
    try:
        html = get(f"https://www.youtube.com/watch?v={vid}&hl=en")
        m = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.+?\});(?:var|</script>)", html, re.S)
        pr = json.loads(m.group(1))
    except Exception as e:  # noqa: BLE001
        return [f"could not read watch page ({e}); try again later or from another network"]
    if pr.get("playabilityStatus", {}).get("status") != "OK":
        issues.append(f"not playable: {pr.get('playabilityStatus', {}).get('status')}")
    tracks = pr.get("captions", {}).get("playerCaptionsTracklistRenderer", {}).get("captionTracks", [])
    if not any(t.get("languageCode", "").split("-")[0] == "en" for t in tracks):
        issues.append("no English captions")
    audio = {f["audioTrack"].get("displayName"): f["audioTrack"].get("audioIsDefault")
             for f in pr.get("streamingData", {}).get("adaptiveFormats", []) if f.get("audioTrack")}
    default = next((k for k, v in audio.items() if v), None)
    asr = [t.get("languageCode") for t in tracks if t.get("kind") == "asr"]
    lang = default or (asr[0] if len(asr) == 1 else "")
    if lang and not lang.lower().startswith(("en", "english")):
        issues.append(f"audio is '{lang}', not English")
    return issues


def main(argv: list[str]) -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    problems = check_schema(data)
    if "--schema" in argv:
        if problems:
            print("videos.json:\n  " + "\n  ".join(problems), file=sys.stderr)
            return 1
        print(f"videos.json: {sum(1 for _ in videos(data))} videos, structure OK")
        return 0
    full = "--quick" not in argv
    bad = list(problems)
    checked = 0
    for where, v, _ in videos(data):
        checked += 1
        for issue in check_online(v["id"], full):
            bad.append(f"{where}: {v['id']} \"{v['title'][:60]}\" - {issue}")
    mode = "full" if full else "quick (exists + embeddable)"
    print(f"videos: {checked} checked ({mode}), {len(bad)} problem(s)")
    for line in bad:
        print(f"  PROBLEM {line}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
