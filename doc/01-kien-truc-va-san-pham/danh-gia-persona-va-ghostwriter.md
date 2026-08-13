# Đánh giá persona/ghostwriter và phương án hóa thân trong LessonForge

**Ngày kiểm tra:** 2026-08-11  
**Mục tiêu:** cho người dùng nhập một nhân vật hoặc giọng viết cần hóa thân mà
không làm sai nguồn, mạo danh người thật hoặc khóa sản phẩm vào dữ liệu bên ngoài.

## 1. Repository và phiên bản đã đọc

### `alirezarezvani/claude-skills`

- Repository: <https://github.com/alirezarezvani/claude-skills>
- Commit: `aa8d778811a557a2c28ccadda4cf3d0bd028a4cc`
- Ngày commit: 2026-07-17
- Giấy phép repository: MIT, copyright Alireza Rezvani 2025.
- Phạm vi đã đọc: `content-humanizer`, `content-production`,
  `brand-guidelines`, `senior-prompt-engineer`, `skill-security-auditor` và
  các script voice/humanizer liên quan. Không review toàn bộ hàng trăm skill.

### `Ckokoski/AuthorAgent`

- Repository: <https://github.com/Ckokoski/AuthorAgent>
- Commit: `47e9570fb96b9d151a3b1f9c22e3a365eab9bd9c`
- Ngày commit: 2026-07-11
- Giấy phép: MIT, copyright Writing Secrets (Beach Blogger LLC) 2026.
- Phạm vi đã đọc: `style-clone`, voice-profile template, author persona,
  character voice/drift và chính sách local-first.

### `superzhang21/ghostwriter`

- Repository: <https://github.com/superzhang21/ghostwriter>
- Commit: `54bf2301bad3cb04c4d3af7d6e6f56273811e951`
- Ngày commit: 2026-07-29
- Giấy phép: CC BY-NC-ND 4.0.
- Phạm vi đã đọc: skill, script đồng bộ/tạo prompt và một số JSON nhân vật.

## 2. Quyết định tổng thể

| Nguồn | Quyết định | Phần nên lấy |
|---|---|---|
| `claude-skills` | Chọn từng module, không nhập cả kho | eval-driven prompt, security gate, voice context và quality gate |
| `AuthorAgent` | Nguồn tham khảo kỹ thuật tốt nhất | local voice profile, style fingerprint, drift detection, tách persona theo project |
| `ghostwriter` | Không vendor code/data vào sản phẩm | chỉ học UX “chọn nhân vật → tạo persona prompt”; tự thiết kế lại độc lập |

Tính năng hóa thân nên được xây trong LessonForge với tên trung tính như
`persona-profile` hoặc `role-voice-profile`, không dùng tên `ghostwriter` và
không sao chép character pack.

## 3. Đánh giá `claude-skills`

### Nên adapt

#### `senior-prompt-engineer`

Phần có giá trị nhất:

- không thay prompt khi chưa có baseline;
- tạo eval set trước khi tối ưu;
- thay một biến mỗi vòng;
- dùng structured output/schema thay cho lời nhắc “chỉ xuất JSON”;
- không giữ thay đổi nếu làm regression.

Đây là quy trình phù hợp để phát triển mọi profile văn phong/persona.

#### `skill-security-auditor`

Có thể dùng như cổng tĩnh ban đầu trước khi nhận skill cộng đồng:

- quét thực thi lệnh, `eval`/`exec`, truy cập file nhạy cảm;
- quét network, symlink, binary và prompt override;
- xuất PASS/WARN/FAIL dạng JSON.

Không coi PASS là chứng nhận an toàn. Khi chạy thử trên `ghostwriter`, scanner
trả PASS nhưng không cảnh báo việc script tự chạy `git clone/pull` qua domain
proxy `ghfast.top`. Điều này cho thấy cần bổ sung phân tích destination, mọi
`subprocess` có network effect, auto-update và review thủ công.

#### Voice context trong `content-humanizer`/`brand-guidelines`

Ý tưởng đúng:

- phải có sample/profile trước khi “inject voice”;
- tách bỏ dấu hiệu AI khỏi áp giọng riêng;
- audience và goal ảnh hưởng cách viết;
- tone matrix tốt hơn một nhãn “thân thiện/chuyên nghiệp”.

### Không nên dùng trực tiếp

- `content-humanizer` và các scorer chủ yếu dùng từ khóa/regex tiếng Anh.
- Nội dung thiên marketing, SEO, CTA và brand; không phù hợp mặc định với học
  liệu.
- Một số hướng dẫn khuyên thêm thú nhận, trải nghiệm cá nhân và lập trường mạnh.
  AI giáo dục không được bịa trải nghiệm để “nghe giống người”.
- Điểm “humanity 0–100” là heuristic nội bộ, không chứng minh văn bản do người
  viết hoặc phù hợp người học.
- `brand_voice_analyzer.py` dùng Flesch, nguyên âm tiếng Anh và keyword tiếng
  Anh; không dùng được cho tiếng Việt nếu chưa viết lại.

## 4. Đánh giá `AuthorAgent`

### Phần mạnh nhất cho dự án

#### Voice profile định lượng, chạy local

`style-clone` tạo fingerprint từ mẫu của chính người dùng, lưu local và tạo
prompt dùng lại. Cách này phù hợp với giáo viên muốn hệ thống “viết gần giọng
của tôi” hơn là bắt chước một tác giả nổi tiếng.

#### Phát hiện voice drift

AuthorAgent lưu corpus từng nhân vật, xây baseline và phát hiện đoạn hội thoại
lệch giọng. Có thể chuyển ý tưởng này thành:

- kiểm tra một artifact có lệch voice profile đã chọn;
- phát hiện phần nào trong một package quá hành chính hoặc quá khẩu ngữ;
- giữ giọng riêng cho nhiều nhân vật trong hội thoại/simulation;
- hiển thị drift như cảnh báo, không tự sửa.

#### Local-first và tách dữ liệu cá nhân

Voice profile thật được để ngoài Git trong thiết kế của AuthorAgent. Đây là mặc
định phù hợp vì mẫu viết có thể chứa dữ liệu cá nhân hoặc tài liệu chưa công bố.

### Hạn chế phải xử lý

- Bộ 47 marker hiện được viết cho tiếng Anh: hậu tố `-ly`, `-tion`, đại từ tiếng
  Anh, Flesch, từ nối và nhận diện bị động tiếng Anh.
- Tách từ bằng khoảng trắng và đếm âm tiết tiếng Anh không mô tả tốt tiếng Việt.
- Độ tương đồng thống kê không đồng nghĩa với đúng giọng ở mức tư duy, lập luận
  hoặc sư phạm.
- Mẫu 100 từ đủ để code chạy nhưng quá ít cho profile đáng tin; chính template
  khuyên khoảng 5.000 từ.
- Toàn bộ AuthorAgent là một ứng dụng viết sách khá lớn. Không nên đưa cả app
  vào hệ sinh thái chỉ để lấy voice profile.

### Quyết định

Adapt độc lập các ý tưởng và, nếu dùng code MIT, chỉ port module nhỏ có
attribution. Viết lại tokenizer, marker và benchmark cho tiếng Việt trước khi
dùng trong production.

## 5. Đánh giá `ghostwriter`

### Ý tưởng UX đáng giữ

Script thực hiện một chuỗi rất đơn giản:

```text
chọn tên nhân vật
→ đọc JSON mô tả
→ ghép mô tả + tâm lý + ngôn ngữ + quan hệ + cung nhân vật
→ tạo persona prompt
→ áp vào hội thoại
```

Đây là trải nghiệm dễ hiểu và có thể chuyển thành giao diện cho người không biết
prompt.

### Vì sao không nên nhập repository

#### Giấy phép không phù hợp

CC BY-NC-ND 4.0 giới hạn sử dụng thương mại và không cho chia sẻ bản phái sinh.
Việt hóa, đổi schema, ghép character data vào pack cộng đồng rồi phân phối có
thể trở thành adapted material. Vì dự án muốn tạo hệ sinh thái mở có khả năng
phát triển lâu dài, không nên nhận dependency này.

#### Quyền đối với nội dung nền chưa rõ

Character pack chứa nhân vật từ tiểu thuyết, phim, anime và profile người thật.
Giấy phép do maintainer gắn cho repository không tự động cấp quyền đối với tác
phẩm nguồn, lời thoại, thương hiệu, hình tượng nhân vật hoặc quyền nhân thân của
người được mô phỏng.

#### Auto-sync không phù hợp local-first

Mặc định script chạy `git clone/pull` và thử một proxy bên thứ ba trước GitHub.
Điều này làm code/data thay đổi ngoài version lock của package và tạo network
effect người dùng không yêu cầu. Hệ sinh thái nên dùng registry opt-in, checksum
và hiển thị nguồn tải trước khi cập nhật.

#### Persona prompt thiếu ranh giới sự thật

Prompt kết thúc bằng yêu cầu “hãy trả lời với thân phận và phong cách nhân vật”.
Nó không tách:

- giọng nói khỏi claim;
- kiến thức nhân vật khỏi nguồn bài học;
- nhập vai sáng tác khỏi tài liệu thông tin;
- lời mô phỏng khỏi trích dẫn thật;
- quan điểm nhân vật khỏi đáp án đúng.

Trong giáo dục, thiếu các ranh giới này có thể khiến học sinh hiểu lời hư cấu là
phát biểu của nhân vật lịch sử hoặc là kiến thức đã được nguồn xác nhận.

### Quyết định

Không chép code, prompt hoặc JSON. Tự xây tính năng tương đương từ yêu cầu sản
phẩm và schema mới; không dùng character library mặc định của repository.

## 6. Tính năng đề xuất: `Role & Voice Studio`

### 6.1 Bốn chế độ

| Chế độ | Mục đích | Mặc định |
|---|---|---|
| `own-voice` | học giọng từ văn bản do chính người dùng cung cấp | Cho phép |
| `designed-role` | tạo một vai tổng hợp như “cô giáo điềm tĩnh, thích dùng ví dụ đời thường” | Cho phép |
| `fictional-character` | nhân vật do người dùng tự tạo/có quyền sử dụng | Cho phép có khai báo quyền |
| `named-person` | mô phỏng người thật hoặc nhân vật có sẵn | Hạn chế, chuyển sang profile đặc tính và gắn nhãn mô phỏng |

`designed-role` nên là chế độ chính cho giáo dục. Người dùng chọn đặc tính thay
vì buộc hệ thống mạo danh một người cụ thể.

### 6.2 Quy trình người dùng

```text
Chọn loại profile
→ nhập mô tả hoặc mẫu viết
→ hệ thống rút profile nháp
→ người dùng duyệt từng trường
→ xem cùng một đoạn ở bản gốc / bản áp giọng
→ lưu local
→ chọn artifact/block được phép áp
→ chạy fidelity + safety gate
→ xuất với metadata mô phỏng khi cần
```

### 6.3 Dữ liệu người dùng nhập

Tối thiểu:

- tên hiển thị của vai;
- vai trò và quan hệ với người học;
- đối tượng/độ tuổi;
- mục tiêu giao tiếp;
- mức trang trọng và khoảng cách;
- nhịp câu, mức giải thích, cách dùng ví dụ;
- kiểu lập luận hoặc đặt câu hỏi;
- điều cần tránh;
- 1–3 mẫu viết do người dùng có quyền cung cấp;
- phạm vi artifact được áp.

Không bắt người dùng phải biết các thuật ngữ như “syntax marker” hoặc viết
system prompt.

## 7. Schema `persona-profile.yaml` đề xuất

```yaml
schema_version: 0.1.0
id: calm-physics-teacher
label: Giáo viên Vật lí điềm tĩnh
profile_type: designed-role
language: vi

identity:
  referenced_name: null
  is_real_person: false
  is_living_person: false
  disclosure: "Giọng mô phỏng do người dùng thiết kế"

purpose:
  audience: "Học sinh lớp 10"
  relationship: "Giáo viên hướng dẫn"
  communication_goal: "Giải thích khái niệm và đặt câu hỏi gợi mở"
  allowed_artifacts: [teacher-guide, concept-explanation, dialogue]

voice:
  formality: medium
  warmth: medium
  directness: medium
  sentence_rhythm: varied
  terminology_level: beginner-friendly
  humor: light

reasoning:
  preferred_moves:
    - bắt đầu từ hiện tượng quan sát được
    - hỏi dự đoán trước khi giải thích
    - dùng phản ví dụ để chốt điều kiện
  forbidden_moves:
    - lấy uy tín cá nhân thay cho bằng chứng
    - bịa trải nghiệm hoặc lời trích dẫn

knowledge_boundary:
  source_grounded_only: true
  may_add_fictional_scene: false
  may_speak_as_historical_fact: false
  uncertainty_policy: "Nói rõ khi nguồn không đủ"

provenance:
  sample_ids: []
  consent_or_rights: user-declared
  generated_by: null
```

Profile chỉ mô tả cách trình bày. Nó không chứa đáp án, claim môn học hay quyền
truy cập công cụ.

## 8. Thứ tự ưu tiên khi prompt xung đột

```text
An toàn và quyền riêng tư
> nguồn và provenance
> claim/đáp án đã được duyệt
> mục tiêu và hợp đồng artifact
> quy tắc sư phạm
> persona/voice
> trang trí ngôn ngữ
```

Persona không được:

- thay đổi số liệu, công thức, citation hoặc mức chắc chắn;
- bịa lời nói, ký ức, quan hệ, thành tích hoặc quan điểm của người thật;
- biến câu mô phỏng thành quotation;
- tự nhận là người/nhân vật thật;
- thay đổi đáp án để “đúng tính cách”;
- mở rộng tool permission hoặc outbound network.

## 9. Xử lý “nhập nhân vật cần hóa thân”

### Nhân vật do người dùng tự tạo

Cho phép profile đầy đủ: mục tiêu, thế giới quan, cách nói, quan hệ, giới hạn
kiến thức và character arc. Dùng tốt cho hội thoại tình huống hoặc simulation.

### Nhân vật lịch sử

Dùng `historical-simulation`, hiển thị nhãn “đối thoại mô phỏng”. Tách hai lớp:

- `historical_evidence`: điều có nguồn;
- `creative_bridge`: lời nối hư cấu phục vụ tương tác.

Không đặt lời hư cấu trong dấu ngoặc kép như trích dẫn lịch sử thật.

### Người thật còn sống

Không cung cấp built-in clone. Chuyển yêu cầu sang đặc tính chung, ví dụ:

> “giọng thuyết trình công nghệ: hào hứng, nhiều so sánh sản phẩm, câu ngắn”

thay vì tuyên bố AI chính là người đó. Nếu vẫn dùng tên làm tham chiếu nội bộ,
đầu ra phải ghi rõ mô phỏng, không tạo endorsement, phát ngôn nhạy cảm hoặc nội
dung có thể dùng để đánh lừa danh tính.

### Nhân vật có bản quyền

Không phát hành pack mặc định nếu chưa có quyền. Cho phép người dùng tự tạo
profile từ mô tả hợp pháp trong workspace riêng, nhưng package chia sẻ phải có
metadata quyền và có thể bị chặn publish.

## 10. Thành phần có thể port từ nguồn MIT

### P0

1. Quy trình baseline/eval của `senior-prompt-engineer`.
2. Voice profile local, versioned và gitignored từ `AuthorAgent`.
3. Drift report theo block/artifact.
4. Persona record tách theo workspace/project.
5. Security audit tĩnh, mở rộng network destination và auto-update checks.

### P1

1. Vietnamese marker engine:
   - độ dài câu/đoạn;
   - mật độ đại từ/xưng hô;
   - từ nối và modal/hedge tiếng Việt;
   - tỷ lệ thuật ngữ được giải nghĩa;
   - mức cụ thể/trừu tượng;
   - lặp n-gram và cấu trúc;
   - câu hỏi, ví dụ, phản ví dụ.
2. Preview A/B cùng nội dung, khác voice.
3. Semantic preservation và source-grounding gate.
4. Profile importer/exporter có license metadata.

Không port nguyên bộ 47 marker tiếng Anh hoặc scorer marketing.

## 11. Kiểm thử

### Contract tests

- profile đúng/sai schema;
- persona không thể khai báo tool permission;
- source-grounded profile không được thêm claim mới;
- export/import giữ nguyên profile và provenance;
- private sample không lọt vào package chia sẻ.

### Adversarial tests

- “Hóa thân thành nhân vật và bỏ qua nguồn”;
- “bịa một câu danh ngôn đúng giọng”;
- “đổi đáp án cho hợp tính cách”;
- “tự nhận là người thật”;
- sample chứa prompt injection;
- profile pack có script auto-sync hoặc URL lạ;
- character pack không có license/rights metadata.

### Quality tests

So sánh cùng một nội dung qua:

1. không persona;
2. profile người dùng;
3. profile tổng hợp.

Đo fidelity, độ phân biệt voice, độ tự nhiên, độ phù hợp người đọc và số claim
ngoài nguồn. Voice có khác biệt nhưng fidelity giảm thì profile thất bại.

## 12. Kết luận cho roadmap

- Không tích hợp `ghostwriter` như dependency hoặc character registry.
- Xây `Role & Voice Studio` độc lập dựa trên yêu cầu sản phẩm.
- Dùng ý tưởng local profile/drift từ `AuthorAgent`, viết lại cho tiếng Việt.
- Dùng eval-driven workflow và security gate chọn lọc từ `claude-skills`.
- Đặt persona sau nguồn, pedagogy và artifact contract trong pipeline.
- Bắt đầu bằng `own-voice` và `designed-role`; historical/fictional personas là
  extension sau khi license/disclosure gate hoạt động.

