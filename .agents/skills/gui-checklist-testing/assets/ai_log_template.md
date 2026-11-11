# Mẫu một entry AI log (Ghi nối tiếp vào cuối `ai_log/AI_Log.md`)

Mỗi lần dùng AI, nối tiếp (**append**) một mục `## Entry NN — ...` vào cuối file duy nhất `ai_log/AI_Log.md` (`NN` là số thứ tự tăng dần). `scripts/ai_audit_export.py` tự động tách toàn bộ các entry trong `ai_log/AI_Log.md` để sinh `AI_Critique_and_Audit_Report.md`. Giữ đúng các nhãn in đậm bên dưới. Không đưa khoá bí mật, dữ liệu người thật hay bài của sinh viên khác vào prompt.

```markdown
## Entry <NN> — <YYYY-MM-DD> - <việc đang làm, vd: Bước 1 / IA-02 nháp checklist>

**Tool:** <Antigravity / Claude / ChatGPT / Gemini / Copilot / Cursor / ...>
**Date and time:** <ngày, giờ, múi giờ>
**Task / Step:** <Task 1, Bước n, IA-0x>
**Prompt:**
<prompt nguyên văn>

**AI output:**
<output nguyên văn hoặc đường dẫn file đã đóng băng, vd checklist/ai-outputs/...>

**Kept:** <phần dùng gần như nguyên bản>
**Changed:** <phần sửa và lý do>
**Rejected:** <phần loại bỏ và lý do>
**By hand:** <phần SV tự viết hoặc tự thực hiện>

---
```

Quy tắc:

- Một lần tương tác, một entry nối tiếp ở cuối `ai_log/AI_Log.md`. Không gộp nhiều bước vào một prompt.
- Prompt ghi đúng nguyên văn đã gửi; nêu rõ bước và IA đang làm.
- Ghi trung thực phần Kept / Changed / Rejected / By hand: SV chịu trách nhiệm toàn bộ nội dung nộp.
- Nếu không dùng AI cho một phần việc nào, không tạo entry cho phần đó. Nếu cả bài không dùng AI: khai báo "I do not use any AI help in this exercise." (mục 9 của đề).
