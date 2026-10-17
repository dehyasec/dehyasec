#!/usr/bin/env python3
"""Builds assets/stats-card.svg from the GitHub API. Standard library only.

Run by .github/workflows/stats.yml. Locally:  GH_USER=dehyasec python scripts/stats.py

Safety: if the API cannot be reached (rate limit, outage) the existing card is left untouched,
so the profile never shows a card full of zeros.
"""
import json
import os
import sys
import urllib.request

USER = os.environ.get("GH_USER", "dehyasec")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "stats-card.svg")

BG, PANEL, PANEL2 = "#090B0D", "#111419", "#171B21"
TXT, MUT, GREEN, RED, BORDER = "#F1F3F5", "#A0A8B4", "#B6FF3B", "#FF5C65", "#292F38"
SANS = "'Segoe UI','Inter',Roboto,'Helvetica Neue',Arial,sans-serif"
LANG_COLORS = {"Python": "#B6FF3B", "Shell": "#8FD14F", "PowerShell": "#7FA8FF", "JavaScript": "#F7DF1E",
               "HTML": "#FF7A59", "CSS": "#5AA9E6", "C": "#A0A8B4", "C++": "#F34B7D", "Go": "#00ADD8"}
FALLBACK = ["#B6FF3B", "#8FD14F", "#A0A8B4", "#FF5C65"]


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats",
               "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        req = urllib.request.Request("https://api.github.com" + path, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as r:
            return json.load(r)
    except Exception as e:  # network, rate limit, 404 ... never break the build
        print("api error:", path, e)
        return None


def fetch(user):
    u = api(f"/users/{user}")
    repos = api(f"/users/{user}/repos?per_page=100&type=owner&sort=pushed")
    if not u or repos is None:
        return None
    own = [r for r in repos if not r.get("fork")]
    langs = {}
    for r in own[:30]:
        for k, v in (api(f"/repos/{user}/{r['name']}/languages") or {}).items():
            langs[k] = langs.get(k, 0) + v
    commits = (api(f"/search/commits?q=author:{user}&per_page=1") or {}).get("total_count")
    return {"repos": u.get("public_repos", len(own)), "commits": commits, "langs": langs}


def short(n):
    if n is None:
        return "-"
    n = int(n)
    if n >= 1000:
        return f"{n/1000:.1f}k".replace(".0k", "k")
    return str(n)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(d, pending=False):
    """d: {'repos': int, 'commits': int|None, 'langs': {name: bytes}}  (None => pending placeholder)."""
    W, pad = 560, 28
    langs = sorted((d or {}).get("langs", {}).items(), key=lambda kv: -kv[1])[:4]
    total = sum(v for _, v in langs)
    rows = max(len(langs), 1)
    tiles_y = 70
    lang_label_y = tiles_y + 92 + 38
    rows_y = lang_label_y + 22
    H = rows_y + rows * 46 + (pad - 8)
    tiles = [("Repositories", None if pending else d["repos"]),
             ("Commits", None if pending else d["commits"]),
             ("Languages", None if pending else len(d["langs"]))]
    gap = 12
    tw = (W - 2 * pad - 2 * gap) / 3
    body = (f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{PANEL}" stroke="{BORDER}"/>'
            f'<rect x="{pad}" y="{pad-4}" width="22" height="4" rx="2" fill="{GREEN}"/>'
            f'<text x="{pad}" y="{pad+26}" font-family="{SANS}" font-size="21" font-weight="700" fill="{TXT}">Public activity</text>')
    for i, (label, val) in enumerate(tiles):
        x = pad + i * (tw + gap)
        body += (f'<rect x="{x+.5:.1f}" y="{tiles_y+.5}" width="{tw-1:.1f}" height="91" rx="10" fill="{PANEL2}" stroke="{BORDER}"/>'
                 f'<text x="{x+16:.1f}" y="{tiles_y+50}" font-family="{SANS}" font-size="36" font-weight="700" fill="{TXT}">{short(val)}</text>'
                 f'<text x="{x+16:.1f}" y="{tiles_y+75}" font-family="{SANS}" font-size="16" fill="{MUT}">{label}</text>')
    body += f'<text x="{pad}" y="{lang_label_y}" font-family="{SANS}" font-size="17" font-weight="700" fill="{MUT}">Languages</text>'
    bx, bw = pad, W - 2 * pad
    if pending or not total:
        msg = "Updates automatically via GitHub Actions" if pending else "No public code detected yet"
        body += (f'<text x="{bx}" y="{rows_y+22}" font-family="{SANS}" font-size="17" fill="{MUT}">{msg}</text>')
    else:
        for i, (name, v) in enumerate(langs):
            y = rows_y + i * 46
            pct = v / total * 100
            col = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
            body += (f'<text x="{bx}" y="{y+16}" font-family="{SANS}" font-size="17" font-weight="600" fill="{TXT}">{esc(name)}</text>'
                     f'<text x="{bx+bw}" y="{y+16}" text-anchor="end" font-family="{SANS}" font-size="16" fill="{MUT}">{pct:.1f}%</text>'
                     f'<rect x="{bx}" y="{y+26}" width="{bw}" height="8" rx="4" fill="{PANEL2}"/>'
                     f'<rect x="{bx}" y="{y+26}" width="{max(8, bw*pct/100):.1f}" height="8" rx="4" fill="{col}"/>')
    label = "Public GitHub activity for " + USER
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="{esc(label)}">\n<title>{esc(label)}</title>\n{body}\n</svg>\n')


def main():
    data = fetch(USER)
    if data is None:
        print("GitHub API unavailable: keeping the existing card.")
        sys.exit(0)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(data))
    print("wrote", os.path.normpath(OUT), {k: v for k, v in data.items() if k != "langs"}, list(data["langs"])[:4])


if __name__ == "__main__":
    main()
