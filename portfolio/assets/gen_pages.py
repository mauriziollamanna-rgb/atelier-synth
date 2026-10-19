#!/usr/bin/env python3
"""Generate case-study pages (modelled on hasbeck.com/portfolio/odds_and_ends.html)
for each Selected Work card in index.html. Reuses each card's isometric motif
and colour as the page hero."""

import re, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")
OUTDIR = os.path.join(ROOT, "work")
os.makedirs(OUTDIR, exist_ok=True)

src = open(INDEX).read()

# Extract cards in document order: colour class, svg inner, title, tagline
card_re = re.compile(
    r'<li class="card reveal" data-tags="([^"]*)">.*?card__media (card__media--\w+)".*?'
    r'(<svg viewBox="0 0 100 100"[^>]*>.*?</svg>).*?<h3>(.*?)</h3>\s*<p>(.*?)</p>',
    re.S)
cards = card_re.findall(src)
assert len(cards) == 11, f"expected 11 cards, got {len(cards)}"

SLUGS = ["vicroads-vehicle-transfer", "vicroads-learner-permit", "anz-vision-pro",
         "toll-movemaestro", "alfred-health-ml", "safety-sphere", "medibank-health-app",
         "stringline-redesign", "nib-cyber-assurance", "drive-marketplace", "belong-north-star"]

CARDS = {}
for slug, (tags, colour, svg, title, tagline) in zip(SLUGS, cards):
    CARDS[slug] = dict(tags=tags, colour=colour, svg=svg, title=title, tagline=tagline)

P = {}  # per-page content

P["vicroads-vehicle-transfer"] = dict(
    num="01", sub="Designing a safer way to buy and sell a used car in Victoria, with payments held in escrow.",
    meta=[("Client", "VicRoads"), ("Type of work", "Service &amp; product design"),
          ("Date", "April – July 2026"), ("My role", "Design lead · 10-week discovery")],
    intro="VicRoads wanted to know if an escrow-backed vehicle transfer service could be built, and what "
          "it would cost. We spent ten weeks finding out, designing the buyer and seller experience in "
          "myVicRoads and connecting it to Shaype's escrow platform.",
    sections=[
        ("The ask", ["Prove the service was feasible, estimate the build, and give VicRoads enough "
          "material to take into a business case.",
          "I led design alongside three lead engineers, working closely with VicRoads Product and "
          "Shaype's integration team."]),
        ("My role", None),
        ("The outcome", None),
    ],
    role=["<b>Experience map:</b> mapped the buyer and seller journeys with VicRoads, so everyone could "
          "see the whole service on one page.",
          "<b>Journeys and edge cases:</b> designed the primary, secondary and tertiary paths, plus the "
          "alternate flows and error states.",
          "<b>Demo:</b> worked with the engineers on a React Native demo for the business case.",
          "<b>Requirements:</b> worked through payments and edge cases with VicRoads and Shaype early, "
          "while they were still cheap to change.",
          "<b>Handover:</b> wrote up the flows, rules and error states as epics the build team can pick "
          "up directly."],
    outcome=["<b>The escrow model works.</b> Funds sit in a joint account and are split automatically "
          "between the seller, SRO, VicRoads and VTS Premium at handover. We designed and tested this "
          "end to end.",
          "<b>Five build-ready epics</b> covering flow steps, alternate flows and error scenarios.",
          "<b>A demo people could use.</b> Stakeholders could click through the service themselves, which "
          "brought up UX and technical questions early.",
          "<b>A build estimate VicRoads can defend,</b> with a recommended plan and team structure."],
    stats=[("10", "week discovery"), ("5", "build-ready epics"), ("4-way", "escrow payment split")],
    related=["vicroads-learner-permit", "toll-movemaestro", "belong-north-star"])

P["vicroads-learner-permit"] = dict(
    num="02", sub="Rethinking the learner permit test for mobile, with an AI study companion.",
    meta=[("Client", "VicRoads"), ("Type of work", "Strategy &amp; product design"),
          ("Date", "November 2025 – February 2026"), ("My role", "Project lead · 8-week discovery")],
    intro="An eight-week discovery into the Learner Permit Test and Hazard Perception Test: what the "
          "experience should be, and which platform VicRoads should build it on.",
    sections=[
        ("The ask", ["Redesign the LPT/HPT experience for mobile, recommend a platform that could scale "
          "and pay its way, and make a case strong enough to get executive funding.",
          "I led a team of three: me, another senior designer and a tech lead. We had daily standups "
          "with VicRoads, ran SME workshops, and played back to senior stakeholders every week."]),
        ("My role", None),
        ("The outcome", None),
    ],
    role=["<b>Research:</b> ran six internal SME sessions and went through customer feedback. Language "
          "barriers and a clunky interface came up again and again.",
          "<b>Experience map:</b> designed a six-stage target state, from first study session to "
          "licence issue.",
          "<b>UI design:</b> high-fidelity, mobile-first designs for web and app.",
          "<b>Tech:</b> worked with the tech leads so the designs fit the recommended Open edX hybrid "
          "platform."],
    outcome=["<b>A future-state experience map,</b> including longer-term ideas like AI cheating "
          "detection and online eye tests.",
          "<b>“Ask Lara”,</b> an AI study companion that gives help specific to each page and adapts to "
          "how each learner studies.",
          "<b>Road safety features</b> grounded in research, like spaced repetition to help people "
          "retain what they learn, and “Results Wrapped”, which shares what the community is getting "
          "right and wrong.",
          "<b>A white-label front end.</b> The UI is headless and themed through configuration, so other "
          "states like NSW could use it.",
          "<b>VicRoads owns the IP.</b> The open-source hybrid model saves money and opens up revenue "
          "from reselling."],
    stats=[("8", "week discovery"), ("6", "SME research sessions"), ("6-stage", "target state blueprint")],
    related=["vicroads-vehicle-transfer", "drive-marketplace", "medibank-health-app"])

P["anz-vision-pro"] = dict(
    num="03", sub="One of the first banking experiences built for Apple Vision Pro in Australia.",
    meta=[("Client", "ANZ"), ("Type of work", "Spatial computing"),
          ("Date", "June – July 2025"), ("My role", "Experience designer")],
    intro="ANZ Institutional runs an expo to show key clients its digital roadmap. They asked Mantel to "
          "rethink it.",
    sections=[
        ("The problem", ["ANZ works across 32 markets and has more than 8.5 million customers. A physical "
          "expo is expensive to run and only reaches the people in the room. ANZ wanted something it "
          "could take anywhere."]),
        ("The design", ["We designed an interactive expo for Apple Vision Pro:",
          "<ul><li>Guided scenarios, presented by an AI avatar.</li>"
          "<li>A 3D map of the expo floor.</li>"
          "<li>A virtual theatrette where remote clients can watch the keynotes.</li></ul>",
          "It can be adapted for different pitches, events and markets."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>More engaging than a booth.</b> Clients work through real examples rather than "
          "reading a stand.",
          "<b>Shown at SIBOS.</b> ANZ became the first bank to complete a proof of concept on the "
          "headset.",
          "<b>Cheaper to run.</b> ANZ can hold the expo anywhere, and estimates savings of up to $200,000 "
          "per physical event.",
          "<b>A competitive edge</b> that could help ANZ in the Peter Lee survey."],
    stats=[("$200K", "potential saving per event"), ("1st", "bank to POC Vision Pro"), ("32", "markets reachable")],
    related=["safety-sphere", "nib-cyber-assurance", "medibank-health-app"])

P["toll-movemaestro"] = dict(
    num="04", sub="A shared vision for how relocations should work, for customers, clients, staff and suppliers.",
    meta=[("Client", "Toll Group"), ("Type of work", "Service design &amp; strategy"),
          ("Date", "January – March 2025"), ("My role", "Experience designer")],
    intro="Toll Transitions relocates employees and their families for the ADF, Home Affairs and "
          "corporate clients. Its systems were holding the business back, technically and commercially.",
    sections=[
        ("The ask", ["Design the ideal moving experience in MoveMaestro for Toll's customers, clients, "
          "employees and suppliers."]),
        ("Our approach", ["<b>Understand:</b> interviewed staff and customers to test the target state "
          "and find the pain points.",
          "<b>Design:</b> low-fidelity flows for customers, Toll staff, clients and suppliers, reviewed "
          "with Toll's SMEs.",
          "<b>Prototype:</b> high-fidelity screens, technology recommendations and a high-level "
          "roadmap."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>A vision map</b> that showed every interaction in one place and gave stakeholders a "
          "clear direction.",
          "<b>Service and journey maps</b> the team used to agree on improvements and make decisions.",
          "<b>A high-fidelity prototype</b> that got clients excited."],
    stats=[("4", "user groups aligned"), ("1", "shared future vision"), ("3", "phase approach")],
    related=["vicroads-vehicle-transfer", "belong-north-star", "stringline-redesign"])

P["alfred-health-ml"] = dict(
    num="05", sub="Designing how clinicians would use a model that predicts blood transfusions.",
    meta=[("Client", "Alfred Health"), ("Type of work", "UX &amp; research"),
          ("Date", "June – July 2024"), ("My role", "UX designer")],
    intro="Alfred Health asked Mantel whether a machine learning model could predict which patients "
          "would need a red blood cell transfusion.",
    sections=[
        ("The ask", ["Part of the work was moving the data team from a largely manual, bespoke setup to "
          "Databricks, with a roadmap for their ML Ops.",
          "My part was the people using it: making the model's predictions clear enough for clinicians "
          "and analysts to trust."]),
        ("My role", None),
        ("The outcome", ["High-fidelity prototypes showing how clinicians would use the prediction "
          "service. They helped the team agree on direction and secure funding for the next phase."]),
    ],
    role=["Defined the problem with the client.",
          "Interviewed key users to understand their journey.",
          "Ran an ideation workshop with clinical and data stakeholders.",
          "Designed high-fidelity prototypes for the funding pitch."],
    outcome=None,
    stats=None,
    related=["nib-cyber-assurance", "medibank-health-app", "vicroads-learner-permit"])

P["safety-sphere"] = dict(
    num="06", sub="Mantel's first project designing for Apple Vision Pro.",
    meta=[("Client", "Mantel (internal R&amp;D)"), ("Type of work", "Spatial computing"),
          ("Date", "May – June 2024"), ("My role", "Designer")],
    intro="An internal project to build up Mantel's skills on Apple Vision Pro. We built a demo app to "
          "show clients what we could do in spatial computing.",
    sections=[
        ("The ask", ["We hadn't done client work in visionOS yet, so we needed a working demo of our own "
          "first."]),
        ("My role", None),
        ("The outcome", ["A working Vision Pro demo, built with our developers. It led to client work in "
          "spatial computing, including ANZ's Digital Expo."]),
    ],
    role=["Ran an ideation workshop with internal stakeholders.",
          "Storyboarded the experience.",
          "Designed the high-fidelity Vision Pro screens.",
          "Worked with the developers to ship the demo."],
    outcome=None,
    stats=None,
    related=["anz-vision-pro", "stringline-redesign", "alfred-health-ml"])

P["medibank-health-app"] = dict(
    num="07", sub="What if your body came with a service manual?",
    meta=[("Client", "Medibank Ventures"), ("Type of work", "Product &amp; UX"),
          ("Date", "April – May 2024"), ("My role", "UX designer · 3-week engagement")],
    intro="Medibank Ventures had an idea: what if your body came with a service manual? They brought me "
          "in to help show what a preventative health service could look like.",
    sections=[
        ("The ask", ["Over three weeks I worked with the Lead Product Designer and a GP from MyHealth "
          "Medical Centre to make the idea concrete enough to get stakeholders behind it."]),
        ("What I made", None),
        ("The outcome", ["A clickable, animated prototype, presented company-wide, that made an abstract "
          "idea feel like a product Medibank could build."]),
    ],
    role=["A journey map that follows someone from their health “service manual” to a booked "
          "preventative appointment.",
          "High-fidelity, animated screens for the whole journey, from learning about your health to "
          "booking a GP.",
          "The company-wide presentation used to bring more stakeholders on board."],
    outcome=None,
    stats=None,
    related=["alfred-health-ml", "vicroads-learner-permit", "nib-cyber-assurance"])

P["stringline-redesign"] = dict(
    num="08", sub="What started as a UI refresh became a rebuild of every flow, ahead of the MVP launch.",
    meta=[("Client", "Stringline"), ("Type of work", "Product &amp; UX"),
          ("Date", "February – April 2024"), ("My role", "Product designer")],
    intro="Stringline is a startup that helps tradespeople and small service businesses with quoting, "
          "invoicing and scheduling.",
    sections=[
        ("The ask", ["The app was about to launch, and the brief was to refresh the UI. Once I looked "
          "closely, the flows were the bigger problem: people had to work too hard to get simple things "
          "done. So we rebuilt them.",
          "I worked with the founder and their developer every day, using what we learned in user "
          "interviews and by walking through each task together."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>30+ flows</b> redesigned across web and mobile.",
          "<b>100+ screens</b> designed for the MVP.",
          "<b>38+ playbacks</b> with the founder in daily standups.",
          "<b>5 rounds of user testing</b> to check the flows before launch."],
    stats=[("30+", "flows redesigned"), ("100+", "screens designed"), ("5", "rounds of user testing")],
    related=["drive-marketplace", "toll-movemaestro", "safety-sphere"])

P["nib-cyber-assurance"] = dict(
    num="09", sub="A dashboard that helps nib's security team explain cyber risk to executives.",
    meta=[("Client", "nib"), ("Type of work", "Product &amp; research"),
          ("Date", "September – November 2023"), ("My role", "Associate designer")],
    intro="nib's cyber team found it hard to explain cyber risk to the business and its executives. "
          "They wanted a data-backed platform showing how well their controls were working.",
    sections=[
        ("The ask", ["Design a dashboard that lets a technical team brief non-technical executives, "
          "with the data still there for anyone who wants to dig in."]),
        ("My role", None),
        ("The outcome", ["The cyber team now uses a dashboard, built on nib's own data, to report the "
          "status of its controls to executives."]),
    ],
    role=["Interviewed the security team and its stakeholders.",
          "Created journey maps, personas and use cases for the dashboard.",
          "Built the story map and split the features into releases."],
    outcome=None,
    stats=None,
    related=["alfred-health-ml", "anz-vision-pro", "drive-marketplace"])

P["drive-marketplace"] = dict(
    num="10", sub="Running design sprints with Nine's product team to plan the next two years of Drive's marketplace.",
    meta=[("Client", "Nine (Drive.com.au)"), ("Type of work", "Research &amp; strategy"),
          ("Date", "June – September 2023"), ("My role", "Sprint lead &amp; coach · 4-week discovery")],
    intro="Drive is Australia's largest automotive content network, owned by Nine Entertainment. Its "
          "Cars 4 Sale and Sell My Car sections are key to growing the marketplace business.",
    sections=[
        ("The ask", ["A four-week discovery with Drive's design and product team, to rethink the "
          "marketplace experience for the next one to two years and build up their research skills "
          "along the way.",
          "The team included the CFO, Head of Product, a Senior Product Manager, a Product Lead and "
          "several designers."]),
        ("My role", None),
        ("The outcome", ["Hero journeys for both marketplace products, with future opportunities and "
          "user archetypes based on the research. These set Drive's product direction for the next two "
          "years."]),
    ],
    role=["Planned and ran design sprints based on the Google Design Sprint, coaching the team "
          "through each one.",
          "Helped produce two high-fidelity responsive web prototypes.",
          "Reviewed competitors to see which UX patterns worked best.",
          "Ran research and ideation workshops, and coached the team in human-centred methods.",
          "Ran two rounds of moderated user research, then synthesised the findings, wrote "
          "recommendations and played them back to stakeholders.",
          "Interviewed SMEs to understand the business and get stakeholders on the same page."],
    outcome=None,
    stats=[("4", "week discovery"), ("2", "hi-fi prototypes"), ("2", "rounds of user research")],
    related=["stringline-redesign", "vicroads-learner-permit", "belong-north-star"])

P["belong-north-star"] = dict(
    num="11", sub="A North Star for Belong's order-to-activate journey, and a shift toward designing around customers.",
    meta=[("Client", "Belong"), ("Type of work", "Service design &amp; strategy"),
          ("Date", "November 2022 – April 2023"), ("My role", "Experience designer")],
    intro="Belong asked Mantel for a North Star vision of the order-to-activate experience, to help the "
          "business put customers at the centre of how it designs and delivers.",
    sections=[
        ("The ask", ["Help Belong agree on what a great order-to-activate journey looks like, and feel "
          "confident about it."]),
        ("Our approach", ["<b>Research:</b> industry and competitor analysis, stakeholder workshops, and "
          "quantitative and qualitative customer research.",
          "<b>Define:</b> mapped the problems and opportunities in a Vision Experience Map.",
          "<b>Ideate:</b> workshops, concept generation and storyboards.",
          "<b>Prototype:</b> wireframes and prototypes for the ideas with the most business value.",
          "<b>Test:</b> several rounds of concept and usability testing."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>Experience principles</b> for every customer interaction, written with the business and "
          "tested with customers.",
          "<b>The Vision Experience Map:</b> the ideal order-to-activate journey from start to finish, with "
          "feature summaries, research and future opportunities. Belong can keep updating it.",
          "<b>Tested concepts and designs,</b> including detailed designs for the first release of eSIM "
          "ordering and activation. Other key journeys followed into delivery from there."],
    stats=None,
    related=["vicroads-vehicle-transfer", "toll-movemaestro", "drive-marketplace"])

# ---------- templates ----------

NAV = """  <header class="nav" id="top">
    <a class="nav__name" href="../index.html">Maurizio&nbsp;Lamanna</a>
    <nav class="nav__links" aria-label="Primary">
      <a href="../index.html#about">About</a>
      <a href="../index.html#work">Work</a>
      <a href="../index.html#cv">CV</a>
      <a href="../index.html#contact">Contact</a>
    </nav>
  </header>"""

FOOTER = """  <footer class="footer" id="contact">
    <p class="footer__eyebrow reveal">Get in touch</p>
    <a class="footer__email reveal" href="mailto:maurizio.lamanna@mantelgroup.com.au">maurizio.lamanna@mantelgroup.com.au</a>
    <div class="footer__cols reveal">
      <div><span>Based in</span><p>Sydney, Australia</p></div>
      <div><span>Elsewhere</span><p><a href="https://www.linkedin.com/">LinkedIn</a></p></div>
      <div><span>Colophon</span><p>Set in Montserrat, Mulish &amp; Lora</p></div>
    </div>
    <div class="footer__base reveal">
      <p>© 2026 Maurizio Lamanna</p>
      <a href="#top">Back to top ↑</a>
    </div>
  </footer>"""

def related_card(slug):
    c = CARDS[slug]
    return f"""      <li class="card reveal">
        <a href="{slug}.html" aria-label="Case study: {re.sub('<[^>]+>', '', c['title'])}">
          <div class="card__media {c['colour']}">
            {c['svg']}
          </div>
          <div class="card__meta">
            <h3>{c['title']}</h3>
            <p>{c['tagline']}</p>
          </div>
        </a>
      </li>"""

def section_html(heading_, paras, role, outcome):
    out = [f'    <h2>{heading_}</h2>']
    if paras:
        for p_ in paras:
            if p_.startswith("<ul>"):
                out.append(f'    {p_}')
            elif p_.startswith("<b>"):
                out.append(f'    <ul class="case-list"><li>{p_}</li></ul>' if False else f'    <ul class="case-list">{"".join(f"<li>{x}</li>" for x in [p_])}</ul>')
            else:
                out.append(f'    <p>{p_}</p>')
    return "\n".join(out)

def build(slug):
    c, p = CARDS[slug], P[slug]
    plain_title = re.sub("<[^>]+>", "", c["title"]).replace("&amp;", "&")
    hero_cls = c["colour"].replace("card__media--", "case-hero--")

    body = []
    for heading_, paras in p["sections"]:
        body.append(f'      <h2 class="reveal">{heading_}</h2>')
        if paras:
            # group consecutive <b>-led strings into one list
            buf = []
            def flush():
                if buf:
                    items = "".join(f"<li>{x}</li>" for x in buf)
                    body.append(f'      <ul class="case-list reveal">{items}</ul>')
                    buf.clear()
            for para in paras:
                if para.startswith("<b>"):
                    buf.append(para)
                elif para.startswith("<ul>"):
                    flush()
                    body.append(f'      <div class="reveal">{para.replace("<ul>", chr(39)*0 + "<ul class=" + chr(34) + "case-list" + chr(34) + ">")}</div>')
                else:
                    flush()
                    body.append(f'      <p class="reveal">{para}</p>')
            flush()
        elif heading_ in ("My role", "What we did", "What I made") and p.get("role"):
            items = "".join(f"<li>{x}</li>" for x in p["role"])
            body.append(f'      <ul class="case-list reveal">{items}</ul>')
        elif heading_ == "The outcome" and p.get("outcome"):
            items = "".join(f"<li>{x}</li>" for x in p["outcome"])
            body.append(f'      <ul class="case-list reveal">{items}</ul>')
            if p.get("stats"):
                cells = "".join(
                    f'<div class="case-stat"><strong>{n}</strong><span>{lbl}</span></div>'
                    for n, lbl in p["stats"])
                body.append(f'      <div class="case-stats reveal">{cells}</div>')
    body_html = "\n".join(body)

    meta_html = "".join(
        f'<div class="fact"><span>{k}</span><p>{v}</p></div>' for k, v in p["meta"])

    related_html = "\n".join(related_card(s) for s in p["related"])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{plain_title} — Maurizio Lamanna</title>
  <meta name="description" content="Case study: {plain_title}. {re.sub('<[^>]+>', '', p['sub'])}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Mulish:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Lora:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

{NAV}

  <section class="case-hero {hero_cls}">
    <a class="case-hero__back reveal" href="../index.html#work">← All work</a>
    <span class="card__index reveal">№ {p['num']}</span>
    {c['svg'].replace('<svg ', '<svg class="reveal" ')}
    <h1 class="reveal">{c['title']}</h1>
    <p class="case-hero__sub reveal">{p['sub']}</p>
  </section>

  <section class="case-meta reveal">
    {meta_html}
  </section>

  <article class="case-body">
    <p class="case-lede reveal">{p['intro']}</p>
{body_html}
  </article>

  <section class="section section--alt case-next">
    <div class="section__head reveal">
      <span class="section__num">Next</span>
      <h2>Explore similar projects</h2>
    </div>
    <ul class="grid grid--three">
{related_html}
    </ul>
  </section>

{FOOTER}

  <script src="../js/main.js"></script>
</body>
</html>
"""

for slug in SLUGS:
    with open(os.path.join(OUTDIR, f"{slug}.html"), "w") as f:
        f.write(build(slug))
    print("wrote", f"work/{slug}.html")
