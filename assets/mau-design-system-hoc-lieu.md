# Learning UI — Master Design System

> Copy thành `design-system/learning-ui/MASTER.md`. Điền quyết định cụ thể; không để các lựa chọn
> đối nghịch cùng tồn tại. Trang riêng chỉ ghi override trong `pages/<page>.md`. Lịch sử sở thích
> được giữ riêng trong `USER-PREFERENCES.md`, không trộn vào quyết định thiết kế gốc.

## 1. Bối cảnh

- Sản phẩm:
- Artifact/màn hình:
- Người dùng chính:
- Bối cảnh dùng: soạn / trình chiếu / tự học / in / mobile:
- Công việc chính:
- Stack đã phát hiện:
- Ràng buộc nguồn và nội dung:

## 2. Design dials

- Variance (1–5):
- Motion (1–5):
- Density (1–5):
- Lý do:

Gợi ý: bài học đọc dài `2 / 1 / 3`; công cụ soạn của giáo viên `2 / 2 / 4`; hoạt động tương tác
cho học sinh chỉ tăng motion khi hiệu ứng truyền đạt trạng thái hoặc quan hệ nhân quả.

## 3. Cấu trúc và trục căn

- Mẫu bố cục:
- Thứ tự nội dung trên mobile:
- Cạnh căn chủ đạo:
- Content width / reading measure:
- Breakpoint theo điểm vỡ nội dung:
- Sticky/fixed và khoảng bù:

## 4. Token

### Màu ngữ nghĩa

- `surface`, `surface-raised`, `text`, `text-muted`, `primary`, `on-primary`, `accent`,
  `on-accent`, `border`, `focus`, `error`, `success`:
- Các cặp tương phản đã kiểm tra:

### Typography

- Display / body / mono:
- Type scale:
- Body size / line-height / measure:
- Fallback và chiến lược tải font:

### Spacing và hình học

- 4/8pt scale:
- Radius scale:
- Elevation scale:
- Z-index scale:
- Touch target:

### Motion

- Duration tokens:
- Easing tokens:
- Số primitive tối đa:
- Reduced-motion behavior:

## 5. Component contracts

Với mỗi component, ghi: mục đích → nội dung → layout → default/hover/focus/active/disabled/
loading/error/success → mobile → reduced motion.

- Navigation:
- Objective/list card:
- Source/citation block:
- Quiz/form:
- Feedback/status:
- Dialog/popover:
- Table/chart:

## 6. Anti-pattern riêng của dự án

- Không ép chiều cao thẻ văn bản bằng số ngẫu nhiên.
- Không đặt badge/icon tuyệt đối để căn với prose.
- Không dùng animation tải/cuộn cho bài đọc dài.
- Không dùng màu hoặc hiệu ứng để thay cho provenance và mức độ chắc chắn.
- Không áp gamification/claymorphism mặc định cho mọi đối tượng giáo dục.
- Bổ sung:

## 7. Cổng bàn giao

- Viewport: 320 / 375 / 414 / 768 / 1024 / 1440px.
- Zoom/text scale 200%, landscape, bàn phím, screen reader smoke test.
- Reduced motion, mạng chậm, lỗi ảnh/font/JavaScript.
- Không horizontal scroll, overlap, clipping, CLS hoặc control bị che.
- `UI-QA · hierarchy _/5 · alignment _/5 · responsive _/5 · states _/5 · motion _/5 · a11y _/5`.

## Page override template

```md
# Page override — <page-name>

- Lý do cần khác Master:
- Token override:
- Layout override:
- Component/state override:
- Motion override và reduced-motion:
- Viewport đã render:
```

## User preference memory template

```md
# User UI Preferences

Agent phải đọc file này trước khi tạo/sửa UI. Chỉ cập nhật từ yêu cầu hoặc xác nhận rõ của người
dùng. Không lưu dữ liệu cá nhân hay nội dung học liệu.

## Active preferences

### PREF-001 — <tên ngắn>

- Confirmed: YYYY-MM-DD
- Scope: component / page / artifact / project
- Status: active
- Rule: <mệnh lệnh ngắn, kiểm tra được>
- Evidence: <mô tả yêu cầu sửa, không cần chép nguyên văn>
- Apply: <ví dụ nên làm>
- Do not apply: <ngoại lệ hoặc phạm vi không áp dụng>

## Superseded preferences

Giữ mục cũ tại đây cùng liên kết tới preference thay thế để còn lịch sử quyết định.
```
