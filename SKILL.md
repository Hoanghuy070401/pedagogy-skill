---
name: soan-bai-hoc
description: Bộ quy tắc soạn bài học tiếng Việt (lesson authoring) trích từ SchoolAI Studio. Dùng khi soạn/sửa/review nội dung bài học, giáo trình, MDX bài giảng, quiz, deep-dive, hoặc khi cần checklist chất lượng sư phạm — giải nghĩa thuật ngữ, sơ đồ hoá quy trình, nhịp học hook→hiểu→thử→phản hồi→áp dụng, bằng chứng học (mục tiêu→dạy→luyện→đánh giá), văn phong người thật (humanize), quy tắc asset và khả năng tiếp cận.
---

# Soạn bài học — bộ quy tắc Studio

Gói này là bản mang đi được (portable) của bộ kỹ năng soạn bài trong SchoolAI Studio.
Mục tiêu: bài học cho người mới **đủ sâu, dễ hiểu, tự kiểm được**, không có giọng dịch máy
và không có mục trống nghĩa.

## Dùng khi nào

- Soạn mới hoặc viết lại một bài học / chương giáo trình.
- Review bản nháp bài học do người hoặc AI viết.
- Xây pipeline agent tự soạn bài (dùng `references/00-rule-set-agent.md` làm hợp đồng prompt).

## Quy trình 5 bước

1. **Chốt năng lực đầu ra** — 1–3 năng lực quan sát được cho mỗi bài. Viết ra trước khi viết chữ nào.
2. **Lập bản đồ**: mỗi năng lực → phần giảng → ví dụ/thực hành → câu hỏi hoặc challenge đánh giá.
   Mục tiêu không có đủ 3 nhánh này là mục tiêu "treo" — bỏ hoặc bổ sung.
3. **Viết theo nhịp**: hook thực tế → giải thích ngắn → dự đoán/tự kiểm → phản hồi → áp dụng →
   bẫy/ranh giới → nối sang bài sau. Không dồn toàn bộ tương tác xuống cuối bài.
4. **Soát 3 lượt văn phong** theo `references/03-van-phong-humanize.md` (bỏ chữ máy móc → phá cấu
   trúc rập khuôn → thêm chất người nhưng trung thực).
5. **Chạy checklist** `references/04-checklist-truoc-merge.md`. Còn một thuật ngữ chưa giải nghĩa,
   một nhãn tiếng Anh nén, hay một kết luận mơ hồ không hệ quả → **chưa được báo hoàn thành**.

## 8 luật không được vi phạm

| # | Luật | Vi phạm điển hình |
|---|---|---|
| 1 | Viết tắt / thuật ngữ chuyên ngành có nghĩa tiếng Việt ngay lần đầu, **trong từng khối đọc độc lập** (đoạn, bảng, sơ đồ, card, quiz) | `runtime (môi trường runtime)`, câu nén ≥3 jargon |
| 2 | Quy trình ≥3 bước hoặc cơ chế nhiều trạng thái → **sơ đồ**, không phải một đoạn văn | "một câu = cả pipeline" |
| 3 | Không card/mục trống nghĩa | Thẻ "Chuẩn ngành" + 2 câu chung chung, meta kể cấu trúc bài |
| 4 | Câu chuyện/ví dụ phải có **thông điệp + bối cảnh + các bước** | Kể đại 4–5 câu nén acronym |
| 5 | Đủ sâu: *là gì → vì sao → cơ chế → dùng khi nào → bẫy* cho mỗi khái niệm chính | Định nghĩa + vài bullet rồi hết |
| 6 | Trực quan, cụ thể: **đầu vào → biến đổi/trạng thái → đầu ra** | "hệ thống xử lý dữ liệu", "API kết nối các thành phần" |
| 7 | Nguồn bên thứ ba chỉ ở mục *Đọc thêm*; thân bài đứng độc lập | "theo roadmap…", "dựa trên tài liệu…", `Brief: research/...` |
| 8 | Không sửa **định danh máy** khi giải nghĩa/humanize | Nhét ngoặc vào `id`, slug, URL, prop, code |

## Tài liệu trong gói

| File | Dùng để |
|---|---|
| `references/00-rule-set-agent.md` | Hợp đồng ngắn nhét thẳng vào prompt agent soạn bài (schema JSON, evidencePlan, teachingPlan) |
| `references/01-huong-dan-soan-bai.md` | Bản đầy đủ: cấu trúc bài, component, sơ đồ, §5 văn phong, §6.1–6.10 luật chi tiết |
| `references/02-quy-tac-asset.md` | Minh hoạ sinh từ code trước; điều kiện dùng ảnh raster; cổng phát hành |
| `references/03-van-phong-humanize.md` | Quy trình 3 lượt + danh sách từ/cấu trúc cần tránh (tiếng Việt) |
| `references/04-checklist-truoc-merge.md` | Checklist chốt trước khi bàn giao |
| `assets/mau-bai-khai-niem.md` | Khung một bài khái niệm để copy |
| `assets/component-kit.md` | Bộ block trực quan cần có ở dự án đích + cách map sang stack khác |

Đọc `references/01` khi cần chi tiết một luật; SKILL.md này chỉ là bản tóm.

## Mang sang dự án khác

Các tài liệu gốc viết cho stack Docusaurus + MDX + Supabase của SchoolAI. Khi áp cho dự án khác,
phần **sư phạm và văn phong giữ nguyên**; chỉ thay lớp kỹ thuật:

- Lệnh `npm run lint:mdx`, `lint:lessons:strict`, `guard-svg` → thay bằng cổng lint tương đương;
  nếu chưa có, ít nhất phải có một bước kiểm cú pháp trước khi bàn giao.
- Component `FlowDiagram`, `GridCards`, `ComparisonPanel`, `LayerStack`, `ThresholdMeter`,
  `QuizBox`, `TerminalDemo`, `Figure` → xem `assets/component-kit.md` để biết mỗi block giải quyết
  nhu cầu trực quan nào, rồi map sang component/Mermaid của dự án đích.
- Phần Supabase/content release (§0.1) chỉ đúng với kiến trúc "MDX là nguồn Git, DB là bản phát
  hành". Dự án không có lớp này thì bỏ qua, nhưng giữ nguyên tắc: **một nguồn sự thật duy nhất,
  không sửa tay ở bản phát hành**.
- Attribution/giấy phép: giữ đúng một nơi canonical trong dự án, không rải vào từng bài.
