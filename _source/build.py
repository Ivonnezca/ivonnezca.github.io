"""Builds index.html for Ivonne Zavala's homepage from papers.py + the template below."""
import html, math, urllib.parse, pathlib
from papers import THEMES

HERE = pathlib.Path(__file__).parent
E = html.escape


def paper_link(title, arxiv):
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}", f"arXiv:{arxiv}"
    q = urllib.parse.quote(f't "{title}"')
    return f"https://inspirehep.net/literature?q={q}", "INSPIRE"


def paper_li(p):
    title, authors, ref, arxiv = p
    url, label = paper_link(title, arxiv)
    auth = E(authors).replace("I. Zavala", "<strong>I.&nbsp;Zavala</strong>")
    return (
        f'<li class="paper"><a class="paper-title" href="{url}">{E(title)}</a>'
        f'<span class="paper-auth">{auth}</span>'
        f'<span class="paper-ref">{E(ref)} <span class="paper-id">{E(label)}</span></span></li>'
    )


def themes_html():
    out = []
    for i, t in enumerate(THEMES, 1):
        n = sum(len(s["papers"]) for s in t["subtopics"])
        subs = []
        for s in t["subtopics"]:
            subs.append(
                f'<div class="sub"><h4>{E(s["title"])}</h4><p>{E(s["text"])}</p></div>'
            )
        lists = []
        for s in t["subtopics"]:
            lists.append(
                f'<h5>{E(s["title"])}</h5><ol class="papers">'
                + "".join(paper_li(p) for p in s["papers"])
                + "</ol>"
            )
        out.append(
            f'''<article class="theme{' wide' if t.get('wide') else ''}" id="{t["id"]}">
  <header class="theme-head"><h3>{E(t["title"])}</h3><p class="theme-q">{E(t["question"])}</p></header>
  <div class="subs">{"".join(subs)}</div>
  <details class="theme-papers"><summary>Selected papers <span class="count">{n}</span></summary>{"".join(lists)}</details>
</article>'''
        )
    return "\n".join(out)


def chirp_path(w=560, h=46, n=420):
    """A gravitational-wave chirp: frequency and amplitude grow, then ring down."""
    pts = []
    tc = 0.86
    for k in range(n + 1):
        x = k / n
        if x < tc:
            tau = tc - x + 0.012
            amp = 0.10 + 0.9 * (0.012 / tau) ** 0.25
            phase = -2 * math.pi * 16 * (tau / tc) ** 0.625
        else:
            amp = math.exp(-(x - tc) * 38)
            phase = 2 * math.pi * 26 * (x - tc)
        y = h / 2 - amp * (h / 2 - 2) * math.sin(phase)
        pts.append(f"{x * w:.1f},{y:.1f}")
    return "M" + " L".join(pts)


TEMPLATE = (HERE / "template.html").read_text()
page = (
    TEMPLATE.replace("{{THEMES}}", themes_html())
    .replace("{{CHIRP}}", chirp_path())
    .replace("{{NPAPERS}}", "93")
)
import base64, re
def _img(m):
    data = (HERE / "img" / m.group(1)).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()
page = re.sub(r"\{\{IMG:([\w.-]+)\}\}", _img, page)
(HERE / "index.html").write_text(page)
print("wrote", len(page), "bytes")
