# Chống văn AI tiếng Việt mà không làm mỏng nội dung

Chỉ dùng tài liệu này **sau** khi bản đồ chiều sâu đã đạt và artifact đã đúng chức năng. Đây là
lượt biên tập, không phải công cụ tạo thêm sự thật hay “làm màu” cho một bản nháp thiếu ý.

## 1. Chẩn đoán trước khi sửa

Đánh dấu từng vấn đề cụ thể thay vì viết lại toàn bài theo cảm giác:

- **Rỗng**: câu đúng ngữ pháp nhưng không cho biết chủ thể, cơ chế, điều kiện hoặc hệ quả.
- **Lặp**: nhiều câu diễn đạt cùng một ý bằng từ khác.
- **Rập khuôn**: mở mục giống nhau, bộ ba liệt kê đều đặn, câu nào cũng chốt một kết luận tròn trịa.
- **Khoa trương**: “vô cùng quan trọng”, “đóng vai trò then chốt”, “mang lại hiệu quả cao” mà
  không có tiêu chí.
- **Giọng dịch**: danh từ hóa nặng, nhiều “nhằm”, “thông qua việc”, “một cách”.
- **Giả người**: bịa trải nghiệm cá nhân, cố nhét “nhé/đấy/mà” hoặc câu đùa không hợp ngữ cảnh.
- **Phẳng**: câu nào cũng có cùng trọng lượng; mọi mục đều mở bằng định nghĩa và kết bằng callout.
- **Đứt mạch**: đoạn sau đúng nhưng không trả lời, mở rộng hoặc làm khó thêm điều đoạn trước đặt ra.
- **Làm dáng**: dùng ẩn dụ, đối câu hoặc khẩu hiệu nơi một câu giải thích trực tiếp sẽ rõ hơn.
- **Lủng củng**: chủ thể xuất hiện muộn, một câu gánh nhiều quan hệ, hoặc đại từ không rõ đang chỉ gì.

Nếu vấn đề thật sự là thiếu cơ chế, ví dụ hay ranh giới, quay lại `05-lap-ke-hoach-chieu-sau.md`.

## 2. Sửa theo thứ tự

1. Cắt câu lặp và đoạn meta kiểu “trong phần này, chúng ta sẽ tìm hiểu…”.
2. Thay động từ trừu tượng bằng hành động có chủ thể và kết quả quan sát được.
3. Đưa nguyên nhân đứng gần kết quả; đưa điều kiện đứng gần khẳng định mà nó giới hạn.
4. Thay ví dụ chung chung bằng một tình huống có dữ kiện, thao tác và kết quả.
5. Viết lại câu đầu và câu cuối của mỗi phần để chúng nối với phần trước/sau. Đừng dùng tiêu đề làm
   chiếc cầu duy nhất.
6. Đổi nhịp câu theo logic của ý. Dùng câu ngắn để chốt điểm khó; dùng câu dài khi phải giữ một
   chuỗi nguyên nhân liền mạch. Không đổi nhịp chỉ để trông “giống người”.
7. Đọc thành tiếng và sửa chỗ vấp, nhưng giữ thuật ngữ cần thiết.

Với prose giải thích, ưu tiên nhịp đoạn đơn giản:

`nêu ý → giải thích cơ chế/căn cứ → chỉ ra hệ quả`

Không bắt mọi đoạn theo đúng ba câu; chỉ dùng nhịp này để phát hiện đoạn đang trộn nhiều việc.

## 3. Nguyên tắc tiếng Việt

- Ưu tiên từ quen thuộc nhưng không hạ thấp độ chính xác.
- Giải nghĩa thuật ngữ lần đầu trong mỗi khối có thể được đọc độc lập.
- Dùng “bạn”, “học sinh”, “giáo viên” theo profile artifact; không mặc định một đại từ cho mọi đầu ra.
- Tránh lặp mẫu “không chỉ X mà còn Y”, “không phải X mà là Y”, câu hỏi tu từ rồi tự trả lời.
- Không ép mọi đoạn thành ba ý, không ép mọi mục có mở–thân–kết giống nhau.
- Dành câu ngắn, khoảng trắng và phép lặp có chủ đích cho kết luận trung tâm; đừng nhấn mọi thứ.
- Dùng câu chuyển ý để cho biết vì sao phần kế tiếp xuất hiện, không dùng “tiếp theo/chúng ta sẽ”.
- Đặt chủ thể và động từ chính gần đầu câu. Tách câu khi có quá hai quan hệ nguyên nhân, đối lập
  hoặc điều kiện.
- Ưu tiên diễn đạt trực tiếp. Chỉ dùng ẩn dụ khi nó làm cơ chế dễ hiểu hơn và không cần một câu khác
  để giải mã ẩn dụ.
- Không lặp một hình ảnh thành khẩu hiệu. Thuật ngữ và quan hệ khoa học phải gánh điểm nhấn chính.
- Không bịa trải nghiệm. Gắn nhãn rõ nếu tình huống là giả định hoặc số liệu là minh họa.
- Không thay định danh máy, code, URL, slug, ký hiệu, công thức và citation khi humanize.

## 4. Kiểm tra chất lượng

Một lượt biên tập đạt khi:

- mỗi đoạn có ít nhất một chức năng rõ;
- bỏ đoạn đó sẽ mất một mắt xích cần thiết, không chỉ mất “độ mượt”;
- ví dụ làm sáng cơ chế hoặc bẫy cụ thể;
- giọng nhất quán với artifact nhưng không lấn át nội dung;
- có một hoặc hai câu người đọc có thể nhớ và dùng để dựng lại toàn bộ lập luận;
- đọc liền mà bỏ tiêu đề vẫn hiểu chủ thể của từng đoạn và quan hệ giữa hai đoạn kề nhau;
- bản sau giữ nguyên inventory ngữ nghĩa theo `07-cong-giu-nguyen-ngu-nghia.md`.

Đừng chấm bằng số lượng từ cấm. Một cụm từ chỉ có vấn đề khi nó làm câu mơ hồ, khoa trương hoặc
rập khuôn trong ngữ cảnh hiện tại.
