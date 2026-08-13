# User UI Preferences

Agent phải đọc file này trước khi tạo hoặc sửa UI trong dự án. Chỉ ghi những lựa chọn đã được người
dùng yêu cầu hoặc xác nhận rõ; không lưu dữ liệu cá nhân, nội dung học liệu hay suy đoán về người dùng.

## Active preferences

### PREF-001 — Căn giữa badge số theo khối chữ

- Confirmed: 2026-08-12
- Scope: component — danh sách/card có badge số đứng cạnh văn bản nhiều dòng
- Status: active
- Rule: Căn giữa badge số theo chiều cao của khối chữ cùng hàng; giữ chính văn căn trái và dễ đọc.
- Evidence: Người dùng yêu cầu sửa badge số đang bám đầu dòng trong thẻ mục tiêu.
- Apply: Dùng Grid hai cột và `align-self: center` cho badge; số vẫn `place-items: center` trong hình tròn.
- Do not apply: Không căn giữa toàn bộ văn bản trong card; không áp cho stepper/timeline cần thể hiện điểm bắt đầu ở đầu đoạn.

## Superseded preferences

Chưa có.
