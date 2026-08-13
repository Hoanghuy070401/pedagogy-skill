# ADR 0002 — Provider boundary: interface tối giản `generate(prompt) -> str`, không phụ thuộc tính năng riêng của 1 provider

**Trạng thái:** Chấp nhận
**Ngày:** 2026-08-11
**Liên quan:** Milestone 1, 3; `lessonforge/src/lessonforge/providers/`

## Bối cảnh

Plan yêu cầu "đổi provider không đổi hợp đồng output" (điều kiện hoàn thành
Milestone 3) và "ít nhất một cloud adapter và một OpenAI-compatible local
adapter qua cùng interface" (mục 4.3). Các provider OpenAI hiện đại có nhiều
tính năng riêng (function calling, JSON mode/structured output qua
`response_format`, logit bias...) mà không phải provider local nào (Ollama, LM
Studio, vLLM chạy model mã nguồn mở) cũng hỗ trợ đầy đủ hoặc hỗ trợ giống hệt
nhau.

## Quyết định

1. `AIProvider` (`providers/base.py`) chỉ có đúng 1 method bắt buộc:
   `generate(self, prompt: str, **params) -> str`. Không có method riêng cho
   structured output, function calling, hay streaming.
2. **Structured output (Milestone 3) được xây ở tầng lessonforge, không phải
   tầng provider.** `lessonforge.structured.generate_structured()` yêu cầu
   model trả JSON thuần qua prompt engineering (mô tả schema mong muốn trong
   prompt, dặn không bọc code fence), tự parse + validate bằng Pydantic, và tự
   retry kèm thông báo lỗi cụ thể nếu model trả sai định dạng. Điều này chạy
   được với MỌI provider hiện có (cloud lẫn local) vì không dựa vào tính năng
   riêng của OpenAI.
3. `AIProvider.cloud: bool` (mặc định `False`) là thuộc tính DUY NHẤT tách
   biệt cloud/local mà phần còn lại của hệ thống được phép dựa vào (dùng cho
   outbound preview — xem ADR 0001). Không có thuộc tính nào khác kiểu
   `supports_json_mode`/`supports_function_calling` — nếu sau này thật sự cần,
   đó là quyết định mới, không phải mặc định ngầm.
4. 3 provider local (`OllamaProvider`, `LMStudioProvider`, `VLLMProvider`) đều
   kế thừa `OpenAICompatibleProvider` (dùng chung REST API dạng OpenAI-
   compatible mà các server này export) — đây là lý do "OpenAI-compatible
   local adapter" trong plan mục 4.3 chỉ cần 1 lớp base dùng chung, không phải
   3 implementation riêng biệt.

## Hệ quả

- **Được:** thêm 1 provider mới chỉ cần implement `generate()`; toàn bộ
  planner/generator (Milestone 3) hoạt động không sửa gì.
- **Mất:** không tận dụng được structured-output mode gốc của OpenAI (nhanh
  hơn, ít lỗi parse hơn so với prompt-engineering JSON). Đánh đổi này được
  chấp nhận vì mục tiêu "không khoá vào 1 nhà cung cấp AI" (mục 2 của
  `plan-xay-dung-he-sinh-thai.md`) quan trọng hơn tốc độ/độ tin cậy của riêng
  1 provider.
- Retry ở `generate_structured` là **cơ chế bù cho việc không có JSON mode
  gốc** — nếu sau này thêm 1 provider hỗ trợ JSON mode thật, nó vẫn phải đi
  qua interface `generate(prompt) -> str` như các provider khác; JSON mode có
  thể bật ở bên trong implementation của provider đó (qua `**params`) nhưng
  không được thay đổi hợp đồng trả về (`str`).
