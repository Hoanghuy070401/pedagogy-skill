# Đánh giá skill văn phong và phương án tích hợp

**Ngày kiểm tra:** 2026-08-11  
**Mục tiêu:** cải thiện văn bản do AI tạo: bớt cứng, bớt lan man, có chiều sâu
và vẫn trung thành với nguồn.

## 1. Nguồn đã kiểm tra

### `hardikpandya/stop-slop`

- Repository: <https://github.com/hardikpandya/stop-slop>
- Commit được đọc: `8da1f030185bdfe8471220585162991eaeb970e9`
- Ngày commit: 2026-03-18
- Giấy phép: MIT, copyright Hardik Pandya 2025.
- Thành phần chính: danh sách cụm từ, cấu trúc dễ lộ giọng AI, ví dụ trước/sau
  và rubric Directness/Rhythm/Trust/Authenticity/Density.

### `christopher47634/writer-style-skill-factory`

- Repository: <https://github.com/christopher47634/writer-style-skill-factory>
- Commit được đọc: `862604d958e7ff89f2cc2b51b7d14a8f7dafb151`
- Ngày commit: 2026-08-10
- Giấy phép: MIT, copyright christopher47634 2026.
- Thành phần chính: framework tạo style skill từ corpus, phân loại mức bằng
  chứng, tìm cơ chế viết, phản mẫu, test set và so sánh mù.

Hai giấy phép cho phép sửa và tái sử dụng, nhưng khi chép phần đáng kể phải giữ
copyright notice và permission notice. Nên ghi attribution rõ cho phần được
adapt, không nên xóa dấu vết nguồn.

## 2. Kết luận ngắn

Có thể dùng cả hai dự án, nhưng **không nên cài hoặc ghép nguyên trạng** vào
pipeline giáo dục.

- `stop-slop` phù hợp làm lớp **biên tập cuối**, giúp cắt sáo ngữ và cấu trúc
  máy móc. Nó không tạo ra lập luận hay chiều sâu nội dung.
- `writer-style-skill-factory` cung cấp phương pháp tốt hơn để xây các profile
  viết có căn cứ. Không nên dùng trực tiếp các skill mô phỏng tác giả hoặc cơ
  quan báo chí cho học liệu Việt Nam.
- Vấn đề “thiếu chiều sâu” phải được xử lý trước khi viết prose, bằng bản đồ
  claim, cơ chế, ví dụ, phản ví dụ, giới hạn và liên kết với nguồn. Humanize chỉ
  sửa cách nói; nó không thể cứu một dàn ý rỗng.

Khuyến nghị: adapt phương pháp, không vendor toàn bộ hai repository.

## 3. Đánh giá `stop-slop`

### Phần hữu ích

- Cắt câu mở đầu không mang thông tin.
- Phát hiện tuyên bố mơ hồ kiểu “điều này rất quan trọng” nhưng không nói hệ quả.
- Phát hiện lặp cấu trúc “không phải X mà là Y”, bộ ba đối xứng và đoạn kết giả
  tạo cảm giác sâu sắc.
- Yêu cầu câu cụ thể, chủ thể rõ và nhịp không đều tăm tắp.
- Có before/after và rubric ngắn, phù hợp chuyển thành evaluator.

### Phần không nên áp dụng như luật tuyệt đối

- “Loại mọi trạng từ”: quá cực đoan; trạng từ có thể cần để mô tả mức độ, điều
  kiện hoặc quan hệ khoa học.
- “Mọi câu đều phải có người làm chủ thể”: không phù hợp văn bản khoa học, mô
  tả hiện tượng và câu lệnh học tập.
- “Luôn dùng chủ động”: bị động có thể đúng khi tác nhân không quan trọng hoặc
  cần giữ trọng tâm vào hiện tượng.
- “Không mở câu bằng từ hỏi”, “không dùng gạch ngang”, “hai ý tốt hơn ba ý”:
  là heuristic tiếng Anh mang tính cá nhân, không phải quy tắc tiếng Việt hay
  quy tắc giáo dục.
- Các ví dụ thường nén văn bản thành câu quảng cáo rất ngắn. Áp quá mạnh sẽ làm
  bài học cụt, thiếu giải thích và càng “cứng”.

### Cách dùng phù hợp

Chuyển các quy tắc thành cảnh báo có ngữ cảnh:

- `filler_phrase`: có thể tự sửa;
- `vague_claim`: bắt buộc yêu cầu tiêu chí/hệ quả;
- `formulaic_structure`: cảnh báo khi lặp từ hai lần trở lên;
- `rhythm_monotony`: cảnh báo thống kê, không ép độ dài giả tạo;
- `overcompression`: chặn khi việc cắt làm mất điều kiện, cơ chế hoặc ví dụ.

Không để bộ humanize sửa công thức, số liệu, citation, thuật ngữ, learning
objective hoặc claim đã được duyệt.

## 4. Đánh giá `writer-style-skill-factory`

### Phần đáng tích hợp

- Dùng corpus thật thay cho một danh sách “từ nghe hay”.
- Tìm 4–8 **cơ chế viết có thể làm thay đổi đầu ra**, không bắt chước từ khóa bề
  mặt.
- Phân biệt `corpus_fact`, `stable_pattern`, `local_pattern` và
  `generation_hypothesis`.
- Viết phản mẫu để ngăn AI dùng lối tắt rẻ tiền.
- Tách profile theo thể loại và mục đích.
- So sánh candidate với bản hiện tại và baseline không dùng skill.
- Chỉ giữ thay đổi khi vượt test trên nhiều đề, có điều kiện dừng và có log.

### Phần không phù hợp nếu dùng trực tiếp

- Các style tác giả và báo chí Trung Quốc không đại diện cho tiếng Việt giáo
  dục.
- Mô phỏng giọng một tác giả/cơ quan có thể biến học liệu thành bắt chước bề
  ngoài, gây nhầm nguồn hoặc tạo giọng không phù hợp học sinh.
- Thuật toán tạo ba bản hoàn chỉnh rồi tự chấm có chi phí cao và dễ sinh bằng
  chứng tự xác nhận nếu cùng một model vừa viết vừa đánh giá.
- Ngưỡng 90/100 và số bài corpus trong repository là quy ước của tác giả, chưa
  phải bằng chứng rằng profile phù hợp với tài liệu giáo dục Việt Nam.
- Một số profile chứa các “từ khuyên dùng”, chính là kiểu bắt chước bề mặt mà
  framework tuyên bố muốn tránh.

### Cách chuyển đổi cho dự án

Không tạo `style-<author>`. Tạo profile theo **người đọc × loại artifact × nhiệm
vụ**:

| Profile | Người đọc | Cơ chế chính |
|---|---|---|
| `concept-explanation` | Học sinh | từ trực giác → cơ chế → ví dụ → giới hạn |
| `teacher-guide` | Giáo viên | thao tác rõ, thời gian, dấu hiệu cần quan sát, phương án B |
| `student-task` | Học sinh | một hành động mỗi yêu cầu, dữ kiện đủ, tiêu chí hoàn thành |
| `answer-feedback` | Học sinh | chỉ ra bước đúng/sai, nguyên nhân, cách sửa, câu tự kiểm |
| `source-quality-report` | Người duyệt | claim, bằng chứng, giới hạn, bất đồng, quyết định |
| `deep-dive` | Người học nâng cao | câu hỏi trung tâm → chuỗi lập luận → phản ví dụ → hệ quả |

Mỗi profile phải có corpus tiếng Việt hợp pháp, phạm vi độ tuổi và phản mẫu riêng.

## 5. Vì sao skill hiện tại vẫn cứng và lan man

`pedagogy-skill` hiện đã cấm nhiều dấu hiệu AI giống `stop-slop`: sáo ngữ, bộ
ba, “không phải X mà là Y”, nhịp đều và ví dụ giả. Tuy vậy, một số vấn đề vẫn
còn:

1. **Quy tắc chiều sâu là checklist, chưa thành dữ liệu bắt buộc.** Luật “là gì
   → vì sao → cơ chế → dùng khi nào → bẫy” chưa được biểu diễn thành các trường
   mà pipeline phải điền và kiểm tra.
2. **Một giọng dùng cho mọi artifact.** Xưng “bạn”, khẩu ngữ và câu ngắn có thể
   hợp phần giải thích nhưng không hợp rubric, báo cáo nguồn hoặc hướng dẫn vận
   hành.
3. **Humanize đi sau bản nháp rỗng.** Nếu claim map và dàn ý thiếu quan hệ nhân
   quả, lớp sửa văn chỉ thay từ mà không tạo hiểu biết.
4. **Checklist khuyến khích đủ mục.** Model có thể viết một đoạn chung chung cho
   mỗi mục để “qua checklist”, làm văn dài mà không thêm thông tin.
5. **Chưa có ngân sách nội dung.** Không giới hạn số ý chính, vai trò từng đoạn,
   độ dài theo mức khó hoặc điều kiện để cắt một đoạn.
6. **Chưa đo giữ nghĩa sau chỉnh văn.** Một bản nghe tự nhiên hơn vẫn có thể làm
   mất điều kiện áp dụng hoặc thêm ví dụ không có nguồn.

## 6. Kiến trúc đề xuất: chiều sâu trước, văn phong sau

### Lớp 1 — `content-depth-plan`

Trước khi viết, mỗi khái niệm chính phải có cấu trúc:

```yaml
concept:
  prior_knowledge: []
  central_question: ""
  core_claims: []
  causal_or_logical_chain: []
  mechanism: ""
  example: ""
  counterexample: ""
  boundary_conditions: []
  common_misconceptions: []
  transfer_task: ""
  citations: []
```

Không phải khái niệm nào cũng cần điền mọi trường. Pipeline phải giải thích trường
nào không áp dụng thay vì sinh câu cho đủ chỗ.

### Lớp 2 — `artifact-voice-profile`

Chọn profile dựa trên artifact và người đọc. Profile điều khiển khoảng cách với
người đọc, mức thuật ngữ, mật độ ví dụ, nhịp câu và cách kết thúc. Không điều
khiển sự thật hoặc thêm claim.

### Lớp 3 — `draft-by-function`

Mỗi đoạn có một `paragraph_function`:

- đặt vấn đề;
- giải thích cơ chế;
- đưa bằng chứng;
- minh họa;
- phân biệt trường hợp;
- chỉ ra giới hạn;
- yêu cầu người học hành động;
- phản hồi.

Hai đoạn liền nhau cùng chức năng và không thêm claim mới là ứng viên gộp/cắt.

### Lớp 4 — `vietnamese-anti-slop`

Chạy sau khi nội dung đã đủ. Dùng một phần heuristic của `stop-slop`, đã Việt
hóa và chuyển từ cấm tuyệt đối thành mức độ/context. Ưu tiên:

- bỏ mở đầu rỗng;
- thay đánh giá mơ hồ bằng tiêu chí/hệ quả;
- giảm meta-commentary;
- phát hiện cấu trúc lặp;
- giữ nhịp tự nhiên nhưng không cắt mất logic.

### Lớp 5 — `semantic-preservation-gate`

So sánh trước/sau biên tập:

- claim và mức chắc chắn không đổi;
- điều kiện/ngoại lệ không mất;
- số liệu, công thức và citation không đổi;
- không có ví dụ, trải nghiệm hoặc nguồn mới bị bịa;
- mục tiêu và đáp án không bị thay nghĩa.

Nếu khác, trả lại bản trước và chỉ ra block gây lệch.

## 7. Cấu trúc skill nên refactor

```text
pedagogy-skill/
  SKILL.md                         # router và workflow ngắn
  references/
    content-depth.md               # depth schema + ví dụ
    artifact-voice-profiles.md     # profile theo loại tài liệu
    vietnamese-anti-slop.md        # heuristic Việt hóa
    semantic-preservation.md       # điều kiện giữ nghĩa
    revision-protocol.md           # draft → audit → revise
  assets/
    depth-plan.example.yaml
    voice-profile.example.yaml
```

Không đưa toàn bộ danh sách tiếng Anh hoặc 16 author skill vào context. Phần
router chỉ tải reference cần cho artifact hiện tại, đúng nguyên tắc progressive
disclosure.

## 8. Kế hoạch thử nghiệm trước khi tích hợp chính thức

### Bộ test

Tạo ít nhất 12 input cố định:

- 3 đoạn giải thích khái niệm;
- 2 teacher guide;
- 2 nhiệm vụ học sinh;
- 2 đáp án/phản hồi;
- 2 deep-dive;
- 1 báo cáo nguồn.

Mỗi input tạo ba phiên bản:

1. không dùng style skill;
2. skill hiện tại;
3. kiến trúc mới.

### Tiêu chí máy có thể kiểm tra

- claim/citation retention;
- số điều kiện và ngoại lệ bị mất;
- tỷ lệ đoạn không thêm thông tin;
- lặp cấu trúc/cụm từ;
- độ dài câu và đoạn, chỉ dùng làm tín hiệu;
- số thuật ngữ chưa giải nghĩa;
- số ví dụ không có căn cứ;
- tỷ lệ block phải viết lại.

### Đánh giá nội bộ

Ẩn nhãn ba phiên bản rồi chấm:

- rõ và cụ thể;
- mạch lập luận;
- chiều sâu cơ chế;
- đúng mức người đọc;
- tự nhiên;
- gọn nhưng không mất ý;
- trung thành với nguồn.

AI blind review chỉ dùng để phát hiện regression nội bộ. Không dùng điểm này để
tuyên bố “giống người” hoặc “được giáo viên duyệt”. Khi có người dùng thật, lấy
đánh giá của họ thay cho evaluator mô phỏng.

## 9. Quyết định tích hợp đề xuất

| Thành phần | Quyết định |
|---|---|
| `stop-slop/SKILL.md` nguyên bản | Không cài trực tiếp vào generation pipeline |
| Cụm từ/cấu trúc anti-slop | Adapt có chọn lọc, Việt hóa, attribution MIT |
| Rubric Directness/Rhythm/Trust/Density | Dùng làm tín hiệu biên tập, thêm Fidelity và Depth |
| Style author/media có sẵn | Không đưa vào sản phẩm giáo dục mặc định |
| Corpus engineering | Tích hợp vào công cụ tạo profile |
| Evidence levels | Tích hợp vào schema style pack |
| Anti-pattern + genre routing | Tích hợp theo loại artifact giáo dục |
| Ba bản hoàn chỉnh mỗi lần | Không mặc định; ưu tiên 2 outline → 1 draft → 1 revision |
| Blind regression testing | Tích hợp vào EduEvals ở mức thử nghiệm nội bộ |

## 10. Thứ tự triển khai

1. Chuyển depth checklist thành `content-depth-plan` có schema.
2. Tách giọng viết theo sáu artifact profile.
3. Tạo `semantic-preservation-gate` trước khi thêm humanize mạnh hơn.
4. Việt hóa phần hữu ích của `stop-slop` thành evaluator/cảnh báo.
5. Tạo corpus/test set tiếng Việt có quyền sử dụng.
6. Chạy A/B/C regression rồi mới thay workflow mặc định của `lessonforge`.

Đây nên là một vertical slice của Milestone 3, không phải một skill trang trí
được nhét thêm vào prompt cuối.

