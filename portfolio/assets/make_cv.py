#!/usr/bin/env python3
"""Generate Maurizio Lamanna's CV PDF, styled to match the portfolio site
(hasbeck.com-inspired: uppercase letterspaced headings, coral accent)."""

import math

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, Frame, Flowable, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, HRFlowable, KeepTogether,
)

ISO_X = math.cos(math.radians(30))  # true 30° isometric

CORAL_LT = HexColor("#A8BCAF")  # roadbook moss, light face
CORAL_DK = HexColor("#4E635A")  # roadbook moss, dark face

def draw_iso_cube(c, x, y, e, top, left, right):
    """Solid 3-face isometric cube; (x, y) = top-back vertex, canvas y-up."""
    ax, ay = x + e * ISO_X, y - e * 0.5
    bx, by = x - e * ISO_X, y - e * 0.5
    cx, cy = x, y - e
    for color, pts in (
        (top,   [(x, y), (ax, ay), (cx, cy), (bx, by)]),
        (left,  [(bx, by), (cx, cy), (cx, cy - e), (bx, by - e)]),
        (right, [(cx, cy), (ax, ay), (ax, ay - e), (cx, cy - e)]),
    ):
        c.setFillColor(color)
        p = c.beginPath()
        p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        p.close()
        c.drawPath(p, stroke=0, fill=1)

def draw_iso_wire(c, x, y, e, h=None):
    """Wireframe isometric box outline; (x, y) = top-back vertex, canvas y-up."""
    h = h if h is not None else e
    ax, ay = x + e * ISO_X, y - e * 0.5
    bx, by = x - e * ISO_X, y - e * 0.5
    cx, cy = x, y - e
    p = c.beginPath()
    p.moveTo(x, y); p.lineTo(ax, ay); p.lineTo(ax, ay - h); p.lineTo(cx, cy - h)
    p.lineTo(bx, by - h); p.lineTo(bx, by); p.close()
    p.moveTo(ax, ay); p.lineTo(cx, cy); p.lineTo(bx, by)
    p.moveTo(cx, cy); p.lineTo(cx, cy - h)
    c.drawPath(p, stroke=1, fill=0)

class IsoHeading(Flowable):
    """Section heading with a small isometric cube bullet."""
    def __init__(self, text, style):
        super().__init__()
        self.text = text
        self.style = style
        self.height = 13

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self.height

    def draw(self):
        c = self.canv
        draw_iso_cube(c, 4.5, 11.5, 4.5, CORAL_LT, CORAL, CORAL_DK)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(CORAL)
        c.drawString(15, 2, tracked_plain(self.text.upper()))

CORAL = HexColor("#71887B")  # roadbook moss accent
INK = HexColor("#25292B")    # roadbook charcoal
SOFT = HexColor("#454B4E")
MUTE = HexColor("#71787A")
LINE = HexColor("#DBD8CB")

OUT = "/Users/mauriziolamanna/Desktop/VicRoads Designs VTS/maurizio-portfolio/assets/Maurizio-Lamanna-CV.pdf"

def tracked(text):
    # Paragraph collapses runs of plain spaces, so word gaps need &nbsp;
    return " ".join("&nbsp;&nbsp;" if ch == " " else ch for ch in text)

def tracked_plain(text):
    # For canvas.drawString (no markup): plain wide word gaps survive
    return " ".join("  " if ch == " " else ch for ch in text)

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=24,
                           leading=28, textColor=INK),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=10.5,
                           leading=14, textColor=CORAL),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5,
                              leading=12, textColor=MUTE),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10,
                         leading=13, textColor=INK, spaceBefore=0),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.2,
                           leading=13.5, textColor=SOFT),
    "when": ParagraphStyle("when", fontName="Helvetica", fontSize=8,
                           leading=12, textColor=MUTE),
    "org": ParagraphStyle("org", fontName="Helvetica-Bold", fontSize=9.5,
                          leading=13, textColor=INK),
    "post": ParagraphStyle("post", fontName="Helvetica-Oblique", fontSize=9.2,
                           leading=13, textColor=SOFT),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.2,
                             leading=13.5, textColor=SOFT, leftIndent=9,
                             bulletIndent=0, spaceAfter=3),
}

def heading(text):
    return [
        Spacer(1, 7 * mm),
        IsoHeading(text, styles["h2"]),
        Spacer(1, 1.5 * mm),
        HRFlowable(width="100%", thickness=0.7, color=LINE),
        Spacer(1, 3.5 * mm),
    ]

def row(when, flowables):
    t = Table([[Paragraph(when.upper(), styles["when"]), flowables]],
              colWidths=[30 * mm, None])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t

def bullet(text):
    return Paragraph(text, styles["bullet"], bulletText="•")

story = []

# ---- Header ----
story.append(Paragraph(tracked("MAURIZIO LAMANNA"), styles["name"]))
story.append(Spacer(1, 2.5 * mm))
story.append(Paragraph(tracked("SENIOR EXPERIENCE DESIGNER"), styles["role"]))
story.append(Spacer(1, 2.5 * mm))
story.append(Paragraph(
    "Sydney, Australia &nbsp;·&nbsp; maurizio.lamanna@mantelgroup.com.au &nbsp;·&nbsp; linkedin.com/in/maurizio-lamanna",
    styles["contact"]))
story.append(Spacer(1, 3 * mm))
story.append(HRFlowable(width="100%", thickness=2.2, color=CORAL))

# ---- Profile ----
story += heading("Profile")
story.append(Paragraph(
    "Sydney-based architect turned experience designer. Architecture taught me to think in "
    "systems — how people move through a space, where friction lives, and how structure shapes "
    "behaviour — and I bring that same spatial logic to digital products. I specialise in the messy "
    "front end of a problem: distilling complex, technical, many-stakeholdered challenges into "
    "refined, playful, human-focused experiences. At Mantel I lead design on discovery and delivery "
    "engagements for clients including VicRoads, ANZ, Toll Group, Medibank, nib and Nine's "
    "Drive.com.au — from experience mapping and user research through to high-fidelity prototypes "
    "and build-ready handover.", styles["body"]))

# ---- Experience ----
story += heading("Experience")

exp1 = [
    Paragraph("MANTEL — Senior Experience Designer", styles["org"]),
    Paragraph("Sydney · July 2022 – present", styles["post"]),
    Spacer(1, 2 * mm),
    Paragraph(  # exp1 flows directly (not via row()) so bullets can split across pages
        "Design lead on discovery and delivery engagements across government, banking, health, "
        "logistics and media. I turn complex technical problems into experiences people love, then "
        "hand them over so build teams can hit the ground running.", styles["body"]),
    Spacer(1, 2.5 * mm),
    bullet("<b>VicRoads — Vehicle Transfer Service (2026):</b> led design on a 10-week discovery for "
           "a vehicle transfer service with escrow-backed payments. Mapped the full buyer/seller "
           "journey, designed golden paths and error states, and co-built a React Native demo — "
           "de-risking a multi-million dollar build decision with 5 epics of build-ready documentation."),
    bullet("<b>VicRoads — Learner Permit &amp; Hazard Perception Test (2025–26):</b> project lead on an "
           "8-week discovery reimagining how Victorians learn to drive — mobile-first with an AI "
           "learning companion (“Ask Lara”). Recommended an open-source hybrid platform giving "
           "VicRoads full IP ownership and a white-label play for other jurisdictions."),
    bullet("<b>ANZ — Digital Expo on Apple Vision Pro (2025):</b> designed one of Australia's first "
           "banking experiences in spatial computing — an interactive institutional expo showcased at "
           "SIBOS, making ANZ first to POC the technology and saving up to $200K per physical event."),
    bullet("<b>Toll Group — MoveMaestro Future Vision (2025):</b> created the target-state vision and "
           "service design for Toll's relocation platform (ADF, Home Affairs, corporate) — vision map, "
           "service/journey maps and hi-fi prototype that aligned stakeholders and de-risked its "
           "commercial future."),
    bullet("<b>Alfred Health — ML for Blood Transfusion Prediction (2024):</b> defined the problem, "
           "mapped the user journey, facilitated ideation and delivered high-fidelity prototypes that "
           "helped secure future funding."),
    bullet("<b>Safety Sphere — Vision Pro demo (2024):</b> internal capability uplift; storyboarded and "
           "designed hi-fi visionOS screens and collaborated with engineering on a working demo."),
    bullet("<b>Medibank — Preventative Health App (2024):</b> designed, prototyped and animated a "
           "“service manual for your body” journey to a booked GP appointment; presented "
           "company-wide to win stakeholder buy-in."),
    bullet("<b>Stringline — Trades App UX/UI Redesign (2024):</b> rebuilt flows with the founder and "
           "developer for MVP launch — 30+ flows reimagined, 100+ screens, 5 rounds of user testing."),
    bullet("<b>nib — Continuous Cyber Assurance (2023):</b> research, journey maps, personas and a "
           "story-mapped feature backlog for a data-backed cyber dashboard now used to brief executives."),
    bullet("<b>Drive.com.au — Marketplace Discovery (2023):</b> planned and coached agile design "
           "sprints with Nine's product team; two rounds of moderated research and two responsive "
           "hi-fi prototypes for the marketplace roadmap."),
    bullet("<b>Belong — North Star Discovery (2022–23):</b> experience principles, a validated Vision "
           "Experience Map and tested concepts for the order-to-activate journey, setting the "
           "foundation for delivery."),
]
story.append(KeepTogether(exp1[:5]))
for fl in exp1[5:]:
    story.append(fl)

story.append(Spacer(1, 4 * mm))
exp2 = [
    Paragraph("MANTEL — Trainee Designer", styles["org"]),
    Paragraph("Sydney · April – July 2022", styles["post"]),
    Spacer(1, 2 * mm),
    Paragraph(
        "Completed Mantel's design traineeship, applying the full discovery process to an internal "
        "service design project — user research, ideation, prototyping and delivery of a notification "
        "tool that streamlined COVID case communication across Mantel hubs.", styles["body"]),
]
story.append(KeepTogether(exp2))

# ---- Education ----
edu = heading("Education") + [
    row("2021", [Paragraph("GENERAL ASSEMBLY", styles["org"]),
                 Paragraph("UX Design Intensive", styles["post"])]),
    Spacer(1, 1.5 * mm),
    row("2019", [Paragraph("THE UNIVERSITY OF SYDNEY", styles["org"]),
                 Paragraph("Master of Architecture", styles["post"])]),
    Spacer(1, 1.5 * mm),
    row("2014", [Paragraph("THE UNIVERSITY OF SYDNEY", styles["org"]),
                 Paragraph("Bachelor of Design (Architecture)", styles["post"])]),
]
story.append(KeepTogether(edu))

# ---- Capabilities ----
cap = heading("Capabilities") + [
    row("Design", [Paragraph(
        "Experience mapping · journey mapping · service design · UX/UI · accessibility · "
        "spatial computing (visionOS)", styles["body"])]),
    Spacer(1, 1.5 * mm),
    row("Research", [Paragraph(
        "User interviews · survey design · usability testing · synthesis · personas · "
        "human-centred design", styles["body"])]),
    Spacer(1, 1.5 * mm),
    row("Delivery", [Paragraph(
        "High-fidelity prototyping (Figma) · design sprints · workshop facilitation · "
        "stakeholder management · design strategy", styles["body"])]),
]
story.append(KeepTogether(cap))

doc = BaseDocTemplate(OUT, pagesize=A4,
                      leftMargin=18 * mm, rightMargin=18 * mm,
                      topMargin=16 * mm, bottomMargin=16 * mm,
                      title="Maurizio Lamanna — CV",
                      author="Maurizio Lamanna")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")

def footer(canvas, doc_):
    canvas.saveState()
    # Roadbook cream page ground (drawn under content)
    canvas.setFillColor(HexColor("#F3F2EB"))
    canvas.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTE)
    canvas.drawString(doc_.leftMargin, 9 * mm, "Maurizio Lamanna — Curriculum Vitae")
    canvas.drawRightString(A4[0] - doc_.rightMargin, 9 * mm, f"Page {canvas.getPageNumber()}")
    if canvas.getPageNumber() == 1:
        # Architectural wireframe cube cluster, top-right of the header
        right = A4[0] - doc_.rightMargin
        top = A4[1] - 14 * mm
        canvas.setLineWidth(0.6)
        canvas.setStrokeColor(HexColor("#B9B6A7"))
        draw_iso_wire(canvas, right - 58, top - 4, 15)
        draw_iso_wire(canvas, right - 24, top - 14, 11)
        canvas.setStrokeColor(CORAL)
        draw_iso_cube(canvas, right - 40, top - 26, 7, CORAL_LT, CORAL, CORAL_DK)
    canvas.restoreState()

doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])
doc.build(story)
print("written:", OUT)
