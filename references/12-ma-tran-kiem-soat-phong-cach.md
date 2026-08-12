# Ma trận kiểm soát phong cách

Dùng ma trận này trước khi viết để vừa giữ chuẩn kỹ thuật, vừa học có giới hạn từ cách viết của người
dùng. Đây là hợp đồng điều khiển, không phải một template cứng áp cho mọi artifact.

## 1. Bốn trục kiểm soát

| Trục | Phải khóa | Cổng kiểm tra | Khi làm quá |
|---|---|---|---|
| Mục đích & đối tượng | `audience`, trình độ, `purpose`, việc người đọc phải làm được | Mọi section phục vụ đúng người đọc và công việc | Quá hẹp, khó tái sử dụng |
| Cấu trúc & định dạng | profile artifact, block bắt buộc, heading, bảng/danh sách/công thức | Không có cấu trúc hội thoại ngoài artifact cần đối thoại | Template cứng, mất mạch tự nhiên |
| Giọng văn & từ vựng | technical baseline + user style layer + negative constraints | Giọng đúng artifact, thuật ngữ nhất quán, không giả người | Học quá mạnh, quay về giọng chat/cá nhân |
| Độ chính xác & dữ liệu | glossary, nguồn, claim, assumption, semantic inventory | Claim truy nguồn hoặc có nhãn giả định | Quá nhiều cảnh báo làm tài liệu nặng |

## 2. Hai lớp phong cách

### 2.1 Technical Baseline — lớp cứng

Baseline thay đổi theo artifact nhưng luôn giữ các điều sau:

- câu hoàn chỉnh, chủ thể rõ và quan hệ logic gần nhau;
- thuật ngữ có một tên chính; biến thể chỉ dùng khi đã khai báo;
- claim có nguồn hoặc nhãn `giả định`, `minh họa`, `chưa xác minh`;
- không bịa số liệu, trải nghiệm, người xác nhận hoặc mức độ chắc chắn;
- không dùng chat filler, lời dẫn meta hay câu hỏi–đáp giả nếu artifact không cần;
- không để style layer sửa code, URL, công thức, citation, đơn vị và điều kiện biên.

Không mặc định ưu tiên câu bị động. Chọn chủ động khi cần làm rõ ai thực hiện hành động; dùng bị động
khi tác nhân không quan trọng hoặc chưa biết.

### 2.2 User Style Layer — lớp mềm

Chỉ học những đặc điểm có thể quan sát và chuyển giao an toàn:

- thuật ngữ chuyên ngành ưa dùng và cách giải nghĩa lần đầu;
- độ dài câu/đoạn, nhịp chuyển ý và mật độ ví dụ;
- thứ tự ưu tiên thông tin và cách tổ chức lập luận;
- mức trang trọng, cách xưng hô, mức dùng bảng/danh sách/công thức;
- kiểu câu chốt, với điều kiện không biến thành câu cửa miệng lặp lại.

Không học từ mẫu người dùng:

- claim hoặc số liệu chưa kiểm chứng;
- lỗi chính tả, lỗi logic và thuật ngữ dùng không nhất quán;
- dữ liệu cá nhân, ký ức, thành tích hoặc quan hệ;
- cách nói có thể khiến đầu ra bị hiểu là do một người thật xác nhận;
- cấu trúc chat nếu mục tiêu là tài liệu kỹ thuật hoặc học liệu độc lập.

## 3. Cấu trúc theo artifact, không theo một template duy nhất

Không bắt mọi tài liệu phải có Mục lục → Phạm vi → Thuật ngữ → Kết luận → Phụ lục. Chọn block theo
công việc:

- **Đặc tả kỹ thuật**: phạm vi → định nghĩa → yêu cầu/ràng buộc → thiết kế → rủi ro → kiểm chứng →
  phụ lục.
- **Hướng dẫn thao tác**: mục tiêu → điều kiện trước → bước làm → kết quả mong đợi → xử lý lỗi → tự
  kiểm.
- **Báo cáo/phân tích**: câu hỏi → dữ liệu/phương pháp → phát hiện → giới hạn → khuyến nghị.
- **Bài học nhập môn**: vấn đề → mô hình tinh thần → cơ chế → ví dụ → bẫy → tự kiểm → nguồn.
- **Giáo án/worksheet/quiz**: dùng cấu trúc trong `06-profile-theo-artifact.md`.

Mục lục chỉ bắt buộc khi chiều dài và nhu cầu tra cứu biện minh cho nó. Glossary có thể là section,
sidebar hoặc giải nghĩa tại chỗ; không tạo bảng thuật ngữ chỉ để đủ template.

## 4. Negative constraints theo ngữ cảnh

Không dùng danh sách từ cấm toàn cục. Mỗi style contract ghi các mẫu phải tránh và lý do. Baseline
cho tài liệu kỹ thuật độc lập thường tránh:

- “trong phần này, chúng ta sẽ…”;
- “hãy cùng khám phá”, “hãy thử xem” khi không có thao tác thật;
- “vô cùng quan trọng”, “đóng vai trò then chốt” khi thiếu tiêu chí;
- câu hỏi tu từ rồi tự trả lời liên tiếp;
- đại từ “bạn/chúng ta” khi không cần chỉ dẫn hoặc thiết lập quan hệ sư phạm.

Không cấm “bạn hãy” trong worksheet hoặc hướng dẫn thao tác nếu nó giúp xác định rõ người thực hiện.
Đánh giá chức năng của câu, không đếm từ khóa máy móc.

## 5. Few-shot có kiểm soát

Chỉ kích hoạt `own-voice` khi có đủ mẫu đại diện:

1. Dùng 3–5 mẫu do người dùng cung cấp hoặc sở hữu; gắn loại artifact và bối cảnh cho từng mẫu.
2. Chọn 2–3 đoạn tốt để trích đặc trưng; chọn 1–2 đoạn không muốn lặp lại và ghi lỗi cụ thể.
3. Không đưa toàn văn mẫu vào prompt nếu một style card đã đủ.
4. Tạo profile tạm ở mức `low` khi chỉ có một mẫu; không suy rộng thành sở thích toàn cục.
5. So đầu ra với đặc trưng, không so chuỗi câu; tránh sao chép cụm từ đặc trưng dài.

## 6. Style Card

Dùng mẫu `assets/mau-style-card.yaml`. Mỗi card phải có provenance và confidence. Chỉ lưu khi người
dùng yêu cầu hoặc xác nhận; nếu không, giữ nó trong phạm vi tác vụ hiện tại.

Các trường tối thiểu:

- `audience`, `purpose`, `artifact`;
- `register`, `address`, `sentence_length`, `paragraph_rhythm`;
- `preferred_terms`, `avoid_terms`, `preferred_moves`, `avoid_moves`;
- mức dùng `tables`, `lists`, `formulas`, `questions`;
- `evidence_basis`, `confidence`, `scope`.

## 7. Checklist hậu sinh

Agent tự sửa trước khi bàn giao nếu một câu trả lời là “không”:

- Audience và purpose có được thể hiện bằng lựa chọn nội dung, không chỉ ghi trong metadata?
- Heading có phân cấp đúng và block có đúng profile artifact?
- Có đoạn nào đang dùng giọng hội thoại hoặc đại từ không phục vụ chức năng?
- Một thuật ngữ có bị gọi bằng nhiều tên mà chưa khai báo không?
- Mọi claim quan trọng có nguồn hoặc nhãn giả định phù hợp không?
- Style layer có làm thay đổi số liệu, code, công thức, citation hay mức chắc chắn không?
- Các câu chuyển ý có mô tả quan hệ logic thay vì kể “tiếp theo sẽ nói gì” không?
- Bảng, danh sách và công thức có được dùng vì giúp hiểu/tra cứu, không phải vì style card yêu cầu?
- Có câu nào bắt chước lỗi, trải nghiệm cá nhân hoặc giọng chat từ mẫu không?
- Đầu ra vẫn đọc tự nhiên khi bỏ metadata và heading hay không?

Nếu baseline và user style layer xung đột, giữ baseline và ghi nhận đặc điểm phong cách không được áp
dụng. Không âm thầm làm yếu chuẩn kỹ thuật để tăng độ giống mẫu.
