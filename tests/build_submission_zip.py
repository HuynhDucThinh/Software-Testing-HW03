#!/usr/bin/env python3
"""Build and verify the Moodle submission archive 23120199_HW03_AI_GUIUsability_100.zip (< 20 MB).

Optional flag:
  python -B tests/build_submission_zip.py --set-youtube "https://youtu.be/..."
  -> Automatically replaces [TODO_YOUTUBE_DEMO_URL] in README.md and Main_Report.md,
     re-exports all 6 PDFs, refreshes git_commit_log.txt, and rebuilds the final .zip!
"""
import argparse
import os
import subprocess
import sys
import zipfile
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
ZIP_STEM = "23120199_HW03_AI_GUIUsability_100"
ZIP_NAME = f"{ZIP_STEM}.zip"
MAX_MB = 20.0

INCLUDE_ROOT_FILES = [
    "README.md",
    "Main_Report.md",
    "Main_Report.pdf",
    "Bug_Report.md",
    "Bug_Report.pdf",
    "AI_Critique_and_Audit_Report.md",
    "AI_Critique_and_Audit_Report.pdf",
    "git_commit_log.txt",
]

INCLUDE_DIRS = [
    ".agents",
    "ai-forms",
    "ai_log",
    "bugs",
    "checklist",
    "screenshots",
    "tests",
    "usability",
]

EXCLUDE_DIR_NAMES = {
    ".git",
    ".local",
    ".expo",
    "node_modules",
    "__pycache__",
    "temp",
    "evidence_raw",
}

EXCLUDE_EXTS = {".mp4", ".webm", ".mkv", ".zip", ".pyc", ".log", ".sqlite", ".sqlite-journal"}

REQUIRED_PATHS_IN_ZIP = [
    "README.md",
    "Main_Report.md",
    "Main_Report.pdf",
    "Bug_Report.md",
    "Bug_Report.pdf",
    "AI_Critique_and_Audit_Report.md",
    "AI_Critique_and_Audit_Report.pdf",
    "git_commit_log.txt",
    "checklist/M1_GUI_Checklist_And_Summary.xlsx",
    "checklist/checklist.json",
    "usability/plan.md",
    "usability/participant_kit.md",
    "usability/participants.md",
    "usability/recordings/LINKS.md",
    "usability/sus_and_metrics_summary.md",
    "usability/findings.md",
    "ai-forms/AI-02_Audit_Report_23120199.md",
    "ai-forms/AI-02_Audit_Report_23120199.pdf",
    "ai-forms/AI-03_Disclosure_Form_23120199.md",
    "ai-forms/AI-03_Disclosure_Form_23120199.pdf",
    "ai-forms/AI-05_Privacy_Checklist_23120199.md",
    "ai-forms/AI-05_Privacy_Checklist_23120199.pdf",
    ".agents/skills/gui-checklist-testing/SKILL.md",
    ".agents/skills/usability-evaluation/SKILL.md",
]


def apply_youtube_url(url: str) -> None:
    url = url.strip()
    md_link = f"[Video Demo YouTube]({url}) (`{url}`)"
    for rel in ("README.md", "Main_Report.md"):
        p = ROOT / rel
        txt = p.read_text(encoding="utf-8")
        txt = txt.replace("`[TODO_YOUTUBE_DEMO_URL]` *(cập nhật sau khi quay xong)*", md_link)
        txt = txt.replace("*(chờ gắn `[TODO_YOUTUBE_DEMO_URL]`)*", "")
        txt = txt.replace("*(chốt khi gắn link YouTube)*", "")
        txt = txt.replace("[TODO_YOUTUBE_DEMO_URL]", url)
        p.write_text(txt, encoding="utf-8")
    subprocess.run(["node", str(ROOT / "tests" / "export_pdfs.mjs")], cwd=ROOT, check=True)
    log_out = subprocess.check_output(
        ["git", "log", "--date=iso-strict", "--stat", "--pretty=fuller"],
        cwd=ROOT,
    )
    (ROOT / "git_commit_log.txt").write_bytes(log_out)


def should_skip(path: Path) -> bool:
    rel_parts = path.relative_to(ROOT).parts
    if any(part in EXCLUDE_DIR_NAMES for part in rel_parts):
        return True
    if path.name.startswith(".tmp_") or path.name in {".DS_Store", "Thumbs.db", ".gitkeep"}:
        return True
    if path.suffix.lower() in EXCLUDE_EXTS:
        return True
    return False


def build_zip() -> Path:
    out_zip = ROOT / ZIP_NAME
    if out_zip.exists():
        out_zip.unlink()

    files_to_pack: list[Path] = []
    for rf in INCLUDE_ROOT_FILES:
        p = ROOT / rf
        if not p.is_file():
            sys.exit(f"[ERROR] Thiếu file bắt buộc ở thư mục gốc: {rf}")
        files_to_pack.append(p)

    for d in INCLUDE_DIRS:
        dp = ROOT / d
        if not dp.is_dir():
            continue
        for root_str, dirs, files in os.walk(dp):
            dirs[:] = sorted(dn for dn in dirs if dn not in EXCLUDE_DIR_NAMES)
            for fn in sorted(files):
                fp = Path(root_str) / fn
                if not should_skip(fp):
                    files_to_pack.append(fp)

    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for fp in files_to_pack:
            rel = fp.relative_to(ROOT).as_posix()
            zf.write(fp, f"{ZIP_STEM}/{rel}")

    # Verify archive integrity and required contents
    with zipfile.ZipFile(out_zip, "r") as zf:
        bad = zf.testzip()
        if bad is not None:
            sys.exit(f"[ERROR] File lỗi CRC trong zip: {bad}")
        namelist = set(zf.namelist())
        for req in REQUIRED_PATHS_IN_ZIP:
            full_req = f"{ZIP_STEM}/{req}"
            if full_req not in namelist:
                sys.exit(f"[ERROR] Thiếu file bắt buộc trong zip: {full_req}")

    size_bytes = out_zip.stat().st_size
    size_mib = size_bytes / (1024 * 1024)
    size_mb_dec = size_bytes / 1_000_000
    ok = size_mib < MAX_MB and size_mb_dec < MAX_MB
    status = "ĐẠT (< 20 MB cả hệ nhị phân MiB & thập phân MB)" if ok else "VƯỢT 20 MB!"
    print(
        f"[OK] Đã tạo {ZIP_NAME}: {len(files_to_pack)} files | {size_mib:.2f} MiB ({size_mb_dec:.2f} MB thập phân / {size_bytes:,} bytes) -> {status}"
    )
    if not ok:
        sys.exit(1)
    return out_zip


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--set-youtube", help="URL YouTube Video Demo Task 4 để điền tự động và đóng gói lại")
    args = ap.parse_args()
    if args.set_youtube:
        apply_youtube_url(args.set_youtube)
    build_zip()


if __name__ == "__main__":
    main()
