# Giới thiệu dành cho giáo viên

**Trạng thái hiện tại:** Ý tưởng và bộ khung thử nghiệm, chưa phải sản phẩm sẵn
sàng triển khai trong trường học.

## Sản phẩm này nhằm giải quyết việc gì?

Giáo viên thường có nhiều tài liệu: sách giáo khoa, văn bản chương trình, tài
liệu tập huấn, giáo trình, bài báo, website, bài trình chiếu hoặc video. Việc
tìm đúng thông tin, kiểm tra nguồn và chuyển chúng thành một bài dạy nhất quán
tốn nhiều thời gian.

Dự án hướng tới một công cụ giúp giáo viên trên toàn quốc sử dụng AI với chính
những nguồn mình lựa chọn để **soạn bài có căn cứ**. Trong lúc lập dàn ý, viết
nội dung hoặc tạo câu hỏi, giáo viên có thể tìm một định nghĩa, số liệu, quy
định hoặc trích dẫn và mở lại đúng vị trí nguồn để kiểm tra.

Trong phiên bản thử nghiệm đầu tiên, tra cứu và trích dẫn là thao tác hỗ trợ bên
trong quy trình soạn bài, không phải một ứng dụng hỏi đáp tài liệu độc lập như
NotebookLM.

## Khác gì với việc hỏi một chatbot thông thường?

Chatbot thông thường có thể trả lời trôi chảy nhưng người dùng khó biết thông
tin đến từ đâu, có nằm trong tài liệu đã chọn hay không và có phù hợp với mục
tiêu bài học không.

Công cụ này được thiết kế theo các nguyên tắc:

- Chỉ sử dụng tập nguồn giáo viên đã chọn, trừ khi giáo viên cho phép tìm thêm.
- Kiến thức quan trọng phải chỉ ra được tài liệu và vị trí hỗ trợ.
- Khi nguồn không đủ hoặc mâu thuẫn, hệ thống phải báo thay vì tự suy đoán.
- AI đề xuất; giáo viên phê duyệt cuối cùng.
- Bài đã tạo có thể tải xuống, sửa bằng công cụ quen thuộc và tiếp tục sử dụng
  khi không còn dịch vụ AI.

## Giáo viên sẽ sử dụng như thế nào?

### Tìm trong nguồn khi đang soạn

1. Giáo viên thêm PDF, Word, PowerPoint, đường dẫn website hoặc nguồn được hỗ
   trợ khác.
2. Giáo viên chọn những nguồn được phép dùng cho câu hỏi hiện tại.
3. Giáo viên đặt câu hỏi bằng tiếng Việt.
4. Hệ thống trả lời kèm tên tài liệu, số trang, đoạn hoặc vị trí tương ứng.
5. Giáo viên mở bằng chứng gốc, kiểm tra và chọn cách trích dẫn phù hợp.

Nếu tài liệu là bản quét khó đọc, thiếu trang hoặc có bảng/hình mà hệ thống
không nhận dạng chắc chắn, công cụ phải đưa cảnh báo.

### Soạn bài từ nguồn

Quy trình dự kiến:

```text
Mục tiêu học tập
    ↓
Nguồn và kiến thức học sinh cần biết trước
    ↓
Dàn ý bài học
    ↓
Hoạt động dạy và học
    ↓
Luyện tập
    ↓
Đánh giá
    ↓
Giáo viên kiểm tra và phê duyệt
```

Trước khi AI viết toàn bộ bài, giáo viên được xem một bảng liên kết:

| Mục tiêu | Nội dung sẽ dạy | Hoạt động luyện tập | Cách đánh giá |
|---|---|---|---|
| Giải thích được khái niệm | Định nghĩa và ví dụ | Phân loại ví dụ | Câu hỏi giải thích |
| Vận dụng vào tình huống mới | Các bước thực hiện | Bài tập tình huống | Bài vận dụng |

Nếu một mục tiêu chưa có phần dạy, luyện hoặc đánh giá tương ứng, hệ thống phải
báo để giáo viên sửa trước khi tiếp tục.

Một ví dụ đầy đủ từ mục tiêu, nguồn, kế hoạch bài dạy, học liệu, bài kiểm tra đến
báo cáo cảnh báo nằm tại
[`pilot-vat-li-10-co-nang-v0.1/`](../02-pilot/pilot-vat-li-10-co-nang-v0.1/README.md).
Ví dụ này là package thủ công chưa thử trong lớp, không phải giáo án mẫu chính
thức.

## Có thể biết nguồn giáo viên chọn là đúng không?

Không có công cụ AI nào bảo đảm một nguồn đúng tuyệt đối. Nguồn chính thống vẫn
có thể cũ, không phù hợp với cấp học hoặc bị dùng sai phạm vi. Công cụ chỉ có
thể giúp giáo viên nhìn rõ bằng chứng và rủi ro.

Mỗi nguồn cần được xem xét theo nhiều tiêu chí:

- Ai là tác giả hoặc cơ quan phát hành?
- Tài liệu được ban hành khi nào và còn hiệu lực không?
- Đây có phải tài liệu gốc không?
- Nội dung có phù hợp môn, lớp và phạm vi sử dụng không?
- Có nguồn nào nói khác không?
- Bản quét có thiếu trang hoặc nhận dạng sai chữ không?
- Giáo viên có quyền sử dụng, trích dẫn hoặc chia sẻ tài liệu không?

Hệ thống không nên hiển thị một con số như “nguồn đúng 87%”. Thay vào đó, nó
nên dùng các trạng thái dễ hiểu:

- Được nguồn có thẩm quyền hỗ trợ.
- Có nhiều nguồn độc lập cùng hỗ trợ.
- Chỉ có một nguồn.
- Các nguồn đang mâu thuẫn.
- Nguồn có thể đã cũ hoặc sai phạm vi.
- Chưa đủ bằng chứng.
- Cần người có chuyên môn quyết định.

Một văn bản chương trình hoặc quy định còn hiệu lực có thể chỉ cần một nguồn
chính thức. Một kết luận nghiên cứu hoặc vấn đề có tranh luận có thể cần nhiều
nguồn. Quy tắc kiểm tra phải thay đổi theo môn và loại kiến thức.

## Nội dung nào cần truy về nguồn?

Không cần gắn nguồn cho từng câu chuyển ý vì điều đó làm tăng gánh nặng không
cần thiết.

**Bắt buộc kiểm tra nguồn:**

- Định nghĩa và kiến thức cốt lõi.
- Số liệu, sự kiện và quy định.
- Nội dung dễ gây hậu quả nếu sai.
- Câu hỏi, đáp án và phần giải thích đáp án.

**Nên kiểm tra nguồn:**

- Diễn giải học thuật.
- Ví dụ thực tế.
- Nội dung dễ gây tranh luận.

**Không cần truy từng câu:**

- Lời dẫn và câu chuyển ý.
- Hướng dẫn thao tác do giáo viên tạo.
- Cách chia nhóm và tổ chức hoạt động.

## Giáo viên nhìn thấy những sản phẩm gì?

Mặc dù hệ thống cần lưu nhiều thông tin kỹ thuật để kiểm tra và cập nhật bài,
giao diện giáo viên chỉ nên có bốn nhóm:

1. **Kế hoạch bài dạy.**
2. **Học liệu dành cho học sinh.**
3. **Kiểm tra, đáp án và tiêu chí đánh giá.**
4. **Nguồn, chất lượng và cảnh báo.**

Giáo viên không phải sửa các tệp kỹ thuật hoặc dùng dòng lệnh. Có thể tải đầu
ra dưới dạng Word, PowerPoint hoặc PDF và tiếp tục chỉnh sửa bình thường.

## Các mức độ đã được thẩm định

Một bài cần ghi rõ trạng thái:

- **Bản nháp:** đang được soạn.
- **Do AI tạo, chưa duyệt:** không nên sử dụng ngay.
- **Đã kiểm tra nguồn:** các nội dung bắt buộc đã được đối chiếu.
- **Đã được giáo viên duyệt:** một giáo viên đã xem và chấp nhận.
- **Đã được tổ chuyên môn duyệt:** có đồng nghiệp hoặc tổ chuyên môn xem xét.
- **Đã thử nghiệm trong lớp:** đã có sử dụng thực tế và ghi nhận kết quả.

“Đã được giáo viên duyệt” không đồng nghĩa với “đã chứng minh có hiệu quả trong
lớp học”.

## Dữ liệu và quyền riêng tư

Thiết kế ưu tiên lưu dữ liệu trên máy của người dùng. Khi cần dùng một dịch vụ
AI trên Internet, giáo viên phải được xem trước dữ liệu nào sẽ rời khỏi máy và
gửi tới đâu. Hệ thống cần phát hiện tên học sinh, email, mã số và thông tin liên
hệ trước khi gửi.

Lưu trên máy không tự động có nghĩa là an toàn. Máy dùng chung, mất máy, sao lưu
không bảo vệ hoặc chia sẻ nhầm tệp vẫn có thể làm lộ dữ liệu. Phiên bản hoàn
chỉnh phải có hướng dẫn và cơ chế bảo vệ phù hợp.

## Bản quyền và chia sẻ

Việc tải được một tài liệu không có nghĩa là được phép phát hành lại. Công cụ
phải phân biệt:

- Dùng tài liệu để soạn bài nội bộ.
- Trích dẫn một phần trong bài dạy.
- Đóng gói và chia sẻ công khai nội dung nguồn.

Nếu giấy phép chưa rõ, bản chia sẻ chỉ nên chứa thông tin nguồn và đường dẫn,
không tự động kèm toàn bộ tài liệu gốc.

## Phạm vi toàn quốc và cách thử nghiệm

Tầm nhìn là phục vụ giáo viên trên toàn quốc, nhưng sản phẩm không thể tuyên bố
phù hợp mọi môn và mọi cấp học ngay từ đầu. Giai đoạn thử nghiệm sẽ chọn một
môn, một lớp và một bài cụ thể để kiểm tra đầy đủ quy trình. Sau đó mới mở rộng
theo:

- Môn và cấp học.
- Khu vực và điều kiện thiết bị.
- Giáo viên có mức kinh nghiệm khác nhau.
- Nhu cầu tra cứu, trích dẫn và soạn bài khác nhau.
- Học sinh và bối cảnh lớp học khác nhau.

Thành công không được đo bằng số lượng bài AI tạo ra. Điều cần đo là thời gian
giáo viên tiết kiệm được, phần nội dung phải sửa lại, số cảnh báo đúng/sai, mức
đồng thuận giữa giáo viên và khả năng học sinh đạt mục tiêu bài học.

## Trạng thái dự án

Hiện dự án mới có tầm nhìn, tài liệu kiến trúc và bộ khung kỹ thuật ban đầu.
Luồng đọc/ghi tệp đã được thử ở mức kỹ thuật, nhưng chưa có bằng chứng rằng hệ
thống tạo được bài chất lượng, chưa được giáo viên sử dụng đầy đủ và chưa thử
nghiệm trong lớp học. Đây là những bước bắt buộc trước khi có thể triển khai
rộng rãi.
