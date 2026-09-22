const fs = require('node:fs/promises');
const path = require('node:path');
const crypto = require('node:crypto');
const sharp = require('sharp');
const YAML = require('yaml');

const root = path.resolve(__dirname, '..');
const outputDir = path.join(root, 'assets', 'img', 'thumbnails');
const widths = [320, 640, 1080];

async function main() {
  const sources = new Map();
  for (const name of ['publications', 'projects']) {
    const items = YAML.parse(await fs.readFile(path.join(root, '_data', `${name}.yml`), 'utf8'));
    for (const item of items) {
      if (item.image) sources.set(item.image, item.image_full || item.image);
    }
  }

  await fs.mkdir(outputDir, { recursive: true });
  const manifest = {};
  let sourceBytes = 0;
  let previewBytes = 0;
  for (const [image, source] of sources) {
    const input = path.resolve(root, `.${source}`);
    if (!input.startsWith(`${path.join(root, 'assets', 'img')}${path.sep}`)) {
      throw new Error(`Image must be inside assets/img: ${source}`);
    }
    const bytes = await fs.readFile(input);
    const metadata = await sharp(bytes).metadata();
    const hash = crypto.createHash('sha256').update(bytes).digest('hex').slice(0, 10);
    const variants = [];
    // Width-only resizing preserves the entire figure, including tall diagrams.
    for (const width of [...new Set(widths.map(width => Math.min(width, metadata.width)))]) {
      const filename = `${path.parse(source).name}-${hash}-${width}.webp`;
      const info = await sharp(bytes)
        .resize({ width, withoutEnlargement: true })
        .webp({ quality: 82, effort: 6, smartSubsample: true })
        .toFile(path.join(outputDir, filename));
      variants.push({ path: `/assets/img/thumbnails/${filename}`, width: info.width, height: info.height, bytes: info.size });
    }
    const preview = variants.find(variant => variant.width >= 640) || variants.at(-1);
    manifest[image] = { source, width: metadata.width, height: metadata.height, preview, variants };
    sourceBytes += (await fs.stat(path.resolve(root, `.${image}`))).size;
    previewBytes += preview.bytes;
  }

  await fs.writeFile(path.join(root, '_data', 'image_thumbnails.json'), `${JSON.stringify(manifest, null, 2)}\n`);
  console.log(`${sources.size} images: ${(sourceBytes / 1024 / 1024).toFixed(2)} MiB -> ${(previewBytes / 1024 / 1024).toFixed(2)} MiB at 640px (${(100 * (1 - previewBytes / sourceBytes)).toFixed(1)}% smaller)`);
}

main().catch(error => { console.error(error); process.exitCode = 1; });
