"""Generate the real resume slides into resume/, following DESIGNS.md."""
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
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
        "tag": "01 · MSc · 2017 – 2018 · GPA 3.7",
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
        "tag": "02 · BSc · 2011 – 2015 · GPA 3.66",
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
    "stack": [
        ("Software Engineering", ["Python", "JavaScript", "C/C++"]),
        ("AI and ML", ["PyTorch", "TensorFlow", "Computer Vision", "NLP"]),
        ("Infra", ["Docker", "Kubernetes", "CI/CD"]),
    ],
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
        ("logo:widya_robotics_icon.png", "Widya Robotics",
         "Led **technical presales** and **end-to-end delivery** for AI projects across Widya "
         "Robotics, serving as the **go-to technical owner** from client discovery and solution "
         "architecture through implementation and production deployment; helped close and "
         "deliver multiple commercial AI projects."),
        ("logo:widya_security_shield.png", "Widya Security",
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
    "logo": "widya_wicara.png",
    "dates": "May 2022 – Present",
    "products_label": "Transkripsi.id & Widya Notulensi",
    "products": "Architected, built and launched **Transkripsi.id** and **Widya Notulensi** "
                "(https://notulensi.id), two production **AI & LLM powered transcription "
                "products**",
    "stats": [("100K+", "users, both products"), ("99.9%", "uptime"), ("> 1000", "AI workloads per month")],
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

SUMMARY = (
    "Senior Software Engineer and hands-on technology leader with **7+ years** of experience "
    "building and shipping **production AI and distributed systems**. Deep experience across "
    "**speech AI**, **RAG/NLP**, **computer vision**, **backend systems**, **Kubernetes**, and "
    "**cloud infrastructure (AWS/GCP)**, with systems serving **100K+ users**. Combines hands-on "
    "engineering with **system architecture**, **technical leadership**, and **client-facing "
    "delivery**, owning complex products from design and model development through production "
    "deployment and optimization."
)

INDIE_PROJECTS = [
    {
        "icon": "img:notespark/icon.png",
        "name": "NoteSpark AI",
        "url_text": "notespark.id",
        "url": "https://notespark.id",
        "years": "2025 – present",
        "stat": ("1,900+", "registered users"),
        "body": "Built and launched an **AI study companion** using **LLMs**, **Next.js**, **Go**, "
                "and **React Native**, reaching **1,900+ registered users** across web, iOS, and "
                "Android. Subscribers **mostly from the US**. {flag:us}",
        "screens": [f"notespark/screen{i}.png" for i in range(1, 6)],
        "weight": 0.64,
    },
    {
        "icon": "hospital",
        "name": "Medical SaaS",
        "url_text": None,
        "url": None,
        "years": "2020 – present",
        "stat": ("2+ years", "in continuous use"),
        "body": "Built and maintained a **production SaaS platform** used continuously by a "
                "**medical clinic** for **2+ years**.",
        "screens": [],
        "weight": 0.36,
    },
]

SKILLS = [
    ("Languages", "Python, Go, TypeScript/JavaScript, C/C++, R"),
    ("AI/ML", "End-to-end from fine-tuning to production of ML systems including but not limited "
              "to Computer Vision, RAG, NLP, Generative AI"),
    ("ML Frameworks", "PyTorch, LangChain, TensorFlow"),
    ("Backend & APIs", "Go/Gin, Flask, FastAPI, Node.js, NestJS, microservices"),
    ("Cloud & Infra", "AWS, GCP, Kubernetes, Docker, Cloud Run, AWS Lambda"),
    ("Frontend & Mobile", "React, React Native, Next.js"),
    ("Data", "SQL, BigQuery, PostgreSQL, Redis"),
    ("DevOps", "CI/CD with GitHub Actions, GitLab CI"),
    ("Leadership", "Technical Leadership, System Architecture, Technical Presales, Mentoring, "
                   "Hiring, Cross-Functional collaboration"),
]

CERTIFICATIONS = [
    ("locked", "Certified Appsec Practitioner V2 (CAP)", "May 2026"),
    ("clipboard", "ISO/IEC 27001:2022 Lead Implementer", "April 2025"),
]

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
    text(c, M, top(140), "Education", SANS_HEAVY, 60, tracking=-4)
    text(c, M, top(188), "Background in Theoretical Physics with Scientific Computing",
         SERIF_IT, 28, MUTED)
    skills = ["Maths", "Physics", "Computing (Python, Fortran)"]
    widths = [text_width(t, "Archivo-Medium", 13) + 18 for t in skills]
    sx = W - M - sum(widths) - 6 * (len(skills) - 1)
    label(c, sx, top(150), "Skills")
    for t, w in zip(skills, widths):
        chip(c, sx, top(176), t, w)
        sx += w + 6
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


def us_flag(c, x, y, h):
    """Small vector US flag, bottom-left at (x, y)."""
    w = h * 1.9
    stripe = h / 13
    c.saveState()
    for i in range(13):
        c.setFillColor(HexColor("#B22234") if i % 2 == 0 else PAPER)
        c.rect(x, y + h - (i + 1) * stripe, w, stripe, fill=1, stroke=0)
    cw, ch = w * 0.4, stripe * 7
    c.setFillColor(HexColor("#3C3B6E"))
    c.rect(x, y + h - ch, cw, ch, fill=1, stroke=0)
    c.setFillColor(PAPER)
    for r in range(4):
        for k in range(5):
            c.circle(x + cw * (k + 0.5) / 5, y + h - ch * (r + 0.5) / 4, h * 0.03, fill=1, stroke=0)
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.rect(x, y, w, h, fill=0, stroke=1)
    c.restoreState()
    return w


INLINE = {"{flag:us}": us_flag}  # tokens drawn as graphics inside rich text


def rich(c, x, y, s, size, width, leading):
    """Draw wrapped text where **phrases** are set in Archivo Bold."""
    font = {False: "Archivo-Regular", True: "Archivo-Bold"}
    words, bold = [], False  # each word: list of (piece, bold) runs
    for token in s.split():
        if token in INLINE:
            words.append([(token, None, size * 0.72 * 1.9)])
            continue
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
                if b is None:
                    INLINE[piece](c, cx, y - k * leading - size * 0.02, size * 0.72)
                else:
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


def header(c, kick, title, sub=None, right=None, logo=None):
    """Kicker, big title + italic subtitle (or logo) on the left, optional big text on the right."""
    kicker(c, kick)
    text(c, W - M, top(52), "NORMA DANI RISDIANDITA", "Serif", 13, INK, tracking=12, align="right")
    right_w = text(c, W - M, top(160), right, SANS_HEAVY, 36, tracking=-3, align="right") if right else 0
    size = 60
    while text_width(title, SANS_HEAVY, size, -4) > W - 2 * M - right_w - 48:
        size -= 2
    text(c, M, top(160), title, SANS_HEAVY, size, tracking=-4)
    if logo:
        c.drawImage(str(LOGOS / logo), M, top(222), 300, 36, mask="auto",
                    preserveAspectRatio=True, anchor="sw")
    elif sub:
        text(c, M, top(205), sub, SERIF_IT, 30, MUTED)
    hline(c, M, W - M, top(240))


def role_header(c, r):
    header(c, f"Experience · {r['dates']}", r["title"], f"at {r['companies']}", r["dates"],
           r.get("logo"))


def infidea(c):
    r = INFIDEA_ROLE
    role_header(c, r)
    text(c, W - M, top(208), "~1.5 Billion IDR", SANS_HEAVY, 26, tracking=-3, align="right")
    unit = "Highest-value project finished"
    label(c, W - M - text_width(unit.upper(), "Archivo-SemiBold", 8.5, 14), top(226), unit)
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
    sw = (W - 2 * M - 36 * (len(r["stack"]) - 1)) / len(r["stack"])
    for i, (lab, items) in enumerate(r["stack"]):
        x = M + i * (sw + 36)
        label(c, x, top(590), lab)
        chips(c, x, top(616), items, sw)

    bottom_bar(c, BLUE, "Client-facing tech lead, end-to-end ML lifecycle, production AI systems.",
               "Co-Founder, Infidea.id")


def widya(c):
    r = WIDYA_ROLE
    header(c, f"Experience · {r['dates']}", r["title"], None, r["dates"])
    # company lockups in place of the subtitle
    icon_w, _ = draw_img(c, LOGOS / "widya_robotics_icon.png", M, top(226), h=38)
    nx = M + icon_w + 12 + text(c, M + icon_w + 12, top(214), "Widya Robotics", "Archivo-Bold", 24,
                                tracking=-1)
    amp_w = text(c, nx + 22, top(214), "&", SERIF_IT, 28, MUTED)
    draw_img(c, LOGOS / "widya_security.png", nx + 22 + amp_w + 22, top(226), h=36)
    size, lead = 17, 25
    lw = 590
    rx = M + lw + 64
    rw = W - M - rx

    y = top(278)
    for i, (icon, lab, body) in enumerate(r["left"]):
        if icon.startswith("logo:"):
            c.drawImage(str(LOGOS / icon[5:]), M, y - 44, 40, 40, mask="auto",
                        preserveAspectRatio=True)
        else:
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
    c.drawImage(str(ROOT / "assets/notulensi/icon.png"), M, y - 44, 40, 40, mask="auto")
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


def summary(c):
    header(c, "Intro · Summary", "Summary", "Senior Software Engineer - Full-Stack & AI/ML")
    headline(c, M, top(296), [("sans", "0-1 Startup Founding Engineer "),
                              ("serif", "and 1 to 100K Maintainer.")], 27)
    headline(c, M, top(334), [("sans", "Client-facing, "),
                              ("serif", "experienced with multiple production AI projects/products.")], 27)
    rich(c, M, top(390), SUMMARY, 21, 860, 31)

    sx = M + 860 + 72
    for i, (num, lab) in enumerate([("7+", "years of experience"), ("100K+", "users served")]):
        y = top(320 + i * 150)
        text(c, sx, y, num, SANS_HEAVY, 72, tracking=-4)
        label(c, sx, y - 30, lab)
        if i == 0:
            hline(c, sx, W - M, y - 62, HAIRLINE, 0.75)

    bottom_bar(c, MUSTARD, "Speech AI · RAG/NLP · Computer Vision · Backend · Kubernetes · AWS/GCP",
               "Senior Software Engineer")


def indie_projects(c):
    header(c, "Indie developer projects", "Indie Developer Projects", None, "2020 – present")
    gap = 72
    x = M
    for i, p in enumerate(INDIE_PROJECTS):
        cw = (W - 2 * M - gap * (len(INDIE_PROJECTS) - 1)) * p["weight"]
        label(c, x, top(285), f"0{i + 1} · {p['years']}")
        if p["icon"].startswith("img:"):
            c.drawImage(str(ROOT / "assets" / p["icon"][4:]), x, top(375), 72, 72, mask="auto")
        else:
            emoji(c, p["icon"], x, top(375), 72)
        text(c, x + 90, top(336), p["name"], "Archivo-Bold", 28, tracking=-2)
        if p["url_text"]:
            w = text(c, x + 90, top(362), p["url_text"], SERIF_IT, 19, MUTED)
            c.linkURL(p["url"], (x + 90, top(368), x + 90 + w, top(346)), relative=0)
        num, unit = p["stat"]
        text(c, x + cw, top(342), num, SANS_HEAVY, 36, tracking=-4, align="right")
        unit_w = text_width(unit.upper(), "Archivo-SemiBold", 8.5, 14)
        label(c, x + cw - unit_w, top(364), unit)
        hline(c, x, x + cw, top(396), HAIRLINE, 0.75)
        n = rich(c, x, top(428), p["body"], 18, cw, 26)

        if p["screens"]:
            sgap = 12
            sw = (cw - sgap * (len(p["screens"]) - 1)) / len(p["screens"])
            sh = sw * 311 / 293
            sy = top(428) - n * 26 - 12 - sh
            if sy < top(656):  # keep clear of the bottom bar
                sh -= top(656) - sy
                sw = sh * 293 / 311
                sy = top(656)
            for k, img in enumerate(p["screens"]):
                c.drawImage(str(ROOT / "assets" / img), x + k * (sw + sgap), sy, sw, sh,
                            mask="auto")
        x += cw + gap

    bottom_bar(c, RED, "NoteSpark AI · Medical SaaS", "Indie developer")


def technical_skills(c):
    header(c, "Technical skills", "Technical Skills")
    y = top(290)
    for i, (cat, items) in enumerate(SKILLS):
        label(c, M, y, cat)
        n = rich(c, M + 240, y, items, 21, W - 2 * M - 240, 28)
        y -= n * 28 + 22
        if i < len(SKILLS) - 1:
            hline(c, M, W - M, y + 28, HAIRLINE, 0.75)


def certifications(c):
    header(c, "Certifications", "Certifications")
    gap = 72
    cw = (W - 2 * M - gap) / 2
    for i, (icon, name, date) in enumerate(CERTIFICATIONS):
        x = M + i * (cw + gap)
        label(c, x, top(290), f"0{i + 1}")
        emoji(c, icon, x, top(420), 104)
        for k, ln in enumerate(wrap(name, "Archivo-Bold", 36, cw)):
            text(c, x, top(480 + k * 42), ln, "Archivo-Bold", 36, tracking=-2)
        text(c, x, top(580), date, SERIF_IT, 24, MUTED)

    bottom_bar(c, GREEN, "norma.risdiandita@gmail.com  ·  +62 813-2861-7302", "danirisdiandita.com")


def img_size(path):
    return ImageReader(str(path)).getSize()


def draw_img(c, path, x, y, h=None, w=None):
    """Draw an image at (x, y) bottom-left, sized by height or width. Returns (w, h)."""
    iw, ih = img_size(path)
    if h is None:
        h = w * ih / iw
    else:
        w = h * iw / ih
    c.drawImage(str(path), x, y, w, h, mask="auto")
    return w, h


def products(c):
    header(c, "Widya Wicara · Products", "Transkripsi.id & Widya Notulensi",
           "Two AI transcription products", "100K+ users")
    unit = "combined"
    uw = text_width(unit.upper(), "Archivo-SemiBold", 8.5, 14)
    label(c, W - M - uw, top(184), unit)

    assets = ROOT / "assets"
    gap = 56
    cw = (W - 2 * M - gap) / 2

    # left: Transkripsi.id
    x = M
    label(c, x, top(270), "01 · Upload & transcribe")
    lw, _ = draw_img(c, assets / "transkripsi/logo.png", x, top(312), h=32)
    w = text(c, x + lw + 16, top(304), "transkripsi.id", SERIF_IT, 19, MUTED)
    c.linkURL("https://transkripsi.id", (x + lw + 16, top(310), x + lw + 16 + w, top(288)), relative=0)
    hh = 300
    hw, _ = draw_img(c, assets / "transkripsi/hero.png", x, top(330) - hh, h=hh)
    rw = cw - hw - 12
    draw_img(c, assets / "transkripsi/result.png", x + hw + 12, top(330) - hh, w=rw)

    # right: Widya Notulensi
    x = M + cw + gap
    label(c, x, top(270), "02 · Meeting bots")
    lw, _ = draw_img(c, assets / "notulensi/logo.png", x, top(312), h=32)
    w = text(c, x + lw + 16, top(304), "notulensi.id", SERIF_IT, 19, MUTED)
    c.linkURL("https://notulensi.id", (x + lw + 16, top(310), x + lw + 16 + w, top(288)), relative=0)
    iw, ih = img_size(assets / "notulensi/dashboard.png")
    dh = cw * ih / iw
    draw_img(c, assets / "notulensi/dashboard.png", x, top(330) - dh, w=cw)
    y = top(330) - dh - 34
    label(c, x, y, "Joins meetings on")
    bx = x
    for img, h in [("zoom_wide.png", 28), ("meet_wide.png", 25), ("teams_wide.png", 30)]:
        w, _ = draw_img(c, assets / "notulensi" / img, bx, y - 16 - h, h=h)
        bx += w + 32

    bottom_bar(c, BLUE, "Transkripsi.id + Widya Notulensi: 100K+ users combined, 99.9% uptime.",
               "Founding engineer / CTO")


PAGES = [
    ("001-intro.pdf", intro),
    ("002-summary.pdf", summary),
    ("003-education.pdf", education),
    ("004-data-science.pdf", data_science),
    ("005-infidea.pdf", infidea),
    ("006-widya.pdf", widya),
    ("007-widya-wicara.pdf", wicara),
    ("008-products.pdf", products),
    ("009-indie-projects.pdf", indie_projects),
    ("010-technical-skills.pdf", technical_skills),
    ("011-certifications.pdf", certifications),
]
FULL_DECK = "resume-full.pdf"

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    full = canvas.Canvas(str(OUT / FULL_DECK), pagesize=(W, H))
    full.setTitle(f"{NAME} — {ROLE}")
    for filename, draw in PAGES:
        c = canvas.Canvas(str(OUT / filename), pagesize=(W, H))
        c.setTitle(f"{NAME} — {ROLE}")
        draw(c)
        c.showPage()
        c.save()
        draw(full)
        full.showPage()
        print(f"wrote resume/{filename}")
    full.save()
    print(f"wrote resume/{FULL_DECK}")
