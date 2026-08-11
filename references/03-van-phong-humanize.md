# Văn phong — viết như người thật

Trích §5 của `01-huong-dan-soan-bai.md`, gom thêm các luật ngôn ngữ nằm rải ở §3 rule set và §6.1.
Áp dụng cho mọi prose bài học, caption, quiz explain và copy giao diện học tập.

Phương pháp gốc: [humanize-writing-skill](https://github.com/lguz/humanize-writing-skill) (MIT),
adapt cho tiếng Việt. Triết lý (Paul Graham): *"viết như một người thông minh đang nghĩ thành tiếng"*.

## Quy trình 3 lượt

### Lượt 1 — bỏ chữ máy móc / giọng dịch máy

Tránh: "nhằm mục đích", "một cách", "đóng vai trò quan trọng", "vô cùng", "hết sức",
"đa dạng và phong phú", "nói chung là", "góp phần", "mang lại hiệu quả cao".

Thay bằng từ đời thường, cụ thể — "giúp bạn" thay vì "đóng vai trò hỗ trợ".

### Lượt 2 — phá cấu trúc rập khuôn (dấu hiệu AI)

- Đừng lặp mẫu "không phải X mà là Y".
- Tránh **bộ ba song song** (liệt kê 3 vế đối xứng cho sang).
- Không lạm dụng gạch ngang và câu đối xứng gương.
- Câu hỏi tu từ rồi tự trả lời: dùng được để dẫn dắt, nhưng đừng thành công thức lặp.

### Lượt 3 — thêm chất người nhưng giữ trung thực

- **Đổi độ dài câu** — xen câu ngắn đanh với câu dài. Nhịp đều tăm tắp = máy viết.
- Dùng khẩu ngữ tự nhiên: "cứ", "thì", "nhé", "đấy", "mà".
- Đưa nhận xét có căn cứ hoặc tình huống minh hoạ được. **Không bịa trải nghiệm cá nhân**
  kiểu "mình từng mắc lỗi này" chỉ để giọng văn có vẻ thật. Tình huống giả định phải nói rõ
  là minh hoạ.
- Cho phép vài ý mở, không cần chốt gọn mọi câu.

## Luật ngôn ngữ đi kèm

- Xưng "bạn", nhất quán, gần gũi, không trịnh trọng.
- Thuật ngữ khó và viết tắt có nghĩa tiếng Việt dễ hiểu ở **lần đầu của từng khối độc lập**
  (đoạn văn, bảng, sơ đồ, card, caption, quiz). Bảng thuật ngữ và tooltip không thay được việc này.
- Giải nghĩa theo mức người mới: trả lời "đây là gì / dùng để làm gì" bằng từ quen thuộc.
  Cấm định nghĩa vòng tròn: `runtime (môi trường runtime)` ❌ → `runtime (môi trường chạy chương trình)` ✅
- Tiếng Việt đứng trước trong tiêu đề và nhãn. Cấm nhãn nén kiểu `1 codebase 2 OS`, `Hire pool web`.
- Từ đánh giá phải có tiêu chí và hệ quả. `Có / Không / cao / thấp / nhanh / nặng` là chưa đủ.
- **Không chèn phần giải nghĩa vào định danh máy**: `id`, slug, URL, path, prop kỹ thuật, tên biến,
  tên component, nội dung code. Muốn diễn giải thì đặt ở `title`, caption hoặc câu văn bên ngoài.
- Nếu script humanize chạy tự động: phải bảo vệ rồi khôi phục nguyên vẹn frontmatter, code fence,
  inline code, prop JSX, URL và import. Không chứng minh được bước khôi phục an toàn thì bỏ qua
  khối kỹ thuật đó. Cấm để lọt placeholder nội bộ (`HOLD1`, ký tự NUL…) vào bài.

## Checklist văn phong

- [ ] Đọc TO lên — nghe có tự nhiên như người nói không?
- [ ] Có câu ngắn đanh xen giữa các câu dài không?
- [ ] Không có bộ-ba-song-song / mẫu lặp máy móc?
- [ ] Có ≥1 ví dụ đời thường + ≥1 nhận xét có căn cứ hoặc tình huống minh hoạ trung thực?
- [ ] Xưng "bạn" nhất quán?
- [ ] Không sáo rỗng ("vô cùng quan trọng", "một cách hiệu quả")?
- [ ] Thuật ngữ / viết tắt đã giải nghĩa trong từng khối độc lập?
- [ ] Quy trình / bảng việc đã thành sơ đồ khi phù hợp?
- [ ] Câu chuyện / ví dụ có thông điệp + bối cảnh + bước?
- [ ] Không có đoạn viết chỉ để đủ mục?
