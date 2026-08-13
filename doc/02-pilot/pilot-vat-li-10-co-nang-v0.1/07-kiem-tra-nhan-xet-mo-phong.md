# 7. Kiểm tra nhận xét của hai giáo viên mô phỏng

**Ngày kiểm tra:** 2026-08-11  
**Đối tượng:** [06-nhan-xet-hai-giao-vien-mo-phong.md](06-nhan-xet-hai-giao-vien-mo-phong.md)

## Kết luận

Bản mô phỏng có ích để tìm vấn đề và chuẩn bị rubric cho giáo viên thật, nhưng
không phải bằng chứng thẩm định bên ngoài. Không dùng kết quả này để gắn
`Teacher-reviewed`, `Peer-reviewed` hoặc xác nhận package đã vượt cổng chất
lượng.

Các phát hiện về tiến trình 45 phút, câu hỏi, hướng dẫn PhET và phương án không
mạng đủ cụ thể để đưa vào backlog sửa v0.2. Hai fixture chưa được kiểm thử mù,
vì reviewer được đọc những tệp đã chỉ rõ vị trí, trạng thái và lý do phải chặn.

## Điểm làm tốt

- Nêu rõ đây là hai tác nhân AI đóng vai, không thay thế giáo viên thật.
- Hai persona khác nhau về kinh nghiệm, điều kiện lớp học và mức quen công nghệ.
- Lưu riêng điểm chấm, lý do, phần hội tụ và phần bất đồng.
- Các nhận xét quan trọng có vị trí cụ thể và phần lớn chuyển được thành việc sửa.
- Không tự nâng trạng thái package sau vòng mô phỏng.

## Hạn chế phương pháp phải ghi nhận

### 1. Fixture bị lộ trước khi chấm

Reviewer được đọc:

- `README.md`, nơi mô tả cả hai lỗi cài sẵn;
- `03-kiem-tra-dap-an-rubric.md`, nơi Câu 8 đã mang nhãn `REJECT — UNTaught` và
  có lời giải thích;
- `04-bao-cao-nguon-chat-luong.md`, nơi F1 đã có kết luận và lý do;
- `05-quy-tac-su-pham-pilot.md`, nơi có ví dụ đạt/chưa đạt gần trùng fixture.

Vì vậy không thể kết luận mục đích số 4 trong README — “phát hiện lỗi nguồn và
câu hỏi vượt ngoài nội dung đã dạy” — đã đạt. Kết quả hiện tại chỉ cho thấy hai
tác nhân có thể nhận lại và giải thích lỗi đã được công bố.

### 2. Chưa đủ bằng chứng về tính độc lập và thời gian

Tệp tổng hợp không lưu prompt, đầu vào chính xác, bản trả lời thô, thời điểm bắt
đầu/kết thúc hoặc cơ chế ngăn hai tác nhân nhìn kết quả của nhau. Các con số
100–230 phút là ước tính theo persona, không phải thời gian quan sát được. Không
dùng chúng làm baseline về gánh nặng của giáo viên.

### 3. Persona có thể bị hiểu nhầm là người thật

Tên cá nhân và trường cụ thể nghe như danh tính thật. Nên đổi thành `Persona AI
A — giáo viên giàu kinh nghiệm, trường đô thị` và `Persona AI B — giáo viên mới,
trường điều kiện thiết bị hạn chế`; hoặc ghi nổi bật rằng mọi tên/trường đều hư
cấu. Không trích dẫn hai persona như ý kiến của trường hay giáo viên có thật.

### 4. Một đề xuất Vật lí cần loại bỏ

Đề xuất “mọi ngoại lực sinh công khác 0 đều làm cơ năng không bảo toàn” quá
rộng và dễ tạo quan niệm sai. Trọng lực có thể sinh công nhưng, khi thế năng
trọng trường đã được đưa vào cơ năng của hệ phù hợp, cơ năng vẫn có thể bảo
toàn. Câu chốt nên bám phạm vi của bài:

> Cơ năng của hệ được bảo toàn khi chỉ có các lực thế thực hiện công; nếu lực
> không bảo toàn như ma sát thực hiện công thì cơ năng có thể thay đổi.

Việc xác định lực “ngoại lực” còn phụ thuộc cách chọn hệ, nên không dùng từ này
như một quy tắc tuyệt đối trong tiết pilot.

### 5. Một số nhận xét vẫn cần xác minh thực địa

- Khung giáo án trường đang áp dụng là yêu cầu theo từng đơn vị, không nên biến
  thành yêu cầu chung cho toàn quốc từ một persona.
- Khả năng dùng PhET ngoại tuyến, ngôn ngữ giao diện và quy trình tải phải được
  kiểm tra trên thiết bị/mạng thật trước khi viết hướng dẫn.
- Khả thi trong 45 phút, cách thu bài ở lớp đông và thời gian chuẩn bị chỉ có thể
  xác nhận qua giáo viên thật và dạy thử.

## Backlog v0.2 rút ra được từ mô phỏng

### P0 — sửa trước khi gửi giáo viên thật

1. Chốt Phần C, Phần D và Quiz câu 4–7 làm ở phút nào hoặc giao về nhà.
2. Đổi Câu 3 và Câu 6 thành “tại vị trí chọn làm mốc thế năng (`Wt = 0`)”.
3. Thay hai phương án nhiễu về “khối lượng” bằng lỗi tư duy có khả năng xảy ra.
4. Tạo bộ biểu đồ giấy dự phòng có số liệu/tỉ lệ, nhãn chữ và đáp án.
5. Thêm hướng dẫn PhET tối thiểu cho trình chiếu chung; ghi rõ phương án không
   mạng/không máy chiếu.
6. Tách bản phát học sinh khỏi fixture và thêm bước kiểm tra tự động/thủ công để
   F1, Câu 8 không lọt sang bản phát hành.
7. Không đưa câu “mọi ngoại lực sinh công...” vào bài; dùng phát biểu theo lực
   thế/lực không bảo toàn và nêu rõ hệ đang xét.

### P1 — kiểm tra với giáo viên thật

1. Thời lượng chuẩn bị và khả thi của tiến trình 45 phút ở lớp khoảng 35 học
   sinh và lớp trên 45 học sinh.
2. Thuật ngữ nào phải Việt hóa hoặc đưa vào phụ lục kỹ thuật.
3. Mức cần thiết của bản chuyển đổi sang mẫu kế hoạch bài dạy tại từng trường.
4. Hình thức thu bằng chứng học tập khả thi mà không tăng tải chấm quá mức.

## Thiết kế vòng thẩm định mù tiếp theo

Chuẩn bị ba gói tách biệt:

1. **Gói reviewer:** kế hoạch, học liệu học sinh, câu hỏi chưa có đáp án/nhãn
   fixture, báo cáo nguồn chỉ chứa claim và trích dẫn cần kiểm tra, rubric trung
   tính.
2. **Khóa đáp án:** vị trí fixture, đáp án, mức nghiêm trọng và tiêu chí pass;
   người điều phối giữ, reviewer không được đọc trước khi nộp bản độc lập.
3. **Gói audit:** prompt, phiên bản/hash các tệp đầu vào, bản trả lời thô, thời
   gian thực tế, thay đổi sau review và kết quả đối thoại.

Hai giáo viên thật phải nộp rubric riêng trước khi nhận khóa đáp án hoặc xem bản
của người kia. Chỉ sau đó mới đối chiếu bất đồng và quyết định sửa.

## Trạng thái sau kiểm tra

- `Rà soát nội bộ bằng AI`: đã có, dùng để lập backlog.
- `Teacher-reviewed`: chưa đạt.
- `Peer-reviewed`: chưa đạt.
- `Classroom-tested`: chưa đạt.

