# Kế hoạch đo pilot

## Mục tiêu

Pilot không nhằm chứng minh rộng rằng sản phẩm làm học sinh học tốt hơn. Nó chỉ
kiểm tra ban đầu ba giả thuyết:

1. Giáo viên hiểu, sửa và phê duyệt được package với ít gánh nặng hơn quy trình
   hiện tại.
2. Cổng nguồn/sư phạm phát hiện được lỗi đã cài và không tạo quá nhiều cảnh báo
   giả.
3. Bài dạy tạo ra bằng chứng học sinh đạt các mục tiêu đã đặt.

## Thiết kế tối thiểu

- Bài: Vật lí 10 — cơ năng và chuyển hóa năng lượng, 45 phút.
- Review trước lớp: hai giáo viên Vật lí chấm độc lập.
- Dạy thử: ít nhất hai lần ở hai lớp khác nhau sau khi package đạt
  `Peer-reviewed`.
- Ghi bối cảnh: trường/lớp ở mức không nhận dạng, sĩ số, kiến thức đã học, thời
  lượng thực, giáo viên, thiết bị, gián đoạn và phiên bản package.

Đây là quan sát thăm dò; không dùng để kết luận quan hệ nhân quả hoặc đại diện
cho giáo viên toàn quốc.

## Trước tiết học

Ba nhiệm vụ ngắn, tối đa 5 phút:

1. Dự đoán vị trí tốc độ lớn nhất trên đường trượt và giải thích.
2. Chọn/sửa phát biểu “ma sát làm năng lượng biến mất”.
3. Bài tính một bước từ `mgh` sang `1/2 mv²` nếu học sinh đã học công thức.

Giáo viên không chữa chi tiết trước hoạt động chính; chỉ dùng kết quả để biết lỗ
hổng tiên quyết.

## Sau tiết học

- Dùng exit ticket câu 1–3 trong package.
- Thêm một nhiệm vụ vận dụng khác bề mặt: vật rơi hoặc con lắc đơn giản, vẫn đo
  cùng nguyên lí.
- Lặp lại câu quan niệm sai bằng cách diễn đạt khác.
- Nếu có điều kiện, kiểm tra giữ lại sau 7–14 ngày bằng hai câu ngắn.

## Chuẩn chấm

Dùng định nghĩa “học sinh hoàn thành mục tiêu” trong
`acceptance-glossary.md`. Hai giáo viên chấm thử một mẫu nhỏ đã ẩn danh trước để
thống nhất cách áp rubric.

Không chỉ dùng tổng điểm. Báo cáo riêng theo từng mục tiêu:

- Giải thích chuyển hóa.
- Phân biệt cơ năng/tổng năng lượng.
- Vận dụng bài toán đơn giản.

## Đo gánh nặng giáo viên

- Thời gian đọc nguồn và package.
- Thời gian chỉnh sửa chủ động.
- Số vòng sửa có kiểm soát.
- Tỷ lệ block phải viết lại.
- Số cảnh báo đúng, sai và bị bỏ sót được reviewer phát hiện.
- Tác vụ nào cần hỗ trợ kỹ thuật.
- Artifact nào thực sự được dùng trong tiết học.

## Phản hồi sau dạy

Không chỉ hỏi “thầy/cô có thích không”. Phỏng vấn dựa trên hành vi:

- Phần nào giáo viên bỏ qua hoặc thay thế?
- Cảnh báo nào giúp quyết định và cảnh báo nào gây nhiễu?
- Khi học sinh không hiểu, giáo viên đã ứng biến thế nào?
- Phần nào vượt hoặc thiếu thời lượng?
- Giáo viên có tin các trích dẫn không, và đã mở kiểm tra phần nào?
- Có dùng lại package cho lớp sau không?

## Cổng quyết định sau pilot

Không mở rộng sang môn/cấp khác trước khi:

- Hai fixture nghiêm trọng đều bị chặn.
- Hai reviewer đạt đồng thuận sau khi tiêu chí được làm rõ.
- Giáo viên hoàn thành review mà không cần biết Git/YAML/JSON.
- Có dữ liệu thời gian và mức viết lại, không chỉ nhận xét cảm tính.
- Kết quả học sinh được báo theo từng mục tiêu và kèm bối cảnh.
- Không có sự cố dữ liệu, bản quyền hoặc thiết bị chưa có phương án xử lý.

