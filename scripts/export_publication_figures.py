"""Render complete PDF figures, including vector labels and overlaid images."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = [
    ("*Verse*.pdf", 3, (52, 83, 558, 304), "verse-listens-back-figure-1"),
    ("*BrickSmart.pdf", 1, (72, 173, 506, 350), "bricksmart-figure-1"),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--pdftoppm", required=True)
    parser.add_argument("--watercolours-source", required=True, type=Path)
    parser.add_argument("--ffmpeg", required=True)
    parser.add_argument("--output-dir", type=Path,
                        default=ROOT / "assets/img/covers")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for pattern, page, box, name in FIGURES:
        matches = list(args.source_dir.glob(pattern))
        if len(matches) != 1:
            raise ValueError(f"Expected one source for {pattern}, found {len(matches)}")
        source = matches[0]
        x0, y0, x1, y1 = box
        output = args.output_dir / name
        # Poppler composites the full page before clipping the figure bounds.
        subprocess.run([
            args.pdftoppm, "-f", str(page), "-l", str(page),
            "-r", "288", "-x", str(x0 * 4), "-y", str(y0 * 4),
            "-W", str((x1 - x0) * 4), "-H", str((y1 - y0) * 4),
            "-singlefile", "-png", str(source), str(output),
        ], check=True)
        records.append({
            "file": output.with_suffix(".png").name,
            "source": source.name,
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "page": page, "figure": 1, "box_points": box, "dpi": 288,
        })

    output = args.output_dir / "export-watercolours-figure-10.png"
    # The author's TIFF has intact outer labels; the publisher's JPEG clips them.
    subprocess.run([
        args.ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(args.watercolours_source), "-frames:v", "1",
        str(output),
    ], check=True)
    thumbnail = args.output_dir / "export-watercolours-figure-10-thumb.png"
    subprocess.run([
        args.ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(output), "-vf", "scale=1200:-1:flags=lanczos",
        "-frames:v", "1", str(thumbnail),
    ], check=True)
    records.append({
        "file": output.name,
        "thumbnail": thumbnail.name,
        "source": args.watercolours_source.name,
        "source_sha256": hashlib.sha256(args.watercolours_source.read_bytes()).hexdigest(),
        "figure": 10,
        "method": "Author's complete radial-map TIFF; lossless PNG conversion",
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
    })
    print(json.dumps(records, indent=2))


if __name__ == "__main__":
    main()
