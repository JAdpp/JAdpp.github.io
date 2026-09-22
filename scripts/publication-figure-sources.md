# Publication cover sources

The three covers below were visually compared with their complete source figures
on 2026-09-22. Use `export_publication_figures.py` to reproduce them.

| Cover | Source | Export |
| --- | --- | --- |
| `verse-listens-back-figure-1.png` | When Verse Listens Back, supplied CHI EA PDF, p. 3, Figure 1 | Render the complete PDF region at 288 dpi. Include all three interface panels and the seven-step workflow. |
| `bricksmart-figure-1.png` | Supplied BrickSmart PDF, p. 1, Figure 1 | Render the complete PDF region at 288 dpi. Include headings, dialogue, arrows, and labels over the illustration. |
| `export-watercolours-figure-10.png` | Author's `figures/Figure_9.tif`, radial CIT tree (Figure 10 in the published article) | Convert the complete 6279 x 6354 TIFF to PNG without cropping or resizing. |

The radial map also has a 1200px-wide `-thumb.png`, downscaled proportionally
without cropping. `image_full` points to the full-resolution version for zooming.

Do not extract a single embedded image from a layered PDF figure: that can omit
vector text, arrows, and overlaid screenshots. Crop only after PDF compositing.
The watercolour article's online JPEG has clipped outer labels; use the author's
TIFF instead. The export script reports source hashes and crop coordinates.

After regenerating, compare the images visually with the source pages and verify
both the thumbnail and enlarged view. Image dimensions and HTTP success alone do
not establish figure completeness.
