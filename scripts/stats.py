#!/usr/bin/env python3
"""Builds assets/stats.svg from the GitHub API. Standard library only.

Run by .github/workflows/stats.yml. Locally:  GH_USER=dehyasec python scripts/stats.py
"""
import json
import os
import urllib.request

USER = os.environ.get("GH_USER", "dehyasec")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "stats.svg")

PANEL = "#0f1626"; PANEL2 = "#141d33"; LINE = "#1f2b45"; INK = "#0a0f1a"
TXT = "#e6ecf5"; SOFT = "#aab8d0"; MUT = "#8091ad"; DIM = "#4a5a78"
RED = "#ff4d5e"; BLUE = "#4cc9ff"; VIO = "#a78bfa"
SANS = "'Segoe UI','Inter',Roboto,'Helvetica Neue',Arial,sans-serif"

LANG_COLORS = {
    "Python": "#4B8BBE", "Shell": "#6FCF45", "PowerShell": "#5391FE", "JavaScript": "#F7DF1E",
    "TypeScript": "#3178C6", "HTML": "#FF6B3D", "CSS": "#3B9BE8", "C": "#8A94A6", "C++": "#F34B7D",
    "C#": "#9B4F96", "Java": "#B07219", "Go": "#00ADD8", "Rust": "#DEA584", "PHP": "#8892BF",
    "Ruby": "#CC342D", "Batchfile": "#C1F12E", "Dockerfile": "#2496ED", "Makefile": "#6E9F3F",
    "Jupyter Notebook": "#F37626", "Assembly": "#6E4C13", "SQL": "#E38C00", "Lua": "#6E7BFF",
}
FALLBACK = [RED, BLUE, VIO, "#ffb454", "#3ddc97", "#ff8fb1"]


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
    u = api(f"/users/{user}") or {}
    repos = api(f"/users/{user}/repos?per_page=100&type=owner&sort=pushed") or []
    own = [r for r in repos if not r.get("fork")]
    langs = {}
    for r in own[:30]:
        for k, v in (api(f"/repos/{user}/{r['name']}/languages") or {}).items():
            langs[k] = langs.get(k, 0) + v

    def total(q):
        return (api(q) or {}).get("total_count", 0)

    return {
        "repos": u.get("public_repos", len(own)),
        "stars": sum(r.get("stargazers_count", 0) for r in own),
        "followers": u.get("followers", 0),
        "commits": total(f"/search/commits?q=author:{user}&per_page=1"),
        "prs": total(f"/search/issues?q=author:{user}+type:pr&per_page=1"),
        "issues": total(f"/search/issues?q=author:{user}+type:issue&per_page=1"),
        "langs": langs,
    }


def short(n):
    n = int(n)
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1000:
        return f"{n/1000:.1f}k".replace(".0k", "k")
    return str(n)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(d):
    W, H, gap = 900, 300, 24
    lw = 438
    rx0 = lw + gap
    body = ""
    defs = ('<linearGradient id="shine" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
            '<stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>')

    def panel(x, w, title, accent):
        return (f'<rect x="{x+.5}" y=".5" width="{w-1}" height="{H-1}" rx="16" fill="{PANEL}" stroke="{LINE}"/>'
                f'<circle cx="{x+30}" cy="36" r="5" fill="{accent}"/>'
                f'<text x="{x+46}" y="42" font-family="{SANS}" font-size="18" font-weight="700" fill="{TXT}">{title}</text>')

    # ---- left: counters
    body += panel(0, lw, "Activity", RED)
    tiles = [("Repositories", d["repos"]), ("Stars earned", d["stars"]), ("Followers", d["followers"]),
             ("Commits", d["commits"]), ("Pull requests", d["prs"]), ("Issues", d["issues"])]
    pad, cols, tg = 28, 3, 12
    tw = (lw - 2 * pad - (cols - 1) * tg) / cols
    th = 92
    for i, (label, val) in enumerate(tiles):
        r, c = divmod(i, cols)
        x = pad + c * (tw + tg)
        y = 68 + r * (th + tg)
        col = RED if r == 0 else BLUE
        body += (f'<rect x="{x+.5:.1f}" y="{y+.5}" width="{tw-1:.1f}" height="{th-1}" rx="12" fill="{PANEL2}" stroke="{LINE}"/>'
                 f'<rect x="{x+16:.1f}" y="{y+16}" width="18" height="3" rx="1.5" fill="{col}"/>'
                 f'<text x="{x+16:.1f}" y="{y+56}" font-family="{SANS}" font-size="32" font-weight="700" fill="{TXT}">{short(val)}</text>'
                 f'<text x="{x+16:.1f}" y="{y+78}" font-family="{SANS}" font-size="13.5" fill="{MUT}">{label}</text>')

    # ---- right: languages
    body += panel(rx0, lw, "Top languages", BLUE)
    langs = sorted(d["langs"].items(), key=lambda kv: -kv[1])[:5]
    total = sum(v for _, v in langs) or 0
    bx, bw = rx0 + 28, lw - 56
    if total:
        for i, (name, v) in enumerate(langs):
            y = 74 + i * 42
            pct = v / total * 100
            col = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
            fill_w = max(6, bw * pct / 100)
            body += (f'<text x="{bx}" y="{y+8}" font-family="{SANS}" font-size="15.5" font-weight="600" fill="{TXT}">{esc(name)}</text>'
                     f'<text x="{bx+bw}" y="{y+8}" text-anchor="end" font-family="{SANS}" font-size="14" fill="{MUT}">{pct:.1f}%</text>'
                     f'<rect x="{bx}" y="{y+18}" width="{bw}" height="8" rx="4" fill="{PANEL2}"/>'
                     f'<clipPath id="lb{i}"><rect x="{bx}" y="{y+18}" width="{fill_w:.1f}" height="8" rx="4"/></clipPath>'
                     f'<g clip-path="url(#lb{i})"><rect x="{bx}" y="{y+18}" width="{fill_w:.1f}" height="8" fill="{col}"/>'
                     f'<rect x="{bx-80}" y="{y+18}" width="80" height="8" fill="url(#shine)">'
                     f'<animate attributeName="x" values="{bx-80};{bx+fill_w:.1f}" dur="2.2s" begin="{i*0.5}s" repeatCount="indefinite"/></rect></g>')
    else:
        body += (f'<text x="{bx}" y="104" font-family="{SANS}" font-size="17" font-weight="600" fill="{TXT}">No public code yet</text>'
                 f'<text x="{bx}" y="130" font-family="{SANS}" font-size="14.5" fill="{MUT}">Languages show up here after the first repos land.</text>')
        for i, wd in enumerate([0.78, 0.52, 0.34]):
            y = 168 + i * 36
            body += (f'<rect x="{bx}" y="{y}" width="{bw}" height="8" rx="4" fill="{PANEL2}"/>'
                     f'<rect x="{bx}" y="{y}" width="{bw*wd:.1f}" height="8" rx="4" fill="{DIM}" opacity=".5"/>')

    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="GitHub stats for {esc(USER)}">\n<title>GitHub stats for {esc(USER)}</title>\n<defs>{defs}</defs>\n{body}\n</svg>\n')


def main():
    data = fetch(USER)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(data))
    print("wrote", os.path.normpath(OUT), {k: v for k, v in data.items() if k != "langs"}, list(data["langs"])[:5])


if __name__ == "__main__":
    main()
