from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
IMG_DIR = ROOT / "assets" / "img"
COVER_DIR = IMG_DIR / "covers"
PHOTO_SOURCE = WORKSPACE / "_resume_latex" / "photo_rect.png"


PALETTE = {
    "teal": "#14665f",
    "deep": "#0e4c47",
    "warm": "#a35c2a",
    "leaf": "#477a5b",
    "paper": "#f8faf9",
    "line": "#d8e0dc",
    "ink": "#22272b",
    "muted": "#626d75",
    "blue": "#416d86",
    "plum": "#6d5a7c",
}


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def wrap_text(draw, text, max_width, fnt):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def make_headshot():
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(PHOTO_SOURCE).convert("RGB")
    w, h = img.size
    target_ratio = 4 / 5
    crop_h = h
    crop_w = int(crop_h * target_ratio)
    if crop_w > w:
        crop_w = w
        crop_h = int(crop_w / target_ratio)
    left = max(0, (w - crop_w) // 2)
    top = max(0, int((h - crop_h) * 0.18))
    img = img.crop((left, top, left + crop_w, top + crop_h))
    img = img.resize((720, 900), Image.Resampling.LANCZOS)
    img.save(IMG_DIR / "yangming-zhang.jpg", quality=88, optimize=True)


def motif_poetry(draw, x0, y0, x1, y1, color):
    for i in range(7):
        x = x0 + 30 + i * 68
        draw.line((x, y0 + 45, x, y1 - 45), fill=color + "55", width=3)
    for i in range(42):
        row = i // 7
        col = i % 7
        x = x0 + 42 + col * 68
        y = y0 + 70 + row * 42
        draw.rounded_rectangle((x, y, x + 30, y + 8), radius=4, fill=color + "88")


def motif_blocks(draw, x0, y0, x1, y1, colors):
    size = 66
    for r in range(4):
        for c in range(5):
            if (r + c) % 2 == 0 or r == 3:
                x = x0 + 42 + c * (size + 13)
                y = y0 + 42 + r * (size + 11)
                draw.rounded_rectangle((x, y, x + size, y + size), radius=8, fill=colors[(r + c) % len(colors)])
                draw.ellipse((x + 18, y + 16, x + 48, y + 46), fill="#ffffff55")


def motif_network(draw, x0, y0, x1, y1, color):
    pts = [(x0 + 80, y0 + 80), (x0 + 220, y0 + 130), (x0 + 160, y0 + 260), (x0 + 380, y0 + 85), (x0 + 430, y0 + 250)]
    for a, b in [(0, 1), (1, 2), (1, 3), (3, 4), (2, 4), (0, 2)]:
        draw.line((*pts[a], *pts[b]), fill=color + "77", width=8)
    for x, y in pts:
        draw.ellipse((x - 22, y - 22, x + 22, y + 22), fill=color)
        draw.ellipse((x - 9, y - 9, x + 9, y + 9), fill="#ffffffaa")


def motif_archive(draw, x0, y0, x1, y1, colors):
    for r in range(3):
        for c in range(4):
            x = x0 + 48 + c * 104
            y = y0 + 45 + r * 78
            draw.rounded_rectangle((x, y, x + 78, y + 48), radius=4, fill=colors[(r * 4 + c) % len(colors)] + "bb")
            draw.line((x + 12, y + 14, x + 62, y + 14), fill="#ffffffaa", width=3)
            draw.line((x + 12, y + 28, x + 50, y + 28), fill="#ffffff88", width=3)


def motif_canon_map(draw, x0, y0, x1, y1, color):
    cards = [
        (x0 + 48, y0 + 58, "world"),
        (x0 + 252, y0 + 48, "canon"),
        (x0 + 120, y0 + 210, "memory"),
        (x0 + 312, y0 + 226, "review"),
    ]
    centers = [(x + 59, y + 29) for x, y, _ in cards]
    for a, b in [(0, 1), (1, 3), (3, 2), (2, 0), (0, 3)]:
        draw.line((*centers[a], *centers[b]), fill=color + "55", width=6)
    for x, y, label in cards:
        draw.rounded_rectangle((x, y, x + 118, y + 58), radius=10, fill="#ffffffee", outline=color + "99", width=4)
        draw.text((x + 16, y + 18), label, fill=color, font=font(16, bold=True))


def motif_scrapbook(draw, x0, y0, x1, y1, colors):
    pieces = [
        (x0 + 45, y0 + 46, 132, 86, colors[0]),
        (x0 + 218, y0 + 42, 122, 96, colors[1]),
        (x0 + 92, y0 + 188, 104, 82, colors[2]),
        (x0 + 282, y0 + 188, 132, 86, colors[3]),
    ]
    for i, (x, y, w, h, color) in enumerate(pieces):
        draw.rounded_rectangle((x, y, x + w, y + h), radius=10, fill=color + "cc")
        draw.rectangle((x + 16, y + 18, x + w - 16, y + 24), fill="#ffffff88")
        draw.rectangle((x + 16, y + 38, x + w - 34, y + 44), fill="#ffffff66")
        if i % 2 == 0:
            draw.ellipse((x + w - 38, y + h - 38, x + w - 18, y + h - 18), fill="#ffffff99")
    for x, y in [(x0 + 214, y0 + 170), (x0 + 372, y0 + 126), (x0 + 176, y0 + 102)]:
        draw.line((x - 18, y, x + 18, y), fill="#22272b55", width=4)
        draw.line((x, y - 18, x, y + 18), fill="#22272b55", width=4)


def make_cover(filename, label, title, accent, motif):
    COVER_DIR.mkdir(parents=True, exist_ok=True)
    w, h = 960, 540
    img = Image.new("RGB", (w, h), PALETTE["paper"])
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, w, h), fill=PALETTE["paper"])
    draw.rounded_rectangle((46, 42, w - 46, h - 42), radius=28, fill="#ffffff", outline=PALETTE["line"], width=2)

    motif_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    md = ImageDraw.Draw(motif_layer)
    if motif == "poetry":
        motif_poetry(md, 430, 86, 875, 390, accent)
    elif motif == "blocks":
        motif_blocks(md, 430, 92, 880, 405, [PALETTE["warm"], PALETTE["teal"], PALETTE["blue"], PALETTE["leaf"]])
    elif motif == "network":
        motif_network(md, 425, 105, 880, 410, accent)
    elif motif == "archive":
        motif_archive(md, 430, 105, 875, 400, [PALETTE["warm"], PALETTE["teal"], PALETTE["plum"], PALETTE["leaf"]])
    elif motif == "canon":
        motif_canon_map(md, 430, 105, 875, 400, accent)
    elif motif == "scrapbook":
        motif_scrapbook(md, 430, 105, 875, 400, [PALETTE["warm"], PALETTE["teal"], PALETTE["plum"], PALETTE["leaf"]])
    else:
        motif_network(md, 425, 105, 880, 410, accent)
    img = Image.alpha_composite(img.convert("RGBA"), motif_layer).convert("RGB")
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle((82, 84, 228, 118), radius=17, fill=accent)
    draw.text((104, 91), label.upper(), fill="#ffffff", font=font(15, bold=True))

    title_font = font(42, bold=True)
    subtitle_font = font(21, bold=False)
    y = 165
    for line in wrap_text(draw, title, 365, title_font)[:4]:
        draw.text((82, y), line, fill=PALETTE["ink"], font=title_font)
        y += 48
    draw.text((82, 414), "Yangming Zhang", fill=PALETTE["muted"], font=subtitle_font)
    draw.line((82, 450, 278, 450), fill=accent, width=5)

    img.save(COVER_DIR / filename, optimize=True, quality=92)


def main():
    make_headshot()
    covers = [
        ("artificial-wisdom.png", "IJHCI", "Artificial Wisdom", PALETTE["deep"], "canon"),
        ("pocketmuseum.png", "Manuscript", "PocketMuseum", PALETTE["leaf"], "archive"),
        ("co-teaching-ai.png", "BJET", "Co-teaching with AI", PALETTE["blue"], "network"),
        ("verse-listens-back.png", "CHI EA", "When Verse Listens Back", PALETTE["teal"], "poetry"),
        ("poemithy.png", "UbiComp", "Poemithy", PALETTE["warm"], "poetry"),
        ("poetic-comfort.png", "ASIS&T", "Poetic Comfort in Busy Life", PALETTE["plum"], "poetry"),
        ("bricksmart.png", "CHI", "BrickSmart", PALETTE["blue"], "blocks"),
        ("export-watercolours.png", "DSH", "Chinese Export Watercolours", PALETTE["leaf"], "archive"),
        ("sucho.png", "DHR", "Digital Heritage in Conflict Areas", PALETTE["deep"], "archive"),
        ("altair.png", "Project", "Altair", PALETTE["deep"], "canon"),
        ("trip-canvas.png", "Project", "Trip Canvas", PALETTE["leaf"], "scrapbook"),
        ("mindtrace.png", "Project", "MindTrace", PALETTE["plum"], "network"),
    ]
    for args in covers:
        if not (COVER_DIR / args[0]).exists():
            make_cover(*args)


if __name__ == "__main__":
    main()
