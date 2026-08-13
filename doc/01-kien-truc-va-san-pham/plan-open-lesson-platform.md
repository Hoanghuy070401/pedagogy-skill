# Plan — Open Lesson Platform

> **Cập nhật hướng triển khai 2026-08-11:** thẩm định giáo viên hiện chưa khả
> dụng. Dự án ưu tiên xây công cụ và chuẩn mở; package Vật lí chỉ còn là fixture
> kỹ thuật. Kế hoạch thực thi hiện hành nằm tại
> [`plan-xay-dung-he-sinh-thai.md`](plan-xay-dung-he-sinh-thai.md). Các cổng
> `Teacher-reviewed` và `Classroom-tested` trong tài liệu này được tạm hoãn,
> không chặn việc xây Milestone 1–3.

**Status:** Product exploration  
**Created:** 2026-08-11  
**Related documents:** `gioi-thieu-cho-giao-vien.md`, `startdoc.md`,
`plan-ecosystem-scaffold.md`, `../03-review/review-notes-for-agent.md`,
`../02-pilot/pilot-vat-li-10-co-nang-v0.1/README.md`, `../02-pilot/acceptance-glossary.md`,
`../02-pilot/data-policy-mvp.md`, `../02-pilot/pilot-measurement-plan.md`,
`../02-pilot/local-cloud-operations-research.md`, `../03-review/review-round-2-resolution.md`

## 1. Bối cảnh

NotebookLM đã làm rất tốt việc nhập nhiều loại nguồn, hỏi đáp có dẫn chứng và
chuyển nguồn thành các dạng trình bày như báo cáo, flashcard, quiz, slide, âm
thanh hoặc video. Vì vậy, dự án này không nên cạnh tranh bằng cách tạo thêm một
giao diện hỏi đáp nguồn hoặc cố bắt kịp số lượng artifact của NotebookLM.

Dự án nên giải một bài toán khác:

> **NotebookLM giúp người dùng hiểu và trình bày nguồn. Open Lesson Platform
> giúp giáo viên biến nguồn cùng chuẩn đầu ra thành một gói bài dạy có thể kiểm
> chứng, chỉnh sửa, đánh giá, bảo trì và sở hữu lâu dài.**

Ba repo hiện tại là nền móng phù hợp cho hướng đi này:

- `pedagogy-skill`: tri thức và quy tắc sư phạm.
- `lessonforge`: pipeline biên soạn học liệu.
- `EduEvals`: cổng kiểm định chất lượng.

## 2. Tầm nhìn sản phẩm

Xây dựng một hạ tầng giáo dục mở phục vụ **giáo viên trên toàn quốc**, local-first
và không khóa người dùng vào một nhà cung cấp AI. Giáo viên thuộc các môn, cấp
học, địa phương và mức thành thạo công nghệ khác nhau đều có thể đưa tài liệu
của mình vào để tra cứu, trích dẫn hoặc soạn bài có căn cứ.

Đây là phạm vi dài hạn của sản phẩm, không phải tuyên bố rằng phiên bản đầu sẽ
hỗ trợ tốt ngay mọi môn và mọi cấp học. MVP phải được kiểm chứng trên một phạm
vi hẹp trước, sau đó mở rộng bằng các bộ quy tắc theo môn/cấp học và bằng chứng
sử dụng thực tế.

Trong đó, giáo viên có thể:

1. Chọn chuẩn đầu ra và cung cấp nguồn.
2. Kiểm tra chất lượng, độ mới và phạm vi của nguồn.
3. Duyệt bản đồ kiến thức trước khi AI viết bài.
4. Tạo một gói bài dạy hoàn chỉnh, không chỉ một văn bản tóm tắt.
5. Truy ngược từng phát biểu, câu hỏi và đáp án về nguồn.
6. Chạy kiểm định sư phạm và kiểm định nội dung trước khi sử dụng.
7. Sửa bài bằng công cụ phổ biến, kể cả khi không còn dịch vụ AI.
8. Chia sẻ, fork, review và cập nhật tài nguyên cùng cộng đồng.

### 2.1 Năng lực cốt lõi của MVP

MVP tập trung vào **tạo bài dạy có căn cứ**. Tra cứu và trích dẫn là năng lực hỗ
trợ nhẹ trong quy trình đó, không phải một sản phẩm hỏi đáp nguồn độc lập và
không nhằm cạnh tranh trực tiếp với NotebookLM.

**Tra cứu và trích dẫn hỗ trợ soạn bài**

- Tìm thông tin cần cho dàn ý, claim, câu hỏi hoặc đáp án trong tập nguồn giáo
  viên đã chọn.
- Tìm đúng đoạn, trang, bảng, hình hoặc thời điểm video có liên quan.
- Trích dẫn theo mẫu phù hợp, kèm đường dẫn hoặc vị trí để kiểm tra lại.
- So sánh các nguồn và hiển thị điểm mâu thuẫn.
- Tóm tắt nhưng không làm mất liên kết với bằng chứng gốc.

**Soạn bài từ nguồn**

- Dùng nguồn giáo viên cung cấp cùng chuẩn đầu ra để lập dàn ý.
- Tạo nội dung giảng dạy, hoạt động, bài luyện tập và đánh giá.
- Truy ngược kiến thức cốt lõi, câu hỏi và đáp án về nguồn.
- Kiểm tra tính nhất quán sư phạm trước khi giáo viên phê duyệt.

MVP có thể cho giáo viên mở nhanh một nguồn hoặc lấy một trích dẫn trong lúc
soạn, nhưng không xây chat workspace, nghiên cứu web tổng quát, audio/video hay
các artifact khám phá nguồn. Sau khi Trusted Lesson MVP được kiểm chứng, nhu
cầu tra cứu độc lập mới được đánh giá như một hướng sản phẩm riêng.

## 3. Nguyên tắc thiết kế

### 3.1 Không phụ thuộc nền tảng

Dự án phải giảm bốn dạng lệ thuộc:

| Dạng lệ thuộc | Nguyên tắc xử lý |
|---|---|
| Dữ liệu | Nguồn, bài học, lịch sử sửa và eval thuộc quyền kiểm soát của người dùng |
| Mô hình | Hỗ trợ nhiều cloud provider và mô hình local qua một interface chung |
| Định dạng | Dùng định dạng mở, có thể xuất DOCX, PPTX, PDF, HTML và chuẩn LMS |
| Quy trình | Bài vẫn mở, sửa, dạy và tái sử dụng được khi AI hoặc ứng dụng không còn hoạt động |

### 3.2 AI hỗ trợ theo chặng, không phải “một prompt tạo cả bài”

Mỗi chặng tạo ra dữ liệu có cấu trúc và cần được duyệt hoặc kiểm tra trước khi
đi tiếp. Việc sửa một hoạt động không được buộc người dùng sinh lại toàn bộ bài.

### 3.3 Nguồn là bằng chứng, không phải instruction

Nội dung lấy từ tài liệu được xem là dữ liệu. Chỉ rule set và yêu cầu của giáo
viên mới điều khiển agent. Pipeline phải chống prompt injection từ nguồn.

### 3.4 Không tuyên bố “nguồn đúng tuyệt đối”

Hệ thống chỉ được trình bày bằng chứng và rủi ro theo từng chiều: thẩm quyền,
độ mới, khả năng truy xuất, mức phù hợp, xung đột và độ phủ. Không tạo một “điểm
đúng 87%” gây cảm giác chắc chắn giả.

### 3.5 Giáo viên là người phê duyệt cuối

AI phát hiện vấn đề, đề xuất sửa và đưa bằng chứng. Giáo viên quyết định sử dụng
nguồn nào và phiên bản nào đủ điều kiện phát hành.

## 4. Người dùng mục tiêu ban đầu

### Primary persona

Giáo viên trên toàn quốc cần tra cứu, trích dẫn hoặc soạn một tiết học từ sách
giáo khoa, văn bản chương trình, tài liệu chính thống và nguồn bổ sung của chính
họ; muốn có kết quả kiểm tra lại được nhưng không muốn đưa toàn bộ dữ liệu lên
một nền tảng đóng.

Sản phẩm phải tính đến sự khác nhau về môn học, cấp học, địa phương, kinh
nghiệm giảng dạy, năng lực công nghệ, thiết bị và chất lượng kết nối mạng.

### Secondary personas

- Nhóm chuyên môn cần review và chuẩn hóa bài của nhiều giáo viên.
- Tác giả khóa học cần quản lý nhiều bài và cập nhật khi nguồn thay đổi.
- Trường học cần chạy local/on-premise và kiểm soát dữ liệu.
- Cộng đồng giáo dục mở muốn chia sẻ curriculum, rubric và benchmark.

## 5. Trải nghiệm soạn bài mục tiêu

### 5.0 Điểm vào đơn giản

Màn hình đầu của MVP bắt đầu bằng **Soạn bài từ tài liệu**. Trong từng bước lập
dàn ý, viết nội dung hoặc tạo đánh giá, giáo viên có thể chọn “Tìm trong nguồn”
hoặc “Lấy trích dẫn” để xem bằng chứng liên quan. Hai hành động này không mở ra
một sản phẩm chat độc lập.

```text
Chọn chuẩn đầu ra
        ↓
Thêm và phân loại nguồn
        ↓
Kiểm tra sức khỏe nguồn
        ↓
AI tạo bản đồ kiến thức và vùng chưa chắc chắn
        ↓
Giáo viên duyệt dàn ý + ma trận sư phạm
        ↓
AI tạo lesson package theo từng artifact
        ↓
Kiểm định nguồn + sư phạm + kỹ thuật
        ↓
Giáo viên xem diff, sửa và phê duyệt
        ↓
Xuất bản / chia sẻ / lưu phiên bản
```

### 5.1 Brief có cấu trúc

`lesson.yaml` cần tiến tới hỗ trợ:

- Môn, lớp, chương và bài.
- Chuẩn đầu ra hoặc năng lực cần đạt.
- Thời lượng.
- Kiến thức tiên quyết.
- Mức nhận thức mong muốn.
- Hình thức dạy và điều kiện thiết bị.
- Đặc điểm người học và nhu cầu hỗ trợ.
- Artifact cần tạo.
- Nội dung bắt buộc, tùy chọn và bị loại trừ.

### 5.2 Phân vai nguồn

Giáo viên có thể đánh dấu mỗi nguồn là:

- `required`: nguồn bắt buộc phải tuân theo.
- `primary`: nguồn kiến thức chính.
- `reference`: nguồn tham khảo bổ sung.
- `example_only`: chỉ dùng cho ví dụ/minh họa.
- `excluded`: không dùng để tạo kiến thức.

### 5.3 Duyệt trước khi viết

Trước khi sinh bài, hệ thống phải đưa ra:

- Danh sách khái niệm dự định dạy.
- Khái niệm nào được nguồn nào hỗ trợ.
- Kiến thức còn thiếu nguồn.
- Các điểm nguồn mâu thuẫn.
- Dàn ý bài học.
- Ma trận mục tiêu → phần giảng → thực hành → đánh giá.

## 6. Open Lesson Package

Đầu ra canonical không phải một notebook hoặc một file Markdown duy nhất mà là
một gói tài nguyên mở:

```text
lesson-package/
├── lesson.yaml
├── curriculum-map.yaml
├── source-manifest.json
├── provenance.json
├── teacher-guide.md
├── student-handout.md
├── slides.md
├── worksheet.md
├── quiz.json
├── answer-key.md
├── rubric.json
├── quality-report.json
└── build-manifest.json
```

Các file DOCX, PPTX, PDF, HTML hoặc QTI/Moodle là bản build từ nguồn canonical,
không phải nguồn sự thật duy nhất.

Cấu trúc file này chỉ dành cho hệ thống và đội phát triển. Giao diện giáo viên
chỉ hiển thị bốn nhóm dễ hiểu:

1. Kế hoạch bài dạy.
2. Học liệu dành cho học sinh.
3. Kiểm tra, đáp án và tiêu chí đánh giá.
4. Nguồn, chất lượng và cảnh báo.

Các manifest, metadata, schema và lịch sử build được quản lý ngầm. Giáo viên
không phải mở YAML/JSON hoặc dùng dòng lệnh để hoàn thành công việc.

### 6.1 `source-manifest.json`

Lưu tối thiểu:

- ID, tên, tác giả và đơn vị phát hành.
- Loại nguồn và vai trò trong bài.
- URL hoặc đường dẫn local.
- Ngày xuất bản, ngày truy cập và phiên bản.
- Hash nội dung đã dùng.
- Phạm vi môn/lớp/quốc gia.
- Giấy phép và quyền sử dụng nếu xác định được.
- Kết quả kiểm tra sức khỏe nguồn.

### 6.2 `provenance.json`

Mỗi claim quan trọng, câu hỏi, đáp án và số liệu phải liên kết được tới:

- `source_id`.
- Trang, heading, đoạn hoặc timestamp.
- Đoạn bằng chứng ngắn.
- Trạng thái `supported`, `contradicted` hoặc `insufficient_evidence`.
- Mức chắc chắn và lý do của hệ thống.

### 6.3 `build-manifest.json`

Lưu thông tin tái lập bản build:

- Phiên bản schema và pedagogy rules.
- Provider/model đã sử dụng.
- Tham số generation quan trọng.
- Thời điểm build.
- Phiên bản từng nguồn.
- Danh sách eval đã chạy và kết quả.

Không lưu API key hoặc dữ liệu nhạy cảm trong manifest.

## 7. Source Trust Engine

Mục tiêu của engine không phải xác nhận chân lý tuyệt đối mà là làm rõ bằng
chứng và giảm rủi ro.

### 7.1 Hồ sơ nguồn theo nhiều chiều

- Thẩm quyền của tác giả/tổ chức.
- Nguồn sơ cấp hay tổng hợp.
- Ngày xuất bản và độ mới.
- Phiên bản và phạm vi áp dụng.
- Khả năng truy lại tài liệu gốc.
- Mức phù hợp với môn, lớp và địa phương.
- Dấu hiệu quảng cáo hoặc xung đột lợi ích.
- Giấy phép và quyền tái sử dụng.
- Chất lượng nhận dạng văn bản đối với bản quét/OCR.
- Tình trạng thiếu trang, sai thứ tự trang hoặc không đọc được bảng/hình.

### 7.2 Thứ hạng nguồn phụ thuộc lĩnh vực

- Chương trình học: văn bản chính thức của cơ quan giáo dục.
- Pháp luật: văn bản gốc còn hiệu lực.
- Y tế: cơ quan y tế và hướng dẫn chuyên môn cập nhật.
- Khoa học: giáo trình, cơ quan khoa học, nghiên cứu gốc hoặc tổng quan hệ thống.
- Công nghệ: đặc tả tiêu chuẩn và tài liệu chính thức đúng phiên bản.
- Sự kiện: nguồn trực tiếp kết hợp nhiều nguồn báo chí độc lập.

Không dùng cùng một tiêu chí authority cho mọi lĩnh vực.

### 7.3 Kiểm chứng chéo và phát hiện nguồn sao chép

Với claim quan trọng, hệ thống nên tìm bằng chứng từ hai nguồn độc lập khi phù
hợp. Hai trang sao chép cùng một nội dung không được tính là hai xác nhận.

Các trạng thái cần hiển thị rõ:

- Được nguồn chính thống hỗ trợ.
- Được nhiều nguồn độc lập hỗ trợ.
- Chỉ có một nguồn.
- Nguồn mâu thuẫn.
- Nguồn đã cũ hoặc sai phạm vi.
- Không tìm thấy đủ bằng chứng.
- Cần chuyên gia duyệt.

Một nguồn chính thống duy nhất có thể đủ khi chính nguồn đó là đối tượng có
thẩm quyền, chẳng hạn văn bản chương trình hoặc quy định còn hiệu lực. Đối với
kiến thức có tranh luận, kết quả nghiên cứu hoặc nội dung thay đổi nhanh, policy
theo môn/lĩnh vực quyết định khi nào cần nhiều nguồn độc lập. Không áp dụng một
quy tắc kiểm chứng giống nhau cho mọi môn học.

### 7.4 Theo dõi thay đổi

Khi hash hoặc phiên bản nguồn thay đổi, hệ thống phải xác định những bài, claim
và câu hỏi nào bị ảnh hưởng; sau đó đề xuất chạy lại generation/eval có phạm vi,
không tự động ghi đè bài đã được giáo viên duyệt.

## 8. EduEvals như cổng phát hành

`EduEvals` cần phát triển từ placeholder scorer thành ba lớp kiểm định.

### 8.1 Kiểm tra deterministic

- Schema và file bắt buộc.
- Link/hình/asset hỏng.
- Mọi mục tiêu có đủ dạy, luyện và đánh giá.
- Quiz không hỏi ngoài nội dung đã dạy.
- Claim cốt lõi có provenance.
- Không có artifact rỗng hoặc placeholder.
- Không lộ secret hoặc dữ liệu học sinh.

### 8.2 Kiểm tra dựa trên mô hình/rubric

- Diễn giải có trung thành với nguồn không.
- Có kết luận vượt quá bằng chứng không.
- Mức đọc có phù hợp người học không.
- Ví dụ, phương án nhiễu và phản hồi có chất lượng không.
- Mức nhận thức có đúng yêu cầu không.
- Có thiên lệch hoặc nội dung không phù hợp không.

### 8.3 Giáo viên phê duyệt

Trạng thái phát hành đề xuất:

```text
Draft
AI-generated
Source-checked
Teacher-reviewed
Peer-reviewed
Classroom-tested
```

Các cảnh báo nghiêm trọng không được tự động bỏ qua. Nếu người dùng vẫn xuất,
artifact phải mang trạng thái `Draft` cùng danh sách rủi ro còn mở.

### 8.4 Mức độ bắt buộc truy nguồn

Để không biến kiểm chứng thành gánh nặng lớn hơn việc soạn bài, nội dung được
chia thành ba mức:

- **Bắt buộc:** định nghĩa, số liệu, sự kiện, quy định, kiến thức cốt lõi, câu
  hỏi và đáp án.
- **Nên có:** diễn giải học thuật, ví dụ thực tế và nội dung dễ gây tranh luận.
- **Không cần từng câu:** lời dẫn, câu chuyển ý, hướng dẫn thao tác và tổ chức
  hoạt động do người soạn tạo ra.

Báo cáo ưu tiên cảnh báo bắt buộc/nghiêm trọng; giáo viên có thể mở chi tiết
những cảnh báo còn lại khi cần.

## 9. Giá trị cộng đồng

Kho cộng đồng không nên chỉ là nơi chứa hàng loạt bài do AI sinh. Những tài sản
có giá trị lâu dài hơn gồm:

- Curriculum pack.
- Bộ nguồn đã được thẩm định.
- Pedagogy framework và rule set.
- Rubric và benchmark.
- Template bài học.
- Bộ kiểm tra tự động.
- Ví dụ đã được giáo viên duyệt.
- Lỗi hiểu sai phổ biến của học sinh.
- Bản dịch và bản địa hóa.

Mỗi đóng góp cần có metadata về tác giả, giấy phép, nguồn, model được dùng,
eval đã chạy và mức review. Cộng đồng có thể fork, dịch, điều chỉnh và gửi thay
đổi qua Git mà không phụ thuộc một marketplace trung tâm.

## 10. Trải nghiệm cho người không dùng Git

Git là lớp hạ tầng, không phải giao diện bắt buộc. Ứng dụng dành cho giáo viên
cần cung cấp các hành động quen thuộc:

- Tạo bài mới.
- Thêm và kiểm tra nguồn.
- Duyệt dàn ý.
- Khóa phần không cho AI sửa.
- Viết lại một phần.
- Xem nguồn của từng claim.
- So sánh hai phiên bản.
- Phê duyệt và rollback.
- Xuất DOCX/PPTX/PDF/LMS.
- Chia sẻ hoặc cập nhật từ cộng đồng.

## 11. Chế độ riêng tư

### Offline

Nguồn, embedding và mô hình đều chạy trên máy. Không cần tài khoản hay mạng sau
khi đã cài đủ model/runtime.

### Private hybrid

Nguồn được phân tích local; chỉ những đoạn cần thiết và đã loại dữ liệu nhạy
cảm mới được gửi tới provider đã chọn.

### Cloud opt-in

Người dùng chủ động chọn provider. Trước khi gửi, giao diện hiển thị dữ liệu nào
sẽ rời máy và gửi tới đâu.

Mọi chế độ phải có bước phát hiện/redact tên học sinh, email, mã số, thông tin
liên hệ và dữ liệu nhạy cảm khác.

Local-first không tự động có nghĩa là an toàn. Thiết kế chi tiết phải bổ sung:

- Rủi ro máy dùng chung, mất máy và sao lưu không an toàn.
- Thời gian lưu, xóa và phục hồi dữ liệu.
- Mã hóa dữ liệu nhạy cảm khi phù hợp.
- Hồ sơ người dùng tách biệt trên máy dùng chung.
- Màn hình xem trước chính xác dữ liệu sắp gửi lên cloud.

### 11.1 Bản quyền và quyền sử dụng nguồn

Hệ thống phải phân biệt:

- Quyền dùng tài liệu để soạn bài nội bộ.
- Quyền trích dẫn trong bài dạy.
- Quyền đóng gói lại hoặc phát hành công khai nội dung nguồn.

Tài liệu tải được không mặc nhiên được phép tái phân phối. Khi giấy phép không
rõ, gói chia sẻ chỉ nên chứa metadata, trích dẫn ở mức được phép và liên kết tới
nguồn; không tự động đóng gói toàn bộ tài liệu gốc.

Policy có thể chuyển thành test case cho MVP nằm tại `doc/02-pilot/data-policy-mvp.md`.
Yêu cầu benchmark cấu hình, chi phí và chất lượng local/cloud nằm tại
`doc/02-pilot/local-cloud-operations-research.md`.

## 12. Lộ trình triển khai

### Giai đoạn 0 — Nghiên cứu và chốt hợp đồng sản phẩm

**Mục tiêu:** xác nhận vấn đề đáng giải trước khi xây giao diện lớn.

Đầu ra:

- Phỏng vấn khám phá 8–12 giáo viên thuộc 2–3 môn, có mức kinh nghiệm, năng lực
  công nghệ, địa phương và điều kiện thiết bị khác nhau. Mẫu này chỉ dùng để
  phát hiện vấn đề, không đại diện cho toàn bộ giáo viên cả nước.
- Thu thập 10 quy trình soạn bài thật và các artifact họ đang sử dụng.
- Chọn một môn/lớp/use case hẹp cho MVP.
- Quan sát nhu cầu tra cứu/trích dẫn như một thao tác bên trong quy trình soạn.
- Viết draft schema Open Lesson Package v0.1.
- Xác định taxonomy nguồn và policy dữ liệu học sinh.
- Tạo 10 bài mẫu cùng bộ lỗi có chủ đích để làm benchmark ban đầu.

**Pilot đã chọn:** Vật lí 10, một tiết 45 phút về cơ năng, chuyển hóa động
năng–thế năng và bảo toàn cơ năng. Package thủ công v0.1 nằm tại
`../02-pilot/pilot-vat-li-10-co-nang-v0.1/`. Đây là lát cắt để kiểm chứng quy trình,
không phải giới hạn đối tượng dài hạn của sản phẩm.

Cổng quyết định:

- Giáo viên xác nhận kiểm chứng nguồn và tính nhất quán của bộ học liệu là vấn
  đề có giá trị hơn việc chỉ tạo slide/video nhanh.
- Có ít nhất 5 giáo viên đồng ý thử prototype bằng tài liệu thật.

### Giai đoạn 1 — Trusted Lesson MVP

**Mục tiêu:** chứng minh workflow khác biệt cốt lõi.

Phạm vi:

- Nhập PDF, DOCX và URL.
- Một điểm vào “Soạn bài từ tài liệu”; tra cứu/trích dẫn nằm trong từng bước.
- `lesson.yaml` có brief và curriculum mapping tối thiểu.
- Source manifest + provenance tới trang/đoạn.
- Duyệt bản đồ kiến thức và dàn ý trước khi viết.
- Sinh `teacher-guide`, `student-handout`, `worksheet`, `quiz`, `answer-key`,
  `rubric`.
- Deterministic eval và một số rubric eval quan trọng.
- Quality report dễ đọc.
- Xuất DOCX, PPTX và PDF.
- Một UI local đơn giản cho luồng duyệt.
- Giao diện tiếng Việt; giáo viên không phải dùng Git, YAML, JSON hoặc CLI.

Ngoài phạm vi:

- Video, podcast, avatar hoặc infographic phức tạp.
- Marketplace tập trung.
- Hỗ trợ mọi môn và mọi chương trình.
- Tự động publish không cần giáo viên duyệt.

Cổng quyết định:

- 100% quiz item truy được tới nội dung đã dạy và nguồn.
- 100% claim cốt lõi có provenance hoặc được đánh dấu thiếu bằng chứng.
- Không có cảnh báo nghiêm trọng bị ẩn khi xuất bản.
- Giáo viên dùng được đầu ra sau một vòng sửa có kiểm soát.
- Thao tác “Tìm trong nguồn” mở đúng vị trí bằng chứng và không đưa nội dung
  ngoài tập nguồn đã chọn mà không gắn cảnh báo rõ ràng.

Hai chỉ tiêu 100% ở trên chỉ đo tuân thủ quy trình truy nguồn, không chứng minh
chất lượng giáo dục. Quyết định mở rộng MVP còn phải dựa vào thời gian giáo viên
cần để có bản dùng được, tỷ lệ phải viết lại, mức đồng thuận giữa người chấm và
kết quả học tập quan sát được.

### Giai đoạn 2 — Community Knowledge Packs

**Mục tiêu:** tạo tài sản cộng đồng mà công cụ đóng khó thay thế.

Phạm vi:

- Curriculum pack cho use case đã chọn.
- Registry nguồn đáng tin cậy theo lĩnh vực.
- Rubric, benchmark và template mở.
- Metadata giấy phép và trạng thái review.
- Workflow fork/review/merge.
- Theo dõi thay đổi nguồn và impact analysis.
- Import/export package không cần server trung tâm.

Cổng quyết định:

- Có contributor ngoài nhóm lõi.
- Có tài nguyên đạt `Teacher-reviewed` và `Classroom-tested`.
- Một nguồn thay đổi có thể chỉ ra đúng artifact cần kiểm tra lại.

Sau thử nghiệm khám phá, nghiên cứu phải mở rộng dần theo môn, cấp học, vùng
miền và điều kiện thiết bị. Quan sát hành vi sử dụng thực tế quan trọng hơn câu
trả lời khảo sát “có thích sản phẩm hay không”. Chỉ dùng cụm từ “phục vụ giáo
viên toàn quốc” như phạm vi thiết kế cho đến khi có mẫu kiểm chứng đủ rộng.

### Giai đoạn 3 — Open Ecosystem

**Mục tiêu:** mở rộng mà vẫn giữ tính portable.

Phạm vi:

- Plugin provider AI.
- Plugin nhập nguồn/OCR/transcript.
- Plugin xuất QTI, Moodle và các LMS phổ biến.
- Đồng bộ Git tùy chọn qua UI.
- Chia sẻ phân tán hoặc catalog chỉ lưu metadata.
- Plugin audio/video/infographic khi cộng đồng có nhu cầu thật.
- Desktop packaging và offline installation ổn định.

## 13. Ba luồng ưu tiên

### 13.1 Kiểm chứng sản phẩm

1. Bài mẫu thủ công.
2. Rule set và rubric có ví dụ đạt/chưa đạt.
3. Prototype giao diện duyệt dùng bốn nhóm đầu ra.
4. Thử độc lập với giáo viên và sửa quy trình.
5. Đo thời gian, mức viết lại, cảnh báo và kết quả học tập pilot.

### 13.2 Kỹ thuật MVP

1. Schema tối thiểu được rút ra từ bài mẫu, không thiết kế trước quá mức.
2. Nhập nguồn và định vị bằng chứng.
3. Tạo bài theo chặng với structured output.
4. Kiểm định theo quy tắc và rubric.
5. Prototype review/diff/lock phát triển song song với schema.
6. Xuất DOCX, PPTX và PDF.

### 13.3 Mở rộng sau cổng MVP

1. LMS và định dạng trao đổi.
2. Curriculum/community packs.
3. Provider/plugin ecosystem.
4. Audio, video và media phức tạp nếu có nhu cầu thật.

Backlog không cho phép ưu tiên plugin, provider mới hoặc media trước khi bài mẫu
và thử nghiệm giáo viên đạt cổng quyết định.

## 14. Chỉ số thành công

Các thuật ngữ dùng để nghiệm thu và cách lưu bằng chứng được định nghĩa tại
`doc/02-pilot/acceptance-glossary.md`. Kế hoạch đo hiệu quả ban đầu của pilot nằm tại
`doc/02-pilot/pilot-measurement-plan.md`.

### Chất lượng

- Tỷ lệ claim cốt lõi có provenance.
- Tỷ lệ quiz item map đúng mục tiêu và nội dung đã dạy.
- Số lỗi nguồn/sư phạm phát hiện trước khi giáo viên duyệt.
- Tỷ lệ cảnh báo đúng và cảnh báo giả.
- Mức độ giáo viên phải viết lại đầu ra.
- Mức đồng thuận giữa hai giáo viên đánh giá độc lập.
- Mức độ học sinh hoàn thành mục tiêu, ghi nhớ, vận dụng và sửa quan niệm sai.

### Hiệu quả người dùng

- Thời gian từ nguồn đến bản dạy được.
- Số vòng chỉnh sửa.
- Tỷ lệ artifact được sử dụng thật.
- Tỷ lệ bài được tái sử dụng hoặc cập nhật thay vì tạo lại.
- Tỷ lệ giáo viên hoàn thành tác vụ mà không cần hỗ trợ kỹ thuật.
- Chênh lệch hiệu quả giữa môn, cấp học, vùng miền và điều kiện thiết bị.

### Sức khỏe cộng đồng

- Số curriculum/source/rubric pack được đóng góp.
- Số contributor và reviewer hoạt động.
- Tỷ lệ tài nguyên có giấy phép rõ ràng.
- Số tài nguyên đạt `Teacher-reviewed` hoặc `Classroom-tested`.

## 15. Rủi ro chính và cách giảm

| Rủi ro | Cách giảm |
|---|---|
| Cố sao chép mọi tính năng NotebookLM | Giữ MVP tập trung vào provenance, pedagogy và eval |
| Local-first quá khó dùng | Git chạy phía sau; cung cấp UI và installer thân thiện |
| Điểm tin cậy nguồn gây hiểu nhầm | Hiển thị nhiều chiều, bằng chứng và trạng thái thay vì một điểm “đúng” |
| LLM judge tự tin sai | Kết hợp deterministic checks, nhiều rubric và giáo viên duyệt |
| Kho cộng đồng đầy nội dung AI chất lượng thấp | Chia trạng thái review, bắt buộc provenance/eval/license |
| Chi phí hỗ trợ nhiều provider | Chuẩn hóa interface; chỉ chứng nhận provider đã qua benchmark |
| Dữ liệu học sinh rời máy | Local default, redact, consent và outbound preview |
| Schema đổi liên tục | Version schema, migration tool và compatibility tests |
| Nguồn có prompt injection | Tách nguồn khỏi instruction, sanitize và kiểm tra hành vi agent |
| Tuyên bố toàn quốc quá sớm | Tách tầm nhìn toàn quốc khỏi phạm vi pilot; mở rộng mẫu theo từng vòng kiểm chứng |
| OCR hoặc bản quét làm sai trích dẫn | Chấm chất lượng OCR, giữ ảnh trang gốc và yêu cầu duyệt khi độ tin cậy thấp |
| Vi phạm bản quyền khi chia sẻ | Tách sử dụng nội bộ khỏi tái phân phối; chia sẻ metadata/link khi giấy phép chưa rõ |

## 16. Câu hỏi cần nghiên cứu tiếp

### Nhu cầu người dùng

- Giáo viên mất thời gian nhất ở dàn ý, tạo học liệu hay kiểm tra chất lượng?
- Họ tin và kiểm tra nguồn hiện nay bằng cách nào?
- Artifact nào được dùng thật: giáo án, slide, worksheet, quiz hay rubric?
- Họ sẵn sàng duyệt những bước nào, bước nào tạo quá nhiều ma sát?
- Bao nhiêu tác vụ thực tế chỉ cần tra cứu/trích dẫn thay vì tạo trọn bộ bài?
- Nhu cầu khác nhau thế nào giữa các môn, cấp học, địa phương và điều kiện mạng?

### Nguồn và độ tin cậy

- Metadata nào có thể lấy tự động cho từng loại nguồn?
- Làm sao nhận biết hai nguồn không độc lập do sao chép?
- Claim nào bắt buộc hai nguồn, claim nào chỉ cần một nguồn chính thống?
- Chính sách freshness cần khác nhau thế nào theo lĩnh vực?

### Kiểm định

- Những lỗi nào deterministic rule bắt được tốt hơn LLM?
- Rubric nào có độ đồng thuận cao giữa giáo viên?
- Benchmark tiếng Việt cần bao nhiêu môn và loại lỗi để có ý nghĩa?
- Làm sao đo false positive của Source Trust Engine?

### Định dạng và tương thích

- Canonical format nên dùng Markdown + YAML/JSON hay một document AST chung?
- Mức fidelity tối thiểu khi xuất DOCX/PPTX là gì?
- Nên ưu tiên QTI hay Moodle XML trong MVP kế tiếp?
- Package cần chữ ký số hoặc content-addressed ID ở giai đoạn nào?

### Cộng đồng và quản trị

- Ai được gắn nhãn `Teacher-reviewed` và `Classroom-tested`?
- Quy trình giải quyết nguồn mâu thuẫn hoặc nội dung bị báo sai?
- Giấy phép mặc định cho template, curriculum metadata và bài học là gì?
- Catalog nên hoàn toàn phân tán hay có một registry metadata tùy chọn?

## 17. Bước tiếp theo đề xuất

Thứ tự cũ dựa vào khả năng mời giáo viên thẩm định trước khi xây. Điều kiện đó
hiện không khả dụng, nên chuyển sang ba milestone kỹ thuật trong
[`plan-xay-dung-he-sinh-thai.md`](plan-xay-dung-he-sinh-thai.md):

1. Chốt Open Lesson Package schema v0.1 và test contract xuyên ba repo.
2. Xây source workspace, provenance và citation resolver.
3. Xây generation vertical slice nhiều artifact cùng quality gate kỹ thuật.
4. Chỉ sau đó chọn thứ tự UI và exporter dựa trên độ ổn định của schema.
5. Giữ thẩm định giáo viên/classroom pilot ở backlog `parked — external
   validation unavailable`; mở lại khi có nguồn lực, không dùng AI mô phỏng để
   thay thế bằng chứng này.

## 18. Tiêu chí giữ hướng sản phẩm

Trước mỗi tính năng mới, trả lời ba câu hỏi:

1. Nó có giúp người dùng sở hữu và di chuyển dữ liệu dễ hơn không?
2. Nó có làm bài học đáng tin, dễ kiểm định hoặc dễ bảo trì hơn không?
3. Nó có tạo tài sản mở mà cộng đồng có thể tái sử dụng không?

Nếu cả ba câu trả lời đều là “không”, tính năng đó có khả năng chỉ đang sao
chép một nền tảng đóng và không nên được ưu tiên.
