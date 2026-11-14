// Script AI viet (luot chup Task 3 ngay 12/11/2026). Duong dan tuyet doi la cua may tac gia; chi de TA doc va doi chieu cach thuc hien.
import { spawn, execFileSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const CHROME_EXE = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const FIREFOX_EXE = process.env.LOCALAPPDATA + '/Microsoft/WindowsApps/firefox.exe';
const SNAP_HELPER = 'C:/Users/DUC THINH/.gemini/antigravity/brain/605f7d68-03dd-46d3-b449-da2c40542878/scratch/win_snap_helper.py';
const OUT_DIR = 'D:/KCPM/GUI_Usability_Testing/screenshots/task3_cross_platform';
const SCRATCH = 'C:/Users/DUC THINH/.gemini/antigravity/brain/605f7d68-03dd-46d3-b449-da2c40542878/scratch';
const STUDENT_STR = '23120199 - Huỳnh Đức Thịnh';
const DRY_RUN = process.env.DRY_RUN === '1';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function ensureSutRunning() {
  let spawned = [];
  let beUp = false;
  let feUp = false;
  try {
    const r = await fetch('http://127.0.0.1:3000/api/products');
    beUp = r.ok;
  } catch {}
  try {
    const r = await fetch('http://localhost:5173/');
    feUp = r.ok;
  } catch {}

  if (!beUp) {
    const be = spawn('node', ['server.js'], {
      cwd: 'D:/KCPM/GUI_Usability_Testing/eshop-sut/backend',
      stdio: 'ignore',
      windowsHide: true,
    });
    spawned.push(be);
  }
  if (!feUp) {
    const fe = spawn(process.execPath, ['./node_modules/vite/bin/vite.js', '--host', '127.0.0.1', '--port', '5173'], {
      cwd: 'D:/KCPM/GUI_Usability_Testing/eshop-sut/frontend-web',
      stdio: 'ignore',
      windowsHide: true,
    });
    spawned.push(fe);
  }

  for (let i = 0; i < 30; i++) {
    try {
      const r1 = await fetch('http://127.0.0.1:3000/api/products');
      const r2 = await fetch('http://localhost:5173/');
      if (r1.ok && r2.ok) return spawned;
    } catch {}
    await sleep(400);
  }
  throw new Error('Timeout waiting for localhost:3000 and localhost:5173');
}

function snapDesktop(kind, fileName) {
  const outPath = path.join(OUT_DIR, fileName);
  if (DRY_RUN) {
    console.log(`[DRY_RUN] Would snap ${kind} -> ${outPath}`);
    return;
  }
  execFileSync('python', [SNAP_HELPER, kind, outPath], { stdio: 'inherit' });
}

class SimpleWSClient {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.id = 0;
    this.pending = new Map();
  }
  async connect() {
    await new Promise((resolve, reject) => {
      this.ws.addEventListener('open', resolve);
      this.ws.addEventListener('error', reject);
    });
    this.ws.addEventListener('message', (ev) => {
      const msg = JSON.parse(String(ev.data));
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) reject(new Error(JSON.stringify(msg.error)));
        else resolve(msg.result);
      }
    });
  }
  send(method, params = {}) {
    const id = ++this.id;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }
  close() {
    try { this.ws.close(); } catch {}
  }
}

const fillExpr = (val) => `
  (() => {
    const inputs = Array.from(document.querySelectorAll('input:not([disabled])'));
    const el = inputs[0];
    if (!el) return 'NO_INPUT';
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(el, ${JSON.stringify(val)});
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
    el.blur();
    window.scrollTo(0, 0);
    return el.value;
  })()
`;

const loginAuthExpr = `
  (async () => {
    const r = await fetch('http://localhost:3000/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: 'test@eshop.com', password: 'Test1234!' })
    });
    const data = await r.json();
    localStorage.setItem('token', data.token);
    localStorage.setItem('user', JSON.stringify(data.user));
    return data.user?.email || 'NO_USER';
  })()
`;

async function runP1Chrome() {
  console.log('\n=== PHASE 1: P1 — Google Chrome Maximized on Windows 11 ===');
  const prof = path.join(SCRATCH, 'tmp_p1_chrome_prof');
  fs.rmSync(prof, { recursive: true, force: true });
  fs.mkdirSync(prof, { recursive: true });

  spawn(CHROME_EXE, [
    `--user-data-dir=${prof}`,
    '--remote-debugging-port=9441',
    '--no-first-run',
    '--no-default-browser-check',
    '--start-maximized',
    'http://localhost:5173/register',
  ], { stdio: 'ignore' });

  let targets = null;
  for (let i = 0; i < 24; i++) {
    await sleep(500);
    try {
      const r = await fetch('http://127.0.0.1:9441/json');
      targets = await r.json();
      if (targets.some((t) => t.type === 'page' && t.url.includes('localhost:5173'))) break;
    } catch {}
  }
  if (!targets) throw new Error('Could not connect to Chrome on port 9441');

  const sutTarget = targets.find((t) => t.type === 'page' && t.url.includes('localhost:5173')) || targets.find((t) => t.type === 'page');
  const cdp = new SimpleWSClient(sutTarget.webSocketDebuggerUrl);
  await cdp.connect();
  await cdp.send('Page.enable');
  await cdp.send('Runtime.enable');

  const evalJS = (expression) => cdp.send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
  await evalJS('localStorage.clear(); true;');

  // 1. Register
  await cdp.send('Page.navigate', { url: 'http://localhost:5173/register' });
  await sleep(1300);
  await evalJS(fillExpr(STUDENT_STR));
  await sleep(400);
  snapDesktop('chrome', 'P1_Register_1.png');

  // 2. Login
  await cdp.send('Page.navigate', { url: 'http://localhost:5173/login' });
  await sleep(1300);
  await evalJS(fillExpr(STUDENT_STR));
  await sleep(400);
  snapDesktop('chrome', 'P1_Login_1.png');

  // 3. ForgotPassword
  await cdp.send('Page.navigate', { url: 'http://localhost:5173/forgot-password' });
  await sleep(1300);
  await evalJS(fillExpr(STUDENT_STR));
  await sleep(400);
  snapDesktop('chrome', 'P1_ForgotPassword_1.png');

  // 4. Profile
  await evalJS(loginAuthExpr);
  await cdp.send('Page.navigate', { url: 'http://localhost:5173/profile' });
  await sleep(1600);
  await evalJS(fillExpr(STUDENT_STR));
  await sleep(400);
  snapDesktop('chrome', 'P1_Profile_1.png');

  // 5. Chrome & Windows 11 Version Proof
  await cdp.send('Page.navigate', { url: 'chrome://version' });
  await sleep(1300);
  snapDesktop('chrome', 'P1_Device_Info.png');

  try { await cdp.send('Browser.close'); } catch {}
  cdp.close();
  await sleep(1000);
}

async function runP2Firefox() {
  console.log('\n=== PHASE 2: P2 — Mozilla Firefox 137.0.1 Maximized on Windows 11 ===');
  const prof = path.join(SCRATCH, 'tmp_p2_ff_prof');
  fs.rmSync(prof, { recursive: true, force: true });
  fs.mkdirSync(prof, { recursive: true });
  fs.writeFileSync(
    path.join(prof, 'user.js'),
    [
      'user_pref("browser.shell.checkDefaultBrowser", false);',
      'user_pref("browser.aboutwelcome.enabled", false);',
      'user_pref("datareporting.policy.dataSubmissionPolicyBypassNotification", true);',
      'user_pref("browser.startup.homepage_override.mstone", "ignore");',
      'user_pref("trailhead.firstrun.didSeeAboutWelcome", true);',
    ].join('\n')
  );

  spawn(FIREFOX_EXE, [
    '-no-remote',
    '-profile', prof,
    '--remote-debugging-port', '9442',
    'http://localhost:5173/register',
  ], { stdio: 'ignore' });

  let bidi = null;
  for (let i = 0; i < 24; i++) {
    await sleep(600);
    try {
      const client = new SimpleWSClient('ws://127.0.0.1:9442/session');
      await client.connect();
      bidi = client;
      break;
    } catch {}
  }
  if (!bidi) throw new Error('Could not connect to Firefox BiDi on port 9442');

  await bidi.send('session.new', { capabilities: {} });
  const tree = await bidi.send('browsingContext.getTree', {});
  const sutCtx = tree.contexts[0].context;

  const ffEval = (expression, awaitPromise = true) =>
    bidi.send('script.evaluate', {
      expression,
      target: { context: sutCtx },
      awaitPromise,
    });

  await ffEval('localStorage.clear(); true;', false);

  // 1. Register
  await bidi.send('browsingContext.navigate', { context: sutCtx, url: 'http://localhost:5173/register', wait: 'complete' });
  await sleep(900);
  await ffEval(fillExpr(STUDENT_STR), false);
  await sleep(400);
  snapDesktop('firefox', 'P2_Register_1.png');

  // 2. Login
  await bidi.send('browsingContext.navigate', { context: sutCtx, url: 'http://localhost:5173/login', wait: 'complete' });
  await sleep(900);
  await ffEval(fillExpr(STUDENT_STR), false);
  await sleep(400);
  snapDesktop('firefox', 'P2_Login_1.png');

  // 3. ForgotPassword
  await bidi.send('browsingContext.navigate', { context: sutCtx, url: 'http://localhost:5173/forgot-password', wait: 'complete' });
  await sleep(900);
  await ffEval(fillExpr(STUDENT_STR), false);
  await sleep(400);
  snapDesktop('firefox', 'P2_ForgotPassword_1.png');

  // 4. Profile
  await ffEval(loginAuthExpr, true);
  await bidi.send('browsingContext.navigate', { context: sutCtx, url: 'http://localhost:5173/profile', wait: 'complete' });
  await sleep(1400);
  await ffEval(fillExpr(STUDENT_STR), false);
  await sleep(400);
  snapDesktop('firefox', 'P2_Profile_1.png');

  // 5. Firefox 137.0.1 & Windows 11 Version Proof
  await bidi.send('browsingContext.navigate', { context: sutCtx, url: 'about:support', wait: 'complete' });
  await sleep(1200);
  snapDesktop('firefox', 'P2_Device_Info.png');

  try { await bidi.send('browser.close', {}); } catch {}
  bidi.close();
  await sleep(1000);
}

async function main() {
  const spawned = await ensureSutRunning();
  try {
    await runP1Chrome();
    await runP2Firefox();
    console.log('\nALL 10 MAXIMIZED WINDOWS 11 SCREENSHOTS (P1 & P2 + VERSION PROOFS) COMPLETED!');
  } finally {
    for (const p of spawned) {
      try { p.kill(); } catch {}
    }
  }
}

main().catch((err) => {
  console.error('FATAL:', err);
  process.exit(1);
});
