"""Generate the real resume slides into resume/, following DESIGNS.md."""
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

from make_sample import (BLUE, GREEN, HAIRLINE, INK, M, MUSTARD, MUTED, PAPER, RED, ROOT, SANS_HEAVY, SERIF_IT,
                         H, W, bottom_bar, emoji, fill_page, headline, hline, kicker,
                         label, text, text_width, top, wrap)

OUT = ROOT / "resume"
LOGOS = ROOT / "assets" / "logos"

NAME = "Norma Dani Risdiandita"
ROLE = "Senior Software Engineer"
CONTACTS = [
    ("Email", "norma.risdiandita@gmail.com", "mailto:norma.risdiandita@gmail.com"),
    ("Phone", "+62 813-2861-7302", "tel:+6281328617302"),
    ("LinkedIn", "linkedin.com/in/risdiandita", "https://www.linkedin.com/in/risdiandita"),
    ("GitHub", "github.com/danirisdiandita", "https://github.com/danirisdiandita"),
    ("Website", "danirisdiandita.com", "https://danirisdiandita.com"),
    ("Based in", "Yogyakarta, Indonesia", None),
]

EDUCATION = [
    {
        "tag": "01 · MSc · 2017 – 2018",
        "logo": "imperial",
        "school": "Imperial College London",
        "degree": "Master of Science, Physics",
        "thesis_label": "Dissertation",
        "thesis": "Activation energies of ionic migration in perovskites, "
                  "via Electrochemical Impedance Spectroscopy",
        "points": [
            ("microscope", "Experimental physics + computation",
             "Impedance measurements on perovskite solar cells, analysed and modelled in Python."),
            ("sun", "Wrote an EIS fitting algorithm",
             "Fit equivalent-circuit models to impedance data by minimising mean-square error."),
            ("chart_increasing", "Results matched theory",
             "Activation energies agreed with prior studies. Linear regression, "
             "Matplotlib visuals."),
        ],
    },
    {
        "tag": "02 · BSc · 2011 – 2015",
        "logo": "ugm",
        "school": "Universitas Gadjah Mada",
        "degree": "Bachelor of Science, Condensed Matter & Materials Physics",
        "thesis_label": "Undergraduate thesis",
        "thesis": "Electronic Transport in Semiconducting Graphene",
        "points": [
            ("laptop", "Theory + computation",
             "Python (NumPy, Matplotlib), Fortran and MATLAB."),
            ("light_bulb", "Modelled a graphene pn junction",
             "Two differently doped graphene layers, assessed for semiconductor devices."),
            ("gear", "Lengthy analytical derivations",
             "Worked the maths through by hand, then solved and visualised it numerically."),
        ],
    },
]

DS_ROLE = {
    "title": "Data Scientist & ML Engineer",
    "companies": "Sorabel, Datanest, Azima",
    "dates": "Mar 2019 – Dec 2020",
    "work": [
        ("logo:sorabel", "Sorabel",
         "Developed **market-basket analysis** and **search/recommendation models** "
         "for fashion e-commerce.",
         ["Python", "NumPy", "SQL (BigQuery)"]),
        ("logo:datanest", "Datanest",
         "Built **demand-forecasting** and **time-series models** to predict when retail "
         "customers were likely to reorder, enabling sales teams to proactively prioritize and "
         "time customer outreach.",
         ["scikit-learn", "TensorFlow", "XGBoost"]),
        ("text:AZIMA AI", "Azima",
         "Built an **end-to-end conversational commerce and logistics system** where "
         "customers ordered products via **WhatsApp** using text or images; implemented **custom NLU** "
         "and **computer vision OCR** for order-to-product mapping and **VRP-based optimization** for "
         "automated delivery routing.",
         ["NLU", "Computer Vision", "Dialogflow", "Text fuzzy matching", "Search algorithm",
          "Vehicle Routing Problem"]),
    ],
}

INFIDEA_ROLE = {
    "title": "Senior Software Engineer / Co-Founder",
    "companies": "Infidea.id",
    "logo": "infidea.png",
    "dates": "Dec 2020 – April 2022",
    "points": [
        ("handshake",
         "Served as a **client-facing technical lead** and **hands-on engineer** for AI/ML "
         "projects, translating business requirements into production systems while "
         "**mentoring junior engineers**."),
        ("package",
         "Owned the **end-to-end ML lifecycle**, from model training and experimentation "
         "through API integration, containerization, and production deployment using "
         "**Docker** and **Kubernetes**."),
        ("satellite_antenna",
         "Delivered production **Text-to-Speech**, **Object Detection**, **OCR**, and "
         "**Crowd Counting** systems for a **major telecommunications client**."),
        ("chart_increasing",
         "Built **MillionRobo**, a **real-time algorithmic trading platform** using "
         "**WebSocket** and **pub/sub** architecture, and **NextSci**, an **optimization "
         "engine** for routing, bin-packing, and scheduling problems."),
    ],
}

WIDYA_ROLE = {
    "title": "Fractional CTO",
    "companies": "Widya Robotics & Widya Security",
    "dates": "Jan 2025 – June 2026",
    "left": [
        ("robot", "Widya Robotics",
         "Led **technical presales** and **end-to-end delivery** for AI projects across Widya "
         "Robotics, serving as the **go-to technical owner** from client discovery and solution "
         "architecture through implementation and production deployment; helped close and "
         "deliver multiple commercial AI projects."),
        ("shield", "Widya Security",
         "Led **cybersecurity initiatives** at Widya Security, including developing "
         "**LLM-powered VAPT reporting platform** that accelerated penetration-testing report "
         "generation."),
    ],
    "projects_intro": "Closed and delivered **multiple commercial AI projects**, including:",
    "projects": [
        ("stethoscope",
         "Led development of a **RAG based clinical assistant** of Skin Clinic doctors: chatbot "
         "recommendation based on internal documents and stock checking for each clinic"),
        ("ship",
         "Architected and delivered **real time vehicle counting, classification, License Plate "
         "Recognition** system for harbor operations, processing **5,000+** of vehicle "
         "detections per day using YOLO, MobileNetV3, PyTorch/TensorRT, FastAPI, RabbitMQ, and "
         "Docker. (Widya Robotics)"),
        ("seedling",
         "Closed and led delivery of a **real-time computer-vision system for fertilizer-bag "
         "counting**, processing **thousands of bags per day** in production. (Widya Robotics)"),
    ],
}

WICARA_ROLE = {
    "title": "Senior Software Engineer / Founding Engineer / CTO",
    "companies": "Widya Wicara",
    "dates": "May 2022 – Present",
    "products_label": "Transkripsi.id & Widya Notulensi",
    "products": "Architected, built and launched **Transkripsi.id** and **Widya Notulensi** "
                "(https://notulensi.id), two production **AI & LLM powered transcription "
                "products**",
    "stats": [("100K+", "users"), ("99.9%", "uptime"), ("> 1000", "AI workloads per month")],
    "sub": [
        "Built production **speech-to-text**, **meeting transcription**, and **multi-participant "
        "speaker diarization** system with data **encrypted in transit and at rest**, and "
        "implemented versioning to preserve meeting-data integrity and provide tamper "
        "traceability.",
        "Shipped **automated meeting-bot integrations** for **Zoom**, **Google Meet**, and "
        "**Microsoft Teams**; migrated meeting-bot workloads from **Kubernetes** to **Google Cloud "
        "Run Jobs**, reducing bot latency join latency from 1-2 minutes and ultimately **<30 "
        "seconds**, while moving compute to an on-demand model that **reduced idle "
        "infrastructure costs**.",
    ],
    "more": [
        ("clapper_board", "More AI products",
         "Architected and shipped additional AI products spanning **conversational AI**, "
         "**text-to-speech**, **generative video**, **content automation**, and **media "
         "processing**, working with models including Wav2Vec, Whisper, FastSpeech2, Parallel "
         "WaveGAN, and ESPnet2."),
        ("busts_in_silhouette", "Team",
         "Built and led the engineering team through multiple headcount stages (**peaking at "
         "15**, later restructured to a **core team of 3**), establishing **hiring standards** "
         "and a **mentoring track** from junior to senior."),
    ],
    "tech": ["Next.js", "NestJS", "Python", "Flask", "PyTorch", "Wav2Vec", "Speaker Embedding",
             "Docker", "Google Cloud Run Service", "Google Cloud Run Job", "Kubernetes"],
}

DIM = HexColor("#8A8A8A")
RULE_DARK = HexColor("#2A2A2A")


def intro(c):
    fill_page(c, INK)
    kicker(c, "Resume · 2026", PAPER)
    text(c, W - M, top(52), "DANIRISDIANDITA.COM", "Serif", 13, PAPER, tracking=12, align="right")

    size = 84
    headline(c, M, top(220), [("sans", f"{NAME}.")], size, PAPER)
    headline(c, M, top(315), [("sans", "Full-stack"), ("emoji", "laptop"),
                              ("sans", "& AI/ML"), ("emoji", "robot")], size, PAPER)
    headline(c, M, top(410), [("serif", f"{ROLE.lower()}.")], size, PAPER)

    hline(c, M, W - M, top(520), RULE_DARK, 1)
    col_w = (W - 2 * M) / 3
    for i, (lab, val, url) in enumerate(CONTACTS):
        x = M + (i % 3) * col_w
        y = top(560 + (i // 3) * 76)
        label(c, x, y, lab, DIM)
        w = text(c, x, y - 28, val, "Archivo-Medium", 20, PAPER, tracking=-1)
        if url:
            c.linkURL(url, (x, y - 34, x + w, y - 8), relative=0)
        if i < 3:
            hline(c, x, x + col_w - 36, y - 48, RULE_DARK, 0.75)

    third = W / 3
    for i, (col, lab) in enumerate([(BLUE, "01 · Full-stack"), (RED, "02 · AI / ML"),
                                    (GREEN, "03 · Shipping products")]):
        c.setFillColor(col)
        c.rect(i * third, 0, third + 1, 32, fill=1, stroke=0)
        label(c, i * third + M, 12, lab, PAPER)


def education(c):
    kicker(c, "Education · Where I trained")
    text(c, W - M, top(52), "NORMA DANI RISDIANDITA", "Serif", 13, INK, tracking=12, align="right")
    headline(c, M, top(165), [("sans", "Physics first,"), ("emoji", "atom_symbol"),
                              ("serif", "code ever since.")], 68)
    hline(c, M, W - M, top(212))

    gap = 72
    col_w = (W - 2 * M - gap) / 2
    for i, ed in enumerate(EDUCATION):
        x = M + i * (col_w + gap)
        label(c, x, top(246), ed["tag"])
        c.drawImage(str(LOGOS / f"{ed['logo']}.png"), x, top(318), 56, 56, mask="auto")
        text(c, x + 72, top(290), ed["school"], "Archivo-Bold", 28, tracking=-2)
        text(c, x + 72, top(316), ed["degree"], SERIF_IT, 19, MUTED)

        label(c, x, top(356), ed["thesis_label"])
        for k, ln in enumerate(wrap(ed["thesis"], "Archivo-SemiBold", 17, col_w)):
            text(c, x, top(380 + k * 22), ln, "Archivo-SemiBold", 17)
        hline(c, x, x + col_w, top(422), INK, 1)

        for j, (icon, title, detail) in enumerate(ed["points"]):
            y = top(450 + j * 74)
            emoji(c, icon, x, y - 24, 32)
            text(c, x + 48, y, title, "Archivo-Bold", 18, tracking=-1)
            for k, ln in enumerate(wrap(detail, "Archivo-Regular", 15, col_w - 48)[:2]):
                text(c, x + 48, y - 22 - k * 19, ln, "Archivo-Regular", 15, MUTED)
            if j < len(ed["points"]) - 1:
                hline(c, x + 48, x + col_w, y - 58, HAIRLINE, 0.75)

    bottom_bar(c, MUSTARD, "Physics taught me to model messy data, then write the code that fits it.",
               "London · Yogyakarta")


def rich(c, x, y, s, size, width, leading):
    """Draw wrapped text where **phrases** are set in Archivo Bold."""
    font = {False: "Archivo-Regular", True: "Archivo-Bold"}
    words, bold = [], False  # each word: list of (piece, bold) runs
    for token in s.split():
        runs = []
        for n, piece in enumerate(token.split("**")):
            if n:
                bold = not bold
            if piece:
                runs.append((piece, bold, text_width(piece, font[bold], size)))
        if runs:
            words.append(runs)
    space = text_width(" ", font[False], size)
    lines, line, lw = [], [], 0
    for runs in words:
        w = sum(r[2] for r in runs)
        if line and lw + space + w > width:
            lines.append(line)
            line, lw = [], 0
        lw += (space if line else 0) + w
        line.append(runs)
    lines.append(line)
    for k, ln in enumerate(lines):
        cx = x
        for runs in ln:
            for piece, b, w in runs:
                text(c, cx, y - k * leading, piece, font[b], size)
                cx += w
            cx += space
    return len(lines)


def chip(c, x, y, s, w):
    """Outlined tag with text baseline at y."""
    c.setStrokeColor(INK)
    c.setLineWidth(0.75)
    c.rect(x, y - 7, w, 24, fill=0, stroke=1)
    text(c, x + 9, y, s, "Archivo-Medium", 13)


def data_science(c):
    r = DS_ROLE
    kicker(c, f"Experience · {r['dates']}")
    text(c, W - M, top(52), "NORMA DANI RISDIANDITA", "Serif", 13, INK, tracking=12, align="right")
    text(c, M, top(160), r["title"], SANS_HEAVY, 60, tracking=-4)
    text(c, M, top(205), f"at {r['companies']}", SERIF_IT, 30, MUTED)
    text(c, W - M, top(160), r["dates"], SANS_HEAVY, 36, tracking=-3, align="right")
    hline(c, M, W - M, top(240))

    gap = 48
    cw = (W - 2 * M - gap * 2) / 3
    for i, (icon, company, body, stack) in enumerate(r["work"]):
        x = M + i * (cw + gap)
        label(c, x, top(285), f"0{i + 1} · {company}")
        if icon.startswith("logo:"):
            c.drawImage(str(LOGOS / f"{icon[5:]}.png"), x, top(375), 150, 72, mask="auto",
                        preserveAspectRatio=True, anchor="sw")
        elif icon.startswith("text:"):
            text(c, x, top(368), icon[5:], SANS_HEAVY, 44, tracking=-3)
        else:
            emoji(c, icon, x, top(375), 72)
        hline(c, x, x + cw, top(400), HAIRLINE, 0.75)
        rich(c, x, top(432), body, 17, cw, 24)
        label(c, x, top(588), "Stack")
        cx, cy = x, top(614)
        for t in stack:
            w = text_width(t, "Archivo-Medium", 13) + 18
            if cx + w > x + cw:
                cx, cy = x, cy - 30
            chip(c, cx, cy, t, w)
            cx += w + 6

    bottom_bar(c, BLUE, "From fashion recommendations to WhatsApp orders: ML inside real products.",
               "Data in, decisions out.")


def role_header(c, r):
    """Kicker, role title + companies on the left, big date range on the right."""
    kicker(c, f"Experience · {r['dates']}")
    text(c, W - M, top(52), "NORMA DANI RISDIANDITA", "Serif", 13, INK, tracking=12, align="right")
    date_w = text(c, W - M, top(160), r["dates"], SANS_HEAVY, 36, tracking=-3, align="right")
    size = 60
    while text_width(r["title"], SANS_HEAVY, size, -4) > W - 2 * M - date_w - 48:
        size -= 2
    text(c, M, top(160), r["title"], SANS_HEAVY, size, tracking=-4)
    if r.get("logo"):
        c.drawImage(str(LOGOS / r["logo"]), M, top(222), 300, 36, mask="auto",
                    preserveAspectRatio=True, anchor="sw")
    else:
        text(c, M, top(205), f"at {r['companies']}", SERIF_IT, 30, MUTED)
    hline(c, M, W - M, top(240))


def infidea(c):
    r = INFIDEA_ROLE
    role_header(c, r)
    gap_x = 72
    cw = (W - 2 * M - gap_x) / 2
    for i, (icon, body) in enumerate(r["points"]):
        x = M + (i % 2) * (cw + gap_x)
        y = top(285 + (i // 2) * 175)
        label(c, x, y, f"0{i + 1}")
        emoji(c, icon, x, y - 70, 48)
        rich(c, x + 72, y - 32, body, 18, cw - 72, 26)
        if i < 2:
            hline(c, x, x + cw, y - 150, HAIRLINE, 0.75)

    bottom_bar(c, BLUE, "Client-facing tech lead, end-to-end ML lifecycle, production AI systems.",
               "Co-Founder, Infidea.id")


def widya(c):
    r = WIDYA_ROLE
    role_header(c, r)
    size, lead = 17, 25
    lw = 590
    rx = M + lw + 64
    rw = W - M - rx

    y = top(278)
    for i, (icon, lab, body) in enumerate(r["left"]):
        emoji(c, icon, M, y - 44, 40)
        label(c, M + 56, y, lab)
        n = rich(c, M + 56, y - 26, body, size, lw - 56, lead)
        y -= 26 + n * lead + 18
        if i < len(r["left"]) - 1:
            hline(c, M + 56, M + lw, y + 6, HAIRLINE, 0.75)
            y -= 18

    y = top(278)
    label(c, rx, y, "Commercial AI projects")
    n = rich(c, rx, y - 26, r["projects_intro"], size, rw, lead)
    y -= 26 + n * lead + 14
    for icon, body in r["projects"]:
        emoji(c, icon, rx, y - 24, 32)
        n = rich(c, rx + 48, y, body, size, rw - 48, lead)
        y -= n * lead + 14

    bottom_bar(c, BLUE, "From presales to production: AI delivery across Widya Robotics "
               "& Widya Security.", "Fractional CTO")


def chips(c, x, y, items, width):
    """Lay out outlined tags left to right, wrapping within width."""
    cx, cy = x, y
    for t in items:
        w = text_width(t, "Archivo-Medium", 13) + 18
        if cx + w > x + width:
            cx, cy = x, cy - 30
        chip(c, cx, cy, t, w)
        cx += w + 6
    return cy


def wicara(c):
    r = WICARA_ROLE
    role_header(c, r)
    size, lead = 15, 22
    lw = 650
    rx = M + lw + 56
    rw = W - M - rx

    # left: flagship products
    y = top(272)
    emoji(c, "studio_microphone", M, y - 44, 40)
    label(c, M + 56, y, r["products_label"])
    n = rich(c, M + 56, y - 24, r["products"], size, lw - 56, lead)
    y -= 24 + n * lead + 12
    for body in r["sub"]:
        c.setStrokeColor(INK)
        c.setLineWidth(1)
        c.circle(M + 61, y + 5, 3.5, fill=0, stroke=1)
        n = rich(c, M + 76, y, body, size, lw - 76, lead)
        y -= n * lead + 12
    label(c, M + 56, top(588), "Tech")
    chips(c, M + 56, top(612), r["tech"], lw - 56)

    # right: stats, more products, team, tech
    y = top(286)
    sw = rw / 3
    for i, (num, lab) in enumerate(r["stats"]):
        text(c, rx + i * sw, y - 12, num, SANS_HEAVY, 36, tracking=-4)
        label(c, rx + i * sw, y - 32, lab)
    y -= 56
    hline(c, rx, rx + rw, y, HAIRLINE, 0.75)
    y -= 26
    for icon, lab, body in r["more"]:
        emoji(c, icon, rx, y - 40, 36)
        label(c, rx + 50, y, lab)
        n = rich(c, rx + 50, y - 22, body, size, rw - 50, lead)
        y -= 22 + n * lead + 16

    bottom_bar(c, BLUE, "Founding engineer to CTO: AI transcription products serving 100K+ users.",
               "Widya Wicara")


PAGES = [("001-intro.pdf", intro), ("002-education.pdf", education),
         ("003-data-science.pdf", data_science), ("004-infidea.pdf", infidea),
         ("005-widya.pdf", widya), ("006-widya-wicara.pdf", wicara)]

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for filename, draw in PAGES:
        c = canvas.Canvas(str(OUT / filename), pagesize=(W, H))
        c.setTitle(f"{NAME} — {ROLE}")
        draw(c)
        c.showPage()
        c.save()
        print(f"wrote resume/{filename}")
