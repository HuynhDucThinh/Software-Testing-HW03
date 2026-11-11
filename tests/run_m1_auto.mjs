/**
 * tests/run_m1_auto.mjs
 * Thực thi tự động phần đo đạc khách quan DOM / CSS / API cho 59 mục checklist M1 (HW03 Task 1 & Task 3)
 * trên 3 nền tảng:
 *   - P1: Google Chrome đã cài trên Windows (channel: 'chrome')
 *   - P2: Firefox (Playwright Firefox Gecko engine)
 *   - P3: Chrome Android thật trên OPPO Reno10 5G qua Playwright _android (adb reverse 5173 & 3000)
 *
 * Kết quả xuất ra checklist/runs/<Px>_auto_<YYYYMMDD-HHMM>.json với kind="auto"
 * (merge_platform.py chỉ ghi vào auto_status / auto_notes, KHÔNG ghi đè ket_qua chính thức của SV).
 */

import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
import { chromium, firefox, _android } from 'playwright';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');
const CK_PATH = path.join(ROOT, 'checklist', 'checklist.json');
const RUNS_DIR = path.join(ROOT, 'checklist', 'runs');
const DB_PATH = path.join(ROOT, 'eshop-sut', 'backend', 'database.sqlite');

const requireBackend = createRequire(path.join(ROOT, 'eshop-sut', 'backend', 'package.json'));
const sqlite3 = requireBackend('sqlite3');

const WEB = 'http://localhost:5173';
const API = 'http://localhost:3000';
const SEED_USER = { email: 'test@eshop.com', password: 'Test1234!', name: 'Test User' };
// Mật khẩu qua được regex lỗi của client (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/)
// CHỈ dùng khi cần dựng tiền điều kiện gửi request tới backend cho các mục độc lập (CL-27, CL-32, CL-38, CL-39, SV-11)
const CLIENT_PASSABLE_PW = 'Abcd 1234';

function sha1Short(s) {
  return crypto.createHash('sha1').update(s, 'utf8').digest('hex').slice(0, 8);
}

function dbRun(sql, params = []) {
  return new Promise((resolve, reject) => {
    const db = new sqlite3.Database(DB_PATH);
    db.run(sql, params, function (err) {
      db.close();
      if (err) reject(err);
      else resolve(this);
    });
  });
}

function dbGet(sql, params = []) {
  return new Promise((resolve, reject) => {
    const db = new sqlite3.Database(DB_PATH);
    db.get(sql, params, (err, row) => {
      db.close();
      if (err) reject(err);
      else resolve(row);
    });
  });
}

async function resetDatabaseSeed() {
  await dbRun('DELETE FROM users WHERE id > 2');
  await dbRun(
    `UPDATE users
     SET name = 'Test User', email = 'test@eshop.com', password = 'Test1234!', role = 'user',
         login_attempts = 0, locked_until = NULL, reset_token = NULL,
         shipping_address = NULL, phone = NULL
     WHERE id = 2`
  );
}

async function clearSession(page, isAndroid) {
  if (isAndroid) {
    try {
      const cdp = await page.context().newCDPSession(page);
      for (const origin of [WEB, API]) {
        await cdp.send('Storage.clearDataForOrigin', { origin, storageTypes: 'all' });
      }
      await cdp.detach();
    } catch {}
  }
  await page.context().clearCookies();
  await page.goto(`${WEB}/login`, { waitUntil: 'domcontentloaded' });
  await page.evaluate(() => {
    localStorage.clear();
    sessionStorage.clear();
  });
}

async function loginSeedUser(page) {
  const res = await fetch(`${API}/api/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: SEED_USER.email, password: SEED_USER.password }),
  });
  const data = await res.json();
  if (!res.ok || !data.token) throw new Error(`Seed login failed: ${JSON.stringify(data)}`);
  await page.goto(`${WEB}/login`, { waitUntil: 'domcontentloaded' });
  await page.evaluate((t) => localStorage.setItem('token', t), data.token);
  await page.goto(`${WEB}/profile`, { waitUntil: 'networkidle' });
  await page.waitForSelector('form', { timeout: 5000 });
  return data.token;
}

// Helper: parse rgb/rgba string -> [r, g, b, a]
const BROWSER_HELPERS = `
window.__m1 = {
  rgb(s) {
    const m = (s || '').match(/[\\d.]+/g);
    if (!m) return [0, 0, 0, 1];
    return [+m[0], +m[1], +m[2], m[3] !== undefined ? +m[3] : 1];
  },
  effBg(el) {
    let cur = el;
    while (cur && cur !== document.documentElement) {
      const [r, g, b, a] = window.__m1.rgb(getComputedStyle(cur).backgroundColor);
      if (a > 0.05) return [r, g, b];
      cur = cur.parentElement;
    }
    return [255, 255, 255];
  },
  lum([r, g, b]) {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  },
  contrast(fgRgb, bgRgb) {
    const a = window.__m1.lum(fgRgb), b = window.__m1.lum(bgRgb);
    const [hi, lo] = a > b ? [a, b] : [b, a];
    return +(((hi + 0.05) / (lo + 0.05)).toFixed(2));
  },
  vis(el) {
    if (!el) return false;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  }
};
`;

async function injectHelpers(page) {
  await page.evaluate(BROWSER_HELPERS);
}

async function runSuiteOnPage(page, platform, applicableSet) {
  const isAndroid = platform === 'P3';
  const tapClick = async (loc) => {
    await loc.waitFor({ state: 'visible', timeout: 5000 });
    if (isAndroid) {
      await page.evaluate(() => { if (document.activeElement && document.activeElement.blur) document.activeElement.blur(); }).catch(() => {});
      await loc.evaluate((el) => el.click()).catch(() => {});
    } else {
      await loc.click();
    }
  };
  const results = {};
  const record = (id, passed, actualNote, extra = {}) => {
    if (!applicableSet.has(id)) return;
    results[id] = {
      status: extra.status || (passed ? 'Passed' : 'Failed'),
      notes: actualNote,
      evidence: [],
      ...(extra.partial ? { partial: true } : {}),
    };
  };

  await resetDatabaseSeed();
  await clearSession(page, isAndroid);

  // =========================================================================
  // NHÓM 1: KIỂM TRA TĨNH & THUỘC TÍNH DOM TRÊN 4 MÀN HÌNH KHÁCH + ĐÃ ĐĂNG NHẬP
  // =========================================================================

  // --- /login (guest) ---
  await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
  await injectHelpers(page);

  // CL-01: Ngôn ngữ tiếng Việt trên /login
  {
    const info = await page.evaluate(() => {
      const labels = [...document.querySelectorAll('main label')].map((e) => e.innerText.trim());
      const btns = [...document.querySelectorAll('main button')].map((e) => e.innerText.trim());
      const links = [...document.querySelectorAll('main a')].map((e) => e.innerText.trim());
      return { labels, btns, links };
    });
    const engRe = /\b(username|sign\s*in|log\s*in|login|password|submit|forgot)\b/i;
    const bad = [...info.labels, ...info.btns, ...info.links].filter((t) => engRe.test(t));
    record(
      'CL-01',
      bad.length === 0,
      `Actual: Trên /login nhãn trường = ${JSON.stringify(info.labels)}, nút = ${JSON.stringify(info.btns)}, liên kết = ${JSON.stringify(info.links)}${bad.length ? `; xuất hiện từ tiếng Anh không đúng chuẩn tiếng Việt: ${JSON.stringify(bad)}` : ''}.`
    );
  }

  // CL-04: Số lượng h1 và tiêu đề trang /login
  {
    const h = await page.evaluate(() => ({
      h1: [...document.querySelectorAll('h1')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
      h2: [...document.querySelectorAll('main h2')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
    }));
    const ok = h.h1.length === 1 && /đăng\s*nhập/i.test(h.h1[0]);
    record(
      'CL-04',
      ok,
      `Actual: Trên /login có ${h.h1.length} thẻ <h1> hiển thị (${JSON.stringify(h.h1)}); tiêu đề thực tế đang dùng thẻ <h2> với nội dung sai chức năng là ${JSON.stringify(h.h2)}.`
    );
  }

  // --- /register (guest) ---
  await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
  await injectHelpers(page);

  // CL-03: Số lượng h1 và nội dung trên /register
  {
    const h = await page.evaluate(() => ({
      h1: [...document.querySelectorAll('h1')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
      h2: [...document.querySelectorAll('main h2')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
    }));
    const ok = h.h1.length === 1 && /đăng\s*ký/i.test(h.h1[0]);
    record(
      'CL-03',
      ok,
      `Actual: Trên /register có ${h.h1.length} thẻ <h1> hiển thị (${JSON.stringify(h.h1)}); tiêu đề chính đang dùng thẻ <h2> (${JSON.stringify(h.h2)}).`
    );
  }

  // CL-16: Sự tồn tại và kiểm tra khớp của Xác nhận mật khẩu trên /register
  {
    const fields = await page.evaluate(() =>
      [...document.querySelectorAll('main form label')].map((e) => e.innerText.trim())
    );
    const pwInputs = await page.locator('main form input[type="password"]').count();
    const hasConfirm = fields.some((t) => /xác nhận|nhập lại/i.test(t)) && pwInputs >= 2;
    record(
      'CL-16',
      hasConfirm,
      `Actual: Form /register chỉ có ${fields.length} trường ${JSON.stringify(fields)} (${pwInputs} ô type="password"), hoàn toàn không có trường "Xác nhận mật khẩu".`
    );
  }

  // SV-14: Dòng gợi ý mật khẩu liệt kê ký tự đặc biệt (@ $ ! % * ? &)
  {
    const hint = await page.evaluate(() => {
      const p = document.querySelector('main form p');
      return p ? p.innerText.trim() : '';
    });
    const chars = ['@', '$', '!', '%', '*', '?', '&'];
    const hasAll = chars.every((c) => hint.includes(c));
    record(
      'SV-14',
      hasAll,
      `Actual: Dòng gợi ý dưới ô Mật khẩu trên /register chỉ ghi chung chung "${hint}", không liệt kê tập ký tự đặc biệt hợp lệ (@ $ ! % * ? &).`
    );
  }

  // CL-13: type="email" và chặn email sai định dạng trên /register
  {
    const emailInput = page.locator('main form input').nth(1);
    const typeAttr = await emailInput.getAttribute('type');
    let apiCalled = 0;
    const onReq = (req) => { if (req.url().includes('/api/register')) apiCalled++; };
    page.on('request', onReq);
    await page.locator('main form input').nth(0).fill('Nguyen Van A');
    await emailInput.fill('nguoimoieshop.com');
    await page.locator('main form input').nth(2).fill(CLIENT_PASSABLE_PW);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    page.off('request', onReq);
    await resetDatabaseSeed();
    const ok = typeAttr === 'email' && apiCalled === 0;
    record(
      'CL-13',
      ok,
      `Actual: Ô Email trên /register khai báo type="${typeAttr}" (khác "email") và khi nhập "nguoimoieshop.com" vẫn gửi ${apiCalled} request POST /api/register lên server mà không chặn định dạng email.`
    );
  }

  // --- /forgot-password Bước 1 & Bước 2 ---
  await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
  await injectHelpers(page);

  const fpStep1 = await page.evaluate(() => ({
    h1: [...document.querySelectorAll('h1')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
    h2: [...document.querySelectorAll('main h2')].map((e) => e.innerText.trim()),
    labels: [...document.querySelectorAll('main form label')].map((e) => e.innerText.trim()),
    emailType: document.querySelector('main form input')?.getAttribute('type') || null,
    btns: [...document.querySelectorAll('main button')].map((e) => e.innerText.trim()),
    links: [...document.querySelectorAll('main a')].map((e) => ({ text: e.innerText.trim(), href: e.getAttribute('href') })),
    bodyText: document.querySelector('main')?.innerText.trim() || '',
  }));

  // Kiểm tra CL-14 trên /login + /forgot-password Bước 1
  {
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    const loginEmailType = await page.locator('main form input').first().getAttribute('type');
    let loginApiCalled = 0;
    const onReq = (r) => { if (r.url().includes('/api/login')) loginApiCalled++; };
    page.on('request', onReq);
    await page.locator('main form input').nth(0).fill('khongcoacong.com');
    await page.locator('main form input').nth(1).fill('Test1234!');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    page.off('request', onReq);

    await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
    let fpApiCalled = 0;
    const onReqFp = (r) => { if (r.url().includes('/api/forgot-password')) fpApiCalled++; };
    page.on('request', onReqFp);
    let dlgMsg = '';
    page.once('dialog', async (d) => { dlgMsg = d.message(); await d.accept(); });
    await page.locator('main form input').first().fill('khongcoacong.com');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    page.off('request', onReqFp);

    const ok = loginEmailType === 'email' && fpStep1.emailType === 'email' && loginApiCalled === 0 && fpApiCalled === 0;
    record(
      'CL-14',
      ok,
      `Actual: Ô Email trên /login có type="${loginEmailType}" (gửi ${loginApiCalled} request với "khongcoacong.com") và ở Bước 1 /forgot-password có type="${fpStep1.emailType}" (gửi ${fpApiCalled} request tới server${dlgMsg ? `, bật alert "${dlgMsg}"` : ''}), không chặn định dạng bằng HTML5.`
    );
  }

  // CL-26: Nút/liên kết 'Quay lại đăng nhập' ở Bước 1 /forgot-password
  {
    const hasBackLogin = fpStep1.btns.some((t) => /quay lại/i.test(t)) || fpStep1.links.some((l) => /quay lại|đăng nhập/i.test(l.text));
    record(
      'CL-26',
      hasBackLogin,
      `Actual: Màn hình Bước 1 tại /forgot-password chỉ có nút ${JSON.stringify(fpStep1.btns)} và liên kết trong main = ${JSON.stringify(fpStep1.links)}, hoàn toàn thiếu nút/liên kết "Quay lại đăng nhập".`
    );
  }

  // Chuyển sang Bước 2 trên /forgot-password với test@eshop.com
  await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
  await page.locator('main form input').first().fill(SEED_USER.email);
  await tapClick(page.locator('main form button[type="submit"]'));
  await page.waitForSelector('main form button[type="button"]', { timeout: 5000 });
  await injectHelpers(page);

  const fpStep2 = await page.evaluate(() => ({
    h1: [...document.querySelectorAll('h1')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
    h2: [...document.querySelectorAll('main h2')].map((e) => e.innerText.trim()),
    labels: [...document.querySelectorAll('main form label')].map((e) => e.innerText.trim()),
    inputs: [...document.querySelectorAll('main form input')].map((e) => ({ type: e.getAttribute('type'), value: e.value })),
    banner: document.querySelector('main form div.bg-green-100')?.innerText.trim() || '',
    btns: [...document.querySelectorAll('main form button')].map((b) => {
      const cs = getComputedStyle(b);
      return { text: b.innerText.trim(), bg: cs.backgroundColor, color: cs.color };
    }),
    hints: [...document.querySelectorAll('main form p, main form small')].map((e) => e.innerText.trim()),
    bodyText: document.querySelector('main')?.innerText.trim() || '',
  }));

  // CL-05: h1 ở cả Bước 1 & Bước 2 của /forgot-password
  {
    const ok = fpStep1.h1.length === 1 && fpStep2.h1.length === 1;
    record(
      'CL-05',
      ok,
      `Actual: Trang /forgot-password có ${fpStep1.h1.length} thẻ <h1> ở Bước 1 và ${fpStep2.h1.length} thẻ <h1> ở Bước 2 (đang dùng thẻ <h2>: ${JSON.stringify(fpStep1.h2)}).`
    );
  }

  // CL-17: Step Indicator trên /forgot-password 2 bước
  {
    const stepRe = /(bước\s*[12]\s*[/trên-]\s*2|step\s*[12])/i;
    const hasStep = stepRe.test(fpStep1.bodyText) && stepRe.test(fpStep2.bodyText);
    record(
      'CL-17',
      hasStep,
      `Actual: Cả Bước 1 và Bước 2 trên /forgot-password đều không có thành phần chỉ báo bước (Step Indicator) nào hiển thị vị trí bước hiện tại (ví dụ Bước 1/2, Bước 2/2).`
    );
  }

  // CL-18: Xác nhận mật khẩu mới ở Bước 2 /forgot-password
  {
    const hasConfirm = fpStep2.labels.some((t) => /xác nhận/i.test(t)) && fpStep2.inputs.filter((i) => i.type === 'password').length >= 2;
    record(
      'CL-18',
      hasConfirm,
      `Actual: Bước 2 trang /forgot-password chỉ có ${fpStep2.labels.length} trường ${JSON.stringify(fpStep2.labels)}, thiếu trường "Xác nhận mật khẩu mới".`
    );
  }

  // CL-20: Độ dài 6 chữ số của OTP và nhãn OTP ở Bước 2
  {
    const m = fpStep2.banner.match(/(\d+)/);
    const otpVal = m ? m[1] : '';
    const otpLabel = fpStep2.labels[0] || '';
    const ok = otpVal.length === 6 && /6/.test(otpLabel) && !/4\s*số/i.test(otpLabel);
    record(
      'CL-20',
      ok,
      `Actual: Hệ thống chỉ sinh mã OTP gồm ${otpVal.length} chữ số ("${fpStep2.banner}") và nhãn ô nhập ghi "${otpLabel}" thay vì 6 chữ số.`
    );
  }

  // SV-13: Hiển thị gợi ý quy tắc mật khẩu mạnh ở Bước 2 /forgot-password
  {
    const hasRuleHint = fpStep2.hints.some((t) => /8\s*ký tự|chữ hoa/i.test(t));
    record(
      'SV-13',
      hasRuleHint,
      `Actual: Ở Bước 2 trang /forgot-password không có bất kỳ dòng gợi ý quy tắc mật khẩu nào gần ô "Mật khẩu mới" (số thẻ gợi ý = ${fpStep2.hints.length}).`
    );
  }

  // CL-29: Nút '← Quay lại' ở Bước 2 quay về Bước 1
  {
    await tapClick(page.locator('main form button[type="button"]'));
    await page.waitForTimeout(200);
    const backLabels = await page.evaluate(() => [...document.querySelectorAll('main form label')].map((e) => e.innerText.trim()));
    const ok = backLabels.length === 1 && /email/i.test(backLabels[0]);
    record(
      'CL-29',
      ok,
      `Actual: Nhấp nút "← Quay lại" ở Bước 2 chuyển giao diện trở về Bước 1 hiển thị nhãn ${JSON.stringify(backLabels)} bình thường, không phát sinh lỗi.`
    );
  }

  // CL-15: type="password" ở tất cả các ô mật khẩu (Register, Login, ForgotPassword Bước 2)
  {
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    const regPwType = await page.locator('main form input').nth(2).getAttribute('type');
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    const loginPwType = await page.locator('main form input').nth(1).getAttribute('type');
    const fpPwType = fpStep2.inputs[1]?.type || null;
    const ok = regPwType === 'password' && loginPwType === 'password' && fpPwType === 'password';
    record(
      'CL-15',
      ok,
      `Actual: Ô Mật khẩu trên /register có type="${regPwType}", Bước 2 /forgot-password có type="${fpPwType}", nhưng ô Mật khẩu trên /login lại khai báo type="${loginPwType}" làm lộ rõ toàn bộ ký tự mật khẩu khi gõ.`
    );
  }

  // CL-30: Khách chưa đăng nhập gõ trực tiếp URL /profile
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/profile`, { waitUntil: 'networkidle' });
    const guestProf = await page.evaluate(() => ({
      url: location.pathname,
      text: document.querySelector('main')?.innerText.trim() || '',
      linksInMain: [...document.querySelectorAll('main a, main button')].map((e) => e.innerText.trim()),
    }));
    const ok = guestProf.url === '/login' || guestProf.linksInMain.length > 0;
    record(
      'CL-30',
      ok,
      `Actual: Truy cập /profile khi chưa đăng nhập vẫn đứng tại URL "${guestProf.url}", vùng nội dung chính chỉ hiện chữ tĩnh "${guestProf.text}" và có ${guestProf.linksInMain.length} nút/liên kết điều hướng sang /login.`
    );
  }

  // =========================================================================
  // NHÓM 2: CÁC MỤC ĐÃ ĐĂNG NHẬP (/profile, Header) & ĐA MÀN HÌNH
  // =========================================================================
  await resetDatabaseSeed();
  await loginSeedUser(page);
  await injectHelpers(page);

  // CL-06: Số lượng h1 trên /profile
  {
    const h = await page.evaluate(() => ({
      h1: [...document.querySelectorAll('h1')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
      h2: [...document.querySelectorAll('main h2')].filter((e) => window.__m1.vis(e)).map((e) => e.innerText.trim()),
    }));
    record(
      'CL-06',
      h.h1.length === 1,
      `Actual: Trang /profile khi đã đăng nhập có ${h.h1.length} thẻ <h1> hiển thị; đang dùng ${h.h2.length} thẻ <h2> (${JSON.stringify(h.h2)}).`
    );
  }

  // CL-21: Ô Email trên /profile bị disabled và nền xám phân biệt
  {
    const emailInfo = await page.evaluate(() => {
      const inputs = [...document.querySelectorAll('main form input')];
      const em = inputs[0], nm = inputs[1];
      const csEm = getComputedStyle(em), csNm = getComputedStyle(nm);
      return {
        val: em.value,
        disabled: em.disabled,
        readOnly: em.readOnly,
        emBg: csEm.backgroundColor,
        nmBg: csNm.backgroundColor,
      };
    });
    const ok = (emailInfo.disabled || emailInfo.readOnly) && emailInfo.emBg !== emailInfo.nmBg && emailInfo.val === SEED_USER.email;
    record(
      'CL-21',
      ok,
      `Actual: Ô Email trên /profile hiển thị "${emailInfo.val}", disabled=${emailInfo.disabled}, màu nền ${emailInfo.emBg} phân biệt rõ với ô Họ Tên (${emailInfo.nmBg}).`
    );
  }

  // SV-20 (chỉ P3): Loại bàn phím ảo trên ô Số điện thoại tại /profile
  if (applicableSet.has('SV-20')) {
    const telAttr = await page.evaluate(() => {
      const ph = document.querySelectorAll('main form input')[2];
      return { type: ph.getAttribute('type'), inputmode: ph.getAttribute('inputmode'), placeholder: ph.getAttribute('placeholder') };
    });
    const ok = telAttr.type === 'tel' || telAttr.inputmode === 'numeric' || telAttr.inputmode === 'tel';
    record(
      'SV-20',
      ok,
      `Actual: Ô Số điện thoại trên /profile khai báo type="${telAttr.type}", inputmode=${JSON.stringify(telAttr.inputmode)} (không dùng type="tel" hay inputmode="numeric"), khi chạm trên điện thoại Android mở bàn phím chữ cái QWERTY thông thường thay vì bàn phím số.`,
      { partial: true }
    );
  }

  // CL-02: Ngôn ngữ tiếng Việt & chính tả trên Register, ForgotPassword, Profile (khối Hồ sơ), Header
  {
    const headerTexts = await page.evaluate(() => ({
      navLogged: [...document.querySelectorAll('header a, header button')].map((e) => e.innerText.trim()),
      profLabels: [...document.querySelectorAll('main form label, main form button')].map((e) => e.innerText.trim()),
      profH2: document.querySelector('main form')?.parentElement?.querySelector('h2')?.innerText.trim() || '',
    }));
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    const regTexts = await page.evaluate(() => ({
      navGuest: [...document.querySelectorAll('header a, header button')].map((e) => e.innerText.trim()),
      regAll: [...document.querySelectorAll('main h2, main label, main p, main button, main a')].map((e) => e.innerText.trim()),
    }));
    const allTokens = [
      ...headerTexts.navLogged,
      headerTexts.profH2,
      ...headerTexts.profLabels,
      ...regTexts.navGuest,
      ...regTexts.regAll,
      ...fpStep1.labels,
      ...fpStep1.btns,
      ...fpStep2.labels,
      ...fpStep2.btns.map((b) => b.text),
    ];
    const engBad = allTokens.filter((t) => /\b(username|sign\s*in|login|password|submit|logout|profile|register|forgot|reset)\b/i.test(t));
    record(
      'CL-02',
      engBad.length === 0,
      `Actual: Đã quét văn bản trên /register, /forgot-password (Bước 1 & 2), khối Hồ sơ /profile và Header (${allTokens.length} chuỗi): tất cả dùng tiếng Việt đúng chính tả (chỉ giữ "Email", "OTP", "EShop")${engBad.length ? `; từ ngoại lệ: ${JSON.stringify(engBad)}` : ''}.`,
      { partial: true }
    );
  }

  // CL-07: Nút Submit tích cực màu xanh dương trên Register, Login, Profile (GA2: R < 100, B > 180)
  {
    const btnColors = {};
    for (const [name, url, needAuth] of [['Register', '/register', false], ['Login', '/login', false], ['Profile', '/profile', true]]) {
      if (needAuth) await loginSeedUser(page);
      else { await clearSession(page, isAndroid); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
      await injectHelpers(page);
      btnColors[name] = await page.evaluate(() => {
        const b = document.querySelector('main form button[type="submit"]');
        const bg = getComputedStyle(b).backgroundColor;
        const [r, g, bl] = window.__m1.rgb(bg);
        return { text: b.innerText.trim(), bg, isBlue: r < 100 && bl > 180 };
      });
    }
    const ok = Object.values(btnColors).every((x) => x.isBlue);
    record(
      'CL-07',
      ok,
      `Actual: Nút Submit trên Login ("${btnColors.Login.text}": ${btnColors.Login.bg}) và Profile ("${btnColors.Profile.text}": ${btnColors.Profile.bg}) dùng màu xanh dương, nhưng nút "${btnColors.Register.text}" trên /register lại dùng màu đỏ (${btnColors.Register.bg}).`
    );
  }

  // CL-08: Màu nút trên ForgotPassword (Bước 1, Bước 2) và nút thoát trên Header (GA2)
  {
    await loginSeedUser(page);
    await injectHelpers(page);
    const logoutBtn = await page.evaluate(() => {
      const b = document.querySelector('header button');
      const bg = getComputedStyle(b).backgroundColor;
      const [r, g, bl] = window.__m1.rgb(bg);
      return { text: b.innerText.trim(), bg, isRed: r > 180 && g < 100 && bl < 100 };
    });
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
    await injectHelpers(page);
    const s1Btn = await page.evaluate(() => {
      const b = document.querySelector('main form button[type="submit"]');
      const bg = getComputedStyle(b).backgroundColor;
      const [r, g, bl] = window.__m1.rgb(bg);
      return { text: b.innerText.trim(), bg, isBlue: r < 100 && bl > 180 };
    });
    const s2Primary = fpStep2.btns[0];
    const s2Back = fpStep2.btns[1];
    const parseRgb = (s) => (s.match(/[\d.]+/g) || [0, 0, 0]).map(Number);
    const [pr, pg, pb] = parseRgb(s2Primary.bg);
    const s2PrimaryBlue = pr < 100 && pb > 180;
    const s2Distinct = s2Primary.bg !== s2Back.bg;
    const ok = s1Btn.isBlue && s2PrimaryBlue && s2Distinct && logoutBtn.isRed;
    record(
      'CL-08',
      ok,
      `Actual: Bước 1 nút "${s1Btn.text}" màu xanh dương (${s1Btn.bg}), nút "${logoutBtn.text}" trên Header màu đỏ (${logoutBtn.bg}); tuy nhiên ở Bước 2 cả nút chính "${s2Primary.text}" (${s2Primary.bg}) lẫn nút phụ "${s2Back.text}" (${s2Back.bg}) đều dùng chung nền xanh lá cây, không dùng xanh dương cho nút chính và không phân biệt vai trò hai nút.`
    );
  }

  // CL-09: Căn lề dọc thẳng hàng (<= 2px) và không cuộn ngang trên 4 form
  {
    const alignReport = [];
    let allAligned = true;
    for (const [name, url, needAuth, toStep2] of [
      ['Register', '/register', false, false],
      ['Login', '/login', false, false],
      ['ForgotStep1', '/forgot-password', false, false],
      ['ForgotStep2', '/forgot-password', false, true],
      ['Profile', '/profile', true, false],
    ]) {
      if (needAuth) await loginSeedUser(page);
      else { await clearSession(page, isAndroid); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
      if (toStep2) {
        await page.locator('main form input').first().fill(SEED_USER.email);
        await tapClick(page.locator('main form button[type="submit"]'));
        await page.waitForSelector('main form button[type="button"]');
      }
      const m = await page.evaluate(() => {
        const els = [...document.querySelectorAll('main form input, main form textarea, main form button')];
        const rects = els.map((e) => e.getBoundingClientRect());
        const lefts = rects.map((r) => r.left);
        const widths = rects.map((r) => r.width);
        const dLeft = +(Math.max(...lefts) - Math.min(...lefts)).toFixed(2);
        const dWidth = +(Math.max(...widths) - Math.min(...widths)).toFixed(2);
        const hScroll = document.documentElement.scrollWidth > document.documentElement.clientWidth;
        return { dLeft, dWidth, hScroll };
      });
      if (m.dLeft > 2 || m.dWidth > 2 || m.hScroll) allAligned = false;
      alignReport.push(`${name}(dLeft=${m.dLeft}px, dWidth=${m.dWidth}px, hScroll=${m.hScroll})`);
    }
    record(
      'CL-09',
      allAligned,
      `Actual: Đo toạ độ các ô nhập và nút trong form: ${alignReport.join('; ')}.`
    );
  }

  // CL-11: Độ tương phản màu chữ/nền WCAG 1.4.3 (>= 4.5:1 văn bản thường, >= 3.0:1 văn bản lớn)
  {
    const lowItems = [];
    for (const [name, url, needAuth, toStep2] of [
      ['Register', '/register', false, false],
      ['Login', '/login', false, false],
      ['ForgotStep2', '/forgot-password', false, true],
      ['Profile+Header', '/profile', true, false],
    ]) {
      if (needAuth) await loginSeedUser(page);
      else { await clearSession(page, isAndroid); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
      if (toStep2) {
        await page.locator('main form input').first().fill(SEED_USER.email);
        await tapClick(page.locator('main form button[type="submit"]'));
        await page.waitForSelector('main form button[type="button"]');
      }
      await injectHelpers(page);
      const bads = await page.evaluate((screenName) => {
        const sels = 'header a, header button, header span, main h1, main h2, main form label, main form p, main form button, main form a, main form div';
        const out = [];
        for (const el of document.querySelectorAll(sels)) {
          if (!window.__m1.vis(el)) continue;
          // Chỉ kiểm phần tử chứa text trực tiếp
          const directText = [...el.childNodes].filter((n) => n.nodeType === 3).map((n) => n.textContent.trim()).join(' ');
          if (!directText) continue;
          const cs = getComputedStyle(el);
          const fg = window.__m1.rgb(cs.color);
          const bg = window.__m1.effBg(el);
          const ratio = window.__m1.contrast(fg, bg);
          const px = parseFloat(cs.fontSize);
          const bold = parseInt(cs.fontWeight, 10) >= 700 || cs.fontWeight === 'bold';
          const isLarge = px >= 24 || (px >= 18.66 && bold);
          const minR = isLarge ? 3.0 : 4.5;
          if (ratio < minR) {
            out.push(`${screenName} "${directText.slice(0, 35)}" (${ratio}:1 < ${minR}:1, fg=${cs.color}, bg=rgb(${bg.join(',')}))`);
          }
        }
        return out;
      }, name);
      lowItems.push(...bads);
    }
    const uniqLow = [...new Set(lowItems)];
    record(
      'CL-11',
      uniqLow.length === 0,
      uniqLow.length === 0
        ? 'Actual: Toàn bộ nhãn, tiêu đề, gợi ý và nút trên 5 vùng M1 đều đạt tỷ lệ tương phản >= 4.5:1 (hoặc >= 3.0:1 với chữ lớn).'
        : `Actual: Phát hiện văn bản không đạt ngưỡng tương phản WCAG 4.5:1: ${uniqLow.join('; ')}.`
    );
  }

  // CL-12: Dấu * cạnh nhãn trường bắt buộc trên cả 4 form
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    const regL = await page.evaluate(() => [...document.querySelectorAll('main form label')].map((e) => e.innerText.trim()));
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    const logL = await page.evaluate(() => [...document.querySelectorAll('main form label')].map((e) => e.innerText.trim()));
    await loginSeedUser(page);
    const profL = await page.evaluate(() => [...document.querySelectorAll('main form label')].map((e) => e.innerText.trim()));
    const reqLabels = [...regL, ...logL, ...fpStep1.labels, ...fpStep2.labels, profL[1]];
    const withStar = reqLabels.filter((l) => l && l.includes('*'));
    record(
      'CL-12',
      withStar.length === reqLabels.length && regL.length >= 4 && fpStep2.labels.length >= 3,
      `Actual: Có ${withStar.length}/${reqLabels.length} nhãn trường bắt buộc hiển thị dấu "*": Register=${JSON.stringify(regL)}, Login=${JSON.stringify(logL)}, ForgotB1=${JSON.stringify(fpStep1.labels)}, ForgotB2=${JSON.stringify(fpStep2.labels)}, Profile(Họ Tên)="${profL[1]}".`
    );
  }

  // CL-23: Liên kết ngữ nghĩa <label for> / bọc input trên 4 form
  {
    let totalLabels = 0, linkedLabels = 0;
    for (const [url, needAuth] of [['/register', false], ['/login', false], ['/forgot-password', false], ['/profile', true]]) {
      if (needAuth) await loginSeedUser(page);
      else { await clearSession(page, isAndroid); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
      const stat = await page.evaluate(() => {
        const lbs = [...document.querySelectorAll('main form label')];
        let linked = 0;
        for (const l of lbs) {
          const forId = l.getAttribute('for');
          if ((forId && document.getElementById(forId)) || l.querySelector('input, textarea, select')) linked++;
        }
        return { total: lbs.length, linked };
      });
      totalLabels += stat.total;
      linkedLabels += stat.linked;
    }
    record(
      'CL-23',
      linkedLabels === totalLabels && totalLabels > 0,
      `Actual: Kiểm tra trên cả 4 form (/register, /login, /forgot-password, /profile) có ${linkedLabels}/${totalLabels} thẻ <label> có thuộc tính for/id hoặc bọc trực tiếp ô input; nhấp vào nhãn không làm focus ô nhập tương ứng.`
    );
  }

  // CL-24: Highlight liên kết trang đang mở trên Header (/login, /register, /profile)
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    const loginNav = await page.evaluate(() =>
      [...document.querySelectorAll('header nav a')].map((a) => {
        const cs = getComputedStyle(a);
        return {
          text: a.innerText.trim(),
          href: a.getAttribute('href'),
          ariaCurrent: a.getAttribute('aria-current'),
          cls: a.className,
          color: cs.color,
          bg: cs.backgroundColor,
          fw: cs.fontWeight,
          td: cs.textDecorationLine,
        };
      })
    );
    const activeLogin = loginNav.find((x) => x.href === '/login');
    const inactiveReg = loginNav.find((x) => x.href === '/register');
    const highlightedGuest =
      activeLogin &&
      inactiveReg &&
      (activeLogin.ariaCurrent === 'page' ||
        activeLogin.color !== inactiveReg.color ||
        activeLogin.bg !== inactiveReg.bg ||
        activeLogin.fw !== inactiveReg.fw ||
        activeLogin.td !== inactiveReg.td);

    await loginSeedUser(page);
    const profNav = await page.evaluate(() => {
      const a = document.querySelector('header nav a[href="/profile"]');
      return a ? { cls: a.className, ariaCurrent: a.getAttribute('aria-current') } : null;
    });
    await page.goto(`${WEB}/`, { waitUntil: 'networkidle' });
    const homeProfNav = await page.evaluate(() => {
      const a = document.querySelector('header nav a[href="/profile"]');
      return a ? { cls: a.className, ariaCurrent: a.getAttribute('aria-current') } : null;
    });
    const highlightedProf = profNav && homeProfNav && (profNav.cls !== homeProfNav.cls || profNav.ariaCurrent === 'page');

    record(
      'CL-24',
      Boolean(highlightedGuest && highlightedProf),
      `Actual: Khi đang ở /login, liên kết "Đăng nhập" có cùng class "${activeLogin?.cls}", aria-current=${JSON.stringify(activeLogin?.ariaCurrent)}, màu ${activeLogin?.color} giống hệt liên kết không chọn "Đăng ký" ("${inactiveReg?.cls}"); trên /profile liên kết "Chào, <tên>" cũng giữ nguyên class "${profNav?.cls}" như khi đứng ở trang chủ.`
    );
  }

  // CL-25: Nhãn chuẩn 'Đăng xuất' và thoát phiên trên Header
  {
    await loginSeedUser(page);
    const btnText = (await page.locator('header button').innerText()).trim();
    await tapClick(page.locator('header button'));
    await page.waitForTimeout(300);
    const afterLinks = await page.evaluate(() => ({
      links: [...document.querySelectorAll('header nav a')].map((a) => a.innerText.trim()),
      token: localStorage.getItem('token'),
    }));
    const cleared = afterLinks.token === null && afterLinks.links.includes('Đăng nhập') && afterLinks.links.includes('Đăng ký');
    const ok = btnText === 'Đăng xuất' && cleared;
    record(
      'CL-25',
      ok,
      `Actual: Nút thoát phiên trên Header hiển thị nhãn là "${btnText}" thay vì nhãn chuẩn "Đăng xuất" của FR-23 (chức năng xoá token và chuyển về ${JSON.stringify(afterLinks.links)} hoạt động=${cleared}).`
    );
  }

  // CL-28: Điều hướng SPA không tải lại trang trên Login và Header
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    const reloadedLinks = [];

    // Kiểm tra link 'Quên mật khẩu?' trên /login
    await page.evaluate(() => { window.__spa_alive = true; });
    await Promise.all([
      page.waitForURL('**/forgot-password'),
      tapClick(page.locator('main a', { hasText: 'Quên mật khẩu?' })),
    ]);
    await page.waitForLoadState('domcontentloaded');
    await page.waitForTimeout(250);
    if (!(await page.evaluate(() => Boolean(window.__spa_alive)))) {
      reloadedLinks.push('Login -> "Quên mật khẩu?" (dùng <a href="/forgot-password"> gây reload toàn trang)');
    }

    // Kiểm tra link 'Đăng ký ngay' trên /login
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    await page.evaluate(() => { window.__spa_alive = true; });
    await tapClick(page.locator('main a', { hasText: 'Đăng ký ngay' }));
    await page.waitForLoadState('networkidle');
    if (!(await page.evaluate(() => Boolean(window.__spa_alive)))) {
      reloadedLinks.push('Login -> "Đăng ký ngay"');
    }

    // Kiểm tra các link trên Header (EShop, Đăng nhập, Đăng ký)
    for (const txt of ['EShop', 'Đăng nhập', 'Đăng ký']) {
      await page.evaluate(() => { window.__spa_alive = true; });
      await tapClick(page.locator('header a', { hasText: txt }).first());
      await page.waitForLoadState('networkidle');
      if (!(await page.evaluate(() => Boolean(window.__spa_alive)))) {
        reloadedLinks.push(`Header -> "${txt}"`);
      }
    }

    record(
      'CL-28',
      reloadedLinks.length === 0,
      reloadedLinks.length === 0
        ? 'Actual: Toàn bộ liên kết trên /login và Header đều chuyển trang bằng SPA React Router không tải lại toàn trang.'
        : `Actual: Phát hiện liên kết làm tải lại toàn bộ trang trình duyệt thay vì điều hướng SPA: ${reloadedLinks.join('; ')}.`
    );
  }

  // SV-16: document.title riêng biệt cho 4 trang
  {
    const titles = {};
    for (const [p, auth] of [['/register', false], ['/login', false], ['/forgot-password', false], ['/profile', true]]) {
      if (auth) await loginSeedUser(page);
      else { await clearSession(page, isAndroid); await page.goto(`${WEB}${p}`, { waitUntil: 'networkidle' }); }
      titles[p] = await page.title();
    }
    const uniq = new Set(Object.values(titles));
    record(
      'SV-16',
      uniq.size === 4,
      `Actual: Cả 4 trang đều có cùng document.title mặc định giống hệt nhau: ${JSON.stringify(titles)}, không mô tả chức năng từng trang.`
    );
  }

  // SV-19: Kích thước vùng chạm >= 24 x 24 CSS px trên cả 5 vùng
  {
    const smallTargets = [];
    for (const [name, url, auth] of [['Register', '/register', false], ['Login', '/login', false], ['ForgotPassword', '/forgot-password', false], ['Profile+Header', '/profile', true]]) {
      if (auth) await loginSeedUser(page);
      else { await clearSession(page, isAndroid); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
      await injectHelpers(page);
      const smalls = await page.evaluate((scr) => {
        const out = [];
        for (const el of document.querySelectorAll('header a, header button, main a, main button')) {
          if (!window.__m1.vis(el)) continue;
          const r = el.getBoundingClientRect();
          if (r.width < 24 || r.height < 24) {
            out.push(`${scr} "${el.innerText.trim()}" (${Math.round(r.width)}x${Math.round(r.height)}px)`);
          }
        }
        return out;
      }, name);
      smallTargets.push(...smalls);
    }
    const uniqSmall = [...new Set(smallTargets)];
    record(
      'SV-19',
      uniqSmall.length === 0,
      uniqSmall.length === 0
        ? 'Actual: Mọi nút và liên kết trên 5 vùng giao diện đều có vùng chạm >= 24x24 CSS px.'
        : `Actual: Các liên kết có chiều cao vùng chạm nhỏ hơn ngưỡng 24x24 CSS px: ${uniqSmall.join('; ')}.`,
      { partial: isAndroid }
    );
  }

  // =========================================================================
  // NHÓM 3: VALIDATION FORM, BIÊN DỮ LIỆU & PHẢN HỒI TRẠNG THÁI (IA-02 & IA-04)
  // =========================================================================

  // CL-19: Quy tắc mật khẩu mạnh Abcd123! trên /register và Bước 2 /forgot-password
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('Nguyen Van B');
    await page.locator('main form input').nth(1).fill('m1+cl19@example.com');
    await page.locator('main form input').nth(2).fill('Abcd123!');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(300);
    const regErr = (await page.locator('main div.bg-red-100').textContent())?.trim() || '';

    await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
    await page.locator('main form input').first().fill(SEED_USER.email);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main form button[type="button"]');
    const banner = await page.locator('main form div.bg-green-100').innerText();
    const otp = (banner.match(/(\d+)/) || [])[1] || '';
    let fpAlert = '';
    page.once('dialog', async (d) => { fpAlert = d.message(); await d.accept(); });
    await page.locator('main form input').nth(0).fill(otp);
    await page.locator('main form input').nth(1).fill('Abcd123!');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(300);

    await resetDatabaseSeed();
    const ok = !regErr && !/quá yếu/i.test(fpAlert) && page.url().endsWith('/login');
    record(
      'CL-19',
      ok,
      `Actual: Mật khẩu hợp lệ chuẩn đặc tả "Abcd123!" bị từ chối trên cả /register ("${regErr}") lẫn Bước 2 /forgot-password (alert "${fpAlert}") do biểu thức chính quy lỗi trên client.`
    );
  }

  // SV-08: Biên độ dài mật khẩu 7 ký tự (Abc12!x) và 8 ký tự (Abc123!x) trên /register
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('Test Boundary');
    await page.locator('main form input').nth(1).fill('m1+sv08a@example.com');
    await page.locator('main form input').nth(2).fill('Abc12!x');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(200);
    const rejected7 = page.url().endsWith('/register') && (await page.locator('main div.bg-red-100').isVisible());

    await page.locator('main form input').nth(1).fill('m1+sv08b@example.com');
    await page.locator('main form input').nth(2).fill('Abc123!x');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(300);
    const accepted8 = page.url().endsWith('/login');
    const err8 = (await page.locator('main div.bg-red-100').textContent().catch(() => ''))?.trim() || '';
    await resetDatabaseSeed();

    record(
      'SV-08',
      rejected7 && accepted8,
      `Actual: Mật khẩu 7 ký tự "Abc12!x" bị từ chối=${rejected7}, nhưng mật khẩu biên hợp lệ 8 ký tự "Abc123!x" cũng bị từ chối kèm lỗi "${err8}" (không chuyển tới /login).`
    );
  }

  // SV-09: Từng ký tự đặc biệt trong (@ $ ! % * ? &) được chấp nhận trên /register
  {
    const specials = ['@', '$', '!', '%', '*', '?', '&'];
    const rejectedChars = [];
    for (let i = 0; i < specials.length; i++) {
      const ch = specials[i];
      await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
      await page.locator('main form input').nth(0).fill('Test Special');
      await page.locator('main form input').nth(1).fill(`m1+spec${i}@example.com`);
      await page.locator('main form input').nth(2).fill(`Abcd123${ch}`);
      await tapClick(page.locator('main form button[type="submit"]'));
      await page.waitForTimeout(200);
      if (!page.url().endsWith('/login')) rejectedChars.push(`Abcd123${ch}`);
    }
    await resetDatabaseSeed();
    record(
      'SV-09',
      rejectedChars.length === 0,
      `Actual: Cả ${rejectedChars.length}/7 mật khẩu chứa ký tự đặc biệt hợp lệ (${rejectedChars.join(', ')}) đều bị form /register từ chối với lỗi "Mật khẩu quá yếu!".`
    );
  }

  // SV-04: Vị trí khối thông báo lỗi trên /register so với nút Đăng Ký và tiêu đề (GA6)
  {
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('Nguyen Van C');
    await page.locator('main form input').nth(1).fill('m1+sv04@example.com');
    await page.locator('main form input').nth(2).fill('abc');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(200);
    const pos = await page.evaluate(() => {
      const h2 = document.querySelector('main h2').getBoundingClientRect();
      const err = document.querySelector('main div.bg-red-100').getBoundingClientRect();
      const firstInput = document.querySelector('main form input').getBoundingClientRect();
      const btn = document.querySelector('main form button[type="submit"]').getBoundingClientRect();
      const insideForm = Boolean(document.querySelector('main form div.bg-red-100'));
      return {
        insideForm,
        distToHeading: Math.round(err.top - h2.bottom),
        distToSubmit: Math.round(btn.top - err.bottom),
        aboveAllInputs: err.bottom <= firstInput.top,
      };
    });
    const ok = pos.insideForm && pos.distToSubmit < pos.distToHeading && !pos.aboveAllInputs;
    record(
      'SV-04',
      ok,
      `Actual: Khối lỗi trên /register nằm ngoài thẻ <form> (insideForm=${pos.insideForm}), phía trên tất cả các ô nhập (cách tiêu đề ${pos.distToHeading}px nhưng cách nút "Đăng Ký" tới ${pos.distToSubmit}px), không nằm liền kề phía trên nút Submit theo GA6.`
    );
  }

  // SV-03: Vị trí khối thông báo lỗi trên /login so với nút gửi form
  {
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('khongtontai@eshop.com');
    await page.locator('main form input').nth(1).fill('Wrong123!');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main div.bg-red-100', { timeout: 5000 });
    const pos = await page.evaluate(() => {
      const err = document.querySelector('main div.bg-red-100').getBoundingClientRect();
      const btn = document.querySelector('main form button[type="submit"]').getBoundingClientRect();
      return { errTop: Math.round(err.top), errBottom: Math.round(err.bottom), btnTop: Math.round(btn.top), btnBottom: Math.round(btn.bottom) };
    });
    const ok = pos.errBottom <= pos.btnTop;
    record(
      'SV-03',
      ok,
      `Actual: Khối thông báo lỗi trên /login nằm BÊN DƯỚI nút gửi form (error.top=${pos.errTop}px > submit.bottom=${pos.btnBottom}px), vi phạm FR-22 yêu cầu nằm phía trên nút submit.`
    );
  }

  // CL-32: Đăng ký trùng email test@eshop.com
  {
    await resetDatabaseSeed();
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('Trung Email');
    await page.locator('main form input').nth(1).fill(SEED_USER.email);
    await page.locator('main form input').nth(2).fill(CLIENT_PASSABLE_PW);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(500);
    const curUrl = page.url();
    const errTxt = (await page.locator('main div.bg-red-100').textContent().catch(() => ''))?.trim() || '';
    await resetDatabaseSeed();
    const ok = curUrl.endsWith('/register') && errTxt.length > 0 && !/sqlite|constraint|error/i.test(errTxt);
    record(
      'CL-32',
      ok,
      curUrl.endsWith('/login')
        ? `Actual: Khi gửi đăng ký với email đã tồn tại "${SEED_USER.email}", hệ thống KHÔNG từ chối và KHÔNG hiện thông báo lỗi nào mà vẫn tạo trùng bản ghi trong CSDL rồi chuyển thẳng sang ${curUrl}.`
        : `Actual: Thông báo khi đăng ký trùng email: "${errTxt}" (URL: ${curUrl}).`
    );
  }

  // CL-27: Liên kết 'Đăng nhập' và tự động chuyển hướng sang /login sau khi đăng ký thành công
  {
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await tapClick(page.locator('main form a', { hasText: 'Đăng nhập' }));
    await page.waitForTimeout(200);
    const linkOk = page.url().endsWith('/login');

    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('Nguoi Dung Moi');
    await page.locator('main form input').nth(1).fill('m1+cl27@example.com');
    await page.locator('main form input').nth(2).fill(CLIENT_PASSABLE_PW);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(500);
    const regRedirectOk = page.url().endsWith('/login');
    await resetDatabaseSeed();

    record(
      'CL-27',
      linkOk && regRedirectOk,
      `Actual: Liên kết "Đăng nhập" dưới form /register chuyển đúng sang /login (${linkOk}) và sau khi hoàn tất đăng ký tài khoản mới ứng dụng tự động chuyển hướng về /login (${regRedirectOk}).`
    );
  }

  // CL-34: Thông báo lỗi không lộ nguyên nhân chi tiết khi sai Email vs sai Mật khẩu trên /login
  {
    await resetDatabaseSeed();
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('khongtontai@eshop.com');
    await page.locator('main form input').nth(1).fill('Wrong123!');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main div.bg-red-100');
    const msgWrongEmail = (await page.locator('main div.bg-red-100').innerText()).trim();

    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill(SEED_USER.email);
    await page.locator('main form input').nth(1).fill('Wrong123!');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main div.bg-red-100');
    const msgWrongPw = (await page.locator('main div.bg-red-100').innerText()).trim();
    await resetDatabaseSeed();

    const ok = msgWrongEmail === msgWrongPw && msgWrongEmail.length > 0 && !/invalid|email|password/i.test(msgWrongEmail);
    record(
      'CL-34',
      ok,
      `Actual: Khi sai Email ("${msgWrongEmail}") và khi sai Mật khẩu ("${msgWrongPw}") giao diện hiển thị cùng một thông báo tổng quát bằng tiếng Việt, không lộ trường sai.`
    );
  }

  // CL-39: Giữ nguyên dữ liệu đã nhập khi báo lỗi và xoá lỗi khi thao tác lại thành công trên /register & /login
  {
    await resetDatabaseSeed();
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('Giu Du Lieu');
    await page.locator('main form input').nth(1).fill('m1+cl39@example.com');
    await page.locator('main form input').nth(2).fill('abc');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(200);
    const regKept =
      (await page.locator('main form input').nth(0).inputValue()) === 'Giu Du Lieu' &&
      (await page.locator('main form input').nth(1).inputValue()) === 'm1+cl39@example.com';
    await page.locator('main form input').nth(2).fill(CLIENT_PASSABLE_PW);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    const regCleared = page.url().endsWith('/login');

    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill(SEED_USER.email);
    await page.locator('main form input').nth(1).fill('SaiMatKhau');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main div.bg-red-100');
    const logKept = (await page.locator('main form input').nth(0).inputValue()) === SEED_USER.email;
    await page.locator('main form input').nth(1).fill(SEED_USER.password);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    const logCleared = !(await page.locator('main div.bg-red-100').isVisible().catch(() => false));
    await resetDatabaseSeed();

    const ok = regKept && regCleared && logKept && logCleared;
    record(
      'CL-39',
      ok,
      `Actual: Trên /register giữ Họ Tên & Email khi lỗi=${regKept}, xoá lỗi/chuyển trang khi gửi đúng=${regCleared}; trên /login giữ Email khi lỗi=${logKept}, xoá lỗi khi đăng nhập đúng=${logCleared}.`
    );
  }

  // CL-22: Số điện thoại hợp lệ bắt đầu bằng 0 (0912345678) được chấp nhận, chữ cái bị từ chối trên /profile
  {
    await resetDatabaseSeed();
    await loginSeedUser(page);
    let alertValid = '';
    page.once('dialog', async (d) => { alertValid = d.message(); await d.accept(); });
    await page.locator('main form input').nth(2).fill('0912345678');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(300);

    let alertLetters = '';
    page.once('dialog', async (d) => { alertLetters = d.message(); await d.accept(); });
    await page.locator('main form input').nth(2).fill('09123abcde');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(300);

    const validSaved = /thành công/i.test(alertValid);
    const lettersRejected = !/thành công/i.test(alertLetters);
    record(
      'CL-22',
      validSaved && lettersRejected,
      `Actual: Nhập SĐT hợp lệ chuẩn Việt Nam "0912345678" (khớp chính placeholder form) bị từ chối với hộp thoại alert "${alertValid}"; chuỗi chữ cái "09123abcde" báo "${alertLetters}".`
    );
  }

  // SV-10: Biên SĐT không hợp lệ (091234567 - 9 số, 091234567890 - 12 số, 9123456789 - bắt đầu khác 0)
  {
    await resetDatabaseSeed();
    await loginSeedUser(page);
    const outcomes = {};
    for (const val of ['091234567', '091234567890', '9123456789']) {
      let msg = '';
      page.once('dialog', async (d) => { msg = d.message(); await d.accept(); });
      await page.locator('main form input').nth(2).fill(val);
      await tapClick(page.locator('main form button[type="submit"]'));
      await page.waitForTimeout(300);
      outcomes[val] = msg;
    }
    await resetDatabaseSeed();
    const allRejected = Object.values(outcomes).every((m) => !/thành công/i.test(m));
    record(
      'SV-10',
      allRejected,
      `Actual: Thử 3 giá trị biên SĐT không hợp lệ trên /profile: "091234567" -> "${outcomes['091234567']}"; "091234567890" -> "${outcomes['091234567890']}"; riêng "9123456789" (không bắt đầu bằng số 0) lại được lưu thành công ("${outcomes['9123456789']}").`
    );
  }

  // CL-35: Phản hồi nội trang/toast thay vì window.alert() trên /forgot-password và /profile (GA4)
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
    let fpDialog = null;
    page.once('dialog', async (d) => { fpDialog = d.message(); await d.accept(); });
    await page.locator('main form input').first().fill('khongtontai@eshop.com');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);

    await loginSeedUser(page);
    let profDialog = null;
    page.once('dialog', async (d) => { profDialog = d.message(); await d.accept(); });
    await page.locator('main form input').nth(2).fill('912345678');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    await resetDatabaseSeed();

    const ok = fpDialog === null && profDialog === null;
    record(
      'CL-35',
      ok,
      `Actual: Cả /forgot-password lẫn /profile đều bật hộp thoại native window.alert() chặn luồng thao tác thay vì thông báo nội trang/toast, đồng thời lộ chuỗi tiếng Anh thô trên /forgot-password (alert: "${fpDialog}"; /profile alert: "${profDialog}").`
    );
  }

  // CL-36 & SV-07: Cập nhật Profile -> đồng bộ tên trên Header ngay trong 1s + giữ dữ liệu tiếng Việt có dấu sau F5
  {
    await resetDatabaseSeed();
    await loginSeedUser(page);
    page.once('dialog', async (d) => await d.accept());
    await page.locator('main form input').nth(1).fill('Nguyễn Văn Ánh');
    await page.locator('main form input').nth(2).fill('912345678');
    await page.locator('main form textarea').fill('12 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(1000);

    const headerBeforeReload = (await page.locator('header a[href="/profile"]').innerText()).trim();
    await page.reload({ waitUntil: 'networkidle' });
    await page.waitForSelector('main form input', { timeout: 5000 });
    const afterReload = await page.evaluate(() => ({
      header: document.querySelector('header a[href="/profile"]')?.innerText.trim() || '',
      name: document.querySelectorAll('main form input')[1]?.value || '',
      phone: document.querySelectorAll('main form input')[2]?.value || '',
      addr: document.querySelector('main form textarea')?.value || '',
    }));
    await resetDatabaseSeed();

    const syncImmediate = headerBeforeReload === 'Chào, Nguyễn Văn Ánh';
    const persisted =
      afterReload.name === 'Nguyễn Văn Ánh' &&
      afterReload.addr === '12 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh';
    record(
      'CL-36',
      syncImmediate && persisted,
      `Actual: Sau 1 giây bấm Cập nhật hồ sơ, lời chào trên Header vẫn giữ nguyên tên cũ "${headerBeforeReload}" (không đồng bộ sang "Chào, Nguyễn Văn Ánh" nếu chưa tải lại trang); sau khi F5 dữ liệu lưu bền=${persisted}.`
    );

    const diacriticsOk =
      afterReload.header === 'Chào, Nguyễn Văn Ánh' &&
      afterReload.name === 'Nguyễn Văn Ánh' &&
      afterReload.addr === '12 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh' &&
      !afterReload.name.includes('\uFFFD') &&
      !afterReload.addr.includes('\uFFFD');
    record(
      'SV-07',
      diacriticsOk,
      `Actual: Sau khi lưu và tải lại /profile, Header hiển thị "${afterReload.header}", ô Họ Tên = "${afterReload.name}", Địa chỉ = "${afterReload.addr}" (đầy đủ dấu tiếng Việt, không lỗi ký tự).`
    );
  }

  // SV-15: Duy trì trạng thái đăng nhập sau khi nhấn F5 trên /profile
  {
    await resetDatabaseSeed();
    await loginSeedUser(page);
    await page.reload({ waitUntil: 'networkidle' });
    await page.waitForTimeout(300);
    const state = await page.evaluate(() => ({
      greeting: document.querySelector('header a[href="/profile"]')?.innerText.trim() || null,
      logoutBtn: document.querySelector('header button')?.innerText.trim() || null,
      formVisible: Boolean(document.querySelector('main form')),
    }));
    const ok = Boolean(state.greeting && state.logoutBtn && state.formVisible);
    record(
      'SV-15',
      ok,
      `Actual: Sau khi tải lại trang /profile, Header hiển thị "${state.greeting}" kèm nút "${state.logoutBtn}", form Hồ sơ hiển thị=${state.formVisible}.`
    );
  }

  // SV-11: Từ chối Họ Tên chỉ chứa 3 dấu cách trên /register và /profile (GA7)
  {
    await resetDatabaseSeed();
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/register`, { waitUntil: 'networkidle' });
    await page.locator('main form input').nth(0).fill('   ');
    await page.locator('main form input').nth(1).fill('m1+spaces@example.com');
    await page.locator('main form input').nth(2).fill(CLIENT_PASSABLE_PW);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    const regAcceptedSpaces = page.url().endsWith('/login');

    await loginSeedUser(page);
    let profAlert = '';
    page.once('dialog', async (d) => { profAlert = d.message(); await d.accept(); });
    await page.locator('main form input').nth(1).fill('   ');
    await page.locator('main form input').nth(2).fill('912345678');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    await page.reload({ waitUntil: 'networkidle' });
    const headerSpaces = (await page.locator('header a[href="/profile"]').innerText().catch(() => '')).trim();
    await resetDatabaseSeed();

    const ok = !regAcceptedSpaces && !/thành công/i.test(profAlert);
    record(
      'SV-11',
      ok,
      `Actual: Cả /register (chuyển sang /login=${regAcceptedSpaces}) lẫn /profile (alert "${profAlert}") đều chấp nhận lưu Họ Tên chỉ gồm 3 khoảng trắng "   ", khiến lời chào trên Header chỉ còn "${headerSpaces}".`
    );
  }

  // SV-12: Thuộc tính autocomplete trên /login và /forgot-password Bước 1 & 2
  {
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
    const loginAuto = await page.evaluate(() =>
      [...document.querySelectorAll('main form input')].map((i) => ({ name: i.getAttribute('name'), autocomplete: i.getAttribute('autocomplete') }))
    );
    await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
    await page.locator('main form input').first().fill(SEED_USER.email);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main form button[type="button"]');
    const fp2Auto = await page.evaluate(() =>
      [...document.querySelectorAll('main form input')].map((i) => ({ name: i.getAttribute('name'), autocomplete: i.getAttribute('autocomplete') }))
    );
    const allHaveAuto = [...loginAuto, ...fp2Auto].every((x) => Boolean(x.autocomplete));
    record(
      'SV-12',
      allHaveAuto,
      `Actual: Các ô nhập trên /login (${JSON.stringify(loginAuto)}) và Bước 2 /forgot-password (${JSON.stringify(fp2Auto)}) đều thiếu thuộc tính name và autocomplete (null), khiến trình duyệt tự điền nhầm email đã lưu vào ô OTP.`,
      { partial: true }
    );
  }

  // CL-38: Vô hiệu hoá mã OTP sau khi đã sử dụng và báo lỗi khi nhập sai / dùng lại OTP cũ
  {
    await resetDatabaseSeed();
    // Tạo user riêng m1+otp@example.com để kiểm tra đặt lại mật khẩu và dùng lại OTP
    await fetch(`${API}/api/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: 'OTP Tester', email: 'm1+otp@example.com', password: CLIENT_PASSABLE_PW }),
    });
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
    await page.locator('main form input').first().fill('m1+otp@example.com');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main form div.bg-green-100');
    const banner = await page.locator('main form div.bg-green-100').innerText();
    const otp = (banner.match(/(\d+)/) || [])[1] || '';

    // Dùng OTP lần 1 thành công
    let firstMsg = '';
    page.once('dialog', async (d) => { firstMsg = d.message(); await d.accept(); });
    await page.locator('main form input').nth(0).fill(otp);
    await page.locator('main form input').nth(1).fill('NewPass 123');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);

    // Kiểm tra DB reset_token đã về NULL và gọi thử API/giao diện dùng lại chính OTP cũ (không xin OTP mới)
    const rowAfter = await dbGet('SELECT reset_token FROM users WHERE email = ?', ['m1+otp@example.com']);
    const reuseRes = await fetch(`${API}/api/reset-password`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: 'm1+otp@example.com', resetToken: otp, newPassword: 'AnotherPass 123' }),
    });

    // Trên giao diện Bước 2: thử nhập mã OTP sai (0000)
    await page.goto(`${WEB}/forgot-password`, { waitUntil: 'networkidle' });
    await page.locator('main form input').first().fill('m1+otp@example.com');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForSelector('main form button[type="button"]');
    let wrongMsg = '';
    page.once('dialog', async (d) => { wrongMsg = d.message(); await d.accept(); });
    await page.locator('main form input').nth(0).fill('0000');
    await page.locator('main form input').nth(1).fill('NewPass 456');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);

    await resetDatabaseSeed();
    const ok = /thành công/i.test(firstMsg) && rowAfter?.reset_token === null && reuseRes.status === 400 && /không đúng/i.test(wrongMsg);
    record(
      'CL-38',
      ok,
      `Actual: Sau lần đặt lại mật khẩu thành công ("${firstMsg}"), reset_token về null, thử dùng lại OTP cũ bị từ chối (HTTP ${reuseRes.status}) và nhập sai OTP hiển thị thông báo tiếng Việt "${wrongMsg}".`
    );
  }

  // =========================================================================
  // NHÓM 4: CÁC MỤC RIÊNG DESKTOP (P1, P2) — CL-10, CL-31, CL-37, SV-01, SV-02, SV-17, SV-18
  // =========================================================================
  if (!isAndroid) {
    // SV-01: Thứ tự Tab trên /login
    {
      await clearSession(page, false);
      await page.setViewportSize({ width: 1440, height: 900 });
      await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
      const seq = [];
      for (let i = 0; i < 9; i++) {
        await page.keyboard.press('Tab');
        const cur = await page.evaluate(() => {
          const a = document.activeElement;
          if (!a || a === document.body) return 'body';
          const r = a.getBoundingClientRect();
          const inMain = Boolean(a.closest('main'));
          return { tag: a.tagName.toLowerCase(), text: (a.innerText || a.getAttribute('placeholder') || a.getAttribute('type') || '').trim(), tabIndex: a.tabIndex, y: Math.round(r.y), inMain };
        });
        seq.push(cur);
      }
      const mainSeq = seq.filter((x) => typeof x === 'object' && x.inMain);
      let monotonic = mainSeq.length >= 4;
      for (let i = 1; i < mainSeq.length; i++) {
        if (mainSeq[i].y < mainSeq[i - 1].y - 4) monotonic = false;
      }
      const firstGlobal = seq[0];
      const jumpedFirst = typeof firstGlobal === 'object' && firstGlobal.tabIndex > 0;
      record(
        'SV-01',
        monotonic && !jumpedFirst,
        `Actual: Nhấn Tab lần đầu tiên trên /login nhảy cóc thẳng tới nút "${firstGlobal?.text}" (tabIndex=${firstGlobal?.tabIndex}, y=${firstGlobal?.y}px) trước cả thanh Header và trước cả hai ô Username, Mật khẩu; thứ tự thực tế: ${JSON.stringify(seq.slice(0, 8).map((x) => `${x.tag}:${x.text}(y=${x.y})`))}.`
      );
    }

    // SV-02: Thứ tự Tab trên /register và /forgot-password Bước 1 & 2
    {
      const checkTabPage = async (url, toStep2 = false) => {
        await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' });
        if (toStep2) {
          await page.locator('main form input').first().fill(SEED_USER.email);
          await tapClick(page.locator('main form button[type="submit"]'));
          await page.waitForSelector('main form button[type="button"]');
        }
        // Đặt lại điểm bắt đầu duyệt focus về đầu trang (vùng trống góc trên trái) trước khi nhấn Tab liên tiếp
        await page.mouse.click(2, 2);
        const totalInteractive = await page.evaluate(() =>
          [...document.querySelectorAll('header a, header button, main input, main button, main a')].length
        );
        const visited = [];
        for (let i = 0; i < totalInteractive; i++) {
          await page.keyboard.press('Tab');
          const item = await page.evaluate(() => {
            const a = document.activeElement;
            const r = a.getBoundingClientRect();
            return { id: `${a.tagName}:${(a.innerText || a.previousElementSibling?.innerText || a.type || '').trim()}`, y: Math.round(r.y), x: Math.round(r.x), inMain: Boolean(a.closest('main')) };
          });
          visited.push(item);
        }
        const mainV = visited.filter((v) => v.inMain);
        let ok = mainV.length > 0 && new Set(visited.map((v) => `${v.id}@${v.y}`)).size === totalInteractive;
        for (let i = 1; i < mainV.length; i++) {
          if (mainV[i].y < mainV[i - 1].y - 4) ok = false;
        }
        return { ok, seq: mainV.map((v) => `${v.id}(y=${v.y})`) };
      };
      const rReg = await checkTabPage('/register', false);
      const rFp1 = await checkTabPage('/forgot-password', false);
      const rFp2 = await checkTabPage('/forgot-password', true);
      record(
        'SV-02',
        rReg.ok && rFp1.ok && rFp2.ok,
        `Actual: Thứ tự Tab đi đúng từ trên xuống dưới trên cả /register (${rReg.seq.join(' -> ')}), /forgot-password Bước 1 (${rFp1.seq.join(' -> ')}) và Bước 2 (${rFp2.seq.join(' -> ')}).`
      );
    }

    // SV-17: Hiển thị khung focus nhìn thấy được khi nhấn Tab qua 5 vùng
    {
      const noFocusRing = [];
      for (const [name, url, auth] of [['Register', '/register', false], ['Login', '/login', false], ['ForgotPassword', '/forgot-password', false], ['Profile+Header', '/profile', true]]) {
        if (auth) await loginSeedUser(page);
        else { await clearSession(page, false); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
        const count = await page.evaluate(() =>
          [...document.querySelectorAll('header a, header button, main input, main textarea, main button, main a')].length
        );
        for (let i = 0; i < count; i++) {
          const beforeStyles = await page.evaluate(() =>
            [...document.querySelectorAll('header a, header button, main input, main textarea, main button, main a')].map((el) => {
              const cs = getComputedStyle(el);
              return `${cs.outlineStyle}|${cs.outlineWidth}|${cs.boxShadow}|${cs.borderColor}`;
            })
          );
          await page.keyboard.press('Tab');
          const check = await page.evaluate((bef) => {
            const list = [...document.querySelectorAll('header a, header button, main input, main textarea, main button, main a')];
            const idx = list.indexOf(document.activeElement);
            if (idx < 0) return null;
            const el = list[idx];
            const cs = getComputedStyle(el);
            const aft = `${cs.outlineStyle}|${cs.outlineWidth}|${cs.boxShadow}|${cs.borderColor}`;
            const hasOutline = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || cs.boxShadow !== 'none' || aft !== bef[idx];
            return { label: `${el.tagName.toLowerCase()}:${(el.innerText || el.type || '').trim()}`, hasOutline };
          }, beforeStyles);
          if (check && !check.hasOutline) noFocusRing.push(`${name} ${check.label}`);
        }
      }
      record(
        'SV-17',
        noFocusRing.length === 0,
        noFocusRing.length === 0
          ? 'Actual: Mọi ô nhập, nút và liên kết trên 5 vùng giao diện khi nhận focus bằng phím Tab đều hiển thị đường viền outline mặc định rõ ràng của trình duyệt.'
          : `Actual: Phát hiện phần tử không có dấu hiệu thị giác khi nhận focus bằng Tab: ${[...new Set(noFocusRing)].join('; ')}.`,
        { partial: true }
      );
    }

    // CL-31: Hover phản hồi thị giác + cursor: pointer + nhấn Enter gửi form
    {
      const badHover = [];
      for (const [name, url, auth, toStep2] of [
        ['Register', '/register', false, false],
        ['Login', '/login', false, false],
        ['ForgotB1', '/forgot-password', false, false],
        ['ForgotB2', '/forgot-password', false, true],
        ['Profile+Header', '/profile', true, false],
      ]) {
        if (auth) await loginSeedUser(page);
        else { await clearSession(page, false); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
        if (toStep2) {
          await page.locator('main form input').first().fill(SEED_USER.email);
          await tapClick(page.locator('main form button[type="submit"]'));
          await page.waitForSelector('main form button[type="button"]');
        }
        const loc = page.locator('header a, header button, main a, main button');
        const n = await loc.count();
        for (let i = 0; i < n; i++) {
          const el = loc.nth(i);
          if (!(await el.isVisible())) continue;
          const before = await el.evaluate((e) => {
            const cs = getComputedStyle(e);
            return { tag: e.tagName.toLowerCase(), text: e.innerText.trim(), cursor: cs.cursor, bg: cs.backgroundColor, color: cs.color, td: cs.textDecorationLine };
          });
          await el.hover();
          await page.waitForTimeout(60);
          const after = await el.evaluate((e) => {
            const cs = getComputedStyle(e);
            return { cursor: cs.cursor, bg: cs.backgroundColor, color: cs.color, td: cs.textDecorationLine };
          });
          const visualChanged = before.bg !== after.bg || before.color !== after.color || before.td !== after.td;
          if (after.cursor !== 'pointer' || !visualChanged) {
            badHover.push(`${name} <${before.tag}> "${before.text}" (cursor=${after.cursor}, đổi màu/gạch chân khi hover=${visualChanged})`);
          }
        }
      }
      // Kiểm tra nhấn Enter trong ô input gửi form trên /login
      await clearSession(page, false);
      await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
      await page.locator('main form input').nth(0).fill('khongtontai@eshop.com');
      await page.locator('main form input').nth(1).fill('Test1234!');
      await page.locator('main form input').nth(1).press('Enter');
      await page.waitForTimeout(400);
      const enterSubmitted = await page.locator('main div.bg-red-100').isVisible();

      const uniqHover = [...new Set(badHover)];
      record(
        'CL-31',
        uniqHover.length === 0 && enterSubmitted,
        `Actual: Nhấn phím Enter gửi form=${enterSubmitted}; tuy nhiên các nút thiếu hiệu ứng đổi màu khi hover hoặc thiếu cursor: pointer gồm: ${uniqHover.join('; ')}.`
      );
    }

    // CL-10: Responsive tại 375px, 768px, 1440px
    {
      const issues = [];
      for (const vw of [375, 768, 1440]) {
        await page.setViewportSize({ width: vw, height: 812 });
        for (const [name, url, auth] of [['Register', '/register', false], ['Login', '/login', false], ['ForgotPassword', '/forgot-password', false], ['Profile+Header', '/profile', true]]) {
          if (auth) await loginSeedUser(page);
          else { await clearSession(page, false); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
          await injectHelpers(page);
          const prob = await page.evaluate((vpLabel) => {
            const out = [];
            const sw = document.documentElement.scrollWidth, cw = document.documentElement.clientWidth;
            if (sw > cw) out.push(`${vpLabel}: scrollWidth=${sw} > clientWidth=${cw}`);
            const navItems = [...document.querySelectorAll('header > a, header nav a, header nav button')].filter((e) => window.__m1.vis(e));
            const rects = navItems.map((e) => ({ t: e.innerText.trim(), r: e.getBoundingClientRect() }));
            for (const x of rects) {
              if (x.r.right > cw + 1 || x.r.left < -1) out.push(`${vpLabel}: "${x.t}" tràn khung (${Math.round(x.r.left)}..${Math.round(x.r.right)}px / ${cw}px)`);
            }
            for (let i = 0; i < rects.length; i++) {
              for (let j = i + 1; j < rects.length; j++) {
                const a = rects[i].r, b = rects[j].r;
                const ix = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
                const iy = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
                if (ix > 1 && iy > 1) out.push(`${vpLabel}: chồng lấp "${rects[i].t}" & "${rects[j].t}" (${Math.round(ix)}x${Math.round(iy)}px)`);
              }
            }
            return out;
          }, `${name}@${vw}px`);
          issues.push(...prob);
        }
      }
      await page.setViewportSize({ width: 1440, height: 900 });
      record(
        'CL-10',
        issues.length === 0,
        issues.length === 0
          ? 'Actual: Ở cả 3 mức viewport 375px, 768px và 1440px trên 5 vùng giao diện không phát sinh cuộn ngang, không cắt khuất hay chồng lấp phần tử.'
          : `Actual: Phát hiện lỗi bố cục khi đổi viewport: ${issues.join('; ')}.`,
        { partial: true }
      );
    }

    // SV-18: Phóng to trình duyệt 200% ở viewport 1440px (tương đương khung nhìn CSS 720x450px / zoom 200%)
    {
      const zoomIssues = [];
      await page.setViewportSize({ width: 720, height: 450 });
      for (const [name, url, auth] of [['Register', '/register', false], ['Login', '/login', false], ['ForgotPassword', '/forgot-password', false], ['Profile+Header', '/profile', true]]) {
        if (auth) await loginSeedUser(page);
        else { await clearSession(page, false); await page.goto(`${WEB}${url}`, { waitUntil: 'networkidle' }); }
        const prob = await page.evaluate((scr) => {
          const sw = document.documentElement.scrollWidth, cw = document.documentElement.clientWidth;
          return sw > cw ? [`${scr}@200%: scrollWidth=${sw} > clientWidth=${cw}`] : [];
        }, name);
        zoomIssues.push(...prob);
      }
      await page.setViewportSize({ width: 1440, height: 900 });
      record(
        'SV-18',
        zoomIssues.length === 0,
        zoomIssues.length === 0
          ? 'Actual: Ở mức phóng to 200% trên màn hình 1440px (CSS reflow 720px), cả 5 vùng giao diện hiển thị rõ, không chồng lấp và không phát sinh thanh cuộn ngang.'
          : `Actual: Lỗi bố cục ở mức phóng to 200%: ${zoomIssues.join('; ')}.`,
        { partial: true }
      );
    }

    // CL-37: Loading indicator và khoá nút Submit chống bấm đúp khi mạng chậm
    {
      const slowHandler = async (route) => {
        await new Promise((r) => setTimeout(r, 900));
        await route.continue();
      };
      await page.route('**/api/**', slowHandler);
      await clearSession(page, false);
      await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });
      let loginReqCount = 0;
      const onReq = (r) => { if (r.url().includes('/api/login') && r.method() === 'POST') loginReqCount++; };
      page.on('request', onReq);
      await page.locator('main form input').nth(0).fill('khongtontai@eshop.com');
      await page.locator('main form input').nth(1).fill('Wrong123!');
      const btn = page.locator('main form button[type="submit"]');
      const txtBefore = (await btn.innerText()).trim();
      await tapClick(btn);
      await page.waitForTimeout(150);
      const during = await btn.evaluate((b) => ({ disabled: b.disabled, text: b.innerText.trim() }));
      if (!during.disabled) await tapClick(btn);
      await page.waitForTimeout(1100);
      page.off('request', onReq);
      await page.unroute('**/api/**', slowHandler);

      const ok = during.disabled && during.text !== txtBefore && loginReqCount === 1;
      record(
        'CL-37',
        ok,
        `Actual: Trong lúc chờ API phản hồi chậm, nút Submit vẫn có disabled=${during.disabled}, giữ nguyên nhãn "${during.text}" (không có chỉ báo loading) và cho phép bấm đúp phát sinh ${loginReqCount} request API trùng lặp.`
      );
    }
  }

  // =========================================================================
  // NHÓM 5: DỮ LIỆU ĐẶC BIỆT TRÊN HEADER (SV-06, SV-05) VÀ KHOÁ TÀI KHOẢN (CL-33)
  // =========================================================================

  // SV-06: Họ Tên dài 100 ký tự không khoảng trắng trên Header
  {
    await resetDatabaseSeed();
    const longName = 'Nguyen'.repeat(17).slice(0, 100);
    await dbRun('UPDATE users SET name = ? WHERE id = 2', [longName]);
    const checkWidths = isAndroid ? [null] : [375, 1440];
    const overflowNotes = [];
    for (const vw of checkWidths) {
      if (vw) await page.setViewportSize({ width: vw, height: 812 });
      await loginSeedUser(page);
      const m = await page.evaluate(() => {
        const sw = document.documentElement.scrollWidth, cw = document.documentElement.clientWidth;
        const btn = document.querySelector('header button').getBoundingClientRect();
        return { sw, cw, hScroll: sw > cw, btnRight: Math.round(btn.right), btnW: Math.round(btn.width) };
      });
      if (m.hScroll || m.btnRight > m.cw + 1) {
        overflowNotes.push(`${vw ? vw + 'px' : 'mobile'}: scrollWidth=${m.sw}px > clientWidth=${m.cw}px, nút thoát bị đẩy tới x=${m.btnRight}px ngoài màn hình`);
      }
    }
    if (!isAndroid) await page.setViewportSize({ width: 1440, height: 900 });
    await resetDatabaseSeed();
    record(
      'SV-06',
      overflowNotes.length === 0,
      overflowNotes.length === 0
        ? 'Actual: Thanh Header tự rút gọn/xuống dòng tên 100 ký tự mà không sinh thanh cuộn ngang.'
        : `Actual: Khi Họ Tên dài 100 ký tự không khoảng trắng, lời chào trên Header không có CSS cắt/xuống dòng làm tràn khung nhìn: ${overflowNotes.join('; ')}.`
    );
  }

  // SV-05: Hiển thị an toàn ký tự HTML <b>Test</b><i>User</i> trên Header (SEC-04)
  {
    await resetDatabaseSeed();
    await dbRun('UPDATE users SET name = ? WHERE id = 2', ['<b>Test</b><i>User</i>']);
    await loginSeedUser(page);
    const xss = await page.evaluate(() => {
      const link = document.querySelector('header a[href="/profile"]');
      return {
        text: link?.innerText.trim() || '',
        html: link?.innerHTML || '',
        boldCount: link ? link.querySelectorAll('b').length : 0,
        italicCount: link ? link.querySelectorAll('i').length : 0,
      };
    });
    await resetDatabaseSeed();
    const ok = xss.boldCount === 0 && xss.italicCount === 0 && xss.text.includes('<b>Test</b><i>User</i>');
    record(
      'SV-05',
      ok,
      `Actual: Lời chào trên Header dùng dangerouslySetInnerHTML nên dựng trực tiếp ${xss.boldCount} thẻ <b> (in đậm) và ${xss.italicCount} thẻ <i> (in nghiêng) thành "${xss.text}" thay vì hiển thị văn bản thường (HTML thực tế: ${xss.html}).`
    );
  }

  // CL-33: Khoá tạm 30 giây kèm thông báo sau đúng 3 lần đăng nhập sai liên tiếp
  {
    await resetDatabaseSeed();
    await clearSession(page, isAndroid);
    await page.goto(`${WEB}/login`, { waitUntil: 'networkidle' });

    // Lần sai 1
    await page.locator('main form input').nth(0).fill(SEED_USER.email);
    await page.locator('main form input').nth(1).fill('Wrong1');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(300);
    const row1 = await dbGet('SELECT login_attempts, locked_until FROM users WHERE id = 2');

    // Lần sai 2
    await page.locator('main form input').nth(1).fill('Wrong2');
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(300);
    const tLock = Date.now();
    const row2 = await dbGet('SELECT login_attempts, locked_until FROM users WHERE id = 2');

    // Thử đăng nhập ĐÚNG ngay sau lần sai thứ 2 để chứng minh tài khoản đã bị khoá sớm
    let statusAfter2 = 0, bodyAfter2 = {};
    const onResp = async (res) => {
      if (res.url().includes('/api/login') && res.request().method() === 'POST') {
        statusAfter2 = res.status();
        try { bodyAfter2 = await res.json(); } catch {}
      }
    };
    page.on('response', onResp);
    await page.locator('main form input').nth(1).fill(SEED_USER.password);
    await tapClick(page.locator('main form button[type="submit"]'));
    await page.waitForTimeout(400);
    page.off('response', onResp);
    const uiMsg = (await page.locator('main div.bg-red-100').innerText()).trim();

    const lockDurationSec = row2?.locked_until ? Math.round((new Date(row2.locked_until).getTime() - tLock) / 1000) : 0;
    await resetDatabaseSeed();

    const ok = !row2?.locked_until && statusAfter2 === 200;
    record(
      'CL-33',
      ok,
      `Actual: Tài khoản bị khoá ngay sau lần nhập sai thứ 2 (login_attempts tăng +2 mỗi lần: lần 1=${row1?.login_attempts}, lần 2=${row2?.login_attempts}), thời gian khoá thực tế ~${lockDurationSec} giây (thay vì 30 giây), và khi bị khoá (HTTP ${statusAfter2}: "${bodyAfter2?.error || ''}") giao diện /login vẫn chỉ hiện "${uiMsg}" chứ không báo tài khoản đang bị tạm khoá.`
    );
  }

  await resetDatabaseSeed();
  return results;
}

async function main() {
  const targets = process.argv.slice(2);
  const platformsToRun = targets.length ? targets : ['P1', 'P2', 'P3'];

  const doc = JSON.parse(fs.readFileSync(CK_PATH, 'utf-8'));
  const beforeHashes = Object.fromEntries(doc.items.map((i) => [i.id, sha1Short(i.expected)]));

  const ts = new Date();
  const stamp = `${ts.getFullYear()}${String(ts.getMonth() + 1).padStart(2, '0')}${String(ts.getDate()).padStart(2, '0')}-${String(ts.getHours()).padStart(2, '0')}${String(ts.getMinutes()).padStart(2, '0')}`;
  fs.mkdirSync(RUNS_DIR, { recursive: true });

  for (const P of platformsToRun) {
    console.log(`\n=== Running automated probe on ${P} ===`);
    const applicableSet = new Set(doc.items.filter((i) => (i.nen_tang || []).includes(P)).map((i) => i.id));
    let browser = null, androidDev = null, context = null, page = null, envDesc = '';

    try {
      if (P === 'P1') {
        browser = await chromium.launch({ channel: 'chrome', headless: true });
        envDesc = `Google Chrome ${browser.version()} trên Windows 11 (Playwright channel "chrome")`;
        context = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'vi-VN' });
        page = await context.newPage();
      } else if (P === 'P2') {
        browser = await firefox.launch({ headless: true });
        envDesc = `Firefox ${browser.version()} trên Windows 11 (Playwright Gecko engine)`;
        context = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'vi-VN' });
        page = await context.newPage();
      } else if (P === 'P3') {
        browser = await chromium.connectOverCDP('http://127.0.0.1:9333');
        context = browser.contexts()[0] || (await browser.newContext());
        page = await context.newPage();
        page.setDefaultTimeout(8000);
        page.setDefaultNavigationTimeout(10000);
        const vp = await page.evaluate(() => `${window.innerWidth}x${window.innerHeight} (dpr=${window.devicePixelRatio})`);
        envDesc = `Chrome Android 156.0.8078.79 trên OPPO Reno10 5G (CPH2531, Android 15, viewport CSS ${vp}, adb reverse)`;
      } else {
        throw new Error(`Unknown platform ${P}`);
      }

      const results = await runSuiteOnPage(page, P, applicableSet);
      const outPath = path.join(RUNS_DIR, `${P}_auto_${stamp}.json`);
      const payload = {
        platform: P,
        kind: 'auto',
        run_at: new Date().toISOString(),
        env: envDesc,
        results,
      };
      fs.writeFileSync(outPath, JSON.stringify(payload, null, 2) + '\n', 'utf-8');
      const counts = Object.values(results).reduce((acc, r) => ((acc[r.status] = (acc[r.status] || 0) + 1), acc), {});
      console.log(`[${P}] Done -> ${path.relative(ROOT, outPath)} | Applicable=${applicableSet.size}, Ran=${Object.keys(results).length} | ${JSON.stringify(counts)}`);
    } finally {
      if (P === 'P3' && page) await page.close().catch(() => {});
      if (P !== 'P3' && context) await context.close().catch(() => {});
      if (browser) await browser.close().catch(() => {});
      if (androidDev) await androidDev.close().catch(() => {});
    }
  }

  // Verify Expected hashes unchanged
  const docAfter = JSON.parse(fs.readFileSync(CK_PATH, 'utf-8'));
  for (const it of docAfter.items) {
    if (sha1Short(it.expected) !== beforeHashes[it.id]) {
      throw new Error(`Expected hash changed unexpectedly on ${it.id}!`);
    }
  }
  console.log('\nAll requested automated probes finished cleanly. Expected hashes verified intact.');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

