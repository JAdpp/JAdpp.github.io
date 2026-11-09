const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const YAML = require('yaml');
const projects = YAML.parse(fs.readFileSync('_data/projects.yml', 'utf8'));
test('English project titles contain no Chinese parentheticals; Chinese names remain', () => {
  for (const project of projects) {
    assert.doesNotMatch(project.title, /[\u3400-\u9fff]/);
    assert.ok(project.title_zh);
  }
});
test('Outbreak preview has separate English and original Chinese assets', () => {
  const project = projects.find(p => p.title === 'RESIDENT EVIL: OUTBREAK NIGHT');
  for (const key of ['preview_mp4','preview_mp4_small','preview_mp4_zh','preview_mp4_small_zh']) assert.ok(fs.existsSync('.' + project[key]));
  assert.notEqual(project.preview_mp4, project.preview_mp4_zh);
  const template = fs.readFileSync('_includes/project-preview.html','utf8');
  assert.match(template, /project.preview_mp4_zh \| default: preview_src/);
  assert.match(template, /<noscript><a href="{{ preview_src_small/);
});
test('Publication author names are not translated in Chinese layout', () => {
  const template = fs.readFileSync('_includes/publication-list.html','utf8');
  assert.doesNotMatch(template, /list_ui.names/);
  assert.match(template, /pub.authors \| escape/);
  assert.match(template, /assign author_name = site.author.name/);
});
