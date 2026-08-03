from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "files" / "Yangming_Zhang_Public_CV.pdf"


PROFILE = (
    "Ph.D. student working on Human-AI Collaboration, multimodal LLM agents, "
    "cultural intelligence, and AI for Wellbeing. My work focuses on culturally "
    "situated human-AI collaboration in emotional support, education, and digital "
    "cultural heritage contexts, combining interactive system building, user "
    "studies, and mixed-methods evaluation."
)


EDUCATION = [
    (
        "Wuhan University",
        "Ph.D. Student, School of Information Management / Cultural Heritage Intelligent Computing Lab",
        "2024-Present",
        "Research interests: Human-AI Collaboration, intelligent computing for digital cultural heritage, AI-native applications.",
    ),
    (
        "University College London",
        "M.Sc. in Digital Humanities, Department of Information Studies",
        "2022-2023",
        "Distinction, Top 1; Dissertation Showcase; Faculty of Arts and Humanities Dean's List.",
    ),
    (
        "Wuhan University",
        "B.Sc., School of Information Management",
        "2015-2019",
        "GPA 85/100; nominated for Excellent Undergraduate Thesis; Excellent Student Researcher.",
    ),
]


PUBLICATIONS = [
    "Yangming Zhang, Zhiqian Li, Bin Wu, Qi Li, Jie Xu, Yunpeng Song, Liang Zhao. When Verse Listens Back: Classical Chinese Poetry as a Culturally Grounded Medium for Multimodal AI-Guided Emotional Support. CHI EA 2026. First author.",
    "Yangming Zhang*, Bin Wu*, Zihan Zeng, Jie Xu, Yunpeng Song, Liang Zhao. Poemithy: Leveraging Multimodal LLMs for Emotional Healing through Classical Chinese Poetry. UbiComp/ISWC Companion 2025. Co-first author.",
    "Yangming Zhang, Liang Zhao, Jie Xu. \"It Helps Me Find Poetic Comfort in My Busy Life\": A Multimodal LLM-Based Classical Chinese Poetry Therapy System Framework. ASIS&T Annual Meeting 2025. First author.",
    "Yujia Liu*, Siyu Zha*, Yuewen Zhang, Yanjin Wang, Yangming Zhang, Qi Xin, Lunyiu Nie, Chao Zhang, Yingqing Xu. BrickSmart: Leveraging Generative AI to Support Children's Spatial Language Learning in Family Block Play. CHI 2025. Co-author.",
    "Jin Gao, Yangming Zhang, Jiawei Liu, Jose Pedro Sousa. A digital humanities approach to Chinese export watercolours: a case study on the Victoria and Albert Museum Collection. Digital Scholarship in the Humanities, 41(2), 692-714, 2026. Second author.",
    "Yangming Zhang. Digital Cultural Heritage Preservation Practices in Conflict Areas: The Case of Saving Ukrainian Cultural Heritage Online. Digital Humanities Research, 3(03), 49-58, 2023. In Chinese. Sole author.",
]


PROJECTS = [
    (
        "Poemithy / Classical Chinese Poetry Therapy",
        "2024-Present",
        "Designed and evaluated a multimodal LLM-based interaction system for emotional support, exploring classical Chinese poetry as a culturally grounded medium. Related outputs include CHI EA 2026, UbiComp/ISWC Companion 2025, and ASIS&T 2025.",
    ),
    (
        "MindTrace, Future Laboratory, Tsinghua University",
        "2025",
        "Designed thought-visualization approaches for creative problem solving in a multi-agent educational system; contributed to system pipeline work, front-end/back-end prototyping, and evaluation planning.",
    ),
    (
        "BrickSmart, Future Laboratory, Tsinghua University",
        "2024",
        "Worked on prompt strategies, multimodal model/API testing, Python/Django back-end development, deployment, and offline user-study support for a parent-child spatial language learning system.",
    ),
    (
        "CuratorGPT",
        "2023",
        "Developed a generative curation prototype integrating language and image generation models, paired with a mixed-methods evaluation framework for virtual exhibition content.",
    ),
    (
        "V&A Chinese Export Watercolours Digitization and Computational Analysis",
        "2022-2023",
        "Worked with Chinese iconography data, open museum metadata, collection digitization, and computational analysis of Chinese export watercolours.",
    ),
]


SKILLS = [
    "LLM and agent systems: LangChain, Dify, Coze, prompt/context orchestration, multimodal API integration and testing.",
    "Programming and systems: Python, JavaScript, Django, SQL, HTML/CSS, Git, data processing, and cloud deployment.",
    "Research methods: Human-AI Collaboration research, user studies, system evaluation, mixed-methods analysis, and digital humanities data analysis.",
    "Design and content production: Photoshop, Illustrator, InDesign, Premiere, digital painting, and AIGC-based visual workflows.",
]


HONORS = [
    "First-Class Academic Excellence Scholarship, School of Information Management, Wuhan University, 2025.",
    "First-Class Guangdong Xinhua Elite Scholarship, School of Information Management, Wuhan University.",
    "Faculty of Arts and Humanities Dean's List, UCL; Distinction / Top 1 in M.Sc. Digital Humanities; Dissertation Showcase, 2023.",
]


def add_section(story, title, styles):
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(title, styles["Section"]))
    story.append(Spacer(1, 1.5 * mm))


def bullet(text, styles):
    return Paragraph(f"- {text}", styles["Bullet"])


def highlight_author(text):
    return text.replace("Yangming Zhang", "<b>Yangming Zhang</b>")


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title="Yangming Zhang CV",
        author="Yangming Zhang",
    )

    base = getSampleStyleSheet()
    styles = {
        "Name": ParagraphStyle(
            "Name",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=25,
            textColor=colors.HexColor("#0e4c47"),
            spaceAfter=2,
        ),
        "Subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            textColor=colors.HexColor("#626d75"),
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.1,
            textColor=colors.HexColor("#22272b"),
        ),
        "Section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12.5,
            leading=15,
            textColor=colors.HexColor("#14665f"),
            borderWidth=0,
            spaceAfter=2,
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.9,
            leading=11.5,
            leftIndent=0,
            textColor=colors.HexColor("#22272b"),
            spaceAfter=3,
        ),
        "Small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.4,
            leading=10.5,
            textColor=colors.HexColor("#626d75"),
        ),
    }

    story = [
        Paragraph("Yangming Zhang", styles["Name"]),
        Paragraph(
            "Ph.D. Student, School of Information Management, Wuhan University",
            styles["Subtitle"],
        ),
        Paragraph(
            "Cultural Heritage Intelligent Computing Lab / Wuhan, China",
            styles["Subtitle"],
        ),
        Paragraph(
            "Google Scholar: scholar.google.com/citations?user=UUmf2HEAAAAJ / GitHub: github.com/JAdpp",
            styles["Subtitle"],
        ),
        Spacer(1, 4 * mm),
        Paragraph(PROFILE, styles["Body"]),
    ]

    add_section(story, "Education", styles)
    edu_rows = []
    for school, degree, period, note in EDUCATION:
        edu_rows.append(
            [
                Paragraph(f"<b>{school}</b><br/>{degree}<br/><font color='#626d75'>{note}</font>", styles["Body"]),
                Paragraph(period, styles["Small"]),
            ]
        )
    table = Table(edu_rows, colWidths=[135 * mm, 30 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(table)

    add_section(story, "Selected Publications", styles)
    for item in PUBLICATIONS:
        story.append(bullet(highlight_author(item), styles))

    story.append(PageBreak())
    add_section(story, "Selected Projects", styles)
    for title, period, summary in PROJECTS:
        story.append(Paragraph(f"<b>{title}</b> ({period})", styles["Body"]))
        story.append(Paragraph(summary, styles["Bullet"]))

    add_section(story, "Technical and Research Skills", styles)
    for item in SKILLS:
        story.append(bullet(item, styles))

    add_section(story, "Honors and Awards", styles)
    for item in HONORS:
        story.append(bullet(item, styles))

    add_section(story, "Additional Experience", styles)
    additional = [
        "National Science Library, Chinese Academy of Sciences, Science Exhibition Curation and Implementation Intern, 2024.",
        "Digital Humanities Institute, Renmin University of China, Student Researcher, 2023-2024.",
        "Tsinghua University Library, Multimedia Resources Services Librarian, 2021-2022.",
    ]
    for item in additional:
        story.append(bullet(item, styles))

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
