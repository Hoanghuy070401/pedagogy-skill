# Quy chuẩn UI học liệu và chuyển động

Áp dụng tài liệu này khi đầu ra là HTML, trang học liệu, bài học tương tác, preview hoặc giao diện
Lesson Studio. Đây là cổng chất lượng bắt buộc, không phải lớp trang trí sau khi đã sinh mã.

## 1. Thứ tự ưu tiên

Khi các mục tiêu xung đột, giải quyết theo thứ tự:

1. Nội dung đúng, nguồn và trạng thái học tập không bị che khuất.
2. Khả năng đọc, bàn phím, trình đọc màn hình và giảm chuyển động.
3. Bố cục ổn định ở mọi kích thước màn hình.
4. Phản hồi tương tác rõ và không gây dịch chuyển bố cục.
5. Thẩm mỹ, cá tính và chuyển động.

Không dùng hiệu ứng để bù cho phân cấp nội dung yếu. Không làm học sinh chờ animation mới đọc
được kiến thức.

## 2. Lập hợp đồng UI trước khi viết mã

Ghi ngắn gọn sáu quyết định sau vào bản nháp triển khai:

| Quyết định | Câu hỏi phải trả lời |
|---|---|
| Người dùng chính | Giáo viên soạn, giáo viên trình chiếu hay học sinh tự học? |
| Công việc chính | Đọc, trình bày, trả lời, kiểm tra nguồn hay chỉnh sửa? |
| Trục nội dung | Phần nào phải được nhìn thấy trước và quan hệ giữa các phần là gì? |
| Mẫu bố cục | Một cột đọc dài, nội dung + mục lục, so sánh, tiến trình hay workbench? |
| Trạng thái | Default, hover, focus, active, disabled, loading, error và success nào thực sự có? |
| Ngân sách motion | Mỗi chuyển động truyền đạt điều gì và khi giảm chuyển động thì thay bằng gì? |

Nếu chưa trả lời được, chưa chọn grid, card hay animation.

### 2.1 Lưu design system theo Master + page overrides

Với dự án có nhiều trang, copy `assets/mau-design-system-hoc-lieu.md` thành
`design-system/learning-ui/MASTER.md`. Đây là nguồn sự thật cho token, typography, layout,
component, accessibility và motion. Mỗi trang chỉ tạo
`design-system/learning-ui/pages/<page>.md` khi thật sự cần khác Master; file trang chỉ ghi phần
khác biệt, không chép lại toàn bộ hệ thống.

Không sinh lại Master nếu file đã tồn tại mà chưa đọc và đối chiếu. Mọi thay đổi có chủ ý phải được
ghi vào Master trước khi sửa hàng loạt component.

### 2.2 Ghi nhớ lịch sử chỉnh sửa của người dùng

Trước khi tạo hoặc sửa UI, tìm và đọc `design-system/learning-ui/USER-PREFERENCES.md`. Nếu chưa có,
tạo từ phần mẫu trong `assets/mau-design-system-hoc-lieu.md`. Sau mỗi yêu cầu sửa trực tiếp của
người dùng, cập nhật file này trong cùng lượt làm việc.

Chỉ ghi một thói quen khi có bằng chứng rõ: người dùng yêu cầu cụ thể, lặp lại lựa chọn, hoặc xác
nhận một phương án. Mỗi mục phải có:

- ngày xác nhận và phạm vi: component, page, artifact, dự án hay mọi UI của dự án;
- quy tắc ngắn ở dạng mệnh lệnh;
- bằng chứng là yêu cầu sửa đã quan sát, không chép dữ liệu nhạy cảm;
- ví dụ nên làm và trường hợp không áp dụng;
- trạng thái `active`, `superseded` hoặc `needs-confirmation`.

Ưu tiên áp dụng: yêu cầu hiện tại → page override → preference `active` mới nhất → Master → mặc
định của skill. Khi hai preference xung đột, giữ cả lịch sử, đánh dấu bản cũ `superseded` và dùng
bản mới. Không âm thầm biến một chỉnh sửa cục bộ thành sở thích toàn dự án. Không ghi nội dung bài,
nguồn, dữ liệu cá nhân hoặc lời nhắc tạm thời vào bộ nhớ thiết kế.

Chốt ba núm thiết kế theo thang 1–5:

- `variance`: mức bất đối xứng/biến thiên bố cục;
- `motion`: mức chuyển động;
- `density`: mật độ thông tin.

Mặc định cho bài học đọc dài là `variance 2 · motion 1 · density 3`. Lesson Studio dành cho giáo
viên có thể dùng `2 · 2 · 4`. Không suy ra phong cách trẻ em, claymorphism hoặc gamification chỉ từ
nhãn “giáo dục”; tuổi người học, công việc chính và loại artifact mới là căn cứ.

## 3. Token và nhịp thị giác

Định nghĩa token ở một nơi rồi chỉ dùng token trong component. Không rải giá trị ngẫu nhiên giữa
các selector.

```css
:root {
  --space-2xs: .25rem;
  --space-xs: .5rem;
  --space-sm: .75rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2.5rem;
  --radius-sm: .5rem;
  --radius-md: .875rem;
  --content-reading: 68ch;
  --target-min: 44px;
  --dur-press: 100ms;
  --dur-state: 180ms;
  --dur-panel: 280ms;
  --ease-out: cubic-bezier(.16, 1, .3, 1);
  --ease-in: cubic-bezier(.7, 0, .84, 0);
  --ease-in-out: cubic-bezier(.65, 0, .35, 1);
}
```

- Dùng `gap` cho khoảng cách giữa các phần tử cùng cấp; dùng margin cho ngắt nhịp có chủ đích.
- Giữ văn bản thân bài từ 45–75 ký tự mỗi dòng, mặc định khoảng `65ch`.
- Cỡ chữ thân bài tối thiểu `1rem`, line-height `1.5–1.65`.
- Tối đa năm cỡ chữ và ba họ font trên một trang; không đổi font chỉ để tạo cảm giác “thiết kế”.
- Mọi nút, lựa chọn, summary và điều khiển chạm được có vùng đích ít nhất `44 × 44px`.

## 4. Quy tắc bố cục chống lệch hàng

### 4.1 Nguyên tắc chung

- Dùng Grid cho cấu trúc trang và Flex/Grid cho nội bộ component.
- Track chứa nội dung dài hoặc ảnh phải dùng `minmax(0, 1fr)`, không dùng `1fr` trần.
- Đặt `min-width: 0` cho con của Grid/Flex có văn bản dài.
- Căn đầu (`align-items: start`) cho các thẻ chứa nhiều dòng. Không căn giữa theo chiều dọc
  chỉ để thẻ trông cân khi nội dung còn ngắn.
- Không đặt `height` hoặc `min-height` tùy ý cho thẻ văn bản. Chỉ đồng chiều cao khi việc so sánh
  thực sự cần và độ dài nội dung đã được kiểm soát.
- Không dùng `position: absolute` để căn badge, icon hoặc nội dung chạy theo văn bản. Absolute chỉ
  dành cho lớp trang trí không tham gia luồng bố cục.
- Không giải quyết lệch hàng bằng các margin âm riêng lẻ.
- Mỗi section có một cạnh căn chủ đạo. Tiêu đề và nội dung dưới nó phải cùng cạnh, trừ khi có chủ
  ý thị giác được mô tả rõ.

### 4.2 Mẫu danh sách mục tiêu có số

Lỗi thường gặp là badge được đặt tuyệt đối, thẻ có `min-height` lớn và đoạn văn phải dùng padding
để né badge. Khi câu dài ngắn khác nhau, phần đầu dòng và khoảng trắng trông lệch.

Dùng hai cột nội bộ: cột badge cố định và cột nội dung co được.

```html
<ol class="objective-grid">
  <li><span>Xác định số proton và neutron trong hạt nhân.</span></li>
  <li><span>Giải thích chuỗi biến đổi bằng số khối và số proton.</span></li>
</ol>
```

```css
.objective-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--space-sm);
  padding: 0;
  list-style: none;
  counter-reset: objective;
}
.objective-grid > li {
  display: grid;
  grid-template-columns: 1.8rem minmax(0, 1fr);
  align-content: start;
  align-items: start;
  gap: var(--space-sm);
  padding: var(--space-md);
  counter-increment: objective;
}
.objective-grid > li::before {
  content: counter(objective);
  display: grid;
  align-self: center;
  width: 1.8rem;
  aspect-ratio: 1;
  place-items: center;
  border-radius: 50%;
}
.objective-grid > li > span {
  min-width: 0;
  overflow-wrap: anywhere;
}
@media (max-width: 40rem) {
  .objective-grid { grid-template-columns: minmax(0, 1fr); }
}
```

Không thêm chiều cao tối thiểu để ép bốn ô bằng nhau. Grid tự kéo các thẻ trong cùng hàng; nội dung
vẫn bám mép trên, còn badge được căn giữa theo chiều cao của khối chữ cùng hàng.

## 5. Responsive là một phần của thiết kế

Thiết kế mobile-first và đặt breakpoint tại nơi nội dung bắt đầu vỡ. Dùng `rem` cho breakpoint và
`clamp()` cho kích thước thay đổi liên tục.

Bắt buộc kiểm tra ở `320`, `375`, `414`, `768`, `1024` và `1440px`, đồng thời kiểm tra zoom 200%.
Tại mỗi kích thước:

- không có cuộn ngang toàn trang;
- tiêu đề, công thức và từ dài không tràn;
- CTA, tab và nút không xuống hai dòng; rút gọn nhãn hoặc cho container đổi hàng;
- bảng được đổi cấu trúc hoặc có vùng cuộn được đặt tên, không đẩy rộng viewport;
- mục lục sticky không đè nội dung hoặc sticky cấp hai;
- nội dung quan trọng không phụ thuộc hover;
- tiếng Việt dài hơn dự kiến vẫn không làm vỡ thẻ.

Đặt lớp an toàn ở gốc:

```css
html, body { overflow-x: clip; }
img, svg, video { max-width: 100%; height: auto; }
h1, h2, h3, .grid > * { min-width: 0; overflow-wrap: anywhere; }
```

Không dùng `width: 100vw` cho container có padding. Dùng `width: 100%`.

### 5.1 Hiệu năng và độ ổn định cảm nhận

- Khai báo `width`/`height` hoặc `aspect-ratio` cho ảnh, video, chart và vùng nội dung bất đồng bộ.
- Dùng `font-display: swap` và fallback có metric gần nhau; không để font tải xong làm đổi hàng chữ.
- Ảnh dưới fold dùng `loading="lazy"`, `srcset`/`sizes` và định dạng phù hợp.
- Không xen kẽ đọc/ghi layout liên tục trong JavaScript; một frame tương tác phải giữ dưới khoảng
  `16ms` khi nhắm 60fps.
- Phản hồi thao tác phải xuất hiện trong khoảng `100ms`. Chỉ hiện spinner/skeleton khi chờ quá
  `300ms` để tránh nhấp nháy.

## 6. Hợp đồng trạng thái tương tác

Với mỗi component tương tác, mô tả và triển khai các trạng thái có ý nghĩa: default, hover, focus,
active, disabled, loading, error, success. Không tạo trạng thái giả chỉ để có animation.

- Focus phải xuất hiện tức thì bằng `:focus-visible`, dày 2–3px và tương phản ít nhất 3:1.
- Hover chỉ đặt trong `@media (hover: hover) and (pointer: fine)` và phải có focus/tap tương đương.
- Border giữ nguyên độ dày giữa các trạng thái; đổi màu hoặc outline để tránh dịch chuyển hình học.
- Error dùng ít nhất hai kênh: thông báo chữ + icon/viền; đặt `aria-invalid` và `aria-describedby`.
- Success im lặng nếu kết quả đã nhìn thấy. Toast dành cho lỗi hoặc thao tác có kết quả bị khuất.
- Loading không xóa nhãn khiến nút đổi chiều rộng; giữ kích thước component ổn định.
- Mỗi màn hình chỉ có một hành động chính. Hành động phụ và nguy hiểm phải khác cấp thị giác.
- Khi đổi route, giữ scroll/filter/dữ liệu nhập nếu người dùng quay lại; chuyển focus tới `main` cho
  trình đọc màn hình.

## 7. Quy chuẩn animation

### 7.1 Cổng quyết định

Trước mỗi animation, ghi một dòng:

`trigger → điều thay đổi → thông tin truyền đạt → thời lượng/easing → reduced-motion`.

Chỉ giữ animation nếu nó làm ít nhất một việc: chỉ hướng không gian, nối nguyên nhân–kết quả, xác
nhận trạng thái hoặc giúp theo dõi sự thay đổi. Nếu bỏ animation mà người dùng không mất thông tin,
hãy bỏ nó.

Trang học liệu đọc dài mặc định **không có animation khi tải hoặc khi cuộn**. Không làm thân bài
fade-in theo từng section. Với giao diện công cụ, tối đa hai animation chính trong một view và ba
primitive chuyển động trên toàn trang.

### 7.2 Thời lượng và thuộc tính

| Nhóm | Thời lượng | Ví dụ |
|---|---:|---|
| Phản hồi tức thì | 80–120ms | nhấn nút, checkbox |
| Đổi trạng thái nhỏ | 150–200ms | hover, tooltip, đổi màu |
| Mở lớp UI | 250–300ms | menu, dialog, panel |
| Chuyển đổi phức hợp | 400–500ms | accordion, toast |
| Không motion | 0ms | focus, lỗi, điều hướng bàn phím |

- Chỉ animate `transform` và `opacity`; accordion có thể dùng `grid-template-rows`.
- Không animate `width`, `height`, `top`, `left`, `margin`, `padding` hoặc border-width.
- Cấm `transition: all`, bounce/overshoot, parallax, cursor follower, gradient chạy và hover scale
  hàng loạt.
- Không dùng vòng lặp vô hạn, trừ loader có chức năng. Không tự chạy carousel.
- Scroll reveal nếu thật sự cần phải chạy một lần bằng `IntersectionObserver`, không dùng listener
  `scroll`, và tắt ở viewport dưới `40rem`.
- Focus ring không được fade hoặc trượt vào.
- Animation phải ngắt được; thao tác mới của người dùng được ưu tiên ngay, không chờ timeline chạy
  xong. Không khóa input hay trì hoãn chuyển trang chỉ để hoàn tất hiệu ứng.

### 7.3 Giảm chuyển động

Giữ trạng thái chức năng nhưng bỏ chuyển động không gian. Với trang học liệu tĩnh, có thể tắt hẳn:

```css
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Với thao tác cần biểu đạt thay đổi trạng thái, thay chuyển động không gian bằng crossfade không quá
`150ms`.

## 8. HTML ngữ nghĩa và khả năng tiếp cận

- Dùng đúng `header`, `nav`, `main`, `section`, `aside`, `footer`; mỗi trang có đúng một `h1` và
  không bỏ cấp heading.
- Có skip link; mọi điều khiển dùng được bằng bàn phím và có tên truy cập được.
- Ảnh có `alt`, `width`, `height`; ảnh trang trí dùng `alt=""`.
- Không dùng màu làm dấu hiệu duy nhất. Văn bản thân bài đạt tương phản 4.5:1; focus/icon đạt 3:1.
- Icon dùng cùng một bộ vector, cùng stroke và kích thước token; căn icon theo baseline của nhãn.
  Không dùng emoji làm icon điều hướng hay điều khiển.
- Công thức, sơ đồ và phản hồi quiz phải có diễn giải chữ. Kết quả bất đồng bộ dùng
  `aria-live="polite"` khi thích hợp.
- `details/summary` ưu tiên hơn accordion JavaScript nếu hành vi gốc đã đủ.
- Giữ nội dung trong DOM và đọc được khi JavaScript lỗi; không để CSS khởi tạo nội dung ở
  `opacity: 0` rồi phụ thuộc JS để hiện.

## 9. Quy trình kiểm tra trước bàn giao

### 9.1 Kiểm tra tĩnh

- không có giá trị màu/font tùy hứng ngoài token;
- không có `transition: all` hoặc transition lên thuộc tính layout;
- có `prefers-reduced-motion` nếu trang có bất kỳ transition/animation nào;
- ID không trùng, liên kết nội trang không gãy, form có label;
- ảnh có kích thước để tránh layout shift;
- công thức và bảng dài có phương án mobile.

### 9.2 Kiểm tra bằng render thật

Render toàn trang ở sáu viewport bắt buộc. Không chỉ xem code hoặc một ảnh desktop. Tại mỗi viewport:

1. Soát cạnh căn trái/phải của heading, badge, văn bản và control.
2. Tìm overlap, clipping, khoảng trắng bất thường và thẻ bị kéo cao vô lý.
3. Dùng bàn phím đi qua mọi control và quan sát focus.
4. Bật reduced motion, kiểm tra nội dung vẫn hiện và trạng thái vẫn hiểu được.
5. Thử câu tiếng Việt dài, công thức dài, 0 mục, 1 mục và số mục lẻ.
6. Thử landscape, zoom/text scale lớn nhất và mạng chậm.
7. Kiểm tra console và thay đổi layout khi tải font/ảnh.

### 9.3 Phiếu tự phê bình trước khi xuất

Chấm 1–5 cho sáu trục: phân cấp, căn chỉnh, responsive, trạng thái, motion và accessibility. Bất kỳ
trục nào dưới 4 phải sửa rồi render lại. Ghi ngắn gọn:

`UI-QA · hierarchy x/5 · alignment x/5 · responsive x/5 · states x/5 · motion x/5 · a11y x/5`.

Không báo “hoàn thành” chỉ vì HTML hợp lệ. UI chỉ hoàn thành sau khi vượt cả kiểm tra tĩnh và render.
