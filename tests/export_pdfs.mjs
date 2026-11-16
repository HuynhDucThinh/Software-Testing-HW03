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
  {
    md: 'ai-forms/AI-02_Audit_Report_23120199.md',
    pdf: 'ai-forms/AI-02_Audit_Report_23120199.pdf',
    docLabel: '[AI-02] FIT@HCMUS — AI Audit Report (23120199)',
  },
  {
    md: 'ai-forms/AI-03_Disclosure_Form_23120199.md',
    pdf: 'ai-forms/AI-03_Disclosure_Form_23120199.pdf',
    docLabel: '[AI-03] FIT@HCMUS — AI Use Disclosure Form (23120199)',
  },
  {
    md: 'ai-forms/AI-05_Privacy_Checklist_23120199.md',
    pdf: 'ai-forms/AI-05_Privacy_Checklist_23120199.pdf',
    docLabel: '[AI-05] FIT@HCMUS — AI Privacy Checklist (23120199)',
  },
];

async function run() {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  try {
    for (const t of TARGETS) {
      const mdPath = path.join(ROOT, t.md);
      const pdfPath = path.join(ROOT, t.pdf);
      const tmpHtmlPath = path.join(path.dirname(mdPath), `.tmp_${path.basename(t.md, '.md')}.html`);
      try {
        execFileSync('python', ['-B', path.join(ROOT, 'tests', 'md_to_html.py'), mdPath, tmpHtmlPath, '--pdf-opt'], {
          stdio: 'inherit',
        });
        const page = await browser.newPage({ viewport: { width: 703, height: 994 } });
        await page.emulateMedia({ media: 'print' });
        await page.goto(pathToFileURL(tmpHtmlPath).href, { waitUntil: 'networkidle' });
        const diag = await page.evaluate(() => {
          const de = document.documentElement;
          const docOverflow = Math.max(0, de.scrollWidth - de.clientWidth);
          const brokenImgs = [...document.querySelectorAll('img')].filter(
            (img) => !img.complete || img.naturalWidth === 0
          ).length;
          return { docOverflow, brokenImgs, tables: document.querySelectorAll('table').length };
        });
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
        execFileSync(
          'python',
          [
            '-B',
            '-c',
            `import fitz, os, sys
p = sys.argv[1]
doc = fitz.open(p)
doc.subset_fonts()
if hasattr(doc, 'rewrite_images'):
    doc.rewrite_images(dpi_threshold=75, dpi_target=72, quality=68)
tmp = p + '.opt.pdf'
doc.save(tmp, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True)
doc.close()
os.replace(tmp, p)`,
            pdfPath,
          ],
          { stdio: 'inherit' }
        );
        const sizeMB = (fs.statSync(pdfPath).size / (1024 * 1024)).toFixed(2);
        console.log(
          `[OK] ${t.pdf} (${sizeMB} MB | tables=${diag.tables} | docOverflow=${diag.docOverflow}px | brokenImgs=${diag.brokenImgs})`
        );
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
