# 4. Báo cáo nguồn, chất lượng và cảnh báo

## Tóm tắt phát hành

**Kết luận hiện tại:** Chưa phát hành. Package đủ để thẩm định thủ công nhưng
chưa được hai giáo viên chấm độc lập và chưa thử trong lớp.

| Nhóm kiểm tra | Trạng thái |
|---|---|
| Kiến thức cốt lõi có nguồn | Đủ ở mức package thủ công |
| Mâu thuẫn/phạm vi nguồn | Có một khác biệt phạm vi đã giải thích |
| Câu hỏi ngoài nội dung dạy | Có một fixture; đã đánh dấu phải chặn |
| Claim sai nguồn có chủ đích | Có một fixture; đã đánh dấu nghiêm trọng |
| Bản quyền | Không đóng gói tài liệu Bộ; OpenStax CC BY 4.0; PhET cần tuân thủ giấy phép hiện hành |
| Giáo viên duyệt | Chưa |
| Thử trong lớp | Chưa |

## Danh mục nguồn

Các URL và điều kiện giấy phép dưới đây được kiểm tra ngày 2026-08-11. Trước
khi phát hành lại package, cần kiểm tra xem nguồn hoặc giấy phép đã thay đổi hay
chưa.

### S1 — Tài liệu Bộ Giáo dục và Đào tạo

- Tên: Tài liệu/kế hoạch môn Vật lí lớp 10 có nội dung Bài 17 “Động năng và thế
  năng. Định luật bảo toàn cơ năng”.
- Vai trò: nguồn bắt buộc về phạm vi chương trình và mức độ đánh giá.
- Vị trí dùng: mục “Động năng và thế năng”, gồm yêu cầu nêu công thức thế năng,
  khái niệm cơ năng, phát biểu định luật và vận dụng trong trường hợp đơn giản.
- Link: [PDF trên moet.gov.vn](https://moet.gov.vn/content/vanban/Lists/VBDH/Attachments/3491/6--mon-vat-ly--lop-10-ban-chinh-thuc-ngay-06-9-2023signed-2909869.pdf)
- Quyền sử dụng: chưa xác định giấy phép tái phân phối; package chỉ lưu link và
  metadata, không đóng gói lại PDF.
- Cảnh báo: cần giáo viên xác nhận tài liệu này phù hợp với kế hoạch đang áp dụng
  tại trường và không thay thế sách/khung phân phối hiện hành.

### S2 — OpenStax Physics, mục 9.2

- Tên: Mechanical Energy and Conservation of Energy.
- Vai trò: nguồn kiến thức chính cho định nghĩa, điều kiện không ma sát, chuyển
  hóa động năng–thế năng và bài toán đơn giản.
- Link: [OpenStax Physics 9.2](https://openstax.org/books/physics/pages/9-2-mechanical-energy-and-conservation-of-energy)
- Giấy phép: CC BY 4.0 theo [preface của sách](https://openstax.org/books/physics/pages/preface).
- Phạm vi: sách Vật lí phổ thông bằng tiếng Anh; nội dung đã được diễn đạt lại
  bằng tiếng Việt, không sao chép đoạn dài.

### S3 — OpenStax University Physics, mục 8.3

- Tên: Conservation of Energy.
- Vai trò: nguồn đối chiếu cho điều kiện lực không bảo toàn và cách phân biệt cơ
  năng với tổng năng lượng.
- Link: [OpenStax University Physics 8.3](https://openstax.org/books/university-physics-volume-1/pages/8-3-conservation-of-energy)
- Giấy phép: CC BY 4.0; cần giữ attribution khi tái sử dụng nội dung.
- Cảnh báo sư phạm: tài liệu ở mức đại học, chỉ dùng để kiểm tra tính chính xác;
  không đưa toàn bộ công thức tổng quát vào tiết lớp 10.

### S4 — PhET Energy Skate Park

- Tên: Energy Skate Park.
- Vai trò: nguồn hoạt động/minh họa cho biểu đồ động năng, thế năng, nhiệt năng
  và tác động của ma sát.
- Link: [PhET Energy Skate Park](https://phet.colorado.edu/en/simulations/energy-skate-park?locale=en)
- Giấy phép hiện hành: trang licensing tiếng Anh nêu Regular HTML Simulation
  Files theo CC BY-NC 4.0; cần attribution và không nhúng vào sản phẩm thương
  mại nếu chưa có giấy phép phù hợp. Xem [PhET Licensing](https://phet.colorado.edu/en/licensing).
- Cách dùng trong package: chỉ liên kết tới mô phỏng; chưa đóng gói file hoặc
  ảnh chụp.

## Bản đồ claim → bằng chứng

| ID | Claim | Nguồn/vị trí | Mức truy nguồn | Trạng thái |
|---|---|---|---|---|
| C1 | Cơ năng trong tình huống bài là tổng động năng và thế năng | S1 mục Động năng và thế năng; S2 §9.2 | Bắt buộc | Supported |
| C2 | Không ma sát/lực cản, cơ năng giữ nguyên giữa hai vị trí | S2 §9.2; S3 §8.3 | Bắt buộc | Supported |
| C3 | Có ma sát, cơ năng có thể chuyển thành nhiệt năng | S2 teacher support; S4 energy bars/friction | Bắt buộc | Supported |
| C4 | Tổng năng lượng không biến mất khi cơ năng giảm nếu xét đủ hệ | S2 §9.2; S3 §8.3 | Bắt buộc | Supported, cần giữ điều kiện hệ |
| C5 | `v = √(2gh)` khi vật thả nghỉ, bỏ qua ma sát và chọn mốc phù hợp | S2 tips/practice | Bắt buộc | Supported |
| C6 | PhET cho phép quan sát động năng, thế năng, nhiệt năng và tổng | S4 Intro/Measure/Graphs | Nên có | Supported |

## Khác biệt phạm vi cần giáo viên thấy

Hai câu dưới đây không thực sự mâu thuẫn nếu nêu đúng phạm vi:

- “Cơ năng được bảo toàn” áp dụng khi lực không bảo toàn không thực hiện công
  hoặc được bỏ qua trong mô hình.
- “Tổng năng lượng được bảo toàn” rộng hơn; khi có ma sát, cơ năng có thể giảm
  trong khi nhiệt năng tăng.

Nếu bài chỉ nói “năng lượng được bảo toàn” mà không xác định đang nói cơ năng
hay tổng năng lượng, đánh dấu `Cần sửa`.

## Fixture lỗi nguồn có chủ đích

### F1 — Claim sai phạm vi

> “OpenStax khẳng định cơ năng luôn được bảo toàn kể cả khi có ma sát.”

- Trạng thái: `CONTRADICTED — SEVERE`.
- Lý do: S2 và S3 đều đặt điều kiện; ma sát có thể làm cơ năng chuyển thành
  dạng năng lượng khác.
- Hành vi mong đợi: chặn phát hành và yêu cầu sửa thành claim C2/C3.

### F2 — Câu hỏi vượt ngoài nội dung dạy

Câu 8 về suy ra thế năng đàn hồi trong tài liệu kiểm tra.

- Trạng thái: `UNTaught — SEVERE`.
- Lý do: mục tiêu, phần giảng và luyện tập không dạy lực đàn hồi/định luật Hooke.
- Hành vi mong đợi: loại khỏi bản học sinh hoặc bổ sung một chuỗi dạy–luyện–đánh
  giá mới, nhưng không được tự mở rộng trong tiết 45 phút hiện tại.

## Cảnh báo cần xử lý trước khi giáo viên thử

1. Giáo viên Vật lí xác nhận mục tiêu và phạm vi phù hợp lớp 10 đang dạy.
2. Chạy thử đúng 45 phút; phần PhET có thể vượt thời lượng nếu thiết bị chậm.
3. Xác nhận học sinh đã học công thức động năng và thế năng.
4. Chuẩn bị phương án biểu đồ cột không mạng.
5. Kiểm tra bản dịch/thuật ngữ “cơ năng”, “nhiệt năng”, “hệ” không gây hiểu sai.
6. Xác nhận cách dùng PhET phù hợp giấy phép nếu sản phẩm sau này có thương mại.

## Checklist trước phát hành

- [ ] Hai giáo viên đã chấm rubric độc lập.
- [ ] Mọi bất đồng đã lưu lý do và quyết định sửa.
- [ ] F1 và F2 không xuất hiện trong bản học sinh.
- [ ] Link nguồn mở được và phiên bản/ngày kiểm tra đã được ghi.
- [ ] Không có dữ liệu học sinh hoặc secret trong package.
- [ ] Bài đã được thử thời lượng với thiết bị mục tiêu.
- [ ] Exit ticket có cùng chuẩn chấm cho tất cả học sinh.
