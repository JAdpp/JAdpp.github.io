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
