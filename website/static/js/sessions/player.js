import moves from './moves.js';
import plans from './plans.js';

const $ = id => document.getElementById(id);
addEventListener('error', e => { $('cue').textContent = 'Error: ' + e.message; });

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

let steps = [], idx = -1, stepStart = 0, paused = false, pausedAt = 0, running = false, previewMove = 'dead-bug';
const video = $('clip'), rest = $('rest');
const ac = window.AudioContext ? new AudioContext() : null;
function beep(f = 660, ms = 120) {
  if (!ac) return; const o = ac.createOscillator(), g = ac.createGain();
  o.frequency.value = f; g.gain.value = 0.08; o.connect(g); g.connect(ac.destination); o.start(); o.stop(ac.currentTime + ms / 1000);
}
const fmt = s => { s = Math.max(0, Math.ceil(s)); return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`; };

function show(id) {
  const m = moves[id];
  const src = `/static/video/sessions/${id}.mp4`;
  if (!video.src.endsWith(src)) { video.src = src; video.play().catch(() => {}); }
  $('badge').textContent = m.family;
  $('name').textContent = m.name; $('cue').textContent = m.cue;
}

function goto(i) {
  idx = i; stepStart = performance.now();
  if (idx >= steps.length) { finish(); return; }
  const st = steps[idx];
  $('block').textContent = st.block;
  if (st.type === 'rest') {
    $('name').textContent = 'Rest'; $('cue').textContent = `Drink some water. Next: ${st.next}.`; $('reps').textContent = '';
    $('badge').textContent = 'One minute'; rest.hidden = false; video.pause();
    document.body.classList.add('resting'); beep(440, 200);
  } else { rest.hidden = true; show(st.move); video.play().catch(() => {}); document.body.classList.remove('resting'); beep(660, 120); }
  $('next').textContent = st.next ? `Next: ${st.next}` : '';
  drawProgress();
}

function drawProgress() {
  const total = steps.reduce((a, s) => a + s.seconds, 0);
  $('progress').innerHTML = steps.map((s, i) => {
    const cls = s.type + (i < idx ? ' done' : i === idx ? ' now' : '');
    return `<i class="${cls}" style="width:${s.seconds / total * 100}%" title="${s.type === 'rest' ? 'Rest' : moves[s.move].name}"></i>`;
  }).join('');
}

function finish() {
  running = false; document.body.classList.remove('resting', 'running'); rest.hidden = true;
  $('name').textContent = 'Done'; $('cue').textContent = 'That is the session. Write down what was easy and what was not.';
  $('reps').textContent = ''; $('timer').textContent = '0:00'; $('next').textContent = ''; beep(880, 300);
}

function tick(now) {
  requestAnimationFrame(tick);
  if (!running || paused) return;
  const st = steps[idx]; const elapsed = (now - stepStart) / 1000; const left = st.seconds - elapsed;
  $('timer').textContent = fmt(left);
  if (st.type === 'work') {
    const m = moves[st.move];
    if (m.hold) $('reps').textContent = `${fmt(left)} to go`;
    else { const total = Math.floor(st.seconds / m.tempo); $('reps').textContent = `${Math.min(total, Math.floor(elapsed / m.tempo))} of ${total} reps`; }
  }
  if (left <= 3 && left > 2.9) beep(520, 80);
  if (left <= 0) goto(idx + 1);
}

$('start').onclick = () => {
  if (ac && ac.state === 'suspended') ac.resume();
  steps = timeline(plans[$('length').value]); running = true; paused = false;
  document.body.classList.add('running'); goto(0);
};
$('pause').onclick = () => {
  if (!running) return;
  paused = !paused; $('pause').textContent = paused ? 'Resume' : 'Pause';
  if (paused) { pausedAt = performance.now(); video.pause(); } else { stepStart += performance.now() - pausedAt; video.play(); }
};
$('skip').onclick = () => { if (running) goto(idx + 1); };
$('stop').onclick = () => { running = false; document.body.classList.remove('running', 'resting'); rest.hidden = true; show(previewMove); video.play().catch(() => {}); $('block').textContent = 'Preview'; $('reps').textContent = ''; $('timer').textContent = ''; $('next').textContent = ''; $('progress').innerHTML = ''; $('pause').textContent = 'Pause'; paused = false; };
const sel = $('preview');
for (const [id, m] of Object.entries(moves)) sel.append(new Option(`${m.name} — ${m.family}`, id));
sel.onchange = () => { previewMove = sel.value; if (!running) show(previewMove); };
sel.value = previewMove; show(previewMove); $('block').textContent = 'Preview';
requestAnimationFrame(tick);
const q = new URLSearchParams(location.search);
if (['30', '45', '60'].includes(q.get('start'))) { $('length').value = q.get('start'); $('start').click(); const at = parseInt(q.get('at') || '0', 10); if (at > 0 && at < steps.length) goto(at); }
