# CV institution logos

Verified 2026-09-22 against current institutional websites and brand guidance. These assets identify institutions in existing CV entries, not endorsements. Official artwork colors and proportions are preserved. Circular seals have excess surrounding whitespace removed and are fitted to 256px white canvases; horizontal wordmarks are kept as vectors. All use `object-fit: contain`.

| File | Source |
| --- | --- |
| `whu-seal.png` | [Official identity page](https://www.whu.edu.cn/xxgk/wdbs.htm), standard two-color PNG from [seal archive](https://www.whu.edu.cn/new2024/wdbsxz/xiaohui.zip); original retained as `whu.png` |
| `ucl-2026.svg` | [Current full-colour logo](https://cdn.ucl.ac.uk/logos/ucl/ucl-logo--primary.svg), checked against [UCL logo guidelines](https://www.ucl.ac.uk/brand-and-experience/brand/visual-guidelines/logo/logo-guidelines). Replaces the older Indigo portico favicon. |
| `pku-seal.png` | [Peking University website touch icon](https://www.pku.edu.cn/pku_logo_red.png); original retained as `pku.png` |
| `tsinghua-seal.png` | Complete embedded `Image78.jpg` from p. 15 of [Tsinghua University statutes](https://www.tsinghua.edu.cn/__local/C/B6/1C/5682B1124834BFE4B7BB43744CF_C7C409E3_C2FAA.pdf), Appendix 1; only outside whitespace removed from `tsinghua.jpg` |
| `ruc-seal.png` | Red seal from the [official identity page](https://www.ruc.edu.cn/xuexiaobiaozhi1924747550510977025.html), [source image](https://www.ruc.edu.cn/template/1/out/imgs/VI/1.png). The surrounding guide frame is not part of the seal. Replaces the gold seal-and-name composition. |
| `cas-seal.png` | [Chinese Academy of Sciences website touch icon](https://www.cas.cn/lib/images/favicon.png); original retained as `cas.png` |
| `vam-wordmark.svg` | Unchanged paths and viewBox of the `valogo` symbol in the [current V&A homepage SVG sprite](https://www.vam.ac.uk/assets/vam-sprite-336679439415943192abd08310316502cdd2edb65ff20acfeb4bd8ed7ce9287d.svg). Extracted with an XML parser into a standalone SVG. Replaces the turquoise touch-icon tile, not a claim of a new logo design. |

Personal projects and entries without an explicit institution retain text-only presentation.

## Sizing

Desktop seals share a 52px image box; mobile seals use 44px. Horizontal marks have a separate 76px / 60px width allowance so that lettering remains legible without stretching. The institution column and logo panel stay fixed within each breakpoint, regardless of artwork shape.

## Recreating the raster exports

Run `node scripts/normalize_cv_seals.cjs assets/img/institutions <downloaded-ruc-source.png>` after `npm ci`. The script finds the colored artwork bounds, retains a small antialiasing margin, checks that each seal is approximately square, and resizes without changing colors or aspect ratio. Earlier source assets remain for reproducibility but are not referenced by the CV.
