# Policy dữ liệu MVP

**Trạng thái:** Draft để chuyển thành checklist và test case; cần người phụ trách
pháp lý/quyền riêng tư của đơn vị triển khai duyệt trước pilot thật.

## Phân loại dữ liệu

| Loại | Ví dụ | Cloud mặc định |
|---|---|---|
| Công khai | Tài liệu mở, đường dẫn công khai | Được gửi sau màn hình xem trước |
| Nội bộ | Giáo án nội bộ, tài liệu tập huấn chưa công khai | Chỉ gửi khi người có quyền xác nhận |
| Dữ liệu học sinh | Tên, mã số, email, bài làm gắn danh tính, thông tin liên hệ | Cấm gửi dạng nhận dạng được |
| Nhạy cảm cao | Sức khỏe, khuyết tật, hoàn cảnh gia đình, kỷ luật | Cấm gửi trong MVP |
| Bí mật hệ thống | API key, token, mật khẩu, private key | Luôn cấm gửi/lưu trong package |

## Quy tắc gửi dữ liệu ra ngoài máy

1. Local là mặc định.
2. Trước mọi cloud request, hiển thị provider, model, đoạn dữ liệu cụ thể và lý
   do cần gửi.
3. Người đang thao tác phải xác nhận; tài liệu nội bộ cần thêm xác nhận họ có
   quyền sử dụng.
4. Dữ liệu học sinh chỉ được gửi sau khi ẩn danh và không còn khả năng liên kết
   ngược hợp lý; dữ liệu nhạy cảm cao không được gửi trong MVP.
5. Nếu bộ phát hiện dữ liệu cá nhân không chắc chắn, chặn gửi và yêu cầu người
   dùng kiểm tra.

## Lưu trữ và xóa

- File dự án: giữ đến khi người dùng xóa; hiển thị rõ vị trí lưu.
- File tạm chứa nội dung: xóa khi tác vụ kết thúc hoặc tối đa 24 giờ sau lỗi.
- Cache nguồn local: mặc định 30 ngày, cho phép xóa ngay.
- Log: chỉ lưu metadata vận hành; không lưu toàn văn nguồn, prompt, bài học hoặc
  dữ liệu học sinh.
- Outbound preview/audit: lưu provider, thời điểm, loại dữ liệu và quyết định;
  không lưu lại phần nội dung nhạy cảm đã gửi.
- Xóa dự án phải có tùy chọn xóa cả cache, embedding, file tạm và bản export.

## Máy dùng chung

- Mỗi người dùng có thư mục/profile tách biệt.
- Không hiển thị dự án gần đây của người khác khi chưa đăng nhập profile.
- Có nút khóa phiên và xóa dữ liệu tạm khi kết thúc.
- Không tự lưu API key trong file dự án.

## Package chia sẻ

Trước khi export/share, quét:

- Tên, mã số, email, số điện thoại và địa chỉ.
- API key, token, mật khẩu và private key.
- Đường dẫn local có tên tài khoản.
- Log, cache và lịch sử outbound.
- Tài liệu nguồn không có quyền tái phân phối.

Nếu phát hiện, chặn share và hiển thị đúng file/vị trí cần xử lý.

## Test case bắt buộc

1. PDF có tên và mã số học sinh → cloud request bị chặn.
2. Bài làm đã thay tên bằng mã ngẫu nhiên nhưng còn email trong footer → vẫn bị
   chặn.
3. `.env` hoặc chuỗi giống API key trong thư mục → không xuất vào package.
4. Màn hình outbound hiển thị đúng provider và chính xác đoạn sắp gửi.
5. Người dùng hủy ở màn hình outbound → không có network request.
6. Xóa dự án → cache, embedding và file tạm liên quan bị xóa.
7. Hai profile trên máy chung → profile A không thấy dự án của B.
8. Nguồn không rõ giấy phép → bản chia sẻ chỉ có metadata/link, không có file
   nguồn.
9. Log sau lỗi provider → không chứa nội dung tài liệu hoặc dữ liệu học sinh.
10. Package pilot → quét tự động không tìm thấy PII/secret.

