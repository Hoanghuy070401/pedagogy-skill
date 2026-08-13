# Plan triển khai hệ sinh thái công cụ tạo tài liệu giáo dục

**Ngày chốt hướng:** 2026-08-11  
**Trạng thái:** kế hoạch thực thi hiện hành  
**Trọng tâm:** xây công cụ và chuẩn mở; chưa thẩm định chất lượng một bài dạy cụ thể

## 1. Quyết định sản phẩm hiện tại

Dự án xây **công cụ giúp người dùng tạo, kiểm tra, chỉnh sửa, xuất và sở hữu tài
liệu giáo dục từ nguồn của họ**. Dự án không lấy việc tự soạn một bài Vật lí mẫu
làm sản phẩm cuối cùng.

Package Vật lí 10 hiện có được giữ làm:

- fixture để thiết kế schema;
- dữ liệu mẫu cho kiểm thử nhập/xuất;
- bộ lỗi có chủ đích cho kiểm thử quy tắc;
- demo nội bộ của luồng tạo package.

Package này chưa phải bằng chứng chất lượng giáo dục. Bước mời giáo viên thật,
đánh giá trong lớp và đo hiệu quả học tập được **tạm hoãn**, không còn là điều
kiện để bắt đầu xây công cụ.

## 2. Kết quả cần đạt

Người dùng có thể thực hiện một luồng hoàn chỉnh trên máy cá nhân:

```text
Tạo workspace
  → thêm nguồn
  → hệ thống trích xuất và định vị nội dung
  → nhập yêu cầu tài liệu
  → duyệt dàn ý/bản đồ claim
  → tạo nhiều artifact liên kết với nhau
  → chạy kiểm tra kỹ thuật và truy nguồn
  → sửa/duyệt
  → xuất package mở + DOCX/PDF/PPTX
```

Đầu ra không bị khóa vào một nhà cung cấp AI. Người dùng có thể đổi model,
chỉnh file bằng công cụ khác, sao lưu bằng Git và tái tạo đầu ra từ manifest.

## 3. Ranh giới tuyên bố

Trong giai đoạn xây hệ sinh thái, công cụ có thể tuyên bố:

- file đúng schema;
- trích dẫn mở được đúng vị trí đã lưu;
- claim có hoặc chưa có bằng chứng;
- câu hỏi có liên kết tới mục tiêu/nội dung đã tạo;
- package có thể xuất, nhập lại và tái tạo;
- dữ liệu nào đã hoặc sắp rời máy;
- provider nào đã vượt bộ compatibility test kỹ thuật.

Công cụ **chưa được tuyên bố**:

- bài dạy đúng tuyệt đối;
- nguồn giáo viên chọn chắc chắn đúng;
- tài liệu phù hợp với mọi lớp học;
- tài liệu đã được giáo viên duyệt hoặc đã chứng minh hiệu quả học tập.

Các nhãn `Teacher-reviewed`, `Peer-reviewed`, `Classroom-tested` vẫn tồn tại
trong schema nhưng mặc định là `unverified` và chỉ người có bằng chứng bên ngoài
mới được nâng trạng thái.

## 4. Kiến trúc hệ sinh thái mục tiêu

### 4.1 `open-lesson-spec` — hợp đồng dùng chung

Trách nhiệm:

- JSON Schema/Pydantic models cho workspace, nguồn, brief, claim, artifact,
  citation, eval result và build manifest;
- versioning và migration;
- bộ fixture hợp lệ/không hợp lệ;
- quy tắc tương thích giữa các phiên bản;
- tài liệu định dạng Open Lesson Package.

Không chứa UI, prompt, provider hoặc nội dung môn học.

Trong giai đoạn đầu, spec có thể nằm trong monorepo hiện tại để thay đổi nhanh.
Chỉ tách thành package/repo độc lập khi có ít nhất hai consumer thật sự cùng
phụ thuộc vào nó.

### 4.2 `pedagogy-skill` — các pack tri thức và quy tắc

Trách nhiệm:

- quy tắc sư phạm dùng khi lập kế hoạch, tạo học liệu và câu hỏi;
- template artifact;
- taxonomy theo cấp học/môn khi đã có nhu cầu;
- metadata phiên bản, ngôn ngữ, phạm vi áp dụng và giấy phép;
- ví dụ pass/fail để máy kiểm thử được.

Pack là dữ liệu phiên bản hóa, không gọi model và không tự ghi file người dùng.

### 4.3 `lessonforge` — engine tạo và biến đổi tài liệu

Các module mục tiêu:

1. `workspace`: tạo/mở dự án local.
2. `ingest`: nhận PDF, DOCX, Markdown, text và URL.
3. `extract`: tách nội dung, trang/đoạn, bảng và metadata.
4. `corpus`: lập chỉ mục cục bộ, tìm đoạn liên quan và lưu hash nguồn.
5. `planner`: biến brief + nguồn + pack thành outline và bản đồ claim.
6. `generator`: tạo từng artifact theo chặng, dùng structured output.
7. `revision`: sửa một block mà không sinh lại toàn bộ package.
8. `providers`: adapter OpenAI-compatible và local model.
9. `exporters`: Markdown/JSON trước; DOCX/PDF/PPTX sau.
10. `package`: đóng/mở Open Lesson Package.

Mọi lời gọi model phải lưu provider/model, tham số, phiên bản prompt/pack, danh
sách source chunk đã dùng và thời điểm tạo. Secret không được ghi vào manifest.

### 4.4 `EduEvals` — engine kiểm tra và báo cáo

Ba lớp kiểm tra:

1. **Deterministic:** schema, link, hash, citation target, trường bắt buộc, ID
   trùng, artifact thiếu, dữ liệu nhạy cảm, license metadata.
2. **Cross-artifact:** mục tiêu → nội dung → hoạt động → câu hỏi → đáp án;
   claim → citation; nội dung học sinh không chứa đáp án/fixture nội bộ.
3. **Model-assisted:** phát hiện mâu thuẫn, thiếu điều kiện, câu hỏi ngoài nội
   dung hoặc cách diễn đạt khó hiểu. Kết quả chỉ là cảnh báo có bằng chứng, không
   là phán quyết cuối.

EduEvals không sửa đầu ra âm thầm. Mỗi cảnh báo có mã, mức độ, vị trí, bằng
chứng, đề xuất và trạng thái xử lý.

### 4.5 `Lesson Studio` — giao diện người dùng local

Chỉ bắt đầu sau khi CLI hoàn thành một vertical slice ổn định. UI có trách nhiệm:

- quản lý workspace và nguồn;
- hiển thị nguồn cạnh đoạn đang soạn;
- cho duyệt outline/claim trước khi tạo;
- soạn thảo theo block, xem diff và khóa block đã duyệt;
- chạy eval, lọc cảnh báo và mở đúng bằng chứng;
- xem trước và xuất tài liệu;
- hiển thị rõ dữ liệu nào sẽ rời máy khi dùng cloud provider.
- cho tạo/chọn `role-voice-profile`, xem trước A/B và giới hạn profile theo
  artifact; profile chỉ điều khiển cách trình bày, không điều khiển nguồn/claim.

Git, YAML và JSON là lớp hạ tầng, không phải kiến thức bắt buộc của người dùng.

### 4.6 Registry và plugin — giai đoạn sau

Registry chỉ lưu metadata/package được người dùng tự nguyện công bố. Plugin có
thể mở rộng provider, bộ nhập, exporter, pack và evaluator. Không thiết kế
marketplace hoặc backend cộng đồng trước khi định dạng package và API plugin ổn
định.

## 5. Hợp đồng dữ liệu tối thiểu

Open Lesson Package v0.1 cần có:

```text
project/
  project.yaml
  sources/
    source-manifest.json
    extracted/
  brief.yaml
  claims.json
  artifacts/
    teacher-guide.md
    student-handout.md
    worksheet.md
    quiz.json
    answer-key.json
    rubric.json
  provenance.json
  eval/
    results.jsonl
    summary.json
    report.md
  build-manifest.json
```

Các ID phải ổn định khi sửa nội dung. Citation tham chiếu `source_id` cùng vị
trí trang/đoạn/chunk, không chỉ lưu URL. Artifact cho học sinh và đáp án phải là
hai đối tượng riêng để giảm nguy cơ xuất nhầm.

## 6. Lộ trình xây dựng

### Giai đoạn A — Contract-first foundation

**Mục tiêu:** ba repo nói cùng một ngôn ngữ dữ liệu.

Đầu ra:

- Open Lesson Package schema v0.1;
- ID, citation, provenance và build manifest conventions;
- 1 package hợp lệ tối thiểu, 5 package lỗi có chủ đích;
- validator CLI;
- ADR cho local-first, provider boundary và versioning.

Điều kiện hoàn thành:

- schema validation có test tự động;
- fixture lỗi thất bại đúng mã lỗi;
- `lessonforge` tạo package mà `EduEvals` đọc được không cần chuyển đổi thủ công;
- export rồi import lại không mất dữ liệu canonical.

### Giai đoạn B — Source workspace

**Mục tiêu:** biến nguồn người dùng thành corpus cục bộ có thể truy lại.

Đầu ra:

- nhập PDF, DOCX, Markdown/text; URL là adapter riêng;
- extraction giữ trang/đoạn và file gốc;
- source manifest, checksum và trạng thái license;
- tìm kiếm lexical cục bộ trước, embedding là tùy chọn;
- source viewer/API mở đúng vị trí citation;
- chống prompt injection ở ranh giới source/instruction.

Điều kiện hoàn thành:

- citation resolver mở đúng fixture trong mọi định dạng hỗ trợ;
- thêm lại cùng một file được phát hiện bằng hash;
- không có mạng khi chạy chế độ local với file local;
- người dùng thấy outbound preview trước mọi lời gọi cloud.

### Giai đoạn C — Generation vertical slice

**Mục tiêu:** tạo một package nhiều artifact từ brief và nguồn.

Đầu ra:

- brief có cấu trúc;
- chọn pedagogy pack;
- source retrieval có giới hạn;
- tạo tuần tự outline → claims → teacher guide → student handout → quiz/đáp
  án/rubric;
- phê duyệt/khóa từng chặng;
- regenerate theo block;
- lập `content-depth-plan` trước prose, chọn voice profile theo loại artifact;
- biên tập anti-slop sau khi nội dung đủ và kiểm tra giữ nguyên nghĩa;
- ít nhất một cloud provider và một OpenAI-compatible local adapter.

Điều kiện hoàn thành:

- mọi artifact đạt schema;
- mỗi claim được tạo có citation hoặc trạng thái `unsupported` rõ ràng;
- đổi provider không đổi hợp đồng output;
- chạy lại cùng input lưu được đầy đủ build provenance;
- lỗi model/JSON không làm hỏng package đã có.

### Giai đoạn D — Quality gate kỹ thuật

**Mục tiêu:** bắt lỗi có thể kiểm tra được trước khi xuất.

Đầu ra:

- deterministic checks;
- ma trận liên kết artifact;
- rule chống đáp án lọt sang bản học sinh;
- cảnh báo citation thiếu/hỏng và claim mâu thuẫn;
- baseline/regression suite dùng fixture Vật lí và fixture tổng quát;
- quality report HTML/Markdown dễ đọc.

Điều kiện hoàn thành:

- bắt 100% fixture P0 đã định nghĩa trước;
- không cho `release` nếu còn lỗi schema, citation hỏng, secret hoặc answer leak;
- warning model-assisted luôn hiển thị bằng chứng và có thể được người dùng bác
  bỏ kèm lý do;
- kết quả eval tái lập được ở lớp deterministic.

### Giai đoạn E — Lesson Studio local

**Mục tiêu:** người không biết CLI/Git dùng được vertical slice.

Đầu ra:

- tạo dự án, thêm nguồn, nhập brief;
- duyệt outline/claim;
- editor theo block + citation panel;
- màn hình eval/review;
- export package và Markdown/JSON;
- cài đặt provider/secret cục bộ;
- autosave, backup và phục hồi phiên.

Điều kiện hoàn thành:

- toàn bộ happy path chạy được không mở terminal;
- crash/restart không mất bản đã duyệt;
- UI không hiển thị secret trong log/export;
- một bộ usability test nội bộ theo kịch bản hoàn thành được. Đây là kiểm thử
  phần mềm, không phải xác nhận của giáo viên.

### Giai đoạn F — Export và khả năng tương tác

**Mục tiêu:** đầu ra dùng được ngoài hệ sinh thái.

Thứ tự:

1. DOCX;
2. PDF;
3. PPTX;
4. Moodle XML hoặc QTI sau khi khảo sát nhu cầu kỹ thuật;
5. template exporter/plugin API.

Điều kiện hoàn thành:

- kiểm tra snapshot/visual cho từng exporter;
- citation và cấu trúc không mất khi xuất;
- answer key không bị ghép vào bản học sinh;
- một package có thể được mở lại và xuất bằng provider khác.

### Giai đoạn G — Packs, plugin và cộng đồng

Chỉ bắt đầu khi A–F ổn định:

- pack môn/cấp học có schema và version;
- plugin SDK + compatibility tests;
- registry metadata tùy chọn;
- ký/checksum package;
- workflow fork/diff/review/merge;
- quy trình báo lỗi, thu hồi pack và migration.

Thẩm định giáo viên và classroom pilot được mở lại ở giai đoạn này hoặc sớm hơn
khi nguồn lực khả dụng. Nó quyết định nhãn chất lượng và hướng cải thiện sản
phẩm, nhưng không phủ nhận các kết quả kiểm thử kỹ thuật đã hoàn thành.

## 7. Ba milestone thực thi gần nhất

### Milestone 1 — Package chạy xuyên ba repo

- chốt schema v0.1;
- nâng `lessonforge` từ `lesson.md` đơn lẻ thành package tối thiểu;
- thay placeholder của EduEvals bằng schema/citation/link validators;
- dùng package Vật lí hiện có làm fixture, không tiếp tục biên soạn nội dung;
- thêm test tích hợp `lessonforge → EduEvals`.

### Milestone 2 — Nguồn và provenance thật

- nhập PDF/DOCX/Markdown;
- chunk có vị trí, hash và metadata;
- claim map và citation resolver;
- outbound preview và chế độ local không mạng;
- test prompt injection, file lỗi, OCR thiếu và nguồn trùng.

### Milestone 3 — Tạo nhiều artifact có kiểm soát

- brief → outline → claims → artifact;
- approve/lock/regenerate block;
- quiz, đáp án và rubric tách riêng;
- depth plan, artifact voice profile và semantic-preservation gate;
- prototype `own-voice` và `designed-role` local; chưa phát hành character pack
  mô phỏng người thật/nhân vật có bản quyền;
- quality report;
- một cloud adapter và một local adapter qua cùng interface.

**Đã đặt nền ngày 11/08/2026:** `pedagogy-skill` đã được tách thành router và các lớp
`content-depth`, `artifact profile`, `Vietnamese anti-slop`, `semantic preservation`,
`role/voice profile`. `lessonforge` không còn nạp toàn bộ reference vào mọi prompt; runtime chọn
profile theo `claims`, `teacher-guide`, `student-handout`, `worksheet`, `quiz`, `answer-key` và
`rubric`. Phần còn lại của Milestone 3 là biến depth plan/voice profile thành dữ liệu có schema,
thêm quality report và cho người dùng chọn persona trong brief/UI.

**Bổ sung ngày 12/08/2026:** thêm lớp `argument-thread-and-emphasis` giữa depth plan và artifact
profile. Lớp này bắt buộc xác định nghịch lí mở đầu, câu hỏi xuyên bài, điểm neo, bước ngoặt, câu
chốt và chuyển giao; đồng thời giới hạn điểm nhấn thị giác theo cấp độ nội dung. Mục tiêu là tránh
đầu ra “đủ mục nhưng phẳng”, trong đó các đoạn đúng riêng lẻ nhưng không tích lũy thành một lập luận.

**Bổ sung UI ngày 12/08/2026:** thêm profile runtime `learning-ui` và lớp
`references/10-quy-chuan-ui-hoc-lieu.md`. Lớp này khóa hợp đồng bố cục trước khi sinh mã, cấm căn
badge/prose bằng absolute + chiều cao ép, yêu cầu Grid co được với `minmax(0, 1fr)`, kiểm tra sáu
viewport, trạng thái bàn phím, reduced motion, CLS và ngân sách tối đa hai animation chính mỗi view.
Design system của sản phẩm được lưu theo `design-system/learning-ui/MASTER.md` + page overrides từ
`assets/mau-design-system-hoc-lieu.md`, để Agent không tự chọn lại spacing, typography, component và
motion ở mỗi lần tạo UI. Quy tắc được chắt lọc từ Hallmark và UI/UX Pro Max, nhưng ưu tiên riêng cho
học liệu có nguồn, bài đọc dài và công cụ giáo viên thay vì áp mặc định claymorphism/gamification.

**Tích hợp Hallmark ngày 12/08/2026:** thêm `references/11-tich-hop-hallmark.md` vào router của
`pedagogy-skill`. Mọi đầu ra HTML/trang web phải dùng Hallmark khi skill khả dụng để chọn genre,
macrostructure, token, typography, nav/footer và chạy anti-slop; Learning UI vẫn giữ quyền ưu tiên
về sư phạm, accessibility, responsive và preference người dùng. Mỗi trang có profile riêng trong
`design-system/learning-ui/pages/` và lịch sử cấu trúc trong `.hallmark/log.json`.

**Bổ sung Style Control Matrix ngày 12/08/2026:** thêm `references/12-ma-tran-kiem-soat-phong-cach.md`
và `assets/mau-style-card.yaml`. Hệ thống tách `Technical Baseline` bắt buộc khỏi `User Style Layer`;
chỉ học thuật ngữ, nhịp câu, ưu tiên thông tin và thói quen tổ chức ý từ mẫu có provenance. Cấu trúc
được chọn theo artifact thay vì ép một template kỹ thuật cho mọi giáo án, bài học hoặc báo cáo.

**Tham khảo `vietnamese-docs-style` ngày 12/08/2026:** thêm lớp tùy chọn
`references/13-bien-tap-tieng-viet-theo-profile.md` cho tài liệu kỹ thuật, báo cáo và văn bản trang
trọng. Tiếp nhận profile routing, placeholder có nhãn, phân biệt dữ kiện–nhận định–kiến nghị và yêu
cầu render DOCX; không nhập mặc định thể thức NĐ30 và không cho phép AI bù chi tiết thiếu bằng số
liệu, tên riêng hoặc nguồn tự tạo.

Thiết kế chi tiết lớp chiều sâu/văn phong và đánh giá hai dự án tham khảo nằm
tại [`danh-gia-skill-van-phong-va-chieu-sau.md`](danh-gia-skill-van-phong-va-chieu-sau.md).
Thiết kế persona, voice profile và đánh giá `claude-skills`, `AuthorAgent`,
`ghostwriter` nằm tại
[`danh-gia-persona-va-ghostwriter.md`](danh-gia-persona-va-ghostwriter.md).

Sau Milestone 3 mới quyết định làm UI ngay hay hoàn thiện exporter trước dựa
trên mức ổn định của hợp đồng dữ liệu.

## 8. Backlog ưu tiên

### P0 — nền móng

- schema và versioning;
- package reader/writer;
- stable IDs;
- source/citation model;
- deterministic validators;
- tích hợp ba repo trong CI;
- secret/privacy tests;
- fixture không phụ thuộc một môn học.

### P1 — tạo tài liệu hữu dụng

- ingest/extract;
- retrieval;
- structured generation;
- content-depth schema và voice profile theo artifact;
- block revision;
- Vietnamese anti-slop audit và semantic-preservation check;
- `Role & Voice Studio`: own voice, designed role, A/B preview và drift report;
- quality report;
- DOCX export;
- local UI happy path.

### P2 — mở rộng

- PPTX/PDF fidelity cao;
- OCR nâng cao;
- nhiều provider;
- plugin SDK;
- pack registry;
- Git sync qua UI;
- LMS export;
- media/audio/video.

Không ưu tiên số lượng provider, video hoặc marketplace trước P0/P1.

## 9. Kiểm thử khi chưa có giáo viên thẩm định

Vẫn có thể kiểm thử nghiêm túc ở bốn cấp:

1. **Unit:** schema, parsing, chunking, ID, citation resolver, policy.
2. **Contract:** cùng package chạy được qua các repo/phiên bản.
3. **Integration:** nguồn → generation → eval → export → import lại.
4. **Adversarial fixtures:** claim sai, nguồn mâu thuẫn, prompt injection, đáp án
   lọt bản học sinh, citation hỏng, file có dữ liệu nhạy cảm.

Kết quả chỉ chứng minh hành vi phần mềm. Các fixture AI hoặc do đội phát triển
viết phải mang nhãn `synthetic`/`internal`, không được nâng thành bằng chứng
giáo dục.

## 10. Chỉ số trong giai đoạn công cụ

- tỷ lệ package hợp lệ qua schema;
- tỷ lệ citation resolve đúng fixture;
- tỷ lệ fixture P0 bị chặn;
- tỷ lệ round-trip không mất dữ liệu;
- thời gian và bộ nhớ ingest/generate/eval;
- tỷ lệ run có provenance đầy đủ;
- số provider vượt contract test;
- tỷ lệ test chạy được hoàn toàn local;
- số lần migration thành công giữa schema versions;
- crash/data-loss/secret-leak count.

Không dùng điểm hài lòng giả lập, thời gian của persona AI hoặc điểm học tập mô
phỏng làm KPI.

## 11. Các quyết định cần chốt trong Milestone 1

1. Spec nằm trong repo hiện tại hay package Python riêng trong giai đoạn đầu.
2. Canonical document model: Markdown + sidecar JSON hay document AST.
3. Citation locator chuẩn cho PDF/DOCX/HTML.
4. Package là thư mục hay file nén có manifest/checksum.
5. Cách đồng bộ version giữa `lessonforge`, `EduEvals` và `pedagogy-skill`.
6. UI desktop hay local web app sau khi CLI ổn định.

Mặc định đề xuất: giữ spec trong workspace hiện tại, dùng Markdown + JSON
sidecar, package dạng thư mục trong lúc phát triển, semantic versioning và local
web app trước desktop packaging.

## 12. Điều kiện mở lại thẩm định giáo viên

Mở lại khi có ít nhất một trong các điều kiện:

- vertical slice đã ổn định và cần biết workflow có dùng được không;
- cần quyết định giữa hai thiết kế UI hoặc hai artifact format;
- chuẩn bị gắn nhãn `Teacher-reviewed`/`Classroom-tested`;
- có đối tác/trường/giáo viên tự nguyện tham gia và quy trình dữ liệu phù hợp.

Khi chưa có các điều kiện này, backlog thẩm định được giữ ở trạng thái
`parked — external validation unavailable`, không phải `failed` và không chặn
Milestone 1–3.
