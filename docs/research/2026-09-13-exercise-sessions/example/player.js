import { poseAt, skeleton, drawSVG, frameFor } from './figure.js';
import { makeScene } from './figure3d.js';
import moves from './moves.js';
import plans from './plans.js';

const $ = id => document.getElementById(id);
// Errors go on the page, not only the console: a local app has no server log.
addEventListener('error', e => { $('cue').textContent = 'Error: ' + e.message; });
addEventListener('unhandledrejection', e => { $('cue').textContent = 'Error: ' + (e.reason && e.reason.message || e.reason); });

// ---- timeline: work steps with a one-minute rest between blocks ----------
function timeline(plan) {
  const steps = [];
  plan.blocks.forEach((b, i) => {
    if (i > 0) steps.push({ type: 'rest', seconds: 60, block: b.name, next: moves[b.items[0][0]].name });
    b.items.forEach(([id, seconds], j) => {
      const next = b.items[j + 1] ? moves[b.items[j + 1][0]].name : (plan.blocks[i + 1] ? 'one minute of rest' : 'done');
      steps.push({ type: 'work', move: id, seconds, block: b.name, next });
    });
  });
  return steps;
}

// ---- state -----------------------------------------------------------------
let steps = [], idx = -1, stepStart = 0, paused = false, pausedAt = 0, running = false;
let view = '2d', three = null, previewMove = 'dead-bug';
const svg = $('fig2d'), canvas = $('fig3d');
const ac = window.AudioContext ? new AudioContext() : null;
function beep(f = 660, ms = 120) {
  if (!ac) return; const o = ac.createOscillator(), g = ac.createGain();
  o.frequency.value = f; g.gain.value = 0.08; o.connect(g); g.connect(ac.destination); o.start(); o.stop(ac.currentTime + ms / 1000);
}

function fmt(s) { s = Math.max(0, Math.ceil(s)); return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`; }

function showFigure(move, elapsed) {
  const u = (elapsed / move.tempo) % 1, rep = Math.floor(elapsed / move.tempo);
  const p = poseAt(move, u, move.alternate && rep % 2 === 1);
  const seg = skeleton(p);
  if (view === '2d') drawSVG(svg, seg, move.weightIn, move._frame || (move._frame = frameFor(move)));
  else { three.draw(seg, move.weightIn); three.render(); }
}

function goto(i) {
  idx = i; stepStart = performance.now();
  if (idx >= steps.length) { finish(); return; }
  const st = steps[idx];
  $('block').textContent = st.block;
  if (st.type === 'rest') {
    $('name').textContent = 'Rest'; $('cue').textContent = `Breathe. Next: ${st.next}.`; $('reps').textContent = '';
    document.body.classList.add('resting'); beep(440, 200);
  } else {
    const m = moves[st.move];
    $('name').textContent = m.name; $('cue').textContent = m.cue;
    document.body.classList.remove('resting'); beep(660, 120);
  }
  $('next').textContent = st.next ? `Next: ${st.next}` : '';
  drawProgress();
}

function drawProgress() {
  const total = steps.reduce((a, s) => a + s.seconds, 0);
  let acc = 0;
  $('progress').innerHTML = steps.map((s, i) => {
    const w = s.seconds / total * 100; const cls = s.type + (i < idx ? ' done' : i === idx ? ' now' : '');
    acc += w; return `<i class="${cls}" style="width:${w}%" title="${s.type === 'rest' ? 'Rest' : moves[s.move].name}"></i>`;
  }).join('');
}

function finish() {
  running = false; document.body.classList.remove('resting', 'running');
  $('name').textContent = 'Done'; $('cue').textContent = 'That is the session. Write down what was easy and what was not.'; $('reps').textContent = ''; $('timer').textContent = '0:00'; $('next').textContent = '';
  beep(880, 300);
}

function tick(now) {
  requestAnimationFrame(tick);
  if (!running) { // preview mode: loop the chosen move
    const m = moves[previewMove]; showFigure(m, now / 1000); return;
  }
  if (paused) return;
  const st = steps[idx]; const elapsed = (now - stepStart) / 1000;
  const left = st.seconds - elapsed;
  $('timer').textContent = fmt(left);
  if (st.type === 'work') {
    const m = moves[st.move]; showFigure(m, elapsed);
    const total = Math.floor(st.seconds / m.tempo), done = Math.min(total, Math.floor(elapsed / m.tempo));
    $('reps').textContent = m.tempo >= 2 ? `${done} of ${total} reps` : `${fmt(left)} to go`;
  } else {
    showFigure(moves['dead-bug'], 0); // a still figure while resting
  }
  if (left <= 3 && left > 2.9) beep(520, 80);
  if (left <= 0) goto(idx + 1);
}

// ---- controls --------------------------------------------------------------
$('start').onclick = () => {
  if (ac && ac.state === 'suspended') ac.resume();
  steps = timeline(plans[$('length').value]); running = true; paused = false;
  document.body.classList.add('running'); goto(0);
};
$('pause').onclick = () => {
  if (!running) return;
  paused = !paused; $('pause').textContent = paused ? 'Resume' : 'Pause';
  if (paused) pausedAt = performance.now(); else stepStart += performance.now() - pausedAt;
};
$('skip').onclick = () => { if (running) goto(idx + 1); };
$('stop').onclick = () => { running = false; document.body.classList.remove('running', 'resting'); $('name').textContent = moves[previewMove].name; $('cue').textContent = moves[previewMove].cue; $('reps').textContent = ''; $('timer').textContent = ''; $('next').textContent = ''; $('block').textContent = 'Preview'; $('progress').innerHTML = ''; };
$('view').onclick = async () => {
  if (view === '2d') {
    if (!three) three = makeScene(canvas);
    view = '3d'; svg.hidden = true; canvas.hidden = false; $('view').textContent = 'Show 2D';
  } else { view = '2d'; canvas.hidden = true; svg.hidden = false; $('view').textContent = 'Show 3D'; }
};
const sel = $('preview');
for (const [id, m] of Object.entries(moves)) if (!id.startsWith('_')) sel.append(new Option(`${m.name} — ${m.family}`, id));
sel.onchange = () => { previewMove = sel.value; if (!running) { $('name').textContent = moves[previewMove].name; $('cue').textContent = moves[previewMove].cue; } };
sel.value = previewMove; sel.onchange();
$('block').textContent = 'Preview';
requestAnimationFrame(tick);
// ?start=30 opens straight into a session; ?view=3d opens the mannequin.
const q = new URLSearchParams(location.search);
if (q.get('view') === '3d') $('view').click();
if (['30', '45', '60'].includes(q.get('start'))) { $('length').value = q.get('start'); $('start').click(); }
