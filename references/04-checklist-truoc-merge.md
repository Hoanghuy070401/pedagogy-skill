# Checklist trước khi bàn giao / merge

Trích §6.10 của `01-huong-dan-soan-bai.md`, đã gỡ lệnh riêng của SchoolAI (thay bằng mô tả cổng
tương đương để dùng ở dự án khác).

## Thuật ngữ và nhãn

- [ ] Rà viết tắt (PR, CI, CD, CVE, K8s, VM, IaC, SLI, SLO, SRE, IAM, DORA, OWASP…): mỗi cái đã có
      nghĩa ở lần đầu?
- [ ] Mọi thuật ngữ khó với người mới đã có nghĩa tiếng Việt dễ hiểu ngay trong ngoặc?
- [ ] Phần giải nghĩa nói được "là gì / dùng làm gì", không định nghĩa vòng tròn bằng jargon khác?
- [ ] Đã rà riêng **từng** bảng, sơ đồ, card, callout, caption và quiz như một khối độc lập?
- [ ] Tiêu đề/nhãn dùng tiếng Việt trước; không còn nhãn Anh–Việt nén kiểu ghi chú nội bộ?
- [ ] Không còn `Có / Không / Cao / Thấp / Không chuẩn` mà thiếu tiêu chí hoặc hệ quả cụ thể?

## Trình bày

- [ ] Không còn đoạn "một câu = cả pipeline"; mọi quy trình ≥3 bước đã thành sơ đồ?
- [ ] Bảng ≥4 cột hoặc bảng dày jargon đã tách thành khối dễ đọc?
- [ ] Không có mục/card meta hoặc "trống nghĩa"?
- [ ] Mọi câu chuyện/ví dụ có thông điệp + bối cảnh + bước, ưu tiên sơ đồ?
- [ ] Học viên đọc to được luồng mà **không** cần tra Google viết tắt?

## Độ sâu

- [ ] Mọi mục tiêu đầu bài đều được dạy đủ trong thân bài?
- [ ] Mỗi khái niệm chính có cơ chế, ví dụ áp dụng và bẫy/ranh giới?
- [ ] Cơ chế/luồng/trạng thái đã có mô tả trực quan: đầu vào → biến đổi → đầu ra?
- [ ] Không còn câu trừu tượng kiểu "xử lý", "tối ưu", "quản lý", "kết nối" mà thiếu chủ thể và
      kết quả cụ thể?
- [ ] Không có placeholder, định nghĩa lướt hoặc đoạn viết chỉ để bài trông dài?
- [ ] Người học kết thúc bài có thể giải thích lại và làm được một việc cụ thể?

## Nhịp học và tương tác

- [ ] Mở bài có tình huống/vấn đề thực tế, nêu rõ năng lực đầu ra, không bắt đầu bằng định nghĩa khô?
- [ ] Mỗi phần chỉ trả lời một câu hỏi học tập chính; phần đào sâu đã tách khỏi phần cần biết ngay?
- [ ] Mỗi ý lớn có điểm dự đoán, tự kiểm hoặc áp dụng trong thân bài; không dồn hết tương tác xuống cuối?
- [ ] Mọi thao tác/bài tập nêu đủ: việc cần làm, kết quả mong đợi, cách tự kiểm, gợi ý khi sai?
- [ ] Mỗi hình/sơ đồ trả lời một câu hỏi học tập cụ thể, caption tự đủ nghĩa, không chỉ truyền ý
      bằng màu sắc/vị trí?
- [ ] Kết bài chốt năng lực, một bẫy và mối nối tự nhiên tới bài sau?
- [ ] Không có trải nghiệm cá nhân bị bịa; tình huống giả định đã nói rõ là minh hoạ?

## Bằng chứng học

- [ ] Mỗi năng lực đầu ra map đủ tới phần giảng, ví dụ/thực hành và quiz/challenge tương ứng
      (nếu không tạo được tương tác thì có tự kiểm bằng chữ và ghi rõ lý do)?
- [ ] Bài có 1–3 năng lực chính; nếu phần core vượt nhịp 10–20 phút thì đã tách bài mà không mất
      phạm vi lộ trình?
- [ ] Kiến thức, công cụ, tài khoản và quyền truy cập tiên quyết đã được nêu trước khi thao tác?
- [ ] Quiz chỉ hỏi nội dung đã dạy; giải thích lý do đúng và hiểu lầm sau các lựa chọn sai đáng chú ý?
- [ ] Challenge có đầu vào, kết quả cần tạo, tiêu chí pass, cách tự kiểm và map đúng năng lực?

## Kiểm chứng kỹ thuật

- [ ] Code/lệnh/truy vấn/cấu hình và output mẫu đã chạy thử khi có thể; phần không chạy được đã ghi
      rõ giới hạn và căn cứ kiểm chứng?
- [ ] Mã giả, dữ liệu giả, output rút gọn và mô phỏng đã được gắn nhãn; phạm vi phiên bản đã xác định
      khi hành vi có thể đổi theo version?
- [ ] Link trong *Đọc thêm / Tài liệu tham khảo* còn mở được và đúng nội dung được viện dẫn?
- [ ] Cú pháp đã qua cổng lint của dự án (ở SchoolAI là `npm run lint:mdx`; dự án khác dùng cổng
      tương đương) sau lần sửa cuối?
- [ ] Định danh máy (`id`, slug, URL, path, prop, code) không bị chèn phần giải nghĩa?
- [ ] Tên tag HTML/JSX trong câu đã bọc backtick; code nhiều dòng đã vào code fence; mọi prop đóng đủ
      quote/ngoặc/tag?
- [ ] Không còn `HOLD…`, ký tự NUL hoặc placeholder nội bộ?

## Trực quan, tiếp cận, đa nền tảng

- [ ] Đã render và xem thật ở desktop lẫn mobile; không có chữ/sơ đồ/bảng tràn hoặc bị cắt?
- [ ] Hình và tương tác quan trọng có đường hiểu tương đương bằng chữ; dùng được bằng bàn phím;
      không phụ thuộc riêng vào màu/chuyển động?
- [ ] Component bị rút gọn (stub) trên nền tảng khác vẫn có fallback giữ đủ mục tiêu học và cách tự kiểm?

## Nguồn và bàn giao

- [ ] Tên/link nguồn bên thứ ba chỉ nằm trong *Đọc thêm / Tài liệu tham khảo*?
- [ ] Không còn câu "theo/dựa trên/lấy từ roadmap, nguồn, tài liệu…" trong phần giảng dạy?
- [ ] Nội dung đã viết lại độc lập bằng tiếng Việt, không sao chép câu chữ/cấu trúc của nguồn?
- [ ] Nếu có link lộ trình do người dùng cung cấp: đã lập danh mục đủ chặng/chủ đề/bài/mục con,
      có trạng thái, và không mục nào bị bỏ vì thiếu link?
- [ ] Mọi thay đổi phạm vi hoặc thứ tự lớn so với lộ trình gốc đều có xác nhận rõ ràng của người dùng?
- [ ] Đã walkthrough toàn bài như người mới, không dùng kiến thức ngoài phần tiên quyết?

**Chốt bàn giao:** tự đọc lại phần prose **và quét riêng nội dung trong bảng / prop component**.
Còn một thuật ngữ khó chưa giải nghĩa, một nhãn tiếng Anh nén, hoặc một kết luận mơ hồ không có hệ
quả → **không được báo hoàn thành**.
