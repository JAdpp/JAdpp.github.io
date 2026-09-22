const sharp = require('sharp');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const inputDir = path.resolve(process.argv[2] || path.join(root, 'assets/img/institutions'));
const rucSource = process.argv[3];
if (!rucSource) throw new Error('Usage: node scripts/normalize_cv_seals.cjs <source-directory> <official-ruc-seal.png>');

async function normalize(name, source) {
  const { data, info } = await sharp(source).flatten({ background: '#ffffff' }).removeAlpha().raw().toBuffer({ resolveWithObject: true });
  let left = info.width, top = info.height, right = -1, bottom = -1;
  // The five seals use colored ink. Ignore white margins and the RUC guide's gray frame.
  for (let y = 0; y < info.height; y++) {
    for (let x = 0; x < info.width; x++) {
      const offset = (y * info.width + x) * info.channels;
      const rgb = [data[offset], data[offset + 1], data[offset + 2]];
      if (Math.max(...rgb) - Math.min(...rgb) < 20) continue;
      left = Math.min(left, x); top = Math.min(top, y);
      right = Math.max(right, x); bottom = Math.max(bottom, y);
    }
  }
  if (right < left || bottom < top) throw new Error(`No colored seal found: ${source}`);
  const padding = 4;
  left = Math.max(0, left - padding); top = Math.max(0, top - padding);
  right = Math.min(info.width - 1, right + padding); bottom = Math.min(info.height - 1, bottom + padding);
  const bounds = { left, top, width: right - left + 1, height: bottom - top + 1 };
  if (Math.abs(bounds.width / bounds.height - 1) > 0.08) throw new Error(`Expected a circular seal: ${name}`);
  const output = path.join(root, 'assets/img/institutions', `${name}-seal.png`);
  await sharp(source).extract(bounds)
    .resize(256, 256, { fit: 'contain', background: '#ffffff' })
    .flatten({ background: '#ffffff' }).png().toFile(output);
  console.log(name, bounds);
}

(async () => {
  for (const [name, file] of [['whu', 'whu.png'], ['pku', 'pku.png'], ['tsinghua', 'tsinghua.jpg'], ['cas', 'cas.png']]) {
    await normalize(name, path.join(inputDir, file));
  }
  await normalize('ruc', path.resolve(rucSource));
})().catch(error => { console.error(error); process.exitCode = 1; });
