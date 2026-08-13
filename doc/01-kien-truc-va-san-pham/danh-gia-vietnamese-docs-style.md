# Đánh giá `vietnamese-docs-style`

Nguồn: <https://github.com/bGiaHuy/vietnamese-docs-style.git>  
Ngày review: 12/08/2026

## Kết luận

Repository hữu ích nhất ở quy trình định tuyến profile tài liệu, xử lý dữ liệu thiếu, biên tập tiếng
Việt theo ngữ cảnh và kiểm tra DOCX có render. Không nên cài nguyên khối vào lõi soạn bài vì trọng tâm
của nó là DOCX hành chính, báo cáo, đề xuất và biên bản; nhiều quy tắc Nghị định 30 không phù hợp với
học liệu HTML hoặc tài liệu học sinh.

## Phần nên tiếp nhận

- Chọn profile trước khi viết và chỉ nạp reference liên quan.
- Không tự bịa tên cơ quan, số văn bản, căn cứ, người ký, số liệu hoặc nguồn.
- Dùng placeholder có nhãn khi người dùng cho phép tạo bản nháp.
- Phân biệt dữ kiện, nhận định và kiến nghị.
- Kiểm tra cả cấu trúc tài liệu lẫn kết quả render.
- Sửa bị động dư thừa, từ nối lặp, filler, tàn dư chatbot và tiêu đề Title Case.

## Phần chỉ dùng theo điều kiện

- Thể thức Nghị định 30 chỉ dành cho văn bản hành chính hoặc yêu cầu rõ ràng.
- Times New Roman, A4, lề và căn đều hai bên là thông số theo profile, không phải chuẩn chung cho mọi
  tài liệu tiếng Việt.
- Emoji, gạch ngang dài và in đậm cần kiểm soát theo register; không cấm tuyệt đối trong học liệu.
- Các ngưỡng như số dòng của câu hoặc số lần dùng từ nối chỉ là tín hiệu để review.

## Phần không tiếp nhận

- Không lấy việc “thiếu số liệu cụ thể” làm lý do để AI tự thêm số, tên riêng hoặc nguồn.
- Không thay một attribution mơ hồ bằng một báo cáo cụ thể nếu nguồn đó chưa được cung cấp hoặc xác
  minh.
- Không dùng danh sách từ khóa như bộ lọc thay từ tự động.
- Không gọi output “chuẩn NĐ30” nếu chỉ áp dụng một phần hình thức.

## Cách tích hợp

Đã thêm `pedagogy-skill/references/13-bien-tap-tieng-viet-theo-profile.md` làm lớp tùy chọn cho tài
liệu kỹ thuật, báo cáo và văn bản trang trọng. Lớp này đứng sau source lock, artifact profile và Style
Control Matrix; mọi lượt biên tập vẫn phải vượt semantic-preservation gate.
