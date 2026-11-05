const test = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const code = fs.readFileSync(path.join(__dirname, '../../assets/js/project-previews.js'), 'utf8');
function setup({ reduced = false, saveData = false, small = false, observer = true, rejectPlay = false, delayedPlay = false } = {}) {
  const events = {}, motionEvents = {}, listeners = {}, attrs = {}, buttonAttrs = {}, classes = new Set(), pending = [];
  const video = { paused: true, dataset: { src: '/large.mp4', srcSmall: '/small.mp4' }, loadCalls: 0, playCalls: 0,
    getAttribute(k) { return k === 'aria-label' ? 'Gameplay' : attrs[k]; },
    set src(v) { attrs.src = v; }, load() { this.loadCalls++; },
    play() {
      this.playCalls++;
      if (rejectPlay) return Promise.reject(Error('NotAllowedError'));
      this.paused = false;
      if (delayedPlay) return new Promise((resolve, reject) => pending.push({ resolve, reject }));
      return Promise.resolve();
    },
    pause() { this.paused = true; }, addEventListener(k,v) { listeners[k] = v; } };
  const button = { hidden: true, dataset: { playLabel:'Play', pauseLabel:'Pause' },
    setAttribute(k,v) {buttonAttrs[k] = v;}, addEventListener(k,v) {listeners['button:'+k]=v;} };
  const card = { querySelector: s => s.includes('video') ? video : button,
    classList: { add: v => classes.add(v), remove: v => classes.delete(v) } };
  const motion = {matches:reduced, addEventListener(k,v) {motionEvents[k]=v;} };
  const document = {hidden:false, querySelectorAll: () => [card], addEventListener(k,v) {events[k]=v;} };
  let intersection;
  const window = {matchMedia: q => q.includes('reduced') ? motion : {matches:small}};
  const ctx = {document, window, navigator:{connection:{saveData,effectiveType:'4g',addEventListener(){}}}};
  if (observer) ctx.IntersectionObserver = window.IntersectionObserver = class {constructor(cb){intersection=cb;} observe() {}};
  vm.runInNewContext(code, ctx);
  const settle = () => new Promise(r => setImmediate(r));
  return { video, button, attrs, buttonAttrs, classes, document, motion, pending, settle,
    async visible(value=true) {intersection([{target:card,isIntersecting:value,intersectionRatio:value?1:0}]);await settle();},
    async click() {listeners['button:click']();await settle();},
    async hidden(value) {document.hidden=value;events.visibilitychange();await settle();},
    async reduced(value) {motion.matches=value;motionEvents.change();await settle();},
    error() {listeners.error();} };
}
test('no request before visibility; small variant on mobile', async () => {
  const s=setup({small:true}); assert.equal(s.attrs.src,undefined); assert.equal(s.button.hidden,false);
  await s.visible(); assert.equal(s.attrs.src,'/small.mp4'); assert.equal(s.video.paused,false); assert.equal(s.video.loadCalls,1); assert.equal(s.video.muted,true);
  await s.visible(false); assert.equal(s.video.paused,true);
  await s.visible(); assert.equal(s.video.loadCalls,1);
});
test('reduced motion remains static until explicit play; new preference stops it', async () => {
  const s=setup({reduced:true}); await s.visible(); assert.equal(s.attrs.src,undefined);
  await s.click(); assert.equal(s.video.paused,false);
  await s.reduced(true); assert.equal(s.video.paused,true);assert.equal(s.classes.has('is-playing'),false);
});
test('Save-Data does not autoplay', async () => {const s=setup({saveData:true}); await s.visible();assert.equal(s.attrs.src,undefined);await s.click();assert.equal(s.video.paused,false);});
test('manual pause persists across scrolling and tab hiding', async () => {
  const s=setup();await s.visible();await s.click();assert.equal(s.video.paused,true);
  await s.visible(false);await s.visible();await s.hidden(true);await s.hidden(false);assert.equal(s.video.paused,true);
  await s.click();assert.equal(s.video.paused,false);await s.hidden(true);assert.equal(s.video.paused,true);
});
test('autoplay rejection and media error keep poster', async () => {
  const s=setup({rejectPlay:true});await s.visible();assert.equal(s.classes.has('is-playing'),false);assert.equal(s.buttonAttrs['aria-pressed'],'false');
  const t=setup();await t.visible();t.error();assert.equal(t.classes.has('is-playing'),false);
});
test('without IntersectionObserver waits for user', async () => {const s=setup({observer:false});assert.equal(s.attrs.src,undefined);await s.click();assert.equal(s.video.paused,false);});
test('stale play rejection cannot pause a newer successful play', async () => {
  const s=setup({delayedPlay:true}); await s.visible(); await s.visible(false); await s.visible();
  assert.equal(s.pending.length,2); s.pending[1].resolve(); await s.settle();
  assert.equal(s.video.paused,false); assert.equal(s.classes.has('is-playing'),true);
  s.pending[0].reject(Error('old interrupted play')); await s.settle();
  assert.equal(s.video.paused,false); assert.equal(s.classes.has('is-playing'),true); assert.equal(s.buttonAttrs['aria-pressed'],'true');
});
test('stale play resolution cannot undo an explicit pause', async () => {
  const s=setup({delayedPlay:true}); await s.visible(); await s.click();
  assert.equal(s.video.paused,true); s.pending[0].resolve(); await s.settle();
  assert.equal(s.video.paused,true); assert.equal(s.classes.has('is-playing'),false); assert.equal(s.buttonAttrs['aria-pressed'],'false');
});
