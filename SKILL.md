---
name: soan-bai-hoc
description: Soạn, sửa, trình bày và đánh giá tài liệu giáo dục tiếng Việt từ nguồn có kiểm soát. Dùng cho giáo án giáo viên, tài liệu học sinh, phiếu học tập, quiz, đáp án, rubric, bài giải thích chuyên sâu và UI/HTML học liệu; đặc biệt khi cần lập chiều sâu nội dung trước khi viết, giữ nguyên claim/công thức/trích dẫn, chọn giọng theo loại tài liệu, giảm văn phong AI hoặc tạo giao diện responsive có animation đúng chức năng.
---

# Soạn bài học từ nguồn

Tạo tài liệu có căn cứ, đúng chức năng và tự nhiên. Đừng cố làm câu chữ “hay” khi bản đồ nội dung
còn mỏng hoặc nguồn chưa đủ.

## Thứ tự ưu tiên

Giải quyết xung đột theo đúng thứ tự này:

1. An toàn, quyền riêng tư và chỉ thị trực tiếp của người dùng.
2. Nguồn, provenance, claim/đáp án đã được duyệt và mức độ chắc chắn.
3. Hợp đồng của artifact và schema đầu ra.
4. Mục tiêu học tập, chiều sâu nội dung và khả năng tiếp cận.
5. Giọng văn, persona và nhịp câu.
6. Trang trí, hình thức và hiệu ứng.

Persona không được sửa sự thật. Văn phong không được che thiếu nguồn.

## Quy trình bắt buộc

1. **Nạp lịch sử sở thích nếu đầu ra có giao diện**: đọc
   `design-system/learning-ui/USER-PREFERENCES.md` khi file tồn tại; áp dụng preference `active`
   đúng phạm vi và cập nhật sau mỗi yêu cầu sửa rõ ràng.
2. **Khóa căn cứ**: phân biệt claim được nguồn hỗ trợ, claim mâu thuẫn và phần chưa đủ căn cứ.
3. **Lập bản đồ chiều sâu** theo `references/05-lap-ke-hoach-chieu-sau.md`. Chưa có cơ chế,
   ví dụ, ranh giới và bằng chứng học thì chưa viết prose.
4. **Dựng mạch lập luận và điểm nhấn** theo `references/09-mach-lap-luan-va-diem-nhan.md`.
   Chọn một câu hỏi kéo xuyên bài, một hình ảnh/quan hệ làm điểm neo và một kết luận đáng nhớ.
5. **Chọn hợp đồng artifact** theo `references/06-profile-theo-artifact.md`. Mỗi đầu ra phục vụ
   một người đọc và một công việc khác nhau.
6. **Khóa ma trận phong cách** theo `references/12-ma-tran-kiem-soat-phong-cach.md`: khai báo
   audience, purpose, cấu trúc theo artifact, technical baseline và user style layer. Nếu học giọng
   người dùng hoặc hóa thân, dựng profile từ `references/08-role-voice-profile.md`; không học claim,
   trải nghiệm cá nhân hay lỗi kỹ thuật từ mẫu.
7. **Khóa hợp đồng UI nếu đầu ra có giao diện** theo `references/10-quy-chuan-ui-hoc-lieu.md`.
   Chốt trục bố cục, trạng thái, responsive và ngân sách motion trước khi sinh HTML/CSS. Với dự án
   nhiều trang, tạo Master từ `assets/mau-design-system-hoc-lieu.md` và chỉ dùng page override cho
   khác biệt có lý do.
8. **Chạy Hallmark cho HTML/trang web** theo `references/11-tich-hop-hallmark.md`. Nếu skill
   `hallmark` khả dụng, phải nạp và dùng skill đó để chọn genre, macrostructure, typography,
   nav/footer và chạy slop test. Hallmark là lớp art direction; không được ghi đè nguồn, mục tiêu
   học tập, khả năng đọc, preference người dùng hay quy chuẩn accessibility của bước 7.
9. **Viết theo chức năng**: mỗi đoạn phải giải thích, chứng minh, minh họa, hướng dẫn, kiểm tra
   hoặc phản hồi. Bỏ đoạn không làm được việc nào.
10. **Soát văn AI** theo `references/03-van-phong-humanize.md`, sau khi nội dung đã đủ sâu. Với
   tài liệu kỹ thuật, báo cáo hoặc văn bản trang trọng, đọc thêm
   `references/13-bien-tap-tieng-viet-theo-profile.md`; không tự thêm dữ kiện để làm câu cụ thể hơn.
11. **Chạy cổng giữ nghĩa và phong cách** theo `references/07-cong-giu-nguyen-ngu-nghia.md` và
   checklist hậu sinh của `references/12-ma-tran-kiem-soat-phong-cach.md`.

## Cách nạp tài liệu

Không nạp toàn bộ `references/` vào mọi nhiệm vụ. Đọc theo nhu cầu:

| Nhiệm vụ | Tài liệu cần đọc |
|---|---|
| Lập claim/bản đồ nội dung | `05`, `07` |
| Giáo án giáo viên | `05`, `09`, `06`, `12`, `03`, `07`; đọc `01`, `02`, `04` khi cần chi tiết |
| Tài liệu học sinh | `05`, `09`, `06`, `12`, `03`, `07` |
| Phiếu học tập | `05`, `09`, `06`, `12`, `07` |
| Quiz, đáp án, rubric | `06`, `12`, `07` |
| Tài liệu kỹ thuật/giải thích công nghệ | `05`, `09`, `06`, `12`, `13`, `03`, `07` |
| Báo cáo học thuật, đề xuất, biên bản hoặc văn bản trang trọng | `06`, `12`, `13`, `03`, `07`; dùng skill `documents` nếu xuất DOCX |
| HTML, trang học liệu, preview hoặc Lesson Studio | `05`, `09`, `06`, `12`, `10`, `11`, `03`, `07`; thêm `02` nếu có asset và nạp skill `hallmark` khi khả dụng |
| Bắt chước giọng người dùng hoặc hóa thân | thêm `08` để dựng user style layer, nhưng vẫn đặt sau nguồn và artifact |
| Review trước bàn giao | `04`, cộng `07` nếu có sửa câu chữ |

`references/00-rule-set-agent.md` và `01-huong-dan-soan-bai.md` là tài liệu tương thích với
SchoolAI Studio. Chỉ nạp khi chạy schema/stack đó; không ghép mặc định vào mọi prompt.

## Cổng hoàn thành

Chỉ báo hoàn thành khi:

- mọi khẳng định dạy học truy được về claim/nguồn hoặc được đánh dấu chưa chắc chắn;
- mỗi mục tiêu có phần dạy, cơ hội luyện và cách quan sát kết quả;
- người đọc có thể nói lại câu hỏi xuyên bài, bước ngoặt và kết luận trung tâm;
- đầu ra đúng người đọc, đúng chức năng, không lẫn lời dành cho đối tượng khác;
- lượt sửa giọng không đổi số liệu, công thức, điều kiện, đáp án, citation hay mức độ chắc chắn;
- UI đã qua render ở `320`, `375`, `414`, `768`, `1024`, `1440px`; không lệch hàng, tràn ngang,
  che nội dung hay phụ thuộc animation; reduced motion và focus bàn phím hoạt động;
- đầu ra web đã ghi Hallmark stamp, dùng token khóa, có page profile và vượt pre-emit critique cùng
  slop test; mọi ngoại lệ Hallmark đều có lý do sư phạm hoặc accessibility;
- style contract đã chỉ rõ audience, purpose, baseline và phạm vi được học từ người dùng; thuật ngữ
  nhất quán, claim có căn cứ hoặc nhãn giả định, không trượt về giọng chat ngoài chủ ý artifact;
- dữ kiện, nhận định và kiến nghị không bị trộn; trường còn thiếu được hỏi lại hoặc dùng placeholder
  có nhãn khi người dùng cho phép bản nháp, không được lấp bằng chi tiết bịa;
- không có đoạn sáo rỗng, meta kể cấu trúc, ví dụ vô căn cứ hoặc nội dung chỉ để kéo dài bài.
