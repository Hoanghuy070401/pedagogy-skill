# Ghi chú phản biện để chỉnh sửa tài liệu và sản phẩm

**Ngày phản biện:** 2026-08-11  
**Phạm vi:** `../01-kien-truc-va-san-pham/startdoc.md`, `../01-kien-truc-va-san-pham/plan-ecosystem-scaffold.md`, `../01-kien-truc-va-san-pham/plan-open-lesson-platform.md`  
**Góc nhìn:** Giảng viên có nhiều năm kinh nghiệm giảng dạy và thẩm định chuyên môn, nhưng không thành thạo AI hoặc công cụ lập trình.

## 1. Kết luận chung

Đề án có định hướng giáo dục đúng và đáng tiếp tục. Những điểm mạnh nổi bật là giáo viên giữ quyền phê duyệt cuối cùng, bài học được xây dựng từ chuẩn đầu ra, nội dung có thể truy về nguồn, chất lượng được kiểm tra trước khi phát hành, dữ liệu thuộc quyền kiểm soát của người dùng và hệ thống không bị khóa vào một nhà cung cấp AI.

Tuy nhiên, tài liệu hiện chứng minh được tầm nhìn và kiến trúc kỹ thuật nhiều hơn là chứng minh hiệu quả sư phạm hoặc khả năng sử dụng thực tế. Một giáo viên không thành thạo công nghệ chưa thể tự sử dụng sản phẩm ở trạng thái hiện tại.

Ước lượng khả năng áp dụng:

- Áp dụng các nguyên tắc vào công việc chuyên môn: **65–75%**.
- Trực tiếp sử dụng phần mềm ở trạng thái hiện tại: **15–20%**.
- Mức sẵn sàng để triển khai rộng rãi trong trường học: **25–30%**.

Agent chỉnh sửa cần phân biệt rõ ba khái niệm trong mọi tài liệu sau này:

1. Kiến trúc kỹ thuật đã hoạt động.
2. Quy trình tạo sản phẩm giáo dục đã hoạt động.
3. Hiệu quả sư phạm đã được kiểm chứng với giáo viên và học sinh.

Hiện tại dự án chủ yếu mới đạt mức thứ nhất.

## 2. Những nội dung cần giữ lại

### 2.1 Bắt đầu từ chuẩn đầu ra

Giữ nguyên tư tưởng không dùng một câu lệnh để tạo toàn bộ giáo án. Quy trình đúng nên là:

```text
Chuẩn đầu ra
  -> nguồn và kiến thức tiên quyết
  -> dàn ý
  -> hoạt động dạy và học
  -> luyện tập
  -> đánh giá
  -> giáo viên duyệt
```

Ma trận `mục tiêu -> nội dung giảng dạy -> hoạt động luyện tập -> đánh giá` phải là cấu trúc trung tâm của sản phẩm.

### 2.2 Phân vai nguồn

Giữ cơ chế phân loại nguồn thành:

- Nguồn bắt buộc phải tuân theo.
- Nguồn kiến thức chính.
- Nguồn tham khảo bổ sung.
- Nguồn chỉ dùng làm ví dụ hoặc minh họa.
- Nguồn không được sử dụng để tạo kiến thức.

Giao diện dành cho giáo viên cần dùng tiếng Việt dễ hiểu; các mã kỹ thuật như `required`, `primary`, `reference`, `example_only`, `excluded` chỉ nên nằm bên dưới hệ thống.

### 2.3 Giáo viên phê duyệt cuối cùng

Giữ nguyên nguyên tắc AI chỉ phát hiện vấn đề, đưa bằng chứng và đề xuất sửa. Giáo viên quyết định nguồn nào được dùng và phiên bản nào đủ điều kiện phát hành.

Không được dùng cách trình bày khiến giáo viên hiểu rằng điểm số do AI tạo ra là kết luận chuyên môn cuối cùng.

### 2.4 Truy xuất nguồn

Giữ yêu cầu truy nguồn đối với định nghĩa, số liệu, sự kiện, quy định, kiến thức cốt lõi, câu hỏi và đáp án. Đây là điểm khác biệt có giá trị của sản phẩm.

### 2.5 Trạng thái thẩm định

Giữ các trạng thái khác nhau, nhưng dịch và giải thích rõ cho giáo viên:

- Bản nháp.
- Do AI tạo, chưa được duyệt.
- Đã kiểm tra nguồn.
- Đã được giáo viên duyệt.
- Đã được đồng nghiệp hoặc tổ chuyên môn duyệt.
- Đã thử nghiệm trong lớp học.

Không được coi `Teacher-reviewed` tương đương với `Classroom-tested`.

### 2.6 Local-first và định dạng mở

Giữ mục tiêu người dùng sở hữu dữ liệu, có thể sửa và sử dụng bài học ngay cả khi dịch vụ AI ngừng hoạt động. Tuy nhiên, kiến trúc này phải được ẩn sau giao diện đơn giản đối với giáo viên.

## 3. Những vấn đề cần sửa

### 3.1 Tài liệu chưa viết cho đúng người dùng mục tiêu

**Vấn đề:** Tài liệu dành cho giáo viên nhưng dùng quá nhiều thuật ngữ như Git, fork, pull request, YAML, JSON, JSONL, schema, pipeline, provider, provenance, deterministic eval, hash, embedding và prompt injection.

**Yêu cầu sửa:**

- Tạo một tài liệu giới thiệu dài khoảng 2–3 trang, viết hoàn toàn bằng ngôn ngữ giáo viên.
- Mỗi thuật ngữ bắt buộc phải dùng cần có lời giải thích tiếng Việt và ví dụ cụ thể.
- Phân tách tài liệu thành hai lớp: `Tài liệu cho giáo viên` và `Đặc tả kỹ thuật cho đội phát triển`.
- Không yêu cầu giáo viên trực tiếp mở hoặc sửa YAML/JSON.
- Git phải là lớp hạ tầng chạy phía sau, không phải thao tác bắt buộc của người dùng phổ thông.

### 3.2 Cách mô tả trạng thái triển khai dễ gây hiểu nhầm

**Vấn đề:** Cụm từ “tested end-to-end” trong `../01-kien-truc-va-san-pham/plan-ecosystem-scaffold.md` có thể khiến người đọc nghĩ rằng hệ thống đã tạo và kiểm định được một bài học hoàn chỉnh. Trên thực tế:

- Logic tạo bài thực chất vẫn nằm ngoài phạm vi scaffold.
- Bộ chấm `EduEvals` đang là placeholder, chủ yếu xác nhận dữ liệu không rỗng.
- Thử nghiệm với Ollama chưa tạo được đầu ra do chưa có mô hình cần thiết.

**Yêu cầu sửa:**

- Đổi cách diễn đạt thành: “Đã kiểm tra luồng kỹ thuật và việc ghi tệp đầu ra; chưa kiểm chứng chất lượng tạo bài hoặc chất lượng đánh giá giáo dục.”
- Tách bảng trạng thái thành `đã xây`, `đã kiểm thử kỹ thuật`, `đã kiểm thử với giáo viên`, `đã thử trong lớp`.
- Không dùng từ “hoàn thành” cho phần chưa có logic nghiệp vụ hoặc chưa có dữ liệu kiểm chứng.

### 3.3 Phần sư phạm còn mỏng hơn phần kỹ thuật

**Vấn đề:** Tài liệu mô tả kỹ cấu trúc tệp và công nghệ nhưng chưa có đặc tả đủ sâu về chất lượng bài học.

**Cần bổ sung:**

- Cách viết mục tiêu học tập có thể quan sát và đánh giá.
- Phân biệt yêu cầu về kiến thức, năng lực và phẩm chất.
- Kiến thức tiên quyết và cách phát hiện lỗ hổng kiến thức.
- Cách phân bổ hoạt động theo thời lượng thực tế.
- Dạy học phân hóa cho các nhóm học sinh.
- Hỗ trợ học sinh có nhu cầu đặc biệt.
- Đánh giá thường xuyên trong quá trình học, không chỉ bài kiểm tra cuối.
- Tiêu chí viết câu hỏi, phương án nhiễu, phản hồi và đáp án.
- Cách xử lý quan niệm sai phổ biến của học sinh.
- Sự khác nhau giữa các môn học và cấp học.
- Mức độ phù hợp với chương trình giáo dục Việt Nam và yêu cầu địa phương.

Không nên mở rộng `pedagogy-skill` bằng nội dung chung chung. Trước hết cần chọn một môn, một lớp và một dạng bài để viết bộ quy tắc đủ sâu.

### 3.4 Gói bài học quá phức tạp đối với giáo viên

**Vấn đề:** Open Lesson Package có nhiều tệp kỹ thuật. Cấu trúc này có thể phù hợp cho hệ thống nhưng gây quá tải nếu giáo viên phải nhìn thấy hoặc quản lý từng tệp.

**Yêu cầu sửa:** Giao diện chỉ nên thể hiện bốn nhóm chính:

1. Kế hoạch bài dạy.
2. Học liệu dành cho học sinh.
3. Kiểm tra, đáp án và rubric.
4. Báo cáo nguồn, chất lượng và cảnh báo.

Các tệp manifest, provenance, build metadata và schema nên được hệ thống quản lý ngầm. Giáo viên chỉ mở chúng khi cần xem chi tiết.

### 3.5 Khối lượng truy nguồn có thể làm tăng gánh nặng

**Vấn đề:** Nếu mọi câu trong mọi tài liệu đều phải truy nguồn, thời gian kiểm tra có thể lớn hơn thời gian tự soạn bài.

**Yêu cầu sửa:** Chia nội dung thành ba mức:

- **Bắt buộc truy nguồn:** định nghĩa, số liệu, sự kiện, quy định, kiến thức cốt lõi, câu hỏi và đáp án.
- **Nên truy nguồn:** diễn giải học thuật, ví dụ thực tế và nội dung dễ gây tranh luận.
- **Không cần truy từng câu:** lời dẫn, hướng dẫn thao tác, câu chuyển ý và tổ chức hoạt động.

Giao diện cần cho phép lọc cảnh báo theo mức nghiêm trọng và chỉ yêu cầu giáo viên xử lý những cảnh báo quan trọng trước.

### 3.6 Kiểm chứng nguồn chưa thể đồng nhất với kiểm chứng chân lý

**Vấn đề:** Nguồn chính thống có thể đúng về nội dung nhưng chưa chắc phù hợp với trình độ học sinh. Hai nguồn độc lập cũng không tự động bảo đảm kết luận đúng. Quy tắc nguồn phải thay đổi theo môn và loại kiến thức.

**Yêu cầu sửa:**

- Tách `độ tin cậy của nội dung` khỏi `độ phù hợp sư phạm`.
- Nêu rõ khi nào một nguồn chính thống duy nhất là đủ, chẳng hạn văn bản chương trình hoặc quy định pháp luật.
- Nêu rõ khi nào cần đối chiếu nhiều nguồn.
- Không dùng một điểm số tổng hợp kiểu “nguồn đúng 87%”.
- Khi nguồn mâu thuẫn, hệ thống phải trình bày bằng chứng và chuyển cho người có chuyên môn quyết định.
- Bổ sung xử lý chất lượng OCR, số trang sai, bản quét thiếu trang và tài liệu đã lỗi thời.

### 3.7 Chỉ tiêu 100% chưa chứng minh chất lượng giáo dục

**Vấn đề:** `100% claim có provenance` và `100% quiz item truy được tới nguồn` là chỉ tiêu tuân thủ quy trình, không phải bằng chứng rằng bài học có chất lượng.

**Yêu cầu sửa:** Bổ sung các nhóm chỉ số:

- Thời gian giáo viên cần để có bản dùng được.
- Tỷ lệ nội dung giáo viên phải viết lại.
- Số vòng sửa trước khi chấp nhận.
- Tỷ lệ cảnh báo đúng và cảnh báo giả.
- Mức đồng thuận giữa hai giáo viên chấm độc lập.
- Mức độ học sinh hoàn thành mục tiêu học tập.
- Khả năng nhớ, vận dụng và sửa quan niệm sai sau bài học.
- Tỷ lệ học liệu được giáo viên sử dụng thật.

Không dùng một tỷ lệ đơn lẻ để tuyên bố bài học “đạt chất lượng”.

### 3.8 Mẫu nghiên cứu ban đầu còn nhỏ

**Vấn đề:** Phỏng vấn 8–12 giáo viên và thử với 3–5 giáo viên phù hợp cho giai đoạn khám phá, nhưng không đủ để khẳng định nhu cầu chung hoặc hiệu quả giáo dục.

**Yêu cầu sửa:**

- Ghi rõ đây là mẫu khám phá, không đại diện cho toàn bộ giáo viên.
- Chọn giáo viên có mức kinh nghiệm và năng lực công nghệ khác nhau.
- Sau thử nghiệm ban đầu, mở rộng theo môn, cấp học, địa phương và điều kiện thiết bị.
- Quan sát hành vi sử dụng thực tế, không chỉ hỏi giáo viên có thích sản phẩm hay không.

### 3.9 Local-first vẫn có rào cản triển khai

**Vấn đề:** Giáo viên không thành thạo công nghệ sẽ khó cài Python, Ollama, mô hình local, cấu hình khóa dịch vụ, xử lý lỗi và quản lý dung lượng. Mô hình local cũng có thể yếu hơn đối với tiếng Việt hoặc cần máy có cấu hình cao.

**Yêu cầu sửa:**

- Xác định cấu hình máy tối thiểu và cấu hình khuyến nghị.
- Có bộ cài đặt một lần, giao diện khởi động đơn giản và cơ chế tự kiểm tra lỗi.
- Có chế độ cloud dễ dùng nhưng hiển thị rõ dữ liệu nào sẽ rời khỏi máy.
- So sánh chất lượng, tốc độ và chi phí giữa mô hình local và cloud trên cùng benchmark tiếng Việt.
- Thiết kế chế độ hỗ trợ kỹ thuật cho trường học, không giả định mỗi giáo viên có thể tự quản trị hệ thống.

### 3.10 Local không tự động có nghĩa là an toàn

**Vấn đề:** Dữ liệu nằm trên máy vẫn có thể bị lộ do máy dùng chung, mất máy, phần mềm độc hại, sao lưu không an toàn hoặc chia sẻ nhầm tệp.

**Yêu cầu sửa:**

- Bổ sung mô hình rủi ro dữ liệu thay vì chỉ tuyên bố local-first.
- Có mã hóa hoặc ít nhất hướng dẫn bảo vệ dữ liệu nhạy cảm.
- Phát hiện và loại tên học sinh, email, mã số và thông tin liên hệ trước khi gửi lên cloud.
- Có màn hình cho người dùng xem trước chính xác dữ liệu nào sẽ được gửi.
- Có quy định thời gian lưu, xóa và sao lưu dữ liệu.
- Kiểm tra trường hợp nhiều người dùng chung một máy.

### 3.11 Thiếu vấn đề bản quyền và giấy phép trong quy trình sử dụng

**Vấn đề:** Tài liệu có nhắc metadata giấy phép nhưng chưa chỉ rõ giáo viên được phép đưa tài liệu nào vào hệ thống, được phép trích bao nhiêu và được chia sẻ đầu ra đến mức nào.

**Yêu cầu sửa:**

- Phân biệt quyền sử dụng để soạn bài nội bộ và quyền phát hành công khai.
- Cảnh báo khi nguồn không rõ giấy phép.
- Không tự động coi tài liệu có thể tải về là tài liệu có thể tái phân phối.
- Lưu thông tin nguồn và giấy phép trong gói bài học.
- Cho phép xuất bản gói chỉ chứa metadata hoặc đường dẫn nếu không được phép đóng gói nội dung nguồn.

### 3.12 Thuật ngữ tiếng Anh và tiếng Việt đang trộn lẫn

**Vấn đề:** Cách viết hiện nay phù hợp với đội kỹ thuật hơn là giáo viên.

**Yêu cầu sửa:**

- Chọn thuật ngữ tiếng Việt thống nhất trong tài liệu người dùng.
- Có bảng thuật ngữ đối chiếu ở cuối tài liệu.
- Chỉ giữ tên tệp và mã trường bằng tiếng Anh trong đặc tả kỹ thuật.
- Ví dụ: dùng “nguồn gốc và bằng chứng” thay cho `provenance`, “kiểm tra theo quy tắc” thay cho `deterministic eval`, “nhà cung cấp mô hình” thay cho `provider`.

## 4. Thứ tự ưu tiên đề nghị

### P0 — Phải làm trước khi tiếp tục mở rộng kỹ thuật

- Chọn một môn, một lớp và một bài mẫu có 3–5 nguồn thật.
- Viết Open Lesson Package v0.1 bằng tay để kiểm tra cấu trúc.
- Rút gọn trải nghiệm giáo viên thành bốn nhóm sản phẩm.
- Viết rubric sư phạm cụ thể cho bài mẫu.
- Sửa lại tuyên bố trạng thái triển khai cho chính xác.
- Tạo tài liệu giới thiệu 2–3 trang bằng ngôn ngữ giáo viên.

### P1 — Phải có trong MVP

- Giao diện local để nhập nguồn, duyệt dàn ý, sửa bài và xuất tài liệu.
- Không bắt giáo viên sửa YAML/JSON hoặc dùng dòng lệnh.
- Truy nguồn theo mức độ quan trọng.
- Kiểm tra deterministic thực chất.
- Báo cáo chất lượng dễ đọc, có cảnh báo ưu tiên.
- Xuất DOCX, PPTX và PDF với định dạng đủ dùng.
- Phát hiện dữ liệu học sinh trước khi gửi ra ngoài máy.

### P2 — Kiểm chứng với người dùng

- Cho 3–5 giáo viên thử một bài thật.
- Đo thời gian, số lần sửa và tỷ lệ nội dung phải viết lại.
- Mời ít nhất hai giáo viên chấm độc lập để đo mức đồng thuận.
- Sau vòng đầu, mở rộng thử nghiệm sang môn hoặc cấp học khác.

### P3 — Chỉ làm sau khi MVP chứng minh được giá trị

- Marketplace hoặc catalog cộng đồng lớn.
- Hỗ trợ nhiều provider hơn mức cần thiết.
- Audio, video, avatar và infographic phức tạp.
- Hỗ trợ đồng thời mọi môn, mọi lớp và mọi chương trình.

## 5. Bài thử nghiệm đầu tiên được đề nghị

Agent nên chọn một bài có phạm vi nhỏ nhưng đủ để kiểm tra toàn bộ quy trình. Bài thử cần có:

- Một chuẩn đầu ra rõ ràng.
- Một nguồn chính thức.
- Hai nguồn bổ sung.
- Ít nhất một điểm có khả năng mâu thuẫn hoặc khác cách diễn giải.
- Một kiến thức tiên quyết.
- Một hoạt động dạy học.
- Một hoạt động luyện tập.
- Năm đến mười câu hỏi, có đáp án và giải thích.
- Một rubric đánh giá sản phẩm hoặc hoạt động.
- Một lỗi cố ý về nguồn và một câu hỏi vượt quá nội dung đã dạy để kiểm tra hệ thống.

Không nên bắt đầu bằng một môn hoặc bài quá rộng. Mục tiêu của bài thử đầu tiên là kiểm tra xem giáo viên có thể hiểu, sửa, phê duyệt và sử dụng đầu ra hay không.

## 6. Tiêu chí hoàn thành vòng sửa tài liệu

Vòng chỉnh sửa tài liệu chỉ được coi là hoàn thành khi:

- Người đọc phân biệt được dự án đang ở giai đoạn ý tưởng, bộ khung, MVP hay đã thử nghiệm trong lớp.
- Giáo viên không thành thạo công nghệ hiểu được quy trình mà không cần biết Git hoặc YAML.
- Có ít nhất một ví dụ đầy đủ về ma trận mục tiêu, nội dung, luyện tập và đánh giá.
- Có rubric sư phạm đủ cụ thể để hai giáo viên có thể dùng chấm độc lập.
- Có quy định nội dung nào bắt buộc truy nguồn và nội dung nào không cần.
- Có kế hoạch xử lý quyền riêng tư, bản quyền và dữ liệu học sinh.
- Các chỉ số thành công bao gồm cả chất lượng học tập và gánh nặng chỉnh sửa của giáo viên.
- Mọi tuyên bố về kiểm thử đều nói rõ đã kiểm thử kỹ thuật, kiểm thử với giáo viên hay thử nghiệm trong lớp.

## 7. Phán quyết cuối cùng

Định hướng sản phẩm có nền tảng tư tưởng tốt: giáo viên làm chủ, nguồn là bằng chứng, AI không có quyền quyết định cuối cùng và học liệu phải có khả năng kiểm tra, sửa chữa, bảo trì. Đây là hướng nên tiếp tục.

Điểm yếu hiện tại là khoảng cách giữa kiến trúc kỹ thuật và công việc thật của giáo viên. Agent sửa tài liệu cần ưu tiên thu hẹp khoảng cách này trước khi mở rộng thêm tính năng. Thành công của sản phẩm không nằm ở số lượng tệp, số mô hình được hỗ trợ hoặc độ phức tạp của kiến trúc; thành công nằm ở việc một giáo viên bình thường có thể tạo được bài dạy đáng tin cậy, sửa được bằng công cụ quen thuộc và sử dụng được trong lớp với ít gánh nặng hơn cách làm hiện nay.

---

## 8. Review vòng 2 sau khi tài liệu đã được chỉnh sửa

### 8.1 Kết quả vòng sửa

Vòng sửa đã xử lý tốt khoảng **75–80%** ý kiến ban đầu. Những nội dung sau đã đạt và không cần làm lại từ đầu:

- Đã có `../01-kien-truc-va-san-pham/gioi-thieu-cho-giao-vien.md` viết bằng ngôn ngữ dễ hiểu.
- Đã nói rõ dự án mới kiểm thử luồng kỹ thuật, chưa kiểm chứng chất lượng giáo dục.
- Đã tách thao tác của giáo viên khỏi Git, YAML, JSON và dòng lệnh.
- Đã gom đầu ra thành bốn nhóm dễ hiểu đối với giáo viên.
- Đã chia yêu cầu truy nguồn thành ba mức độ.
- Đã bổ sung rủi ro OCR, tài liệu thiếu trang và nguồn mâu thuẫn.
- Đã bổ sung quyền riêng tư, máy dùng chung, thời gian lưu/xóa và dữ liệu gửi lên cloud.
- Đã bổ sung bản quyền, quyền trích dẫn và quyền tái phân phối.
- Đã nói rõ mẫu 8–12 giáo viên chỉ dùng để khám phá.
- Đã bổ sung chỉ số về thời gian, mức phải viết lại, đồng thuận người chấm và kết quả học tập.

Chất lượng tài liệu hiện có thể đánh giá khoảng **80–85%**, nhưng mức sẵn sàng sử dụng phần mềm vẫn chỉ khoảng **15–20%** vì chưa có bài mẫu hoàn chỉnh, rubric sư phạm thực chất và thử nghiệm với giáo viên.

### 8.2 P0 — Sửa mâu thuẫn về trạng thái repo

**Vấn đề:** Phần `Current state (recap)` trong `../01-kien-truc-va-san-pham/plan-ecosystem-scaffold.md` vẫn ghi `lessonforge` và `EduEvals` là repo rỗng. Cuối cùng tài liệu lại ghi các scaffold đã được xây và đã kiểm tra luồng kỹ thuật. Hai phần đang mô tả hai thời điểm khác nhau nhưng không ghi rõ.

**Yêu cầu sửa:** Chọn một trong hai cách:

1. Đổi `Current state (recap)` thành `State before scaffold implementation`; hoặc
2. Cập nhật bảng theo trạng thái hiện tại và đưa trạng thái ban đầu vào một mục lịch sử riêng.

Phương án 2 được khuyến nghị vì người đọc thường cần biết trạng thái hiện tại trước.

**Tiêu chí hoàn thành:** Không còn chỗ nào trong cùng tài liệu vừa nói repo rỗng vừa nói scaffold đã xây mà thiếu mốc thời gian hoặc lời giải thích.

### 8.3 P0 — Chốt vai trò của chức năng tra cứu và trích dẫn

**Vấn đề:** Phần mở đầu `../01-kien-truc-va-san-pham/plan-open-lesson-platform.md` nói dự án không nên cạnh tranh bằng một giao diện hỏi đáp nguồn giống NotebookLM. Tuy nhiên, phần `Hai nhu cầu cốt lõi` lại đưa tra cứu và trích dẫn thành một chế độ sản phẩm độc lập. Điều này tạo mâu thuẫn chiến lược và có thể làm MVP tăng phạm vi.

**Agent phải làm rõ một trong hai lựa chọn:**

- **Lựa chọn A — Khuyến nghị cho MVP:** Tra cứu/trích dẫn là chức năng hỗ trợ nhẹ trong quy trình tạo “bài dạy có căn cứ”. Nó không phải sản phẩm cạnh tranh độc lập với NotebookLM.
- **Lựa chọn B:** Tra cứu/trích dẫn là một sản phẩm độc lập. Nếu chọn cách này, phải sửa lại tuyên bố khác biệt với NotebookLM, bổ sung lý do cạnh tranh, phạm vi, chỉ số thành công và nguồn lực riêng.

Không được giữ đồng thời hai cách hiểu.

**Tiêu chí hoàn thành:** Tuyên bố định vị, phạm vi MVP, trải nghiệm người dùng và chỉ số thành công cùng mô tả một vai trò thống nhất cho chức năng tra cứu.

### 8.4 P0 — Tạo một bài mẫu và Open Lesson Package v0.1 thủ công

**Vấn đề:** Tài liệu vẫn chỉ ghi đây là “bước tiếp theo”, vì vậy yêu cầu quan trọng nhất của review trước chưa được thực hiện.

**Yêu cầu:** Chọn đúng một môn, một lớp và một bài. Soạn bằng tay một package hoàn chỉnh trước khi tiếp tục tự động hóa sâu. Package tối thiểu phải có:

- Chuẩn đầu ra hoặc mục tiêu học tập.
- 3–5 nguồn thật, trong đó có một nguồn chính thức.
- Kiến thức tiên quyết.
- Ma trận mục tiêu → nội dung dạy → hoạt động luyện tập → đánh giá.
- Kế hoạch bài dạy.
- Học liệu cho học sinh.
- Bài luyện tập.
- 5–10 câu hỏi có đáp án và giải thích.
- Rubric.
- Báo cáo nguồn và cảnh báo.
- Ít nhất một lỗi nguồn cố ý.
- Ít nhất một câu hỏi cố ý vượt ngoài nội dung đã dạy.

**Tiêu chí hoàn thành:** Hai giáo viên có thể đọc package, hiểu bài mà không mở tệp kỹ thuật và dùng cùng một rubric để đánh giá độc lập.

### 8.5 P0 — Chuyển phần sư phạm từ danh sách mong muốn thành quy tắc có thể chấm

**Vấn đề:** Tài liệu đã nhắc đến kiến thức tiên quyết, đặc điểm người học, mức nhận thức, phương án nhiễu và quan niệm sai, nhưng chưa có quy tắc đủ cụ thể để hệ thống hoặc hai giáo viên áp dụng nhất quán.

**Cần bổ sung cho use case MVP:**

- Ví dụ mục tiêu học tập đạt và không đạt.
- Cách xác định hành vi có thể quan sát và đánh giá.
- Cách phân biệt mục tiêu kiến thức, năng lực và phẩm chất khi phù hợp.
- Cách kiểm tra kiến thức tiên quyết.
- Cách phân bổ hoạt động theo thời lượng thật của tiết học.
- Tiêu chí nhận biết bài quá dễ, quá khó hoặc quá tải.
- Quy tắc dạy học phân hóa cho các nhóm học sinh.
- Hỗ trợ học sinh có nhu cầu đặc biệt.
- Điểm kiểm tra thường xuyên trong quá trình học.
- Quy tắc viết câu hỏi, đáp án, phương án nhiễu và phản hồi.
- Cách phát hiện và xử lý quan niệm sai phổ biến.
- Tiêu chí riêng cho môn/lớp/dạng bài được chọn.

Mỗi quy tắc nên có ít nhất một ví dụ đạt, một ví dụ chưa đạt và cách sửa.

**Tiêu chí hoàn thành:** Hai giáo viên dùng rule set và rubric trên cùng một bài phải đạt mức đồng thuận được xác định trước; nếu chưa có ngưỡng thống kê, tối thiểu phải ghi nhận và giải thích mọi tiêu chí họ chấm khác nhau.

### 8.6 P1 — Sắp xếp lại thứ tự ưu tiên

**Vấn đề:** `Thứ tự ưu tiên kỹ thuật` hiện bắt đầu bằng schema, ingestion, provenance và structured output; prototype giao diện duyệt xuất hiện quá muộn. Cách sắp xếp này vẫn thiên về xây hệ thống trước khi kiểm chứng thao tác của giáo viên.

**Yêu cầu sửa thành ba luồng ưu tiên:**

1. **Kiểm chứng sản phẩm:** bài mẫu thủ công → rubric → thử với giáo viên → sửa quy trình.
2. **Kỹ thuật MVP:** nhập nguồn → định vị bằng chứng → tạo bài theo chặng → kiểm định → prototype giao diện duyệt → xuất tài liệu.
3. **Mở rộng:** LMS → community pack → plugin → media phức tạp.

`UI hoàn chỉnh` có thể triển khai sau, nhưng prototype dùng để kiểm tra luồng duyệt phải được làm sớm và song song với schema.

**Tiêu chí hoàn thành:** Backlog không cho phép xây plugin, thêm provider hoặc media trước khi bài mẫu và thử nghiệm giáo viên đạt cổng quyết định.

### 8.7 P1 — Định nghĩa các thuật ngữ dùng trong tiêu chí nghiệm thu

Các thuật ngữ sau hiện chưa đủ rõ để đo nhất quán:

- `claim cốt lõi`.
- `cảnh báo nghiêm trọng`.
- `một vòng sửa có kiểm soát`.
- `tỷ lệ nội dung phải viết lại`.
- `học sinh hoàn thành mục tiêu`.
- `Teacher-reviewed`.
- `Peer-reviewed`.
- `Classroom-tested`.

**Yêu cầu sửa:** Với mỗi thuật ngữ, ghi rõ:

- Định nghĩa.
- Cách đo hoặc cách xác nhận.
- Ai có quyền xác nhận.
- Bằng chứng phải lưu.
- Trường hợp ngoại lệ.

Ví dụ, `tỷ lệ nội dung phải viết lại` cần nói rõ đo theo từ, đoạn, component hay thời gian chỉnh sửa. `Classroom-tested` cần quy định tối thiểu số lớp/lần dạy và loại ghi nhận phải lưu.

**Tiêu chí hoàn thành:** Hai nhóm đánh giá độc lập có thể áp dụng cùng tiêu chí và đi đến cùng trạng thái phát hành từ cùng một bộ bằng chứng.

### 8.8 P1 — Hoàn thiện kế hoạch vận hành local và cloud

**Vấn đề:** Tài liệu đã nhắc installer và giao diện nhưng chưa có yêu cầu vận hành đủ cụ thể.

**Cần bổ sung vào đầu ra MVP hoặc nghiên cứu kỹ thuật:**

- Cấu hình máy tối thiểu và cấu hình khuyến nghị.
- Dung lượng cài đặt và dung lượng từng mô hình local.
- Thời gian xử lý một nguồn và một bài mẫu.
- Giới hạn kích thước/số lượng tài liệu.
- Chi phí ước tính cho cùng tác vụ khi dùng cloud.
- So sánh chất lượng tiếng Việt giữa local và cloud trên cùng benchmark.
- Chế độ cài đặt một lần và tự kiểm tra môi trường.
- Cách cập nhật phần mềm và mô hình.
- Cách sao lưu, khôi phục và xóa dữ liệu.
- Cơ chế hỗ trợ khi giáo viên gặp lỗi.

**Tiêu chí hoàn thành:** Một giáo viên thuộc nhóm thử nghiệm có thể cài hoặc khởi động prototype theo hướng dẫn, hoàn thành tác vụ và biết cần làm gì khi hệ thống báo lỗi mà không cần hiểu Python hoặc Ollama.

### 8.9 P1 — Chuyển nguyên tắc quyền riêng tư thành policy kiểm thử được

**Vấn đề:** Các rủi ro đã được liệt kê đúng nhưng vẫn ở mức định hướng.

**Yêu cầu bổ sung:**

- Loại dữ liệu nào bị cấm gửi lên cloud.
- Loại dữ liệu nào được gửi sau khi loại thông tin nhận dạng.
- Ai phê duyệt việc gửi.
- Dữ liệu được lưu bao lâu và xóa bằng cách nào.
- Tệp tạm, log và cache có chứa nội dung nhạy cảm hay không.
- Hành vi khi phát hiện tên, mã số hoặc thông tin liên hệ của học sinh.
- Cách xử lý trên máy dùng chung.
- Test case chứng minh màn hình xem trước outbound hoạt động.
- Test case chứng minh secret và dữ liệu học sinh không xuất hiện trong package chia sẻ.

**Tiêu chí hoàn thành:** Policy có thể chuyển trực tiếp thành checklist và test case, không chỉ là tuyên bố “ưu tiên quyền riêng tư”.

### 8.10 P1 — Làm rõ cách đo hiệu quả học tập

**Vấn đề:** Tài liệu đã bổ sung “mức độ học sinh hoàn thành mục tiêu, ghi nhớ, vận dụng và sửa quan niệm sai”, nhưng chưa nói đo bằng cách nào.

**Yêu cầu:** Trong pilot cần định nghĩa tối thiểu:

- Bài đo trước và sau khi học nếu phù hợp.
- Nhiệm vụ vận dụng thay vì chỉ hỏi nhớ lại.
- Cách ghi nhận quan niệm sai trước và sau bài học.
- Cùng một chuẩn chấm cho nhóm học sinh.
- Bối cảnh lớp, thời lượng, giáo viên và điều kiện thiết bị.
- Phân biệt kết quả quan sát ban đầu với bằng chứng đủ để kết luận hiệu quả.

Không cần thiết kế nghiên cứu quy mô lớn ở MVP, nhưng không được dùng phản hồi “giáo viên thấy tốt” thay cho bằng chứng học sinh học tốt hơn.

### 8.11 P2 — Bổ sung thông tin đối tượng và liên kết tài liệu

**Đối với `../01-kien-truc-va-san-pham/startdoc.md`:**

- Ghi rõ đây là tài liệu kiến trúc dành cho đội phát triển.
- Đặt liên kết ngay đầu tài liệu tới `../01-kien-truc-va-san-pham/gioi-thieu-cho-giao-vien.md` cho người đọc không chuyên kỹ thuật.

**Đối với `../01-kien-truc-va-san-pham/plan-ecosystem-scaffold.md`:**

- Giữ là tài liệu kỹ thuật, không cần dịch toàn bộ.
- Bảo đảm trạng thái đầu tài liệu phản ánh đúng trạng thái hiện tại.

**Đối với `../01-kien-truc-va-san-pham/plan-open-lesson-platform.md`:**

- Có thể giữ thuật ngữ kỹ thuật vì đây là product/technical plan.
- Khi dùng thuật ngữ quyết định nghiệp vụ, cần gắn với định nghĩa hoặc mục glossary.

**Đối với `../01-kien-truc-va-san-pham/gioi-thieu-cho-giao-vien.md`:**

- Giữ văn phong hiện tại.
- Sau khi có bài mẫu, thêm một ví dụ ngắn từ đầu vào đến bốn nhóm đầu ra.

### 8.12 Cổng kết thúc review vòng 2

Không đóng review chỉ vì tài liệu đã dài và đầy đủ hơn. Review vòng 2 chỉ được coi là hoàn thành khi:

- Bảng trạng thái repo không còn mâu thuẫn.
- Vai trò của tra cứu/trích dẫn được chốt thống nhất.
- Có một môn, lớp và bài MVP cụ thể.
- Có Open Lesson Package v0.1 thủ công từ nguồn thật.
- Có rubric sư phạm với ví dụ đạt/chưa đạt.
- Các thuật ngữ nghiệm thu quan trọng đã có định nghĩa và cách đo.
- Backlog ưu tiên kiểm chứng với giáo viên trước các tính năng mở rộng.
- Policy dữ liệu có thể chuyển thành checklist và test case.
- Có kế hoạch đo hiệu quả học tập ở mức pilot.
- Tài liệu cho giáo viên có ví dụ cụ thể từ đầu vào đến đầu ra.

Sau khi đạt các điều kiện trên, có thể đánh giá lại xem dự án đã đủ cơ sở chuyển từ `Product exploration` sang `MVP implementation` hay chưa.
