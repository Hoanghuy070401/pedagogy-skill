# Role & Voice Profile

Persona là lớp điều khiển cách diễn đạt, không phải nguồn kiến thức. Chỉ áp sau khi đã khóa claim,
artifact và bản đồ chiều sâu.

## Chọn chế độ

### `own-voice` — giọng của chính người dùng

Dùng mẫu viết do người dùng sở hữu/cung cấp. Trích **cơ chế** thay vì sao chép câu:

- mức trang trọng và cách xưng hô;
- độ dài câu/đoạn và nhịp chuyển ý;
- cách mở ví dụ, giải thích thuật ngữ, đặt câu hỏi;
- mật độ hình ảnh, hài hước và nhận xét;
- điều người viết thường tránh.

Cần nhiều mẫu đại diện. Một đoạn ngắn chỉ đủ tạo profile tạm, phải ghi độ tin cậy thấp.

### `designed-role` — vai được thiết kế

Mô tả bằng thuộc tính chức năng: vai trò, đối tượng, mục đích, mức chuyên môn, thái độ, nhịp và
ranh giới. Ví dụ: “giáo viên Vật lí giàu kinh nghiệm, giải thích bằng hiện tượng trước công thức,
không dùng giọng quyền uy”.

### `fictional-character` — nhân vật hư cấu

Chỉ dùng như khung sáng tạo và phải phù hợp lứa tuổi. Không để lời thoại nhân vật che khuất mục tiêu
học, giả làm nguồn, hoặc biến toàn bộ bài thành diễn xuất.

### `named-person` — người thật có tên

Không bắt chước sát giọng của người thật chỉ từ tên. Chuyển yêu cầu thành các thuộc tính chung,
không gây nhầm lẫn: lĩnh vực, mức trang trọng, cách lập luận, mật độ ví dụ. Không tuyên bố nội dung
do người đó viết hay xác nhận.

## Schema profile gợi ý

```yaml
mode: own-voice | designed-role | fictional-character | named-person
role: ""
audience: ""
purpose: ""
register: conversational | neutral | formal
explanation_pattern: ""
sentence_rhythm: ""
preferred_moves: []
avoid: []
evidence_basis: []
confidence: low | medium | high
```

Không lưu các câu mẫu nhạy cảm nếu không cần. Cho người dùng xem, sửa, xuất và xóa profile.

## Cổng persona

- Không đổi inventory trong `07-cong-giu-nguyen-ngu-nghia.md`.
- Không bịa ký ức, trải nghiệm, thành tích hoặc quan hệ cá nhân.
- Không dùng persona để tăng độ chắc chắn của claim.
- Không thêm câu cửa miệng vào mọi đoạn; profile là tập khuynh hướng, không phải bộ lọc thay từ.
- Nếu persona làm giảm độ rõ hoặc không phù hợp artifact, ưu tiên artifact và sư phạm.
