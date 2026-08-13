# Page profile — Giới thiệu Android

- Artifact: `doc/gioi-thieu-android.html`
- Updated: 2026-08-12
- Primary reader: người mới bắt đầu tìm hiểu phát triển Android
- Primary job: hiểu quan hệ giữa nền tảng, công cụ build và cấu trúc ứng dụng trước khi làm codelab
- Central question: từ vài dòng Kotlin, bằng cách nào Android tạo ra một ứng dụng có thể cài đặt,
  khởi chạy và tiếp tục hoạt động đúng khi thiết bị thay đổi?

## Hallmark contract

- Genre: editorial / technical learning document
- Macrostructure: Long Document
- Theme: Almanac, giấy ấm + mực xanh đậm + Android green dùng làm điểm nhấn
- Enrichment: none; nội dung và sơ đồ CSS là trọng tâm
- Navigation: N9 Edge-aligned minimal
- Footer: Ft4 Dense typographic
- Knobs: `variance 2 · motion 1 · density 3`
- Typography: Newsreader / IBM Plex Sans / JetBrains Mono; mono chỉ dành cho wordmark và code

## Style Control Matrix

- Audience: người mới, chưa có mô hình tinh thần hoàn chỉnh về nền tảng Android.
- Purpose: giải thích quan hệ giữa hệ điều hành, cấu trúc ứng dụng và công cụ phát triển trước khi
  người đọc làm ứng dụng đầu tiên.
- Structure: bài học nhập môn — một lần chạm → hai hành trình build-time/runtime → các lớp nền tảng
  → cấu trúc ứng dụng → trạng thái và kiến trúc → thực hành → bẫy → tự kiểm → nguồn. Không dùng
  template đặc tả kỹ thuật.
- Technical baseline: thuật ngữ Android nhất quán; claim có citation chính thức; APK/AAB được phân
  biệt; sơ đồ giản lược phải ghi rõ phạm vi.
- User style layer: chưa kích hoạt vì chưa có 3–5 mẫu viết do người dùng cung cấp. Chỉ áp dụng các
  preference UI đã xác nhận trong `USER-PREFERENCES.md`.
- Negative constraints: tránh lời dẫn “chúng ta sẽ”, câu hỏi tu từ liên tiếp, giọng quảng bá và các
  cụm khẳng định tầm quan trọng không có căn cứ.
- Vietnamese editorial profile: `technical-explainer`; tiêu đề dùng sentence case tiếng Việt, dữ
  kiện tách khỏi diễn giải, attribution phải trỏ đến nguồn cụ thể. Không thêm số liệu/tên riêng chỉ
  để câu có vẻ thuyết phục hơn.

## Page-specific decisions

- Dùng hai tuyến song song: hành trình build trước khi cài và hành trình runtime sau khi mở. Các lớp
  nền tảng được giải thích bằng một yêu cầu camera đi từ ứng dụng xuống phần cứng.
- Giữ một cột đọc chính khoảng `65ch`; sơ đồ có thể rộng hơn nhưng không full-bleed.
- Danh sách mục tiêu dùng badge số căn giữa theo khối chữ, theo `PREF-001`.
- Không dùng animation khi tải hoặc cuộn. Chỉ có hover dịch chuyển nhẹ trên thiết bị có con trỏ mịn;
  `prefers-reduced-motion` tắt chuyển động.
- Citation đặt sát claim và liên kết tới danh mục nguồn chính thức cuối bài.

## Verification state

- Static: một `h1`; ID không trùng; fragment không gãy; link mở tab mới có `rel`; có reduced motion.
- Render: Quick Look desktop 1440px đã kiểm tra phần đầu trang, không thấy tràn hoặc lệch baseline.
  Quick Look cỡ nhỏ chỉ thu tỉ lệ canvas desktop, không mô phỏng viewport responsive; `320`, `375`,
  `414`, `768` và zoom 200% vẫn phải kiểm tra bằng trình duyệt trước khi coi visual QA hoàn tất.
- Hallmark pre-emit critique hiện tại: `P5 H5 E4 S5 R5 V4`.
- Semantic gate: PASS cho inventory nguồn `[1]–[8]`, phân biệt APK/AAB, bốn component, năm lớp nền
  tảng, Compose khai báo và mô hình kiến trúc UI/data/domain.
