# Kế hoạch nghiên cứu vận hành local và cloud

Tài liệu này định nghĩa những gì phải đo trước khi công bố cấu hình tối thiểu,
chi phí hoặc khẳng định mô hình local đủ tốt cho giáo viên Việt Nam. Hiện chưa
có số benchmark nên không đưa ra con số giả định.

## Ma trận cấu hình cần thử

Tối thiểu ba nhóm máy thực tế:

1. Máy phổ thông không GPU rời.
2. Máy có RAM/GPU tầm trung.
3. Máy khuyến nghị cho mô hình local lớn hơn.

Với mỗi nhóm, ghi:

- Hệ điều hành, CPU, RAM, GPU/VRAM và dung lượng trống.
- Thời gian cài lần đầu.
- Dung lượng ứng dụng, model và cache.
- Thời gian khởi động và kiểm tra môi trường.
- Nhiệt độ/tải máy hoặc tình trạng treo nếu ảnh hưởng sử dụng.

## Tác vụ benchmark chung

Dùng cùng package Vật lí 10 và cùng đầu ra mong đợi để so sánh:

- Nhập một PDF văn bản, một PDF bản quét và một URL.
- Tìm bằng chứng cho 10 claim.
- Tạo dàn ý và ma trận sư phạm.
- Tạo một học liệu, 8 câu hỏi và rubric.
- Chạy kiểm định nguồn/sư phạm.
- Xuất DOCX, PPTX và PDF.

## Chỉ số local

- Thời gian xử lý mỗi nguồn và toàn bài.
- Giới hạn kích thước/số nguồn trước khi lỗi hoặc chậm không chấp nhận được.
- Chất lượng tiếng Việt theo cùng rubric.
- Tỷ lệ trích dẫn mở đúng vị trí.
- Tỷ lệ lỗi OCR.
- Dung lượng lưu trữ phát sinh.
- Tỷ lệ tác vụ hoàn thành không cần hỗ trợ.

## Chỉ số cloud

- Provider/model/version và khu vực xử lý nếu biết.
- Token/chi phí thực tế cho toàn workflow và từng bước.
- Độ trễ, lỗi mạng, retry và giới hạn tốc độ.
- Chất lượng tiếng Việt trên cùng benchmark.
- Dữ liệu thực tế rời máy sau redact.
- Chính sách retention của provider tại thời điểm thử.

## Trải nghiệm cài đặt và hỗ trợ

Prototype phải có:

- Bộ cài một lần, không yêu cầu giáo viên tự cài Python.
- Kiểm tra tự động RAM, dung lượng, model và kết nối.
- Thông báo lỗi bằng tiếng Việt kèm hành động tiếp theo.
- Cập nhật ứng dụng/model có rollback.
- Sao lưu, khôi phục và xóa dữ liệu từ giao diện.
- Gói chẩn đoán không chứa nội dung nguồn hoặc dữ liệu học sinh.

## Cách công bố kết quả

Chỉ gắn nhãn:

- `Tối thiểu`: hoàn thành được workflow nhưng có thể chậm.
- `Khuyến nghị`: hoàn thành trong ngưỡng thời gian được giáo viên thử nghiệm chấp
  nhận.
- `Không hỗ trợ`: thiếu tài nguyên hoặc có lỗi không khắc phục an toàn.

Mỗi nhãn phải kèm model, kích thước nguồn, phiên bản ứng dụng và ngày benchmark.
Không dùng một cấu hình duy nhất để đại diện mọi môn/tài liệu.

