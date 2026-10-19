#!/usr/bin/env python3
"""Generate case-study pages (modelled on hasbeck.com/portfolio/odds_and_ends.html)
for each Selected Work card in index.html. Reuses each card's isometric motif
and colour as the page hero."""

import re, os, html

ROOT = "/Users/mauriziolamanna/Desktop/VicRoads Designs VTS/maurizio-portfolio"
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
    num="01", sub="Escrow-backed vehicle transfers, designed end to end and proven buildable.",
    meta=[("Client", "VicRoads"), ("Type of work", "Service &amp; product design"),
          ("Date", "April – July 2026"), ("My role", "Design lead · 10-week discovery")],
    intro="A 10-week discovery to prove feasibility, size the effort and de-risk a production-grade "
          "Vehicle Transfer Service — the full buyer and seller experience through myVicRoads, wired "
          "into Shaype's escrow platform.",
    sections=[
        ("The ask", ["VicRoads wanted to know whether an escrow-backed vehicle transfer service could "
          "actually be built — and what it would take. Over ten weeks we designed and prototyped the "
          "full buyer/seller experience, sized the build effort, and packaged everything so it could "
          "go straight into a future business case.",
          "I led the design alongside three Lead Engineers, working shoulder-to-shoulder with VicRoads "
          "Product and Shaype's integration team."]),
        ("My role", None),
        ("The outcome", None),
    ],
    role=["<b>Experience mapping:</b> built the VTS Experience Map with VicRoads — a visual, "
          "high-level journey covering both buyer and seller, showing the flexibility in the overall design.",
          "<b>Golden path &amp; UX design:</b> designed the primary, secondary and tertiary paths across "
          "the end-to-end journey, alongside alternate flows and error scenarios.",
          "<b>Prototyping &amp; demo:</b> collaborated on a React Native demo — a key artefact for the "
          "future business case.",
          "<b>Requirements &amp; estimation:</b> gathered requirements across payments and the end-to-end "
          "design, aligning VicRoads and Shaype on edge cases upfront so nothing bites in the build phase.",
          "<b>Documentation for handover:</b> turned ten weeks of decisions into build-ready epic "
          "documentation — flows, rules and error states."],
    outcome=["<b>Proved the hardest part works:</b> designed and validated the Shaype escrow model end to "
          "end — funds locked in a joint account and split automatically across Seller, SRO, VicRoads "
          "and VTS Premium on handover.",
          "<b>Foundational documentation:</b> five epics covering flow steps, alternate flows and error "
          "scenarios, so the build team can hit the ground running.",
          "<b>Made it real, not theoretical:</b> a working React Native demo turned an abstract pitch into "
          "something stakeholders could hold and click through, surfacing UX and technical decisions while "
          "they were still cheap to change.",
          "<b>De-risked a multi-million dollar decision:</b> turned an ambition into a defensible "
          "effort-to-build number, with a recommended plan and team structure attached."],
    stats=[("10", "week discovery"), ("5", "build-ready epics"), ("4-way", "escrow payment split")],
    related=["vicroads-learner-permit", "toll-movemaestro", "belong-north-star"])

P["vicroads-learner-permit"] = dict(
    num="02", sub="Reimagining how Victorians learn to drive — mobile-first, with an AI companion.",
    meta=[("Client", "VicRoads"), ("Type of work", "Strategy &amp; product design"),
          ("Date", "November 2025 – February 2026"), ("My role", "Project lead · 8-week discovery")],
    intro="An 8-week discovery reimagining the Learner Permit Test and Hazard Perception Test experience, "
          "while identifying the future-proof platform the VicRoads test should move to.",
    sections=[
        ("The ask", ["Reimagine the LPT/HPT experience and recommend the right platform to design and "
          "build a mobile-first, frictionless test that is scalable, has a commercial outlook, and secures "
          "executive funding.",
          "Our team was myself as project lead, another senior designer and a tech lead, working closely "
          "with the VicRoads team — daily standups, multiple SME workshops and a weekly playback with "
          "high-level stakeholders to keep alignment from beginning to end."]),
        ("My role", None),
        ("The outcome", None),
    ],
    role=["<b>Stakeholder &amp; customer research:</b> ran six internal SME sessions and analysed customer "
          "feedback to identify pain points like language barriers and interface friction.",
          "<b>Experience mapping:</b> designed the Target State Experience — a six-stage strategic "
          "blueprint from research to final licence issuance.",
          "<b>Prototyping &amp; UI design:</b> delivered high-fidelity, mobile-first designs for both web "
          "and app.",
          "<b>Cross-functional collaboration:</b> partnered with technical leads to keep design solutions "
          "viable within the recommended Open edX hybrid platform."],
    outcome=["<b>The future-state experience map:</b> a strategic blueprint for the ideal journey, with "
          "future ideas like AI anti-cheat detection and online eye tests.",
          "<b>“Ask Lara” AI companion:</b> a smart assistant providing continuous learning, page-specific "
          "support and training that adapts to individual learning styles.",
          "<b>Road safety uplift:</b> research-backed features like “Results Wrapped” — turning personal "
          "assessment into community learning — and spaced repetition to combat knowledge decay.",
          "<b>Scalable, white-label framework:</b> a headless UI architecture with configuration-driven "
          "theming, ready to white-label for other jurisdictions like Service NSW.",
          "<b>Commercial sovereignty:</b> the open-source hybrid model gives VicRoads full IP ownership — "
          "significant cost savings and new revenue streams through reselling."],
    stats=[("8", "week discovery"), ("6", "SME research sessions"), ("6-stage", "target state blueprint")],
    related=["vicroads-vehicle-transfer", "drive-marketplace", "medibank-health-app"])

P["anz-vision-pro"] = dict(
    num="03", sub="One of Australia's first banking experiences in spatial computing.",
    meta=[("Client", "ANZ"), ("Type of work", "Spatial computing"),
          ("Date", "June – July 2025"), ("My role", "Experience designer")],
    intro="ANZ's institutional arm is the No. 1 institutional bank across Australia and New Zealand. To "
          "better engage key banking clients and showcase its digital roadmap, ANZ asked Mantel to "
          "reimagine its traditional banking expo.",
    sections=[
        ("The problem", ["As one of Australia's Big Four banks, ANZ operates across 32 markets and serves "
          "over 8.5 million customers. Its traditional expo format carried heavy logistical and cost "
          "burdens, and could only reach the people physically in the room. The goal: transform the event "
          "into a scalable, interactive experience."]),
        ("The design", ["We created a pioneering interactive experience for the Apple Vision Pro headset:",
          "<ul><li>Hyper-engaging, guided scenarios led by an AI avatar.</li>"
          "<li>A dynamic Interactive Expo Map — a 3D representation of the event.</li>"
          "<li>A Virtual Theatrette where remote customers watch keynote speakers.</li></ul>",
          "The entire concept was designed to be scalable and adaptable — specific pitches, different "
          "expos, any market."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>Enhanced customer experience:</b> real-life examples and guided scenarios lift engagement "
          "beyond what a physical booth can do.",
          "<b>Broader reach:</b> the interactive demo was showcased at the SIBOS conference — making ANZ "
          "the first bank to complete a proof of concept with the technology.",
          "<b>Scalable framework:</b> ANZ can now run the expo anytime, anywhere, with potential savings "
          "of up to $200,000 per physical event.",
          "<b>Strategic advantage:</b> a “game changer” platform with competitive upside, including a "
          "potential Peter Lee survey win."],
    stats=[("$200K", "potential saving per event"), ("1st", "bank to POC Vision Pro"), ("32", "markets reachable")],
    related=["safety-sphere", "nib-cyber-assurance", "medibank-health-app"])

P["toll-movemaestro"] = dict(
    num="04", sub="A target-state vision for relocations that aligned four user groups around one experience.",
    meta=[("Client", "Toll Group"), ("Type of work", "Service design &amp; strategy"),
          ("Date", "January – March 2025"), ("My role", "Experience designer")],
    intro="Toll Transitions manages employee and family relocations for the ADF, Home Affairs and "
          "corporate businesses. Existing systems were insufficient — posing technical and commercial "
          "risks to future growth.",
    sections=[
        ("The ask", ["Create a target-state vision and ideal moving experience for Toll customers, "
          "clients, employees and suppliers using MoveMaestro."]),
        ("Our approach", ["<b>Capture the vision:</b> validated the target-state experience through "
          "internal and customer interviews, addressing pain points and opportunities.",
          "<b>Create the experience:</b> low-fidelity designs for the Customer, Toll, Client and Supplier "
          "flows, aligned with Toll SMEs.",
          "<b>Bring it to life:</b> high-fidelity screens of the target state, technology "
          "recommendations, and a high-level roadmap."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>The vision map:</b> gave stakeholders a clear strategic direction and a holistic view of "
          "every interaction — the anchor for alignment.",
          "<b>The service &amp; journey map:</b> enabled practical alignment on improvements, supported "
          "informed decision-making and drove strategic discussions.",
          "<b>High-fidelity prototype &amp; screens:</b> a tangible representation of the future "
          "experience that generated real excitement among clients."],
    stats=[("4", "user groups aligned"), ("1", "shared future vision"), ("3", "phase approach")],
    related=["vicroads-vehicle-transfer", "belong-north-star", "stringline-redesign"])

P["alfred-health-ml"] = dict(
    num="05", sub="Making a machine-learning model usable — and fundable.",
    meta=[("Client", "Alfred Health"), ("Type of work", "UX &amp; research"),
          ("Date", "June – July 2024"), ("My role", "UX designer")],
    intro="Alfred Health engaged Mantel to explore whether a machine-learning model could predict which "
          "patients would need a red blood cell transfusion.",
    sections=[
        ("The ask", ["The project involved uplifting the data analytics team's approach to ML Ops and "
          "providing a roadmap to migrate them from a bespoke, largely manual solution onto a scalable "
          "Databricks implementation.",
          "The design challenge: make a highly technical prediction model legible and trustworthy for "
          "the clinicians and analysts who would rely on it."]),
        ("My role", None),
        ("The outcome", ["High-fidelity prototypes that showed what the prediction service could look "
          "like in clinicians' hands — clear enough to align the team and compelling enough to help "
          "secure future funding for the program."]),
    ],
    role=["Defined the problem together with the client.",
          "Understood the user journey through interviews with key users.",
          "Facilitated an ideation workshop across clinical and data stakeholders.",
          "Delivered high-fidelity prototypes used to secure future funding."],
    outcome=None,
    stats=None,
    related=["nib-cyber-assurance", "medibank-health-app", "vicroads-learner-permit"])

P["safety-sphere"] = dict(
    num="06", sub="Mantel's first foray into designing for Apple Vision Pro.",
    meta=[("Client", "Mantel — internal R&amp;D"), ("Type of work", "Spatial computing"),
          ("Date", "May – June 2024"), ("My role", "Designer")],
    intro="An internal initiative to uplift Mantel's capability on Apple Vision Pro — our first demo app "
          "built to show clients what we can design and deliver in spatial computing.",
    sections=[
        ("The ask", ["Before ANZ, before client work in visionOS, we needed our own proof: a working "
          "demo experience that showed we could take spatial computing from idea to hardware."]),
        ("My role", None),
        ("The outcome", ["A working Vision Pro demo, delivered with our development team — the "
          "capability foundation that later won and shaped client engagements in spatial computing, "
          "including ANZ's Digital Expo."]),
    ],
    role=["Aligned internal stakeholders through an ideation workshop.",
          "Created the storyboard for the proposed experience.",
          "Delivered high-fidelity Vision Pro designs.",
          "Collaborated with the development team to ship a working demo."],
    outcome=None,
    stats=None,
    related=["anz-vision-pro", "stringline-redesign", "alfred-health-ml"])

P["medibank-health-app"] = dict(
    num="07", sub="What if your body came with a service manual?",
    meta=[("Client", "Medibank Ventures"), ("Type of work", "Product &amp; UX"),
          ("Date", "April – May 2024"), ("My role", "UX designer · 3-week engagement")],
    intro="Medibank Ventures had a great question: what if your body came with a service manual? I was "
          "engaged to help create a vision and visual narrative around preventative health.",
    sections=[
        ("The ask", ["Over three weeks I worked closely with the Lead Product Designer, in consultation "
          "with a GP from the MyHealth Medical Centre, to make the concept tangible enough to win "
          "stakeholder buy-in."]),
        ("What I made", None),
        ("The outcome", ["A company-wide presentation that put a clickable, animated future in front of "
          "wider stakeholders — turning an abstract preventative-health concept into something people "
          "could see themselves shipping."]),
    ],
    role=["A user journey map showing a health journey — the “service manual” — leading into a booked, "
          "pre-scheduled preventative appointment.",
          "Designed, prototyped and animated high-fidelity screens of the entire journey, from uncovering "
          "your health story to booking a GP appointment.",
          "Created the company-wide presentation used to bring wider stakeholders on board."],
    outcome=None,
    stats=None,
    related=["alfred-health-ml", "vicroads-learner-permit", "nib-cyber-assurance"])

P["stringline-redesign"] = dict(
    num="08", sub="From UI uplift to a ground-up rebuild of every flow — in time for MVP launch.",
    meta=[("Client", "Stringline"), ("Type of work", "Product &amp; UX"),
          ("Date", "February – April 2024"), ("My role", "Product designer")],
    intro="Stringline is a startup helping sole traders and businesses in trades and services streamline "
          "their business — quoting, invoicing and scheduling.",
    sections=[
        ("The ask", ["With the app's release imminent, the original ask was a UI uplift of the existing "
          "screens. On closer examination, the flows demanded a lot of cognitive effort and exploration "
          "for users to achieve what they needed — so the engagement became a rebuild.",
          "Working side-by-side with the client and their developer, flows were rebuilt from findings "
          "from user interviews and from stepping through user objectives together."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>30+ flows</b> reimagined and optimised across web and mobile.",
          "<b>100+ screens</b> designed for the MVP.",
          "<b>38+ client playbacks</b> as part of daily standups — decisions made with the founder, not "
          "for them.",
          "<b>5 user tests</b> to provide direction and validate flows before launch."],
    stats=[("30+", "flows reimagined"), ("100+", "screens designed"), ("5", "rounds of user testing")],
    related=["drive-marketplace", "toll-movemaestro", "safety-sphere"])

P["nib-cyber-assurance"] = dict(
    num="09", sub="Turning cyber-risk data into a conversation executives can actually have.",
    meta=[("Client", "nib"), ("Type of work", "Product &amp; research"),
          ("Date", "September – November 2023"), ("My role", "Associate designer")],
    intro="The nib cyber team were struggling to communicate cyber risks to the business and its "
          "executives. They wanted a continuous assurance platform, backed by data, that could carry the "
          "conversation about the effectiveness of cyber controls.",
    sections=[
        ("The ask", ["Design the dashboard experience that would let a technical security team brief "
          "non-technical executives — without losing the data underneath."]),
        ("My role", None),
        ("The outcome", ["The nib cyber team now have a cyber security dashboard backed by the data "
          "within their organisation, used to communicate the status of cyber controls to the "
          "executive."]),
    ],
    role=["Performed user interviews across the security team and its stakeholders.",
          "Created journey maps, personas and business use cases for the dashboard.",
          "Built the story map and feature list, divided into releases."],
    outcome=None,
    stats=None,
    related=["alfred-health-ml", "anz-vision-pro", "drive-marketplace"])

P["drive-marketplace"] = dict(
    num="10", sub="Coaching Nine's product team through design sprints for the marketplace's next two years.",
    meta=[("Client", "Nine — Drive.com.au"), ("Type of work", "Research &amp; strategy"),
          ("Date", "June – September 2023"), ("My role", "Sprint lead &amp; coach · 4-week discovery")],
    intro="Drive is Australia's largest automotive content network, owned by Nine Entertainment. Cars 4 "
          "Sale and Sell My Car are the consumer-facing sections crucial to generating green shoots for "
          "the marketplace business.",
    sections=[
        ("The ask", ["A four-week discovery to support Drive's UX research and design capability — "
          "partnering with their UI design and product team to reimagine the customer experience and "
          "features of the marketplace for the next one to two years.",
          "The cross-functional team ran deep: CFO, Head of Product, a Senior Product Manager, Product "
          "Lead, digital designers and UX/UI designers."]),
        ("My role", None),
        ("The outcome", ["Hero journeys for the two marketplace products — ideal customer experiences "
          "and further opportunities — plus user archetypes grounded in the research, setting Drive's "
          "product direction for the next two years."]),
    ],
    role=["Planned, executed and coached the Drive team through agile design sprints, modelled on the "
          "Google Design Sprint methodology.",
          "Supported production of two high-fidelity responsive web prototypes.",
          "Conducted an industry review of key competitors to identify optimal UX patterns.",
          "Led research techniques and ideation workshops, coaching the team on human-centred methods.",
          "Planned and executed two rounds of moderated user research — synthesis, design "
          "recommendations and stakeholder playbacks.",
          "Interviewed key SMEs for contextual understanding and stakeholder alignment."],
    outcome=None,
    stats=[("4", "week discovery"), ("2", "hi-fi prototypes"), ("2", "rounds of user research")],
    related=["stringline-redesign", "vicroads-learner-permit", "belong-north-star"])

P["belong-north-star"] = dict(
    num="11", sub="A North Star vision that pivoted Belong toward customer-centric design and delivery.",
    meta=[("Client", "Belong"), ("Type of work", "Service design &amp; strategy"),
          ("Date", "November 2022 – April 2023"), ("My role", "Experience designer")],
    intro="Belong engaged Mantel to create a North Star vision for the order-to-activate customer "
          "experience — helping pivot the organisation towards a more customer-centric approach to design "
          "and delivery.",
    sections=[
        ("The ask", ["Help Belong gain confidence and alignment on what an ideal, customer-centric "
          "order-to-activate journey looks like."]),
        ("Our approach", ["<b>Empathise:</b> extensive research, industry and competitor analysis, "
          "stakeholder workshops, and quantitative and qualitative customer research.",
          "<b>Define:</b> mapped challenges and opportunities through a Vision Experience Map.",
          "<b>Ideate:</b> ideation workshops, concept canvassing, concept generation and storyboarding.",
          "<b>Prototype:</b> wireframed and prototyped the high-value business ideas.",
          "<b>Validate:</b> multiple rounds of concept and usability testing."]),
        ("The outcome", None),
    ],
    role=None,
    outcome=["<b>Experience principles:</b> guiding principles that underpin and measure every customer "
          "interaction with Belong — created with the business and validated through customer testing.",
          "<b>The Vision Experience Map:</b> a holistic, end-to-end view of the ideal order-to-activate "
          "journey — feature summaries, supporting research and future opportunities. Designed as a "
          "living document that matures as Belong does.",
          "<b>Validated concepts and designs:</b> future-state concepts plus granular designs for the "
          "first release of the eSIM ordering and activation experience — the foundation for other key "
          "journeys to go into delivery."],
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
  <meta name="description" content="Case study: {plain_title} — {re.sub('<[^>]+>', '', p['sub'])}">
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
