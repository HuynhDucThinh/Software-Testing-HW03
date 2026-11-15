# Mẫu bug report (Markdown và GitHub Issue)

Dưới chính sách `AI Policy: Open`, `scripts/bug_skeleton.py` gom nhóm và trích xuất khung dữ kiện (`item`, `nền tảng`, `môi trường`, `Expected`, `Actual`, `ảnh`); AI có thể hỗ trợ soạn nháp mô tả từ dữ kiện thực tế nhưng **SV bắt buộc kiểm duyệt, hiệu đính toàn bộ nội dung kỹ thuật và mức `Severity`** trước khi chốt (`Human review`). Dùng **cùng nội dung** cho `Bug_Report.md` và GitHub Issue. Đăng issue bằng `gh issue create --body-file BUG-<n>.md` hoặc dán trên web; **đính ảnh vào issue**.

```markdown
# [IA-0x] <Tiêu đề ngắn mô tả hiện tượng>

## Summary
<1 đến 2 câu: lỗi là gì, ở màn hình nào.>

- Bug ID: BUG-<n>
- Checklist item: <CL-xx / SV-xx>
- Requirement: <FR-xx>
- Loại lỗi: <Visual-Layout | State | Responsive | Typo-Localization>
- Severity: <Critical | Major | Minor | Cosmetic>
- Priority: <High | Medium | Low>

## Environment
- SUT: eshop-sut @ <commit>
- Nền tảng: <trình duyệt + phiên bản, OS, thiết bị>
- URL: http://localhost:5173/<route>
- Viewport: <w x h>

## Preconditions
<Trạng thái cần có: khách / đã đăng nhập, dữ liệu seed.>

## Steps to reproduce
1. ...
2. ...

## Expected result
<Theo đặc tả, kèm mã FR.>

## Actual result
<Nguyên văn quan sát được.>

## Impact
<Ảnh hưởng đến người dùng.>

## Reproducibility
<Tái hiện trên P1 / P2 / P3? Luôn luôn hay thỉnh thoảng?>

## Evidence
![<mô tả>](../screenshots/task1_failed/P1_CL-xx.png)
```

Mức severity gợi ý:

- Critical: chặn hoàn thành luồng chính (đăng ký / đăng nhập / đặt lại mật khẩu).
- Major: sai đặc tả làm người dùng khó hoặc dễ nhầm lẫn đáng kể.
- Minor: sai đặc tả nhưng luồng chính vẫn dùng được.
- Cosmetic: khác biệt thị giác nhỏ.

