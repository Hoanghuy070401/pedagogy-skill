# Page profile — Android trong mười phút (bản ngắn)

- Artifact: `doc/android-ban-do-10-phut.html`
- Updated: 2026-08-12
- Primary reader: cùng người đọc với bản dài, nhưng ở lần tiếp xúc đầu tiên hoặc khi cần ôn lại nhanh
- Primary job: định vị — biết thứ gì nằm ở đâu và tên gọi đúng của nó, trước khi đọc bản dài
- Central question: hai câu hỏi “Android chạy thế nào” và “mình tạo ứng dụng thế nào” gặp nhau ở đâu?

## Quan hệ với bản dài

Đây là bản đối chiếu có chủ đích của `doc/gioi-thieu-android.html`. Cùng chủ đề, cùng hệ nguồn, cùng
theme; khác ở cấu trúc và độ dài. 953 từ so với 2 399 từ (40 %).

Biến số được giữ cố định để so sánh có nghĩa: theme Almanac, `tokens.css`, bộ ba typeface.
Biến số được thay đổi: macrostructure (Long Document → Map / Diagram), nav (N9 → N6), footer
(Ft4 → Ft2), số lượng eyebrow (9 → 0), kỷ luật trích nguồn.

## Hallmark contract

- Genre: editorial
- Macrostructure: Map / Diagram
- Theme: Almanac — **cố ý không xoay theme**, phá luật theme-diversification vì mục đích của trang là
  đối chiếu; nếu đổi màu thì không tách được khác biệt cấu trúc khỏi khác biệt thị giác
- Enrichment: none — bản đồ dựng bằng CSS grid và hairline, không ảnh, không SVG sinh sẵn
- Navigation: N6 Newspaper masthead
- Footer: Ft2 Inline single line
- Knobs: `variance 2 · motion 1 · density 2`
- Pre-emit critique: `P5 H5 E5 S5 R5 V4` (V4 vì theme trùng bản trước, đã ghi lý do)

## Page-specific decisions

- Trục nền tảng dựng bằng `flex-direction: column-reverse`: thứ tự DOM đi từ nhân Linux lên ứng dụng
  (đúng thứ tự khái niệm), thứ tự hiển thị có đáy nằm dưới cùng (đúng cách hình gốc được vẽ). Bản dài
  liệt kê từ trên xuống rồi ghi chú “đọc từ dưới lên” — bản này bỏ được ghi chú đó.
- Zero eyebrow. Bản dài dùng 9 nhãn `01 · …`; quy tắc Hallmark giới hạn 1–2 mỗi trang.
- Điểm gặp của hai trục là khối duy nhất đảo màu, dùng làm tiêu điểm thị giác thay cho một hero.
- Bỏ hẳn phần tự kiểm tra và bảng thuật ngữ của bản dài; ba mục “dễ nhầm” gánh vai trò đó ở dạng ngắn.

## Kỷ luật trích nguồn (khác bản dài)

- Deep link tới heading, không chỉ tới trang: `fundamentals#Components`.
- Mỗi nguồn có ngày truy cập riêng (`<time datetime>`), không chỉ một dòng ngày cho cả bài.
- Mỗi nguồn ghi rõ nó chống lưng cho claim nào.
- Có nguồn ngoài Google Developers: AOSP `source.android.com` và tài liệu Kotlin của JetBrains.
- Trang App quality được dẫn kèm cảnh báo rằng đó là hướng dẫn gắn với Google Play, không phải chuẩn
  kỹ thuật trung lập.
- Toàn bộ liên kết trỏ bản tiếng Anh; bản dài trộn một liên kết `?hl=vi` với bảy liên kết tiếng Anh.

## Verification state

- Static: một `h1`; 8 id không trùng; không fragment gãy; mọi link ngoài có `rel="noreferrer"`; không
  có màu/font nào nằm ngoài token; có `prefers-reduced-motion`.
- Nguồn: 8/8 URL trả HTTP 200 vào 2026-08-12; anchor `#Components` đã kiểm tồn tại.
- Render: chưa xác nhận trên sáu viewport. Cần kiểm 320 / 375 / 414 / 768 px trước khi coi visual QA
  hoàn tất — cùng trạng thái với bản dài.
