"""Generate a sample resume-as-slides PDF following DESIGNS.md."""
from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).parent
FONTS = ROOT / "assets" / "fonts"
EMOJI = ROOT / "assets" / "emoji"

# ── tokens (DESIGNS.md §1–3) ────────────────────────────────────────────────
W, H = 1440, 810
M = 54
INK = HexColor("#111111")
PAPER = HexColor("#FFFFFF")
MUTED = HexColor("#6B6B6B")
HAIRLINE = HexColor("#E6E6E6")
MUSTARD = HexColor("#D9A520")
BLUE = HexColor("#2643A8")
RED = HexColor("#E0352B")
GREEN = HexColor("#3E8E4E")

for name in ["Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black"]:
    pdfmetrics.registerFont(TTFont(f"Archivo-{name}", FONTS / f"Archivo-{name}.ttf"))
pdfmetrics.registerFont(TTFont("Serif", FONTS / "DMSerifDisplay-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Italic", FONTS / "DMSerifDisplay-Italic.ttf"))

SANS_HEAVY = "Archivo-Black"
SERIF_IT = "Serif-Italic"

# ── content ────────────────────────────────────────────────────────────────
NAME = "Alex Morgan"
EMAIL = "alex.morgan@example.com"

EXPERIENCE = [
    ("Senior Product Engineer", "Lumen Labs", "2022 – now",
     "Rebuilt the billing platform", "Failed-payment churn down 31%. Mentored 4 engineers."),
    ("Full-Stack Engineer", "Brightwave", "2019 – 2022",
     "Real-time collaboration", "Used by 120k monthly users. p95 latency 840ms → 190ms."),
    ("Web Developer", "Freelance", "2017 – 2019",
     "20+ sites and apps", "For startups and local businesses, end to end."),
]

SKILLS = [
    ("Languages", ["TypeScript", "Python", "Go", "SQL"]),
    ("Frontend", ["React", "Next.js", "Tailwind", "Figma"]),
    ("Backend", ["Node.js", "PostgreSQL", "Redis", "GraphQL"]),
    ("Infra", ["AWS", "Docker", "Terraform", "CI/CD"]),
]

PROJECTS = [
    ("glowing_star", "4.2k", "GitHub stars", "Shipfast Notes", "Open-source markdown notes app."),
    ("coin", "$3k", "monthly recurring revenue", "PriceWatch", "Indie SaaS that tracks competitor pricing."),
    ("megaphone", "1", "conference talk", "Boring Tech Wins", "Speaker at JSConf EU 2024."),
]


# ── primitives ─────────────────────────────────────────────────────────────
def top(y):
    """Convert a distance from the top edge into reportlab's bottom-up y."""
    return H - y


def track(font, size, pct):
    return size * pct / 100


def text_width(s, font, size, tracking=0):
    return pdfmetrics.stringWidth(s, font, size) + track(font, size, tracking) * len(s)


def text(c, x, y, s, font, size, color=INK, tracking=0, align="left"):
    w = text_width(s, font, size, tracking)
    if align == "right":
        x -= w
    elif align == "center":
        x -= w / 2
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setCharSpace(track(font, size, tracking))
    t.setFillColor(color)
    t.textOut(s)
    c.drawText(t)
    return w


def emoji(c, name, x, y, size):
    c.drawImage(str(EMOJI / f"{name}.png"), x, y, size, size, mask="auto")


def headline(c, x, y, parts, size, color=INK):
    """Draw one headline line. parts: list of ('sans'|'serif'|'emoji', value)."""
    for kind, val in parts:
        if kind == "sans":
            x += text(c, x, y, val, SANS_HEAVY, size, color, tracking=-4)
        elif kind == "serif":
            x += text(c, x, y, val, SERIF_IT, size, color)
        else:
            s = size * 0.95
            x += size * 0.12
            emoji(c, val, x, y - size * 0.14, s)
            x += s + size * 0.16
    return x


def wrap(s, font, size, width):
    lines, line = [], ""
    for word in s.split():
        trial = f"{line} {word}".strip()
        if pdfmetrics.stringWidth(trial, font, size) > width and line:
            lines.append(line)
            line = word
        else:
            line = trial
    return lines + [line]


def hline(c, x1, x2, y, color=INK, width=1.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y, x2, y)


def kicker(c, s, color=INK, x=M, y=top(50)):
    text(c, x, y, s.upper(), "Archivo-Bold", 8.5, color, tracking=18)


def label(c, x, y, s, color=MUTED):
    text(c, x, y, s.upper(), "Archivo-SemiBold", 8.5, color, tracking=14)


def chrome(c, kick, color=INK):
    kicker(c, kick, color)
    text(c, W - M, top(52), NAME.upper(), "Serif", 13, color, tracking=12, align="right")


def bottom_bar(c, accent, left, right=None):
    y, h = 76, 64
    c.setFillColor(accent)
    c.rect(M, y, W - 2 * M, h, fill=1, stroke=0)
    fg = INK if accent == MUSTARD else PAPER
    text(c, M + 22, y + 25, left, "Archivo-Bold", 18, fg, tracking=-1)
    if right:
        text(c, W - M - 22, y + 25, right, SERIF_IT, 18, fg, align="right")


def ghost(accent, alpha=0.25):
    """Paper at `alpha` over the accent color (DESIGNS.md §2)."""
    r, g, b = (a + (1 - a) * alpha for a in (accent.red, accent.green, accent.blue))
    return Color(r, g, b)


def fill_page(c, color):
    c.setFillColor(color)
    c.rect(0, 0, W, H, fill=1, stroke=0)


# ── slides ─────────────────────────────────────────────────────────────────
def title_slide(c):
    fill_page(c, INK)
    chrome(c, "Resume · Oct 2026", PAPER)
    size = 76
    headline(c, M, top(250), [("sans", "Hi, I'm Alex."), ("emoji", "waving_hand")], size, PAPER)
    headline(c, M, top(340), [("sans", "I build"), ("emoji", "laptop"), ("sans", "and ship"),
                              ("emoji", "rocket")], size, PAPER)
    headline(c, M, top(430), [("serif", "products people pay for.")], size, PAPER)

    x = M + text(c, M, top(580), "with ", SERIF_IT, 22, PAPER)
    text(c, x, top(580), NAME, "Archivo-Bold", 22, PAPER, tracking=-1)
    text(c, M, top(612), f"Senior Product Engineer  ·  Berlin  ·  {EMAIL}",
         "Archivo-Regular", 15, HexColor("#BBBBBB"))

    third = W / 3
    for i, (col, lab) in enumerate([(BLUE, "01 · Work"), (RED, "02 · Side projects"),
                                    (GREEN, "03 · Contact")]):
        c.setFillColor(col)
        c.rect(i * third, 0, third + 1, 32, fill=1, stroke=0)
        label(c, i * third + M, 12, lab, PAPER)


def about_slide(c):
    chrome(c, "Intro · Who's talking")
    headline(c, M, top(190), [("sans", "Eight years,"), ("emoji", "briefcase")], 72)
    headline(c, M, top(270), [("serif", "shipping for real users.")], 72)

    text(c, M, top(330), NAME, "Archivo-Bold", 22, tracking=-1)
    text(c, M, top(356), "Senior Product Engineer, Berlin. I ship end to end: schema to pixel.",
         "Archivo-Regular", 16, MUTED)
    hline(c, M, W - M, top(388))

    rows = [("graduation_cap", "BSc Computer Science, TU Munich"),
            ("briefcase", "ex-Brightwave, now Lumen Labs"),
            ("hammer_and_wrench", "Full-stack: TypeScript, Postgres, AWS"),
            ("glowing_star", "Speaker, JSConf EU 2024")]
    col_w = 620
    for i, (icon, s) in enumerate(rows):
        y = top(388) - 22 - i * 52
        emoji(c, icon, M + 4, y - 34, 34)
        text(c, M + 56, y - 24, s, "Archivo-Regular", 18)
        if i < len(rows) - 1:
            hline(c, M, M + col_w, y - 42, HAIRLINE, 0.75)

    sx = M + col_w + 70
    stats = [("8+", "years shipping"), ("120k", "monthly users served"), ("31%", "churn cut at Lumen")]
    sw = (W - M - sx) / 3
    for i, (num, lab) in enumerate(stats):
        x = sx + i * sw
        text(c, x, top(480), num, SANS_HEAVY, 54, tracking=-4)
        label(c, x, top(510), lab)

    # highlight row (mustard)
    y, h = 76, 72
    c.setFillColor(MUSTARD)
    c.rect(M, y, W - 2 * M, h, fill=1, stroke=0)
    emoji(c, "coin", M + 16, y + 14, 44)
    text(c, M + 76, y + 40, "Latest win: failed-payment churn down 31% in one quarter",
         "Archivo-Bold", 20, tracking=-1)
    text(c, M + 76, y + 18, "Billing rebuild at Lumen Labs  ·  retries + dunning emails  ·  "
         "~$400k ARR recovered per year", "Archivo-Regular", 14)


def divider(c, accent, act, numeral, lines, inside):
    fill_page(c, accent)
    for i in range(3):
        c.setFillColor(PAPER)
        c.setStrokeColor(PAPER)
        c.setLineWidth(1)
        c.circle(M + 4 + i * 14, top(47), 4, fill=int(i == act - 1), stroke=1)
    kicker(c, f"Act {act} of 3 · {inside[0]}", PAPER, x=M + 50)
    text(c, W - M, top(52), NAME.upper(), "Serif", 13, PAPER, tracking=12, align="right")

    text(c, M - 10, top(560), numeral, SANS_HEAVY, 300, ghost(accent), tracking=-6)

    for i, parts in enumerate(lines):
        headline(c, 640, top(290 + i * 92), parts, 80, PAPER)

    hline(c, M, W - M, top(720), PAPER, 0.75)
    x = M + text(c, M, top(752), "INSIDE THIS ACT:", "Archivo-Bold", 9, PAPER, tracking=14) + 24
    text(c, x, top(752), "  ·  ".join(inside[1]), "Archivo-Regular", 13, PAPER)


def experience_slide(c):
    chrome(c, "Work · Experience")
    headline(c, M, top(190), [("sans", "Three roles,"), ("emoji", "chart_increasing"),
                              ("serif", "one direction.")], 72)
    hline(c, M, W - M, top(250))

    cols = [M, M + 420, M + 620]
    for x, h in zip(cols, ["01 · Role / company", "02 · When", "03 · What I shipped"]):
        label(c, x, top(280), h)
    for i, (role, co, when, what, detail) in enumerate(EXPERIENCE):
        y = top(330 + i * 110)
        text(c, cols[0], y, role, "Archivo-Bold", 24, tracking=-2)
        text(c, cols[0], y - 28, co, SERIF_IT, 20, MUTED)
        text(c, cols[1], y, when, "Archivo-Medium", 18)
        text(c, cols[2], y, what, "Archivo-Bold", 20, tracking=-1)
        text(c, cols[2], y - 28, detail, "Archivo-Regular", 17, MUTED)
        if i < len(EXPERIENCE) - 1:
            hline(c, M, W - M, y - 56, HAIRLINE, 0.75)

    bottom_bar(c, BLUE, "Every role shipped to production and was measured in numbers.",
               "Impact over output.")


def skills_slide(c):
    chrome(c, "Work · Toolbox")
    headline(c, M, top(190), [("sans", "My toolbox,"), ("emoji", "toolbox"),
                              ("serif", "built for shipping.")], 72)
    hline(c, M, W - M, top(250))

    gap = 36
    cw = (W - 2 * M - gap * 3) / 4
    for i, (group, items) in enumerate(SKILLS):
        x = M + i * (cw + gap)
        label(c, x, top(285), f"0{i + 1} · {group}")
        hline(c, x, x + cw, top(300), INK, 1)
        for j, item in enumerate(items):
            y = top(345 + j * 58)
            text(c, x, y, item, "Archivo-Bold", 24, tracking=-2)
            if j < len(items) - 1:
                hline(c, x, x + cw, y - 22, HAIRLINE, 0.75)

    bottom_bar(c, BLUE, "TypeScript end to end, Postgres underneath, AWS around it.",
               "Boring tech wins.")


def projects_slide(c):
    chrome(c, "Side projects · Proof")
    headline(c, M, top(190), [("sans", "Nights and weekends,"), ("emoji", "trophy"),
                              ("serif", "real users.")], 72)
    hline(c, M, W - M, top(250))

    gap = 48
    cw = (W - 2 * M - gap * 2) / 3
    for i, (icon, num, unit, name, desc) in enumerate(PROJECTS):
        x = M + i * (cw + gap)
        emoji(c, icon, x, top(370), 84)
        text(c, x + 104, top(330), num, SANS_HEAVY, 64, tracking=-4)
        label(c, x + 106, top(358), unit)
        hline(c, x, x + cw, top(400), HAIRLINE, 0.75)
        text(c, x, top(445), name, "Archivo-Bold", 26, tracking=-2)
        for k, ln in enumerate(wrap(desc, "Archivo-Regular", 18, cw)):
            text(c, x, top(478 + k * 26), ln, "Archivo-Regular", 18, MUTED)

    bottom_bar(c, RED, "Small bets, shipped fast, kept only if people paid.",
               "Proof beats promises.")


def contact_slide(c):
    divider(c, GREEN, 3, "03",
            [[("sans", "Let's build"), ("emoji", "handshake")],
             [("serif", "something people")],
             [("serif", "pay for.")]],
            ("Contact", [EMAIL, "github.com/alexmorgan", "linkedin.com/in/alexmorgan", "Berlin, DE"]))


SLIDES = [
    title_slide,
    about_slide,
    lambda c: divider(c, BLUE, 1, "01",
                      [[("sans", "Where I've")], [("sans", "worked"), ("emoji", "briefcase")],
                       [("serif", "and what I shipped.")]],
                      ("Work", ["Lumen Labs", "Brightwave", "Freelance", "Toolbox"])),
    experience_slide,
    skills_slide,
    lambda c: divider(c, RED, 2, "02",
                      [[("sans", "Things I built"), ("emoji", "rocket")],
                       [("serif", "on my own time.")]],
                      ("Side projects", ["Shipfast Notes", "PriceWatch", "Boring Tech Wins"])),
    projects_slide,
    contact_slide,
]

if __name__ == "__main__":
    out = ROOT / "sample-resume-slides.pdf"
    c = canvas.Canvas(str(out), pagesize=(W, H))
    c.setTitle(f"{NAME} — Resume")
    for slide in SLIDES:
        slide(c)
        c.showPage()
    c.save()
    print(f"wrote {out.name}")
