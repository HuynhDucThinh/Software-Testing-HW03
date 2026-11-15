import fs from 'fs';
import path from 'path';
import { execFileSync } from 'child_process';
import { createRequire } from 'module';
import { pathToFileURL } from 'url';

const require = createRequire(import.meta.url);
const { chromium } = require('./node_modules/playwright');

const ROOT = path.resolve(import.meta.dirname, '..');

const TARGETS = [
  {
    md: 'Main_Report.md',
    pdf: 'Main_Report.pdf',
    docLabel: 'Main Report — HW03-AI (M1 & F1)',
  },
  {
    md: 'AI_Critique_and_Audit_Report.md',
    pdf: 'AI_Critique_and_Audit_Report.pdf',
    docLabel: 'AI Critique & AI Audit Report — HW03-AI',
  },
  {
    md: 'Bug_Report.md',
    pdf: 'Bug_Report.pdf',
    docLabel: 'Bug Report (BUG-01..BUG-28) — HW03-AI',
  },
];

async function run() {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  try {
    for (const t of TARGETS) {
      const mdPath = path.join(ROOT, t.md);
      const pdfPath = path.join(ROOT, t.pdf);
      const tmpHtmlPath = path.join(ROOT, `.tmp_${path.basename(t.md, '.md')}.html`);
      try {
        execFileSync('python', ['-B', path.join(ROOT, 'tests', 'md_to_html.py'), mdPath, tmpHtmlPath], {
          stdio: 'inherit',
        });
        const page = await browser.newPage();
        await page.goto(pathToFileURL(tmpHtmlPath).href, { waitUntil: 'networkidle' });
        await page.pdf({
          path: pdfPath,
          format: 'A4',
          printBackground: true,
          displayHeaderFooter: true,
          margin: {
            top: '15mm',
            bottom: '16mm',
            left: '12mm',
            right: '12mm',
          },
          headerTemplate: `
            <div style="width:100%; font-family:'Segoe UI',Arial,sans-serif; font-size:7.5pt; color:#64748b; padding:0 12mm; display:flex; justify-content:space-between;">
              <span>${t.docLabel}</span>
              <span>Huỳnh Đức Thịnh — 23120199 (23120199@student.hcmus.edu.vn)</span>
            </div>`,
          footerTemplate: `
            <div style="width:100%; font-family:'Segoe UI',Arial,sans-serif; font-size:7.5pt; color:#64748b; padding:0 12mm; display:flex; justify-content:space-between;">
              <span>Software Testing — HW03-AI (GUI &amp; Usability Testing)</span>
              <span>Trang <span class="pageNumber"></span> / <span class="totalPages"></span></span>
            </div>`,
        });
        await page.close();
        const sizeMB = (fs.statSync(pdfPath).size / (1024 * 1024)).toFixed(2);
        console.log(`[OK] ${t.pdf} (${sizeMB} MB)`);
      } finally {
        if (fs.existsSync(tmpHtmlPath)) {
          fs.unlinkSync(tmpHtmlPath);
        }
      }
    }
  } finally {
    await browser.close();
  }
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
