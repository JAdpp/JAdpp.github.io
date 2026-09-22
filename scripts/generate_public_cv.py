from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "files" / "Yangming_Zhang_Public_CV.pdf"

FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("TimesNewRoman", str(FONT_DIR / "times.ttf")))
pdfmetrics.registerFont(TTFont("TimesNewRoman-Bold", str(FONT_DIR / "timesbd.ttf")))
pdfmetrics.registerFont(TTFont("TimesNewRoman-Italic", str(FONT_DIR / "timesi.ttf")))


PROFILE = (
    "Ph.D. student in the School of Information Management at Wuhan University and a student researcher "
    "at the Intelligent Computing Laboratory for Cultural Heritage (ICLCH). I study human-AI collaboration, "
    "culturally grounded multimodal LLM agents, AI for mental wellbeing and education, digital cultural heritage, "
    "and AI-native games."
)


EDUCATION = [
    (
        "Wuhan University",
        "Ph.D. student, School of Information Management / ICLCH",
        "2024-Present",
        "Research on human-AI collaboration, intelligent computing for digital cultural heritage, and AI-native applications.",
    ),
    (
        "University College London (UCL)",
        "M.Sc. Digital Humanities, Department of Information Studies",
        "2022-2023",
        "Distinction; Top 1; Dissertation Showcase; Faculty of Arts and Humanities Dean's List.",
    ),
    (
        "Wuhan University",
        "B.Sc., School of Information Management",
        "2015-2019",
        "GPA 85/100; nominated for Excellent Undergraduate Thesis; Excellent Student Researcher.",
    ),
]


RESEARCH_EXPERIENCE = [
    (
        "Department of Information Management, Peking University",
        "Visiting student",
        "Sep 2025-Jan 2026",
        "",
    ),
    (
        "MindTrace, Future Laboratory, Tsinghua University",
        "Research intern",
        "2025",
        "Designed thought-visualization approaches for creative problem solving in a multi-agent educational system; contributed to system prototyping and evaluation planning.",
    ),
    (
        "V&A Chinese Export Watercolours Digitization and Computational Analysis",
        "Research assistant / project researcher",
        "2022-2023",
        "Worked with the Victoria and Albert Museum collection: transcribed 5,000+ corpus records, prepared 300 metadata records, digitized 3,000+ paintings, and supported computational classification into 22 thematic categories.",
    ),
    (
        "Generative AI for Digital Content Curation in Cultural Heritage",
        "M.Sc. dissertation, UCL",
        "2023",
        "Built a prototype combining GPT-3.5 and DALL-E 2 for virtual-exhibition curation and developed a mixed evaluation framework for generated cultural-heritage content.",
    ),
    (
        "BrickSmart, Future Laboratory, Tsinghua University",
        "Research intern",
        "2024",
        "Supported prompt design, multimodal model testing, Python/Django development, deployment, and user-study preparation for a family block-play learning system.",
    ),
    (
        "Digital Humanities Institute, Renmin University of China",
        "Student researcher",
        "2023-2024",
        "Produced digital-humanities review reports and helped plan and organize an academic salon on AI agents.",
    ),
    (
        "National Science Library, Chinese Academy of Sciences",
        "Science exhibition curation and implementation intern",
        "2024",
        "Developed a Coze-based agent workflow for science communication, curated 60 CAS WeChat posts, and contributed to a strategic proposal for the 15th Five-Year Plan.",
    ),
]


PUBLICATIONS = [
    "Yangming Zhang, Zhiqian Li, Bin Wu, Qi Li, Jie Xu, Yunpeng Song, and Liang Zhao. When Verse Listens Back: Classical Chinese Poetry as a Culturally Grounded Medium for Multimodal AI-Guided Emotional Support. CHI EA 2026.",
    "Jin Gao, Yangming Zhang, Jiawei Liu, and Jose Pedro Sousa. A digital humanities approach to Chinese export watercolours: a case study on the Victoria and Albert Museum Collection. Digital Scholarship in the Humanities, 41(2), 692-714, 2026.",
    "Yangming Zhang*, Bin Wu*, Zihan Zeng, Jie Xu, Yunpeng Song, and Liang Zhao. Poemithy: Leveraging Multimodal LLMs for Emotional Healing through Classical Chinese Poetry. UbiComp/ISWC Companion 2025. (*Co-first authors.)",
    "Yangming Zhang, Liang Zhao, and Jie Xu. \"It Helps Me Find Poetic Comfort in My Busy Life\": A Multimodal LLM-Based Classical Chinese Poetry Therapy System Framework. ASIS&T Annual Meeting 2025.",
    "Yujia Liu*, Siyu Zha*, Yuewen Zhang, Yanjin Wang, Yangming Zhang, Qi Xin, Lunyiu Nie, Chao Zhang, and Yingqing Xu. BrickSmart: Leveraging Generative AI to Support Children's Spatial Language Learning in Family Block Play. CHI 2025. (*Co-first authors.)",
    "Yangming Zhang. Digital Cultural Heritage Preservation Practices in Conflict Areas: The Case of Saving Ukrainian Cultural Heritage Online. Digital Humanities Research, 3(03), 49-58, 2023. In Chinese.",
]


PROJECTS = [
    (
        "Poemithy / Classical Chinese Poetry Therapy",
        "2024-Present",
        "A multimodal LLM interaction system that connects poetic interpretation, dialogue, and visual expression for culturally grounded emotional support.",
        "https://github.com/JAdpp",
    ),
    (
        "dsh-whale-galgame",
        "2026-Present",
        "An open-source multi-model visual-novel plugin for DeepSeek Harness, with character-aware routing, persistent state, and interactive story extensions.",
        "https://github.com/JAdpp/dsh-whale-galgame",
    ),
    (
        "Co-Created Travel Journal (Trip Canvas)",
        "2026-Present",
        "An open-source agent skill for turning travel materials into editable visual journals, object manifests, layout plans, and mini-comics.",
        "https://github.com/JAdpp/trip-canvas",
    ),
    (
        "Mengdie Ji",
        "2026-Present",
        "A culturally grounded interactive narrative project exploring dream, memory, and classical literary motifs through agent-assisted storytelling.",
        "https://github.com/JAdpp/myth-ritual-demo",
    ),
    (
        "Woyou",
        "2026-Present",
        "An AI-assisted cultural-heritage curation project for organizing, interpreting, and presenting digital materials as exploratory exhibits.",
        "https://github.com/JAdpp/inquiry-curator",
    ),
]


ADDITIONAL_EXPERIENCE = [
    (
        "Tsinghua University Library",
        "Multimedia Resources Services Librarian",
        "2021-2022",
        "Created metadata for vinyl records and multimedia resources, and supported reading promotion, video production, and user surveys.",
    ),
    (
        "Research on Chinese Academic Integrity Policy Data",
        "Research intern",
        "2017",
        "Collected academic norms and morality policies from 100+ institutions and contributed to a preliminary research dataset.",
    ),
    (
        "Application of Virtual Reality in Chinese Public Libraries",
        "Team leader",
        "2016-2017",
        "Led a four-student field-research team, conducted 500+ questionnaires and expert interviews, and produced a 20,000-word report with recommendations.",
    ),
    (
        "Wuhan Library, Chinese Academy of Sciences",
        "Intern leader",
        "2018",
        "Transcribed 500+ records and organized 10,000+ government-information records using Excel/VBA and improved label-code accuracy.",
    ),
]


HONORS = [
    "First-Class Academic Excellence Scholarship, School of Information Management, Wuhan University, 2025.",
    "First-Class Guangdong Xinhua Elite Scholarship, Wuhan University.",
    "UCL Faculty of Arts and Humanities Dean's List; Distinction / Top 1 in M.Sc. Digital Humanities; Dissertation Showcase, 2023.",
    "Merit Award, Global Digital Intelligence Education Innovation Competition; CDH2024 AIGC Excellent Project Award, for Poemithy.",
    "Excellent Graduation Thesis Nomination, Wuhan University, 2019; Excellent Practical Student Researcher, 2016.",
]


SKILLS = (
    "Programming and systems: Python, JavaScript, PHP, Django, LangChain, Dify, multimodal LLM application development, HTML/CSS, Git. "
    "Methods: human-AI collaboration research, user studies, mixed-methods evaluation, digital humanities data analysis. "
    "Languages: Chinese (native), English (fluent)."
)


def text(value):
    return escape(value, quote=False)


def author_text(value):
    escaped = text(value)
    return escaped.replace("Yangming Zhang", "<b>Yangming Zhang</b>")


def linked_label(label, url):
    return f'<link href="{escape(url, quote=True)}" color="#111111"><u>{text(label)}</u></link>'


def add_section(story, title, styles):
    story.append(Spacer(1, 3.4 * mm))
    story.append(Paragraph(text(title).upper(), styles["Section"]))
    story.append(Spacer(1, 0.7 * mm))
    story.append(HRFlowable(width="100%", thickness=0.45, color=colors.black, spaceBefore=0, spaceAfter=1.3 * mm))


def entry(title, meta, period, description, styles, link=None):
    heading = f"<b>{text(title)}</b>"
    if link:
        heading += f" &nbsp; {linked_label('link', link)}"
    content = heading + f"<br/><font color='#444444'>{text(meta)}</font>"
    if description:
        content += f"<br/>{text(description)}"
    left = Paragraph(content, styles["Entry"])
    right = Paragraph(text(period), styles["Date"])
    table = Table([[left, right]], colWidths=[152 * mm, 25 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2 * mm),
            ]
        )
    )
    return table


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("TimesNewRoman", 7.5)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawCentredString(A4[0] / 2, 8 * mm, f"Yangming Zhang  |  CV  |  {doc.page}")
    canvas.restoreState()


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=13 * mm,
        bottomMargin=13 * mm,
        title="Yangming Zhang CV",
        author="Yangming Zhang",
    )

    base = getSampleStyleSheet()
    styles = {
        "Name": ParagraphStyle(
            "Name", parent=base["Title"], fontName="TimesNewRoman-Bold", fontSize=22,
            leading=24, alignment=1, textColor=colors.black, spaceAfter=1.5 * mm,
        ),
        "Contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="TimesNewRoman", fontSize=8.3,
            leading=10, alignment=1, textColor=colors.HexColor("#222222"), spaceAfter=1.5 * mm,
        ),
        "Profile": ParagraphStyle(
            "Profile", parent=base["Normal"], fontName="TimesNewRoman", fontSize=9.1,
            leading=11.2, textColor=colors.black, spaceAfter=0,
        ),
        "Section": ParagraphStyle(
            "Section", parent=base["Heading2"], fontName="TimesNewRoman-Bold", fontSize=10.4,
            leading=12, textColor=colors.black, borderWidth=0, borderPadding=0,
            spaceAfter=0, keepWithNext=True,
        ),
        "Entry": ParagraphStyle(
            "Entry", parent=base["Normal"], fontName="TimesNewRoman", fontSize=8.25,
            leading=9.85, textColor=colors.black, spaceAfter=0,
        ),
        "Date": ParagraphStyle(
            "Date", parent=base["Normal"], fontName="TimesNewRoman", fontSize=8.1,
            leading=9.7, alignment=2, textColor=colors.HexColor("#555555"),
        ),
        "Publication": ParagraphStyle(
            "Publication", parent=base["Normal"], fontName="TimesNewRoman", fontSize=8.25,
            leading=9.9, textColor=colors.black, leftIndent=4.5 * mm, firstLineIndent=-4.5 * mm,
            spaceAfter=1.6 * mm,
        ),
        "Body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="TimesNewRoman", fontSize=8.5,
            leading=10.2, textColor=colors.black,
        ),
    }

    story = [
        Paragraph("Yangming Zhang", styles["Name"]),
        Paragraph(
            "Wuhan University | ICLCH | "
            + linked_label("Google Scholar", "https://scholar.google.com/citations?user=UUmf2HEAAAAJ")
            + " | "
            + linked_label("GitHub", "https://github.com/JAdpp")
            + " | "
            + linked_label("Homepage", "https://jadpp.github.io/"),
            styles["Contact"],
        ),
        Paragraph(PROFILE, styles["Profile"]),
    ]

    add_section(story, "Education", styles)
    for school, degree, period, note in EDUCATION:
        story.append(entry(school, degree + ". " + note, period, "", styles))

    add_section(story, "Research Experience", styles)
    for title, meta, period, description in RESEARCH_EXPERIENCE:
        story.append(entry(title, meta, period, description, styles))

    add_section(story, "Skills", styles)
    story.append(Paragraph(text(SKILLS), styles["Body"]))

    story.append(PageBreak())

    add_section(story, "Publications", styles)
    for item in PUBLICATIONS:
        story.append(Paragraph(f"- {author_text(item)}", styles["Publication"]))

    add_section(story, "Selected Projects", styles)
    for title, period, description, link in PROJECTS:
        story.append(entry(title, "Independent / collaborative project", period, description, styles, link=link))

    add_section(story, "Additional Experience", styles)
    for title, meta, period, description in ADDITIONAL_EXPERIENCE:
        story.append(entry(title, meta, period, description, styles))

    add_section(story, "Honors and Awards", styles)
    for item in HONORS:
        story.append(Paragraph(f"- {text(item)}", styles["Publication"]))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_pdf()
