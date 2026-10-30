// The same skeleton as capsules in three.js, so the move can be orbited.
import * as THREE from 'three';
import { OrbitControls } from './vendor/three/OrbitControls.js';
import { LEN } from './figure.js';

export function makeScene(canvas) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio));
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(32, 1, 0.05, 20);
  camera.position.set(1.6, 0.75, 2.1); camera.lookAt(0, 0.5, 0);
  const controls = new OrbitControls(camera, canvas); controls.target.set(0, 0.5, 0); controls.enableDamping = true;
  scene.add(new THREE.HemisphereLight(0xfbfaf7, 0x8a8f9a, 1.1));
  const sun = new THREE.DirectionalLight(0xffffff, 1.2); sun.position.set(2, 3, 2); scene.add(sun);
  const floor = new THREE.Mesh(new THREE.CircleGeometry(1.1, 48), new THREE.MeshStandardMaterial({ color: 0xF3F0E8 }));
  floor.rotation.x = -Math.PI / 2; scene.add(floor);
  scene.add(new THREE.GridHelper(2.2, 11, 0xD9DDE3, 0xE8EBEF));
  const near = new THREE.MeshStandardMaterial({ color: 0x1F2A4D, roughness: 0.6 });
  const far = new THREE.MeshStandardMaterial({ color: 0x5B6690, roughness: 0.6 });
  const amber = new THREE.MeshStandardMaterial({ color: 0xC97B1E, roughness: 0.5 });
  const pool = new Map();
  function capsule(key, a, b, w, z, mat) {
    let m = pool.get(key);
    const len = Math.hypot(b[0] - a[0], b[1] - a[1]);
    // Segment lengths are constant, so each capsule is built once at its size.
    if (!m) { m = new THREE.Mesh(new THREE.CapsuleGeometry(w / 2, Math.max(len - w, 0.01), 4, 12), mat); scene.add(m); pool.set(key, m); }
    m.material = mat;
    m.position.set((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, z);
    const dir = new THREE.Vector3(b[0] - a[0], b[1] - a[1], 0).normalize();
    m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), len > 0 ? dir : new THREE.Vector3(0, 1, 0));
    return m;
  }
  function draw(seg, weightIn) {
    for (const s of seg) {
      const z = s.side === 'L' ? -0.075 : s.side === 'R' ? 0.075 : 0;
      const mat = s.side === 'L' ? far : near;
      if (s.name === 'head') {
        let h = pool.get('head');
        if (!h) { h = new THREE.Mesh(new THREE.SphereGeometry(LEN.head, 20, 16), near); scene.add(h); pool.set('head', h); }
        h.position.set(s.a[0], s.a[1], 0); continue;
      }
      capsule(s.name + s.side, s.a, s.b, s.w, z, mat);
      if (weightIn && s.name === 'fore' && 'arm' + s.side === weightIn) {
        let k = pool.get('weight');
        if (!k) { k = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.11, 0.06), amber); scene.add(k); pool.set('weight', k); }
        k.visible = true; k.position.set(s.b[0], s.b[1] - 0.06, z);
      }
    }
    if (!weightIn && pool.get('weight')) pool.get('weight').visible = false;
  }
  function resize() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (canvas.width !== w || canvas.height !== h) { renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
  }
  function render() { resize(); controls.update(); renderer.render(scene, camera); }
  return { draw, render };
}
