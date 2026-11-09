# Yangming Zhang Academic Homepage

Jekyll academic homepage for GitHub Pages.

Live site: https://jadpp.github.io/

Repository: https://github.com/JAdpp/JAdpp.github.io

## Local build

This machine may need Ruby first. When Ruby and Bundler are available:

```powershell
bundle install
bundle exec jekyll serve
```

## Deployment

Deploy from the `main` branch of `JAdpp/JAdpp.github.io` using GitHub Pages. No custom domain is configured.

## CV

The CV is generated from `scripts/generate_public_cv.py` and excludes phone number, direct email, and application-specific wording.

## Image previews

Publication and project `image` paths remain the source images. Optional `image_full` paths select a higher-resolution source for enlargement. After changing those images or adding entries, regenerate the committed WebP previews:

```powershell
npm ci
npm run build:thumbnails
```

The script reads both YAML files, resizes without cropping, and writes 320px, 640px, and 1080px variants plus `_data/image_thumbnails.json`. Content-hashed filenames refresh browser caches when the source changes. The browser selects a preview through `srcset`; the lightbox requests the original only on click. Node is used only for preparing assets, not by GitHub Pages or site visitors.

## Game-card motion previews

Only the English and Chinese Games & Interaction pages load the silent previews.
Each loop uses 1.25 seconds of the title cover, verified project footage,
and 1.25 seconds of the title cover. Preview files use H.264 MP4 rather than GIF
for smaller transfers. The 640px variant serves narrow layouts and the 960px
variant serves desktop cards; no audio track is included.

`assets/js/project-previews.js` waits until a card is visible before adding a
video source. Reduced-motion, Save-Data, and slow-connection visitors keep the
static cover unless they explicitly play. Off-screen and background-tab videos
pause, manual pauses persist, and failed playback falls back to the cover.
Altair and dsh-whale-galgame remain static until verified motion footage exists.
OUTBREAK NIGHT uses a PV excerpt, clearly labeled PV highlights rather than gameplay.
Its opening and closing typography uses language-specific previews: English-only on
the English page, with the original bilingual title card preserved on the Chinese page.
Optional `preview_mp4_zh` and `preview_mp4_small_zh` select the Chinese media;
other projects fall back to their shared footage. English project titles omit
Chinese parenthetical names. Publication author names retain their original
English spelling on both languages, including the author highlight.
The development recording can be newer than the linked playable prototype.

To prepare another loop from a verified recording:

```sh
scripts/build_game_preview.sh title-cover.png gameplay.mp4 assets/video/preview-name
node --test scripts/tests/project-previews.test.cjs
```

Keep source recordings outside this public repository. Do not substitute concept
art animation, staged screenshots, or cutscenes for footage labeled gameplay.
