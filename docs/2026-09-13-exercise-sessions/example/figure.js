// The figure: one set of joint angles drives both the 2D and the 3D view.
// Angles are absolute degrees in the sagittal plane (0 right, 90 up).

export const LEN = { torso: 0.30, neck: 0.05, head: 0.055, upper: 0.16, fore: 0.15, thigh: 0.24, shin: 0.24, foot: 0.06 };

const rad = d => d * Math.PI / 180;
const step = (a, b) => (b - a + 540) % 360 - 180;     // shortest signed arc
function lerpAngle(a, b, u) { return a + step(a, b) * u; }
const ease = u => u * u * (3 - 2 * u);                  // smoothstep between keyframes

/** Interpolated joint angles at phase u in [0,1) of one repetition. */
export function poseAt(move, u, mirror = false) {
  const kf = move.keyframes;
  let i = 0;
  while (i < kf.length - 2 && u >= kf[i + 1].t) i++;
  const a = kf[i], b = kf[i + 1];
  const w = ease(Math.min(1, Math.max(0, (u - a.t) / (b.t - a.t || 1))));
  const mix = (x, y) => Array.isArray(x) ? x.map((v, k) => lerpAngle(v, y[k], w)) : lerpAngle(x, y, w);
  const p = {};
  for (const k of ['torso', 'head', 'armL', 'armR', 'legL', 'legR']) p[k] = mix(a[k], b[k]);
  if (mirror) { [p.armL, p.armR] = [p.armR, p.armL]; [p.legL, p.legR] = [p.legR, p.legL]; }
  let dy = 0;
  if (move.rootMotion) {
    const rm = move.rootMotion; let j = 0;
    while (j < rm.length - 2 && u >= rm[j + 1][0]) j++;
    const ww = ease((u - rm[j][0]) / (rm[j + 1][0] - rm[j][0] || 1));
    dy = rm[j][1] + (rm[j + 1][1] - rm[j][1]) * ww;
  }
  return { ...p, root: [move.root[0], move.root[1] + dy] };
}

/** World-space segments [{name, side, a:[x,y], b:[x,y], w}] for a pose. */
export function skeleton(p) {
  const seg = [];
  const go = (from, ang, len) => [from[0] + Math.cos(rad(ang)) * len, from[1] + Math.sin(rad(ang)) * len];
  const hip = p.root;
  const shoulder = go(hip, p.torso, LEN.torso);
  const neckEnd = go(shoulder, p.head, LEN.neck);
  const headC = go(neckEnd, p.head, LEN.head);
  seg.push({ name: 'torso', side: 'C', a: hip, b: shoulder, w: 0.085 });
  seg.push({ name: 'head', side: 'C', a: headC, b: headC, w: LEN.head * 2 });
  for (const side of ['L', 'R']) {
    const [ua, fa] = p['arm' + side];
    const elbow = go(shoulder, ua, LEN.upper), hand = go(elbow, fa, LEN.fore);
    seg.push({ name: 'upper', side, a: shoulder, b: elbow, w: 0.055 });
    seg.push({ name: 'fore', side, a: elbow, b: hand, w: 0.048 });
    const [th, sh] = p['leg' + side];
    const knee = go(hip, th, LEN.thigh), ankle = go(knee, sh, LEN.shin);
    const foot = go(ankle, sh + 90, LEN.foot);        // toes point 'forward' of the shin
    seg.push({ name: 'thigh', side, a: hip, b: knee, w: 0.065 });
    seg.push({ name: 'shin', side, a: knee, b: ankle, w: 0.055 });
    seg.push({ name: 'foot', side, a: ankle, b: foot, w: 0.045 });
  }
  return seg;
}

// ---- 2D: an SVG in the site's palette; the far side is drawn lighter ------
/** A square window that holds every pose of the move, with a margin. */
export function frameFor(move) {
  let xs = [], ys = [];
  for (let i = 0; i <= 24; i++) for (const mirror of [false, true])
    for (const s of skeleton(poseAt(move, i / 24, mirror))) { xs.push(s.a[0], s.b[0]); ys.push(s.a[1], s.b[1]); }
  const m = 0.12, x0 = Math.min(...xs) - m, x1 = Math.max(...xs) + m, y0 = Math.min(0, ...ys) - 0.05, y1 = Math.max(...ys) + m;
  return { x0, y1, w: Math.max(x1 - x0, 0.8), h: Math.max(y1 - y0, 0.5) };
}

export function drawSVG(svg, seg, weightIn, frame) {
  const near = '#1F2A4D', far = '#9AA3BF';
  const W = frame ? frame.w : 1.9, H = frame ? frame.h : 1.15, x0 = frame ? frame.x0 : -0.95, y0 = frame ? frame.y1 : 1.10;
  // The viewBox follows the move's own proportions; the square stage letterboxes it (meet), so the figure is centred.
  svg.setAttribute('viewBox', `0 0 ${(100).toFixed(0)} ${(100 * H / W).toFixed(2)}`);
  const X = x => ((x - x0) / W * 100).toFixed(2), Y = y => ((y0 - y) / W * 100).toFixed(2);
  const order = seg.slice().sort((s, t) => (s.side === 'L') - (t.side === 'L')).reverse(); // L (far) first
  let out = `<line x1="0" y1="${Y(0)}" x2="100" y2="${Y(0)}" stroke="#D9DDE3" stroke-width="0.4"/>`;
  for (const s of order) {
    const col = s.side === 'L' ? far : near;
    if (s.name === 'head') { out += `<circle cx="${X(s.a[0])}" cy="${Y(s.a[1])}" r="${(LEN.head / W * 100).toFixed(2)}" fill="${col}"/>`; continue; }
    out += `<line x1="${X(s.a[0])}" y1="${Y(s.a[1])}" x2="${X(s.b[0])}" y2="${Y(s.b[1])}" stroke="${col}" stroke-width="${(s.w / W * 100).toFixed(2)}" stroke-linecap="round"/>`;
    if (weightIn && s.name === 'fore' && 'arm' + s.side === weightIn)
      out += `<rect x="${(+X(s.b[0]) - 2.2).toFixed(2)}" y="${(+Y(s.b[1]) - 0.5).toFixed(2)}" width="4.4" height="5" rx="0.8" fill="#C97B1E"/>`;
  }
  svg.innerHTML = out;
}
