# Tích hợp Hallmark cho học liệu HTML

Áp dụng khi tạo mới, thiết kế lại hoặc audit một trang HTML học liệu. Hallmark chống giao diện rập
khuôn và tạo art direction; quy chuẩn học liệu trong `10-quy-chuan-ui-hoc-lieu.md` vẫn là cổng quyết
định cuối cùng.

## 1. Phân quyền giữa hai lớp

| Lớp | Quyết định |
|---|---|
| Sư phạm | nguồn, mạch bài, mục tiêu, hoạt động học, citation và mức độ chắc chắn |
| Learning UI | khả năng đọc, responsive, a11y, trạng thái, lịch sử preference và motion budget |
| Hallmark | genre, macrostructure, nhịp thị giác, font pairing, palette, nav/footer và anti-slop |

Khi xung đột, ưu tiên: yêu cầu hiện tại → nguồn/sư phạm → accessibility → preference đã xác nhận →
Learning UI → Hallmark. Không dùng Hallmark để biến bài học thành landing page quảng cáo.

## 2. Quy trình bắt buộc

1. Đọc `design-system/learning-ui/USER-PREFERENCES.md` và page profile hiện có.
2. Nếu skill `hallmark` khả dụng, đọc toàn bộ `SKILL.md`; nạp đúng genre, một macrostructure đã chọn,
   component nav/footer đã chọn và các reference bắt buộc của skill.
3. Ghi hợp đồng ngắn trước khi code: genre, macrostructure, theme hoặc studied DNA, enrichment,
   archetype nav/footer, `variance · motion · density`, câu hỏi xuyên bài và người đọc chính.
4. Tạo hoặc cập nhật `design-system/learning-ui/pages/<slug>.md`. Chỉ ghi lựa chọn và khác biệt của
   trang, không chép lại toàn bộ Master hay Hallmark.
5. Đặt Hallmark stamp ở dòng đầu CSS. Đặt pre-emit critique stamp trong artifact.
6. Khóa màu, font, spacing, radius, shadow, duration và easing trong token; component chỉ dùng token.
7. Tạo nội dung semantic trước, sau đó mới art-direct. Không để grid/card quyết định mạch bài.
8. Chạy kiểm tra Learning UI và Hallmark slop test ở cuối. Sửa mọi lỗi trước khi bàn giao.
9. Ghi một mục vào `.hallmark/log.json` để tránh lặp macrostructure ở trang tiếp theo.

## 3. Chọn cấu trúc cho học liệu

Không mặc định Hero → ba card → CTA. Chọn theo công việc đọc:

- **Long Document**: bài nhập môn, bài giải thích chuyên sâu, hồ sơ khái niệm; một tuyến đọc chính.
- **Workbench**: công cụ giáo viên, tạo/sửa/đối chiếu tài liệu; nhiều trạng thái và control.
- **Index hoặc reference**: thư viện nguồn, glossary, danh mục bài; ưu tiên tra cứu.
- **Comparison**: đặt hai mô hình, phương án hoặc hiện tượng cạnh nhau; chỉ dùng khi so sánh là nhiệm
  vụ học thật.

Với bài đọc dài, không có load animation hay scroll reveal. Hero phải vừa màn hình laptop chuẩn và
đưa người đọc vào câu hỏi, không đóng vai trò quảng cáo.

## 4. Quy tắc chống “AI slop” quan trọng cho học liệu

- Không dùng gradient chữ, blob trang trí, emoji làm icon hoặc ba card bằng nhau chỉ để lấp chỗ.
- Không dùng cùng một eyebrow cho mọi section nếu số chương không hỗ trợ điều hướng học tập.
- Không bịa metric, lời chứng thực, logo đối tác hoặc ví dụ để làm đầy bố cục.
- Không dựng giả browser/điện thoại/IDE; khi cần giao diện thật, dùng screenshot có nguồn.
- Không dùng quá ba họ font; mono chỉ giữ một vai trò rõ như code.
- Không có màu/font tự phát ngoài token; không dùng `transition: all`.
- `html, body` dùng `overflow-x: clip`; heading dài có `overflow-wrap: anywhere`.
- Link/nút không xuống hai dòng; vùng chạm tối thiểu 44px; focus xuất hiện tức thì.
- Phần tối phải đặt màu chữ sáng trong cùng rule và kiểm tra tương phản.
- Mọi hình trang trí có `aria-hidden="true"`; hình mang nghĩa có tên truy cập hoặc chú thích chữ.

## 5. Pre-emit critique và bàn giao

Chấm 1–5 cho sáu trục Hallmark:

`P` philosophy · `H` hierarchy · `E` execution · `S` specificity · `R` restraint · `V` variety.

Bất kỳ trục nào dưới 3 phải sửa trước slop test. Sau đó chạy thêm phiếu Learning UI:

`hierarchy · alignment · responsive · states · motion · a11y`.

Không tuyên bố đã render nếu chỉ kiểm tra mã tĩnh. Nếu môi trường không có trình duyệt khả dụng, ghi
rõ phần render còn mở; không tự đánh dấu các cổng viewport hoặc visual contrast là pass.
