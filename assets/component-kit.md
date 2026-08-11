# Bộ block trực quan — nhu cầu và cách map sang stack khác

SchoolAI Studio dùng một bộ component MDX đăng ký toàn cục. Khi mang skill sang dự án khác,
điều cần giữ là **nhu cầu trực quan**, không phải tên component. Bảng dưới ghi nhu cầu → block gốc
→ phương án thay thế phổ biến.

| Nhu cầu trực quan | Block gốc (SchoolAI) | Thay thế ở dự án khác |
|---|---|---|
| Sơ đồ luồng bước → bước | `<FlowDiagram>` | Mermaid `flowchart`, hoặc component stepper |
| Chuỗi segment có nhãn (tên miền, semver, cú pháp) | `<FlowDiagram variant="pill">` | Chuỗi `<code>` có chú thích dưới, hoặc SVG đơn giản |
| So sánh 2–3 hộp cạnh nhau (trước/sau, A vs B) | `<ComparisonPanel>` | Grid 2–3 cột có tiêu đề + bullet |
| Lưới thẻ icon/tiêu đề/mô tả | `<GridCards>` | Card grid của design system sẵn có |
| Hộp lồng nhau (box model) / kim tự tháp phân tầng | `<LayerStack>` | SVG tay hoặc div lồng có nhãn |
| Ngưỡng đo lường theo mức / thang xếp hạng | `<ThresholdMeter>` | Bảng ngưỡng có nhãn mức + chữ mô tả |
| Cây phân cấp, sequence, ER, state, class | Mermaid code block | Mermaid (hầu hết stack docs đều hỗ trợ) |
| Sơ đồ tuỳ biến không khớp mẫu nào | `<Figure>` bọc SVG tay | Ngoại lệ có chủ đích; cần caption tự đủ nghĩa |
| Thực hành lệnh terminal | `<TerminalDemo>` | Code block + phần "kết quả mong đợi" viết rõ |
| Quiz có dữ liệu ngay trong bài | `<QuizBox>` | Component quiz của dự án, hoặc phần tự kiểm bằng chữ |

## Luật đi kèm (giữ nguyên ở mọi stack)

1. **Chỉ dùng component nằm trong allowlist của dự án.** Component lạ làm vỡ pipeline import/render.
   Nếu dự án có bước chuẩn hoá nội dung, mỗi component mới phải có policy tương ứng, kèm test chặn
   khi hai danh sách lệch nhau.
2. **Ưu tiên hình sinh từ code** (Mermaid, SVG có kiểm soát, component). Ảnh raster chỉ dùng khi
   người học cần thấy giao diện thật — chi tiết ở `../references/02-quy-tac-asset.md`.
3. **Trước khi tự vẽ SVG tay:** kiểm bảng trên; phần lớn hình lặp lại đã có block sẵn.
4. **Tông màu theo token dùng chung**, không tự chọn hex mới. Ở SchoolAI: `primary` (đúng/tiến bộ),
   `blue` (thông tin), `purple` (mốc/cấp độ), `gold` (thành tích/cảnh báo nhẹ), `coral` (sai/khẩn),
   `neutral`. Dự án khác map sang token semantic tương ứng.
5. **Mỗi hình có caption hoặc mô tả chữ tự đủ nghĩa**; ảnh thật có `alt`. Không truyền trạng thái
   chỉ bằng màu hoặc chuyển động.
