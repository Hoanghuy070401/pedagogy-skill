# Theo dõi xử lý review vòng 2

**Ngày cập nhật:** 2026-08-11  
**Nguồn review:** `review-notes-for-agent.md`, mục 8

## Trạng thái từng nhận xét

| Mục | Quyết định/thay đổi | Trạng thái còn lại |
|---|---|---|
| 8.2 Trạng thái repo | Bảng đầu `../01-kien-truc-va-san-pham/plan-ecosystem-scaffold.md` đã phản ánh working tree hiện tại; baseline repo rỗng chuyển thành lịch sử | Đã xử lý ở tài liệu |
| 8.3 Vai trò tra cứu | Chọn phương án A: tra cứu/trích dẫn là thao tác hỗ trợ khi soạn bài, không là sản phẩm độc lập trong MVP | Đã chốt |
| 8.4 Package thủ công | Chọn Vật lí 10, một tiết về cơ năng; tạo package v0.1 với 4 nhóm đầu ra, 4 nguồn và 2 fixture lỗi; đã có vòng rà soát bằng hai persona AI và biên bản kiểm tra phương pháp | Có backlog v0.2; vẫn chờ hai giáo viên thật thẩm định mù |
| 8.5 Rule sư phạm | Tạo `../02-pilot/pilot-vat-li-10-co-nang-v0.1/05-quy-tac-su-pham-pilot.md` với 12 quy tắc, ví dụ đạt/chưa đạt/cách sửa | Chờ đo đồng thuận reviewer |
| 8.6 Thứ tự ưu tiên | Đổi thành ba luồng: kiểm chứng sản phẩm, kỹ thuật MVP, mở rộng | Đã xử lý ở plan |
| 8.7 Thuật ngữ nghiệm thu | Tạo `../02-pilot/acceptance-glossary.md`, định nghĩa cách đo, người xác nhận và bằng chứng | Cần kiểm tra qua review thật |
| 8.8 Local/cloud | Tạo `../02-pilot/local-cloud-operations-research.md` với ma trận cấu hình và benchmark chung | Chưa chạy benchmark |
| 8.9 Policy dữ liệu | Tạo `../02-pilot/data-policy-mvp.md` với phân loại, retention và 10 test case | Chưa triển khai/chạy test |
| 8.10 Hiệu quả học tập | Tạo `../02-pilot/pilot-measurement-plan.md` với pre/post, nhiệm vụ vận dụng và ngưỡng theo mục tiêu | Chưa dạy pilot |
| 8.11 Đối tượng/liên kết | `../01-kien-truc-va-san-pham/startdoc.md` ghi rõ đối tượng kỹ thuật và link tài liệu giáo viên; tài liệu giáo viên link package mẫu | Đã xử lý |

## Cổng review hiện tại

Review vòng 2 **chưa đóng**. Tài liệu và mẫu thủ công đã sẵn sàng cho bước kiểm
chứng, nhưng còn các bằng chứng bên ngoài chưa thể tự tạo:

Vòng hai giáo viên mô phỏng trong package chỉ là rà soát nội bộ. Do reviewer đã
thấy nhãn và đáp án của hai fixture, vòng này không chứng minh khả năng phát hiện
lỗi độc lập và không thay đổi các cổng bằng chứng dưới đây.

1. Hai giáo viên Vật lí THPT chấm package độc lập.
2. Ghi và xử lý bất đồng rubric.
3. Chạy prototype review với 3–5 giáo viên.
4. Triển khai test case dữ liệu và nguồn.
5. Benchmark local/cloud trên máy thật.
6. Chỉ sau khi package được duyệt mới tiến hành hai lần dạy pilot và đo kết quả.

Cho đến khi hoàn thành các bước trên, trạng thái dự án vẫn là
`Product exploration`, không chuyển sang `MVP implementation` hoặc
`Classroom-tested`.

## Quyết định tạm hoãn thẩm định

Từ 2026-08-11, bước mời giáo viên thật và dạy pilot được chuyển sang
`parked — external validation unavailable`. Đây không còn là blocker của việc
xây công cụ. Nhóm tiếp tục Milestone 1–3 trong
`../01-kien-truc-va-san-pham/plan-xay-dung-he-sinh-thai.md`, dùng package hiện có
như fixture kỹ thuật và giữ nguyên giới hạn: chưa gắn nhãn `Teacher-reviewed`,
`Peer-reviewed` hoặc `Classroom-tested`.
