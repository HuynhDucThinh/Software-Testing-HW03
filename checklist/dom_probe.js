// dom_probe.js - dán vào DevTools Console của từng trang M1 (Register, Login, ForgotPassword, Profile).
// Chỉ ĐỌC DOM, không sửa gì. In JSON dữ kiện cho người chạy checklist chấm; KHÔNG tự kết luận Pass/Fail.
// Bước 3 của skill gui-checklist-testing: chép file này vào thư mục checklist/.
(() => {
  const txt = (el) => (el?.innerText || el?.value || "").trim().replace(/\s+/g, " ").slice(0, 80);
  const box = (el) => { const r = el.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }; };
  const visible = (el) => !!(el.offsetParent || el.getClientRects().length) && getComputedStyle(el).visibility !== "hidden";
  const labelOf = (el) => {
    if (el.id) { const l = document.querySelector(`label[for="${CSS.escape(el.id)}"]`); if (l) return { text: txt(l), linked: true }; }
    const wrap = el.closest("label"); if (wrap) return { text: txt(wrap), linked: true };
    const prev = el.parentElement?.querySelector("label"); return prev ? { text: txt(prev), linked: false } : null;
  };
  // luminance / contrast theo WCAG 2.x để lấy dữ kiện tương phản chữ-nền của nút
  const lum = (rgb) => { const [r, g, b] = rgb.map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
  const parse = (s) => (s.match(/[\d.]+/g) || []).slice(0, 3).map(Number);
  const contrast = (fg, bg) => { const a = lum(parse(fg)), b = lum(parse(bg)); const [hi, lo] = a > b ? [a, b] : [b, a]; return +(((hi + 0.05) / (lo + 0.05)).toFixed(2)); };

  const focusables = [...document.querySelectorAll("a[href], button, input, select, textarea, [tabindex]")]
    .filter((e) => !e.disabled && e.tabIndex >= 0 && visible(e));
  // thứ tự Tab theo quy tắc trình duyệt: tabindex > 0 tăng dần trước, sau đó tabindex = 0 theo thứ tự DOM
  const tabOrder = [...focusables.filter((e) => e.tabIndex > 0).sort((a, b) => a.tabIndex - b.tabIndex),
                    ...focusables.filter((e) => e.tabIndex === 0)]
    .map((e) => ({ tag: e.tagName.toLowerCase(), text: txt(e) || e.getAttribute("placeholder") || e.type, tabindex: e.tabIndex, y: box(e).y }));
  const fields = [...document.querySelectorAll("input, textarea, select")].map((e) => {
    const l = labelOf(e);
    return { tag: e.tagName.toLowerCase(), type: e.type, name: e.name || null, required: e.required, disabled: e.disabled, readonly: e.readOnly,
             label: l?.text ?? null, label_linked: l?.linked ?? false, label_has_asterisk: !!l?.text?.includes("*"),
             placeholder: e.getAttribute("placeholder"), maxlength: e.getAttribute("maxlength"), autocomplete: e.getAttribute("autocomplete"),
             aria_label: e.getAttribute("aria-label"), aria_describedby: e.getAttribute("aria-describedby") };
  });
  const buttons = [...document.querySelectorAll("button, input[type=submit]")].map((b) => {
    const cs = getComputedStyle(b);
    return { text: txt(b), type: b.type, disabled: b.disabled, bg: cs.backgroundColor, color: cs.color, contrast: contrast(cs.color, cs.backgroundColor),
             font: `${cs.fontFamily} ${cs.fontSize}`, ...box(b) };
  });
  const submit = document.querySelector("form button[type=submit], form input[type=submit]");
  const alerts = [...document.querySelectorAll('[role=alert], [class*="red-"], [class*="error"], [class*="green-"]')]
    .filter((e) => visible(e) && txt(e))
    .map((e) => ({ text: txt(e), cls: e.className, y: box(e).y, above_submit: submit ? box(e).y < box(submit).y : null }));
  const overflowX = [...document.querySelectorAll("body *")].filter((e) => visible(e) && e.scrollWidth > e.clientWidth + 1 && getComputedStyle(e).overflowX === "visible").slice(0, 10).map(txt);
  const out = {
    url: location.href, ua: navigator.userAgent, viewport: `${innerWidth}x${innerHeight}`,
    prefers_dark: matchMedia("(prefers-color-scheme: dark)").matches,
    title: document.title, lang: document.documentElement.lang, dir: document.documentElement.dir || getComputedStyle(document.documentElement).direction,
    h1: [...document.querySelectorAll("h1")].map(txt), headings: [...document.querySelectorAll("h1,h2,h3")].map((h) => `${h.tagName}: ${txt(h)}`),
    horizontal_scroll: document.documentElement.scrollWidth > innerWidth,
    fields, buttons, tab_order: tabOrder, messages: alerts,
    nav_links: [...document.querySelectorAll("header a, nav a, header button")].map((a) => ({ text: txt(a), href: a.getAttribute("href"), aria_current: a.getAttribute("aria-current"), cls: a.className })),
    innerhtml_risk: [...document.querySelectorAll("header *")].filter((e) => e.children.length && /<[a-z]/i.test(e.textContent)).map(txt),
    images_without_alt: [...document.images].filter((i) => !i.getAttribute("alt")).length,
    links_without_text: [...document.querySelectorAll("a")].filter((a) => !txt(a) && !a.getAttribute("aria-label")).length,
    text_overflow_candidates: overflowX,
    note: "Dữ kiện thô để SV chấm; không phải kết luận Pass/Fail.",
  };
  console.log(JSON.stringify(out, null, 2));
  return out;
})();
