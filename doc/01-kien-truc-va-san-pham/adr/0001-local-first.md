# ADR 0001 — Local-first: dữ liệu và package không rời máy trừ khi có lời gọi cloud provider tường minh

**Trạng thái:** Chấp nhận
**Ngày:** 2026-08-11
**Liên quan:** Milestone 1–2, Giai đoạn A của `plan-xay-dung-he-sinh-thai.md`

## Bối cảnh

Open Lesson Package chứa nguồn giáo viên tự cung cấp (có thể có bản quyền chưa
rõ ràng — xem `04-bao-cao-nguon-chat-luong.md` trong pilot Vật Lý 10) và nội
dung bài dạy. Người dùng cần biết chắc dữ liệu của họ không bị gửi đi đâu ngoài
ý muốn, đặc biệt khi vẫn dùng provider cục bộ (Ollama/LM Studio/vLLM).

## Quyết định

1. **Toàn bộ package là 1 thư mục trên đĩa cục bộ**, không có bước upload/sync
   bắt buộc nào trong `open-lesson-spec`, `lessonforge`, `EduEvals`.
2. **Ingest/extract/corpus (Milestone 2) không gọi mạng cho file local.**
   `lessonforge.corpus.add_source` xử lý PDF/DOCX/Markdown/text hoàn toàn cục
   bộ; chỉ `add_source_from_url` mới cần mạng, và đó là adapter TÁCH RIÊNG
   (`ingest_url`/`extract_url`), không lẫn vào đường xử lý file local. Test
   `lessonforge/tests/test_corpus.py::test_local_ingest_and_search_make_no_network_calls`
   chặn `socket.socket.connect` để khẳng định điều này bằng code, không chỉ
   bằng tài liệu.
3. **Mọi lời gọi ra ngoài máy tới provider cloud phải qua outbound preview.**
   `AIProvider.cloud: bool` phân biệt cloud/local; `lessonforge.preview.
   require_outbound_confirmation` chặn lời gọi tới provider `cloud=True` nếu
   người dùng chưa xác nhận (`--confirm-outbound`), và luôn in ra chính xác
   nội dung sẽ gửi đi trước khi gửi.
4. **Không lưu secret vào package.** `ProvenanceRecord` chỉ lưu tên
   provider/model, không lưu API key. `EduEvals.check_secrets` (Giai đoạn D)
   quét ngược lại: nếu 1 secret vô tình lọt vào artifact/provenance, đó là
   lỗi chặn phát hành (`eduevals release`).

## Hệ quả

- Provider local (Ollama/LM Studio/vLLM) là công dân hạng nhất, không phải
  "chế độ dự phòng" của cloud — cùng interface `AIProvider.generate`, cùng
  luồng generate-artifacts, không có code path nào giả định phải có mạng.
- Người dùng chọn dùng cloud provider vẫn phải xác nhận từng lần chạy có gọi
  cloud (`--confirm-outbound`) — không có "ghi nhớ lựa chọn" ở M1–M3; nếu sau
  này cần UX mượt hơn (ví dụ nhớ lựa chọn trong 1 phiên CLI), đó là thay đổi
  có chủ đích, cần ADR riêng, không phải nới lỏng ngầm.
- Chi phí: mỗi lần chạy CLI với provider cloud phải build lại prompt 2 lần
  (1 lần để preview, 1 lần trong hàm generate thật) ở lệnh `generate` một-phát
  của Milestone 1 — chấp nhận được vì đây là I/O cục bộ rẻ, không phải lời gọi
  model.
