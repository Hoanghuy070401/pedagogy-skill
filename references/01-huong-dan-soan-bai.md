<!-- Nguồn: schoolAI-deploy/website/HUONG-DAN-SOAN-BAI.md (copy nguyên bản).
     Phần sư phạm và văn phong (§3, §5, §6) dùng được ở mọi dự án.
     Phần kỹ thuật riêng SchoolAI — đọc có chọn lọc khi mang đi:
       §0.1  kiến trúc MDX (Git) → content release (Supabase); dự án khác bỏ qua, giữ nguyên tắc
             "một nguồn sự thật duy nhất, không sửa tay ở bản phát hành".
       §1    cấu trúc thư mục Docusaurus.
       §2,§4 tên component cụ thể — xem ../assets/component-kit.md để map sang stack khác.
       lệnh  npm run lint:mdx / lint:lessons:strict / guard-svg → thay bằng cổng lint tương đương. -->

# Hướng dẫn soạn bài học (Lesson Kit)

> Chuẩn dựng bài cho các roadmap nghề. **Bài mẫu tham chiếu:** [docs/frontend/fe-dns-ten-mien.mdx](docs/frontend/fe-dns-ten-mien.mdx)
> — dùng làm khuôn cho **mọi bài KHÔNG chứa code/giải thuật** (bài khái niệm).

## 0. BẮT BUỘC MỌI AGENT khi soạn / sửa bài (đọc trước khi viết)

Áp dụng cho **mọi** file `.mdx` bài học, deep-dive ngành, quiz explain, copy UI học.
Agent **không được** bỏ qua. Chi tiết đầy đủ ở **§5–§6**; đây là bản tóm bắt buộc:

| # | Rule | Không được |
|---|---|---|
| 1 | **Viết tắt / thuật ngữ chuyên ngành** (§6.1) — lần đầu phải có nghĩa tiếng Việt dễ hiểu trong ngoặc | Câu nén ≥3 thuật ngữ không giải; giải nghĩa bằng một thuật ngữ khó khác |
| 2 | **Quy trình ≥3 bước** → sơ đồ (`FlowDiagram` / GridCards / ComparisonPanel / Mermaid) | Một đoạn văn = cả pipeline |
| 3 | **Không card/mục trống nghĩa** — meta “neo research”, “Chuẩn ngành” chung chung | Thẻ trang trí không việc/số |
| 4 | **Câu chuyện / ví dụ** — thông điệp + bối cảnh (ai·lúc nào·user thấy) + bước; ưu tiên vẽ | Kể đại 4–5 câu acronym |
| 5 | **Văn phong người** (§5) — tiếng Việt đời thường, không sáo | Giọng dịch-máy / bộ-ba-AI |
| 6 | **Component MDX** — chỉ dùng component đã đăng ký `MDXComponents` + có policy trong `scripts/content/normalize.mjs` | JSX lạ làm **vỡ import** content release |
| 7 | **Đủ sâu, đủ lõi** (§6.5) — giải thích cặn kẽ từ nền tảng đến cách dùng, có ví dụ và bẫy thường gặp | Bài làm cho có, lướt khái niệm, mục tiêu nêu ra nhưng không dạy đủ |
| 8 | **Trực quan, cụ thể** (§6.5) — cho người học thấy đầu vào → biến đổi/trạng thái → đầu ra bằng sơ đồ, ví dụ hoặc đối chiếu | Mô tả trừu tượng, ẩn dụ mơ hồ, nói “hệ thống xử lý” nhưng không chỉ ra xử lý gì |
| 9 | **Nguồn bên thứ ba chỉ ở tài liệu tham khảo** (§6.6) — nội dung bài phải đứng độc lập, nói thẳng với học viên. Attribution/giấy phép chỉ ở `website/docs/intro.mdx` (`/gioi-thieu`); cấm comment `LICENSE`, `CC-BY`, `Brief:` và đường dẫn `research/...` trong bài. `npm run lint:lessons:strict` là cổng chặn. | “Theo roadmap…”, “dựa trên nguồn…”, `LICENSE`, `Brief: research/...`, hoặc kể quy trình biên soạn trong bài |
| 10 | **Không sửa định danh máy** (§6.1) — `id`, slug, URL, path, prop kỹ thuật và code chỉ dùng ký tự hợp lệ | Nhét nghĩa trong ngoặc hoặc dấu `/` vào `id`, làm Docusaurus không build được |
| 11 | **Lộ trình từ link người dùng cung cấp** (§6.7) — lập danh mục đầy đủ theo thứ tự/phạm vi gốc trước khi soạn; dùng checklist trạng thái nếu triển khai nhiều lượt | Tự rút gọn, bỏ/gộp bài vì lộ trình dài, hoặc tiếp tục soạn mà không đối chiếu phần còn thiếu |
| 12 | **Nhịp bài học & tương tác** (§6.8) — hook → hiểu → thử → phản hồi → áp dụng; từng ý lớn có tự kiểm | Dồn tương tác ở cuối, viết liên tục quá lâu, hình chỉ để trang trí, hoặc kết bài cụt |
| 13 | **Mục tiêu → dạy → luyện → đánh giá** (§6.9) — mỗi năng lực đầu ra phải được dạy, thực hành và kiểm tra tương ứng | Mục tiêu “treo”, quiz hỏi ngoài bài, hoặc thực hành không đo năng lực đã nêu |
| 14 | **Phạm vi, thời lượng & tiên quyết** (§6.9) — 1–3 năng lực chính, core hướng tới 10–20 phút; bài dài phải tách mà không mất roadmap | Nhồi nhiều mục tiêu vào một bài hoặc dùng kiến thức chưa được dạy |
| 15 | **Ví dụ kỹ thuật phải kiểm chứng** (§6.9) — chạy thử khi có thể, ghi rõ mã giả/mô phỏng và phạm vi phiên bản | Bịa output, đưa code không chạy như code thật, hoặc dùng hướng dẫn đã lỗi thời |
| 16 | **Quiz/challenge có phản hồi học được** (§6.9) — hỏi đúng nội dung, giải thích lý do, sai vì hiểu lầm thật | Câu mẹo, đáp án chỉ báo đúng/sai, hoặc lựa chọn sai vô nghĩa |
| 17 | **QA trực quan, khả năng tiếp cận & đa nền tảng** (§6.9) — kiểm desktop/mobile, bàn phím, mô tả chữ và fallback | Sơ đồ tràn/vỡ, tương tác mất nghĩa trên mobile, hoặc chỉ truyền ý bằng màu/hình |
| 18 | **Kiểm chứng với người học** (§6.9) — walkthrough trước phát hành; sau phát hành dùng dữ liệu hành vi để cải thiện | Tuyên bố “giữ chân tốt” chỉ từ cảm giác người soạn |

**Test nhanh trước khi xong:** học viên đọc to được luồng, kể lại 3–5 câu bằng lời, giải thích được
ý cốt lõi và mang đi được 1 việc/số/quyết định — **không** cần Google viết tắt hoặc tự tìm một bài
khác để lấp phần kiến thức nền còn thiếu.

### 0.1 MDX và dữ liệu Supabase (agent cần biết)

| Lớp | Vai trò | Sửa MDX có đụng? |
|---|---|---|
| **Track legacy** | Git MDX là nguồn nhập; pipeline chuyển MDX thành JSON blocks | Chỉ sửa MDX, sau đó build release |
| **Track `studio_canonical` / nội dung mới** | Studio/Postgres giữ bản JSON canonical của revision | Review và preview đọc JSON revision |
| **Content release** (`content_releases` / lessons / blocks) | JSON immutable cho web/mobile đọc release `published` | Không edit tay DB; đi qua `parse/validate → candidate → publish` |
| **Supabase user data** (progress, comments, settings, auth) | Học viên | **Không** dính nội dung bài |

- Sửa prose / sơ đồ / thẻ trong MDX **không** phá schema BE, **không** cần migration.
- Nội dung mới lên mobile/runtime Supabase chỉ sau **publish content release** (immutable). Chưa publish = web Git/Docusaurus vẫn là nơi học chính.
- Component trong bài (`FlowDiagram`, `GridCards`, `ComparisonPanel`, `QuizBox`…) đã có **map** trong normalizer → thành block JSON. Component **chưa** có policy → pipeline **throw** (fail import). Interactive (`TerminalDemo`, runners…) → `stub` trên mobile.
- Với Studio, JSON revision là dữ liệu dùng cho preview, content review và mobile. Nếu chưa chuẩn hóa
  thành JSON hợp lệ thì phải chặn revision, không review lại từ một chuỗi MDX khác.
- **Không** hand-edit Dashboard Supabase để “sửa bài”. Sửa = Git → publish release mới.
- Repo có **CI GitHub Actions** (`.github/workflows/ci.yml`) — mọi push/PR vào `main` chạy toàn bộ
  cổng lint (`lint:mdx`, `lint:routes`, `lint:lessons[:strict]`, `guard-svg`) + unit test + smoke
  release (build + validate dry-run, không đụng Supabase) + build site. Local vẫn có pre-hook npm
  như cũ: `prestart`/`predev`/`prebuild` chạy lint, còn chuỗi publish
  (`npm run content:publish[:mobile][:dry]`) tự lint + build lại từ MDX qua `precontent:*`. Version
  release tự sinh theo ngày (CalVer `YYYY.MM.DD.N`), phát hành lần 2+ trong ngày thì truyền
  `--version` tay; cờ `--allow-stale-commit` chỉ dùng khi cố ý publish artifact lệch HEAD. Chi tiết:
  `scripts/content/README.md`.

## 1. Cấu trúc thư mục

```
src/components/            ← chia theo MODULE (không để phẳng)
  lesson/                  ← BỘ DỰNG BÀI dùng chung: Figure, FlowDiagram, TerminalDemo,
                             QuizBox… (+ index.js barrel) — đăng ký MDX toàn cục.
                             LessonCheckpoint (lưu tiến độ) do theme tự render — không dùng trong MDX
  roadmap/                 ← RoadmapView, WorldMap, PracticeEnv, DestinationLanding,
                             DestinationPicker, DestinationSwitcher, ReviewQueue
  dsa/                     ← PythonRunner, Quiz, StepThrough, GuessGame, AlgoVisualizer,
                             Term, DocThem, VisuAlgoLink, ForgettingCurve, MazeGame
  app/                     ← AuthButton, Comments, Hero, LessonProgress
src/theme/MDXComponents.js ← ĐĂNG KÝ TOÀN CỤC lesson kit → .mdx dùng thẳng, KHÔNG cần import
src/data/quizzes.js        ← Kho câu hỏi legacy; không phải nguồn bắt buộc cho Studio canonical
src/data/roadmaps/<nghề>.js← sơ đồ node của từng nghề (+ ico) → route /nghe/{id} TỰ SINH
src/data/destinationLandings.js ← SEO landing đích đến → route /dich-den/{slug} TỰ SINH
src/data/exercises.js      ← bài luyện → route /luyen-tap/{id} TỰ SINH
src/lib/                   ← logic (analytics, grade, review, streak, pyodide, maze)
src/contexts/              ← state (Auth, Destination)
docs/<nghề>/<node>.mdx     ← nội dung mỗi bài (viết tay; màn hình template fill data)
```

### 1.1 Màn hình = fill data (không viết page mới)

| Cần thêm | Chỉ việc | Không làm |
|----------|----------|-----------|
| Nghề mới | `src/data/roadmaps/<id>.js` + MDX bài + `npm run generate-data` | Tạo `src/pages/nghe/<id>.js` |
| Landing đích đến | Object trong `destinationLandings.js` | Tạo `src/pages/dich-den/*.js` |
| Bài luyện code | Object trong `exercises.js` | Tạo page luyện mới |

Route do plugin trong `docusaurus.config.js` sinh. Chi tiết: `../doc/plans.md` (#personalization-plan) §5.

### 1.2 Rubric sư phạm

Xem **[HUONG-DAN-PEDAGOGY.md](HUONG-DAN-PEDAGOGY.md)** — mục tiêu observable, 3 tầng evidence, checklist ship.

### 1.3 Research corpus (cào nguồn — không publish nguyên văn)

Khi soạn / viết lại bài Frontend, đọc brief đã scrape:

```
research/frontend/briefs/<nodeId>.json
```

- `sources[].url` → mục **Đọc thêm**
- `headings` / `keyPoints` / `excerpt` → chỉ để **hiểu & viết lại 100% tiếng Việt**
- Không paste `excerpt` vào MDX publish
- Tên nguồn, roadmap, website hoặc tài liệu bên thứ ba chỉ xuất hiện trong mục **Đọc thêm / Tài liệu
  tham khảo**. Không đưa lời kể về nguồn hay quy trình lấy dữ liệu vào phần giảng dạy.

Cào lại / node mới: xem `research/README.md` (`build-sources-map` + `scrape-sources`).

## 2. Bộ component dùng chung (đã đăng ký toàn cục — dùng thẳng trong .mdx)

Không cần `import`. Dùng trực tiếp:

| Component | Dùng để | Ví dụ |
|---|---|---|
| `<FlowDiagram>` | Sơ đồ luồng động (trạm tròn nối tiếp) | `<FlowDiagram caption="…" back={{label:'IP ✓'}} stations={[{ico:'🧑‍💻',title:'Bạn',sub:'trình duyệt'}]} />` |
| `<FlowDiagram variant="pill">` | Chuỗi segment màu nối tiếp có nhãn (tên miền, semver, quy tắc CSS) | `<FlowDiagram variant="pill" separators={['.','.']} segments={[{txt:'blog',tone:'purple',label:'subdomain'}]} />` |
| `<ComparisonPanel>` | So sánh 2-3 hộp cạnh nhau (trước/sau, A vs B) | `<ComparisonPanel arrow={{label:'push / pull'}} items={[{title:'Git',tone:'primary',points:['…']}]} />` |
| `<GridCards>` | Lưới thẻ icon/tiêu đề/mô tả | `<GridCards cards={[{ico:'👁️',title:'Khiếm thị',desc:'…',tone:'primary'}]} />` |
| `<LayerStack variant="nested">` | Hộp lồng nhau (box model, cấu trúc lồng) | `<LayerStack layers={[{label:'margin',tone:'gold',dashed:true},{label:'content',sub:'…',tone:'blue'}]} />` |
| `<LayerStack variant="pyramid">` | Kim tự tháp phân tầng (testing pyramid…) | `<LayerStack variant="pyramid" sideLabels={{top:'chậm,đắt',bottom:'nhanh,rẻ'}} layers={[{label:'E2E',tone:'gold'}]} />` |
| `<ThresholdMeter>` | Ngưỡng đo lường theo mức (Tốt/Cần cải thiện/Kém) | `<ThresholdMeter metrics={[{key:'LCP',zones:[{range:'≤2.5s',label:'Tốt',tone:'primary'}]}]} />` |
| `<ThresholdMeter variant="ladder">` | Thang xếp hạng độ mạnh (specificity CSS…) | `<ThresholdMeter variant="ladder" sideLabel="mạnh hơn" items={[{code:'#header',tag:'id',tone:'purple'}]} />` |
| Mermaid (```mermaid) | Cây phân cấp cha-con (DOM tree, file tree…) | xem mục 4 — dùng thay vì tự vẽ SVG tree |
| `<Figure>` | Bọc sơ đồ tự vẽ tay (SVG hiếm gặp, không khớp component trên) | `<Figure caption="…"><svg>…</svg></Figure>` |
| `<TerminalDemo>` | Thực hành lệnh | `<TerminalDemo command="nslookup google.com" output={[{t:'Address: …', hl:true}]} />` |
| `<QuizBox>` | Rương ôn tập có dữ liệu ngay trong bài | `<QuizBox questions={[{"q":"…","choices":["…","…","…"],"answer":0,"why":"…"}]} />` |

**Không chèn tag đánh dấu hoàn thành.** `LessonCheckpoint` tự render cuối mọi bài qua
`src/theme/DocItem/Footer` và tự lưu tiến độ.

Đăng ký component mới vào `MDXComponents.js` **phải** kèm policy trong
`scripts/content/normalize.mjs` — test `tests/content-pipeline.test.mjs` tự fail khi hai danh
sách lệch nhau.

`tone` dùng chung cho Comparison/GridCards/LayerStack/ThresholdMeter: `primary` (xanh — đúng/tiến bộ),
`blue` (thông tin), `purple` (mốc/cấp độ), `gold` (thành tích/cảnh báo nhẹ), `coral` (sai/khẩn),
`neutral` (trung tính). Map thẳng biến `--as-*` đã có trong `custom.css` — không tự chọn màu hex mới.

Với bài do Studio/agent tạo, agent phải ghi `evidencePlan` trong JSON revision, gồm cả quyết định boss
chặng. Chỉ tạo câu hỏi inline khi đã đánh giá `needed=true` và `feasible=true`; mỗi câu phải có phản hồi sửa hiểu lầm.
Nếu nguồn quá ngắn, mục tiêu không đo được bằng quiz hoặc thiếu dữ liệu, được phép bỏ quiz nhưng
phải ghi lý do. `evidencePlan.boss` phải ghi `afterLessonNumber` và `mode` (`none`, `create`, hoặc `add`);
chỉ tạo/thêm boss khi đủ dữ liệu đánh giá tổng hợp. Không trỏ tới ngân hàng tĩnh như bằng chứng duy nhất.
Nếu nguồn gốc quá mỏng, agent được phép đề xuất nguồn Internet chính thống bổ sung qua `researchUrls`;
runner phải kiểm tra allowlist và tải lại trước khi soạn. Không dùng nguồn không kiểm chứng hoặc bịa nội dung.

## 3. Khung 1 bài khái niệm (theo bài mẫu DNS)

1. Frontmatter: `id`, `title`, `sidebar_label`, `description` (SEO), `tags`.
2. `:::info Bạn sẽ học được gì` — tóm 2-3 dòng.
3. **Mở bài có hook** — dùng tình huống, lỗi, câu hỏi, kết quả bất ngờ hoặc quyết định quen thuộc để
   tạo lý do học. Câu chuyện là một lựa chọn, không phải công thức bắt buộc.
4. Các mục nội dung — mỗi khái niệm 1 sơ đồ khi cần hình dung.
5. `## Thử ngay` — `<TerminalDemo>` khi có lệnh thực hành.
6. `## Ôn lại nhanh` — dùng `<QuizBox questions={…}/>` khi `evidencePlan.quiz.feasible=true`;
   nếu không đủ dữ liệu, ghi quyết định bỏ quiz trong JSON review, không tạo component rỗng.
7. `## Đọc thêm` — link nguồn chính thống.
8. **Không** chèn tag đánh dấu hoàn thành — `LessonCheckpoint` tự render cuối bài (xem §2).
9. **Không** thêm comment attribution/giấy phép riêng vào từng bài; nơi canonical duy nhất là
   `/gioi-thieu`.
Cuối cùng: đặt `href` của node trong `src/data/roadmaps/<nghề>.js`.

## 4. Vẽ sơ đồ / hình minh hoạ — chiến lược "sinh từ code, KHÔNG lưu asset"

Nguyên tắc (giữ source nhẹ, hạ tầng ~0): **mọi hình sinh từ code/text → SVG ngay trên trình duyệt,
KHÔNG lưu PNG/GIF/MP4** trong repo.

| Nhu cầu | Công cụ | Trạng thái |
|---|---|---|
| Sơ đồ luồng (bước → bước) | `<FlowDiagram>` | ✅ sẵn |
| Chuỗi segment nối tiếp có nhãn | `<FlowDiagram variant="pill">` | ✅ sẵn |
| So sánh 2-3 hộp cạnh nhau | `<ComparisonPanel>` | ✅ sẵn |
| Lưới icon/thẻ | `<GridCards>` | ✅ sẵn |
| Hộp lồng nhau / kim tự tháp phân tầng | `<LayerStack>` | ✅ sẵn |
| Ngưỡng đo lường / thang xếp hạng | `<ThresholdMeter>` | ✅ sẵn |
| Cây phân cấp cha-con, flowchart/sequence/ER/state/class | **Mermaid** (```mermaid code block) | ✅ **đã cài** (`@docusaurus/theme-mermaid`) |
| Sơ đồ tuỳ biến — KHÔNG khớp component/Mermaid nào ở trên | SVG tay trong `<Figure>` | ✅ sẵn (ngoại lệ có chủ đích, chạy `npm run guard-svg` để tự kiểm) |
| Phong cách vẽ tay (Wabi-Sabi, roadmap game) | **Rough.js** (~9KB) | thêm khi cần |
| Công thức toán (Big-O, xác suất) | **KaTeX** (remark-math) | thêm khi cần |

Trước khi tự vẽ `<svg>` tay: kiểm bảng trên trước — phần lớn hình lặp lại đã có component. Chạy
`npm run guard-svg` để phát hiện `<svg>` thô mới nằm ngoài `<Figure>` (không tính SVG trong `<Figure>`
hợp lệ hay trong prop demo như `<WebPlayground html={...}>`).

Ví dụ Mermaid (đã dùng được ngay, 0 asset):

    ```mermaid
    flowchart LR
      A[Bạn gõ URL] --> B[Resolver] --> C[Root] --> D[TLD] --> E[Authoritative] --> A
    ```

**Thư viện được phép thêm** (dự án phi lợi nhuận, ưu tiên nhẹ + tin cậy): chỉ thêm khi có nhu cầu
thật, ưu tiên lib render-từ-code (không kéo asset nặng). Ứng viên: Rough.js (vẽ tay), KaTeX (toán).
Tránh: thư viện kéo font/ảnh/video nặng, hoặc cần server.

## 5. Văn phong — viết như người thật (BẮT BUỘC mọi bài)

Phương pháp: [humanize-writing-skill](https://github.com/lguz/humanize-writing-skill) (MIT), adapt cho
tiếng Việt. Triết lý (Paul Graham): *"viết như một người thông minh đang nghĩ thành tiếng"*.

**Quy trình 3 lượt khi soạn & soát lại:**

1. **Bỏ chữ máy móc / giọng dịch-máy.** Tránh: "nhằm mục đích", "một cách", "đóng vai trò quan trọng",
   "vô cùng / hết sức", "đa dạng và phong phú", "nói chung là". Thay bằng từ đời thường, cụ thể —
   "giúp bạn" thay vì "đóng vai trò hỗ trợ".
2. **Phá cấu trúc rập khuôn (dấu hiệu AI):** đừng lặp mẫu "không phải X mà là Y"; tránh **bộ ba song
   song** (liệt kê 3 vế đối xứng cho sang); không lạm dụng gạch ngang và câu đối xứng gương. Câu hỏi
   tu từ rồi tự trả lời: dùng ĐƯỢC để dẫn dắt, nhưng đừng biến thành công thức lặp.
3. **Thêm chất người nhưng giữ trung thực:** **đổi độ dài câu** — xen câu ngắn đanh với câu dài
   (nhịp đều tăm tắp = máy viết). Dùng khẩu ngữ tự nhiên ("cứ", "thì", "nhé", "đấy", "mà"). Có thể
   đưa nhận xét có căn cứ hoặc tình huống minh hoạ; không bịa trải nghiệm cá nhân kiểu "mình từng
   mắc lỗi này" chỉ để giọng văn có vẻ thật. Cho phép vài ý mở, không cần chốt gọn mọi câu.

**Checklist trước khi xong 1 bài:**
- [ ] Đọc TO lên — nghe có tự nhiên như người nói không?
- [ ] Có câu ngắn đanh xen giữa các câu dài không?
- [ ] Không có bộ-ba-song-song / mẫu lặp máy móc?
- [ ] Có ≥1 ví dụ đời thường + ≥1 nhận xét có căn cứ hoặc tình huống minh hoạ trung thực?
- [ ] Xưng "bạn" nhất quán, gần gũi, không trịnh trọng?
- [ ] Không sáo rỗng ("vô cùng quan trọng", "một cách hiệu quả")?
- [ ] **Thuật ngữ / viết tắt** đã giải nghĩa (mục 6)?
- [ ] **Quy trình / bảng việc** đã là sơ đồ khi phù hợp (mục 6)?
- [ ] **Câu chuyện / ví dụ** có thông điệp + bối cảnh + bước, không kể đại (mục 6.4)?
- [ ] Nội dung đã đủ sâu và đủ các ý cốt lõi; không có đoạn viết cho đủ mục (mục 6.5)?

## 6. Thuật ngữ, viết tắt & sơ đồ quy trình (BẮT BUỘC mọi bài)

Áp dụng cho **mọi** MDX bài học, deep-dive ngành, quiz explain, và copy UI học tập. Học viên không
được đoán nghĩa từ viết tắt.

### 6.1 Viết tắt & thuật chuyên ngành — luôn có nghĩa

**Mặc định bắt buộc:** coi người học **chưa biết bất kỳ từ chuyên ngành hoặc viết tắt tiếng Anh nào**.
Agent không được tự cho rằng `JS`, `TS`, `OS`, `UI`, `API`, `SDK`, `RN`, `OTA`, `Native`, `runtime`…
“đã quá phổ biến nên khỏi giải thích”. Không giải nghĩa đúng chỗ = bài chưa hoàn thành.

1. **Lần xuất hiện đầu** trong bài (hoặc trong mỗi khối độc lập: sơ đồ, thẻ, bảng): mọi từ viết tắt,
   từ tiếng Anh và thuật ngữ chuyên ngành mà người mới có thể chưa biết phải kèm nghĩa tiếng Việt
   dễ hiểu **ngay trong dấu ngoặc**. Ví dụ: `Dart (ngôn ngữ lập trình dùng để xây ứng dụng Flutter)`,
   `Flutter (bộ công cụ tạo ứng dụng chạy trên nhiều nền tảng)`, `CI (quy trình tự động kiểm tra và
   build code)`.
2. **Ưu tiên tiếng người trước** khi có thể: tiêu đề trạm/sơ đồ dùng nghĩa dễ hiểu; viết tắt để
   `sub` / ngoặc: `{ title: 'Gộp code', sub: 'PR' }` thay vì `{ title: 'PR', sub: '…' }` nếu học viên
   mới chưa biết PR.
3. **Không** nhét ≥3 viết tắt / jargon trong **một câu** mà không giải nghĩa từng cái.
4. Lặp lại trong bài: có thể rút gọn sau khi đã giải lần đầu **trong cùng mục**. Mục mới (sơ đồ
   khác, bảng khác) — giải lại ngắn nếu người đọc có thể nhảy mục.
5. Ngoại lệ hẹp: tên riêng sản phẩm đã phổ biến trong ngữ cảnh vừa giải (Docker, Terraform) — vẫn
   nên 1 cụm “là gì” lần đầu trên bài mở đầu nghề.
6. **Giải nghĩa theo mức người mới.** Phần trong ngoặc phải trả lời ngắn gọn “đây là gì / dùng để làm
   gì” bằng từ quen thuộc. Cấm định nghĩa vòng tròn hoặc thay một từ khó bằng từ khó khác, ví dụ
   `runtime (môi trường runtime)` là **không đạt**. Viết `runtime (môi trường chạy chương trình)`.
7. **Không bắt người học đi tìm nghĩa ở nơi khác.** Bảng thuật ngữ và tooltip chỉ là phần hỗ trợ;
   chúng không thay thế nghĩa trong ngoặc ở lần xuất hiện đầu tiên của bài, sơ đồ, card hoặc bảng.
8. **Mỗi khối đọc độc lập phải tự đủ nghĩa.** Bảng, sơ đồ, card, callout, caption và quiz có thể được
   học viên đọc riêng. Thuật ngữ xuất hiện lần đầu trong từng khối này phải được giải nghĩa lại, dù đã
   giải ở đoạn văn phía trên.
9. **Tiếng Việt đứng trước trong tiêu đề và nhãn.** Cấm nhãn nén kiểu `1 codebase 2 OS`, `Hire pool
   web`, `UI pixel-OS`, `Module native lạ`. Phải viết `Một bộ mã nguồn cho hai hệ điều hành`, `Khả
   năng tuyển người đã biết web`, `Mức độ giống giao diện hệ điều hành`.
10. **Không có “jargon trần”.** Trong nội dung dành cho người mới, mỗi thuật ngữ khó phải được giải
    nghĩa ngay tại lần xuất hiện đầu của khối; không còn ngưỡng cho phép “dưới 3 từ khó”. Quy tắc cấm
    ≥3 jargon trong một câu vẫn là chốt phụ, không phải giấy phép để để lại 1–2 từ chưa giải.
11. **Không nén nghĩa vào ngoặc khó đọc.** Nếu một ô bảng cần giải thích dài hơn khoảng một câu ngắn,
    hãy đổi bảng thành `ComparisonPanel`/`GridCards` hoặc đặt phần giải thích ngay dưới bảng. Không
    nhồi 4–5 thuật ngữ và nhiều dấu `/` vào một ô.
12. **Từ đánh giá phải có tiêu chí và hệ quả.** `Có`, `Không`, `cao`, `thấp`, `tốt nhất`, `không
    chuẩn`, `nhanh`, `nặng` là chưa đủ nếu người mới không biết đang đo gì. Phải nói rõ điều kiện hoặc
    hệ quả, ví dụ: `Có — phần giao diện và logic dùng chung; tính năng thiết bị vẫn có thể cần mã riêng`.

#### 6.1.1 Ngoại lệ bắt buộc: không giải nghĩa trong định danh máy

Quy tắc “giải nghĩa trong ngoặc” **chỉ áp dụng cho chữ mà học viên đọc**. Tuyệt đối không chèn phần
giải thích vào dữ liệu kỹ thuật hoặc chuỗi mà chương trình dùng để định danh.

- Frontmatter `id` chỉ dùng chữ thường không dấu, số và dấu gạch ngang; phải khớp biểu thức
  `^[a-z0-9]+(?:-[a-z0-9]+)*$`. Ví dụ đúng: `id: and-lifecycle`.
- `id` **không được** có khoảng trắng, `/`, `\\`, ngoặc, dấu tiếng Việt, dấu hai chấm hoặc phần chú
  thích. Ví dụ sai: `id: and-lifecycle (vòng đời app/màn)`.
- Không tự đổi `id` đã tồn tại để “dễ hiểu hơn”; `id` còn được roadmap, quiz, tiến độ và liên kết dùng.
- Quy tắc tương tự áp dụng cho slug, URL, đường dẫn file, `lessonId`, `checkpointId`, key dữ
  liệu, tên biến, tên hàm, tên component, import và nội dung code mẫu.
- Muốn diễn giải cho người học, đặt nghĩa trong `title`, `sidebar_label`, đoạn văn hoặc caption hiển
  thị — **không** đặt vào `id` hay prop định danh.

**Trước khi lưu MDX:** tách rõ hai lớp:

| Lớp | Ví dụ | Có thêm nghĩa trong ngoặc? |
|---|---|---|
| Chữ học viên đọc | `Dart`, `runtime`, caption sơ đồ | Có, ở lần xuất hiện đầu |
| Định danh máy | `id: fl-dart-basics`, `lessonId="fl-dart-basics"` | Không bao giờ |
| Code/lệnh/URL | `onCreate()`, `/mobile/android/...` | Giữ nguyên cú pháp; giải thích ở câu bên ngoài |

#### 6.1.2 Cú pháp MDX phải nguyên vẹn

MDX vừa là Markdown vừa hiểu JSX và biểu thức JavaScript. Một ký tự thiếu có thể làm toàn site không
build được, nên agent phải giữ đúng các ranh giới sau:

1. **Tag HTML/JSX dùng làm chữ phải bọc backtick.** Viết `` `<picture>` ``, `` `<iframe>` `` hoặc
   `` `<img>` `` khi đang nhắc tên thẻ trong câu. Viết `<picture>` trần khiến MDX tưởng đó là tag mở
   và chờ `</picture>`.
2. **Ví dụ code nhiều dòng phải nằm trong fenced code block** (ba backtick + ngôn ngữ). Không thả
   trực tiếp HTML, JSX, object `{...}` hoặc callback JavaScript vào đoạn văn MDX.
3. **Prop JSX phải đóng đủ nháy và ngoặc.** Với component như `html={\`...\`}`, `code={\`...\`}` hoặc
   mảng/object `{[...]}`, kiểm tra đủ cặp `"..."`, `'...'`, backtick, `{}`, `[]`, `()` và tag đóng
   `/>` trước khi lưu.
4. **Không để placeholder nội bộ lọt vào bài.** Cấm chuỗi `HOLD1`, `HOLD2`…, ký tự NUL, token tạm
   hoặc đoạn code bị thay bằng placeholder sau bước humanize/replace.
5. **Không sửa từng mảnh bên trong code bằng regex prose.** Script humanize phải bảo vệ rồi khôi phục
   nguyên vẹn frontmatter, code fence, inline code, JSX prop, URL và import. Nếu không chứng minh được
   bước restore an toàn thì bỏ qua khối kỹ thuật đó.
6. **Bắt buộc chạy kiểm tra cú pháp:** `npm run lint:mdx` sau khi soạn/sửa MDX. Chưa qua lệnh này thì
   bài chưa hoàn thành. `start`, `dev` và `build` cũng tự chạy chốt này sau bước generate nội dung.

**Ba lỗi điển hình cần chặn:**

| Lỗi | Viết sai | Viết đúng |
|---|---|---|
| Tag bị hiểu là JSX | `dùng <picture> để đổi ảnh` | ``dùng `<picture>` để đổi ảnh`` |
| Quote JSX bị hở | `<Demo html="<p>...` | Đóng đủ quote/ngoặc hoặc dùng fenced code block |
| Biểu thức bị cắt | `onClick={() => goiAPI('...` | Đóng đủ `')}`, tag và prop chứa nó |

**Sai:** `quét CVE, deploy K8s bằng IaC, on-call khi SLI xấu`  
**Đúng:** `quét CVE (lỗ hổng bảo mật đã biết) → đưa lên K8s (điều phối container) bằng IaC (hạ tầng
khai báo bằng code); ca trực (on-call) khi SLI (chỉ số mức dịch vụ user cảm nhận) xấu`

### 6.2 Quy trình / bảng việc → sơ đồ, không nhồi chữ

1. Nếu nội dung là **chuỗi bước** (ship, sự cố, review, ETL…): dùng `<FlowDiagram>` (hoặc Mermaid
   flowchart) — **không** gói cả pipeline vào một đoạn văn dài.
2. Nếu là **tập vai trò / checklist / so sánh**: dùng `<GridCards>` / `<ComparisonPanel>` — **không**
   bảng chữ dày chỉ để “liệt kê việc”.
3. Bảng markdown chỉ giữ khi cần **tra cứu 2–3 cột ngắn** (thuật ngữ ↔ nghĩa). Hàng nào dài hơn
   ~1 dòng “việc chính” → tách thẻ hoặc sơ đồ.
4. Caption sơ đồ viết **tiếng Việt đời thường**; `sub` mỗi trạm = nghĩa ngắn (≤ ~6 từ).
5. Bảng so sánh công nghệ/quyết định có từ 4 cột trở lên hoặc chứa thuật ngữ chuyên ngành phải được
   tách thành `ComparisonPanel`/`GridCards`, hay chia thành nhiều bảng nhỏ có phần giải thích. Không
   giao một “bức tường ô” cho người mới rồi để họ tự suy ra.
6. Mỗi tiêu chí so sánh phải nói được **đang đo gì → khác nhau ở đâu → khác biệt đó ảnh hưởng quyết
   định thế nào**. Chỉ ghi `Có/Không/Cao/Thấp` là không đạt.

### 6.3 Không soạn card / mục “trống nghĩa” (BẮT BUỘC)

**Cấm** (hoặc hạn chế tối đa) các khối chỉ để “trông có học thuật” mà học viên không mang đi được việc:

| Dạng xấu | Ví dụ | Làm thay |
|---|---|---|
| Meta về bài | “Đoạn này neo research — không thay tự kiểm” | Xóa. Đừng kể cấu trúc bài cho học viên |
| Card / heading rỗng | “Chuẩn ngành” + 2 câu chung chung không có số/việc | Chỉ giữ nếu có **nội dung học được** (vd 4 chỉ số DORA, 1 checklist OWASP) |
| Lặp “Đọc thêm” | Mục “Chuẩn” copy ý link bên dưới | Gộp vào **Đọc thêm**; mỗi link 1 dòng *vì sao mở* |
| Badge / thẻ trang trí | Icon + title không có `desc` có nghĩa | Bỏ thẻ hoặc viết đủ nghĩa |

**Quy tắc nhanh:** học viên đọc xong khối đó có **kể lại được 1 việc / 1 con số / 1 quyết định** không?  
→ Không thì **đừng soạn**.

### 6.4 Câu chuyện / ví dụ tình huống (BẮT BUỘC nếu đã kể)

**Cấm** “kể đại” một đoạn nén jargon (một câu = cả đêm sự cố) mà học viên **không nắm thông điệp**.

Khi bài có *Câu chuyện thật*, *Ví dụ*, *Case*, *Một ngày mẫu* dạng kể:

1. **Thông điệp trước hoặc sau rõ ràng** — 1–2 câu: học viên phải mang đi được *gì* (quyết định / phản xạ / anti-pattern). Không thông điệp → **đừng kể**.
2. **Đủ bối cảnh thực** — ai (vai trò), lúc nào, user/hệ thống thấy gì, con số hoặc tỉ lệ nếu có (vd canary 10%, 5xx). Không cần tiểu thuyết, nhưng phải **tưởng tượng được đêm đó**.
3. **Diễn biến có bước** — không gói 6 hành động vào một câu mũi tên. Ưu tiên:
   - `<FlowDiagram>` / Mermaid theo thời gian, **và/hoặc**
   - danh sách đánh số (phát hiện → giảm cháy → gốc → sửa ray → học).
4. **Giải jargon trong chuyện** — lần xuất hiện trong story vẫn cần nghĩa ngắn (đúng §6.1).
5. **Nên có đối chiếu** khi thông điệp là “cách A vs B”: `<ComparisonPanel>` (sai/đúng, trước/sau).
6. **Độ dài tối thiểu có ích:** đủ để người mới **kể lại 3–5 câu** bằng lời mình. Một đoạn 4–5 câu nén acronym = **không đạt**.

**Sai (nén, không thông điệp rõ):**  
`Service tăng 5xx → canary đỏ → rollback → trace probe → HEALTHCHECK → postmortem. Đó là DevOps.`

**Đúng:** bối cảnh user → sơ đồ thời gian → từng bước có *vì sao* → so sánh SSH vs đường ray → 1 câu mang đi.

### 6.5 Độ sâu và độ đầy đủ của bài học (BẮT BUỘC)

Mọi bài phải được soạn như một bài học hoàn chỉnh cho người mới phù hợp với cấp độ của lộ trình,
không phải một bản ghi chú sơ lược. **Không đặt số chữ tối thiểu** để tránh kéo dài cho đủ; độ dài
phải đi theo lượng kiến thức thật cần dạy.

1. **Dạy đủ nội dung cốt lõi.** Với mỗi khái niệm chính, phải trả lời được: *là gì*, *vì sao cần*,
   *hoạt động ra sao*, *dùng khi nào* và *dễ sai ở đâu*. Ý nào đã nêu trong mục tiêu đầu bài phải
   được giải thích đầy đủ trong thân bài.
2. **Đi từ nền đến áp dụng.** Không nhảy thẳng vào công thức, lệnh hoặc kết luận. Trước khi dùng một
   khái niệm, cho người học đủ nền để hiểu nó; sau phần giải thích phải có ví dụ cụ thể hoặc thao tác
   để thấy khái niệm chạy trong thực tế.
3. **Mô tả trực quan và cụ thể.** Với cơ chế, luồng dữ liệu hoặc sự thay đổi trạng thái, phải chỉ rõ
   **đầu vào → bước biến đổi/trạng thái trung gian → đầu ra**. Dùng sơ đồ, ví dụ có giá trị cụ thể,
   bảng trước–sau, đoạn mã nhỏ hoặc tình huống quan sát được. Người học phải hình dung được “thứ gì
   đang ở đâu và thay đổi thế nào”, không chỉ nghe một chuỗi từ trừu tượng.
4. **Có chiều sâu thực, không làm cho có.** Cấm đoạn kiểu “X rất quan trọng, hãy tìm hiểu thêm”, danh
   sách thuật ngữ không giải thích, ví dụ một dòng không phân tích, placeholder, hoặc mục chỉ lặp lại
   tiêu đề. Nếu một ý là cốt lõi, phải giải thích cơ chế và hệ quả chứ không chỉ định nghĩa.
5. **Chỉ ra ranh giới và bẫy.** Nêu ít nhất các hiểu lầm, lỗi thường gặp hoặc trường hợp không nên áp
   dụng nếu chúng có thật trong chủ đề. Khi có đánh đổi, nói rõ được–mất thay vì kết luận một chiều.
6. **Diễn đạt dễ hiểu, dễ nghe.** Ưu tiên câu ngắn, từ quen thuộc và ví dụ đời thường; thuật ngữ chuyên
   môn được giải nghĩa ngay lúc xuất hiện. Đọc thành tiếng phải tự nhiên, không giống tài liệu dịch hay
   văn bản liệt kê máy móc.
7. **Kết thúc bằng năng lực cụ thể.** Sau bài, người học phải tự giải thích lại ý chính và làm được ít
   nhất một việc quan sát được: phân biệt, lựa chọn, mô phỏng, sửa lỗi, viết đoạn mã, hoặc hoàn thành
   một thao tác. Quiz và phần ôn lại phải kiểm tra đúng nội dung đã dạy, không hỏi kiến thức ngoài bài.

**Cấm mô tả mơ hồ:** “dữ liệu được xử lý”, “hệ thống tối ưu hiệu năng”, “framework quản lý trạng
thái”, “API kết nối các thành phần” nếu không nói rõ dữ liệu nào, ai thực hiện, trạng thái trước/sau,
khi nào diễn ra và người dùng hoặc chương trình quan sát được kết quả gì. Ẩn dụ chỉ dùng để mở đường;
ngay sau đó phải quay về cơ chế thật.

**Một bài chưa đạt nếu:** chỉ có định nghĩa + vài bullet; bỏ mất mắt xích khiến người mới phải tự tra;
ví dụ không được giải thích; mục tiêu đầu bài không xuất hiện trong thân bài; hoặc nội dung dài nhưng
không giúp người học hiểu thêm cơ chế, quyết định hay cách làm.

### 6.6 Nguồn bên thứ ba và lời kể về quá trình biên soạn (BẮT BUỘC)

Nguồn bên thứ ba dùng để người soạn kiểm chứng và mở rộng hiểu biết. Phần giảng dạy phải đứng độc
lập, diễn đạt trực tiếp kiến thức cho học viên bằng lời của AlgoSchool.

1. **Chỉ hiển thị nguồn ở cuối bài.** Tên roadmap, website, sách, bài viết, repository hoặc tổ chức
   cung cấp tài liệu chỉ được đặt trong mục **Đọc thêm / Tài liệu tham khảo**, kèm liên kết và một câu
   ngắn cho biết tài liệu đó giúp đào sâu phần nào.
2. **Cấm kể quy trình lấy nguồn trong thân bài.** Không viết: “theo roadmap…”, “dựa theo…”, “tham
   khảo từ…”, “tôi lấy dữ liệu/nội dung này từ…”, “roadmap này giúp xây bài…”, hoặc biến thể tương tự.
3. **Không biến nguồn thành nội dung học.** Không đặt card, callout, badge, caption hay đoạn mở bài để
   nói bài được tổng hợp từ đâu. Hãy dạy thẳng khái niệm, cơ chế, ví dụ và cách áp dụng.
4. **Viết lại bằng hiểu biết đã kiểm chứng.** Không sao chép câu chữ, cấu trúc đoạn hoặc ví dụ đặc thù
   của nguồn. Đối chiếu nhiều nguồn khi cần, kiểm tra tính đúng rồi diễn đạt lại tự nhiên bằng tiếng Việt.
5. **Ngoại lệ chỉ dành cho ngữ cảnh kiến thức thật sự cần nguồn.** Có thể nhắc tên một tiêu chuẩn,
   đặc tả hoặc công cụ trong thân bài khi chính nó là đối tượng đang học (ví dụ tiêu chuẩn HTTP, hướng
   dẫn OWASP), nhưng không dùng cách nói meta rằng bài “được viết dựa theo” tài liệu đó.
6. **Không rải attribution hoặc dấu vết biên soạn.** `LICENSE`, `CC-BY`, `Attribution`, `Brief:` và
   đường dẫn như `research/...` không thuộc bài học, kể cả khi đặt trong comment hoặc mục Đọc thêm.
   Attribution/giấy phép toàn site chỉ ở `website/docs/intro.mdx` (`/gioi-thieu`). `npm run
   lint:lessons:strict` chặn vi phạm này trên **toàn bộ** `docs/` — cổng chạy local qua pre-hook
   npm (`prebuild`, `precontent:*`) và chạy lại trên CI GitHub Actions cho mọi push/PR vào `main`.

Quy định ghi công và giấy phép toàn site vẫn tuân theo nơi canonical tại `/gioi-thieu`; không sao chép
đoạn attribution/giấy phép vào từng bài học.

### 6.7 Bám sát lộ trình từ link người dùng cung cấp (BẮT BUỘC)

Khi người dùng đưa một link có lộ trình bài học, lộ trình đó là phạm vi cần bảo toàn. Trước khi tạo
hoặc sửa nội dung, người soạn phải đọc lộ trình và lập **danh mục bao quát** gồm toàn bộ chặng, chủ
đề, bài và mục con có ý nghĩa giảng dạy, giữ nguyên thứ tự phụ thuộc kiến thức của lộ trình gốc.

1. **Lập danh mục trước, rồi mới soạn.** Danh mục phải đủ chi tiết để có thể đối chiếu từng mục;
   ghi trạng thái rõ ràng như `chưa soạn`, `đang soạn`, `đã soạn` và, khi có thể, nơi đặt bài tương
   ứng trong kho nội dung.
2. **Không tự cắt phạm vi.** Không bỏ, gộp làm mất ý nghĩa, hoặc thay thế mục của lộ trình chỉ vì
   số lượng bài lớn, nội dung quen thuộc hay khó soạn. Có thể tách một mục lớn thành nhiều bài nhỏ
   hơn để dạy rõ hơn, nhưng tổng kiến thức và thứ tự phụ thuộc phải vẫn được bao phủ.
3. **Mục chưa có link vẫn phải được nghiên cứu.** Nếu roadmap để trống link cho một mục hoặc không
   cung cấp tài liệu, người soạn phải chủ động tìm và kiểm chứng kiến thức từ nguồn chính thống đáng
   tin cậy. Ưu tiên tài liệu của nhà phát triển công nghệ, đặc tả của tổ chức tiêu chuẩn, tài liệu của
   cơ quan có thẩm quyền hoặc tài liệu kỹ thuật gốc; đối chiếu thêm nguồn phù hợp khi chủ đề cần.
   Không được bỏ mục, thay bằng phần đoán mò, hoặc coi mục là hoàn tất chỉ vì roadmap không gắn link.
   Khi tìm dữ liệu từ web, dùng ScrapeGraphAI theo policy của dự án.
4. **Triển khai theo đợt khi cần.** Nếu lộ trình quá dài cho một lượt, công khai danh mục/checklist
   trước, sau đó thêm bài theo từng nhóm hợp lý. Mỗi lượt tiếp theo phải bắt đầu bằng việc đối chiếu
   checklist và cập nhật trạng thái, không dựa vào trí nhớ.
5. **Chỉ thay đổi khi có xác nhận.** Mọi quyết định bỏ mục, đổi thứ tự lớn, hoặc thu hẹp phạm vi cần
   người dùng xác nhận rõ ràng. Khi phát hiện link thiếu phần nội dung, không được tự đoán để coi là
   hoàn tất; phải nêu phần chưa đọc được và xin hướng dẫn nếu điều đó ảnh hưởng phạm vi.

Danh mục/checklist là công cụ quản lý biên soạn, không đưa lời kể về link, roadmap hoặc quá trình lấy
nguồn vào phần giảng dạy của học viên (§6.6).

### 6.8 Nhịp bài học, tương tác và giữ chân người học (BẮT BUỘC)

Một bài đủ kiến thức vẫn có thể khiến người học rời đi nếu họ không biết mình đang học để làm gì,
không được tự thử, hoặc phải đọc quá lâu mới thấy kết quả. Mỗi bài phải có nhịp rõ ràng: **gặp vấn
đề → hiểu một ý → dự đoán/thử → nhận phản hồi → dùng được ý đó**. Điều này không có nghĩa là nhét
tương tác vào mọi câu; mục tiêu là tạo những điểm dừng có ích để người học chủ động tham gia.

1. **Mở bài có hook và lời hứa cụ thể.** Trong phần đầu, dùng một tình huống quen thuộc, lỗi dễ gặp,
   kết quả bất ngờ hoặc quyết định thực tế để trả lời: “Vì sao mình nên học việc này ngay bây giờ?”
   Ngay sau đó, nói rõ sau bài người học làm được gì, điều kiện đầu vào cần có và, nếu phù hợp, một
   kết quả nhỏ họ sẽ thấy trong vài phút đầu. Không mở bằng định nghĩa khô, lời khen chung chung hoặc
   câu chuyện không liên quan đến năng lực cần học.
2. **Mỗi phần trả lời một câu hỏi học tập chính.** Tiêu đề nên là câu hỏi hoặc kết luận dễ hiểu; phần
   nội dung chỉ giữ những gì giúp trả lời câu hỏi đó. Tách kiến thức `cần biết để làm bài` khỏi phần
   `đào sâu khi cần`; phần đào sâu phải được gắn nhãn rõ, không chen vào làm đứt mạch người mới. Khi
   một giải thích đã đủ cho quyết định hoặc thao tác hiện tại, dừng lại thay vì thêm thông tin chỉ để
   bài dài hơn.
3. **Luân phiên giải thích và hành động.** Với mỗi ý lớn, ưu tiên nhịp: giải thích ngắn → hỏi người
   học dự đoán/chọn cách làm → cho họ quan sát hoặc tự thử → giải thích vì sao kết quả như vậy → áp
   dụng vào một tình huống mới. Không được để toàn bộ bài là đoạn đọc liên tục rồi mới đặt quiz ở cuối.
`QuizBox` cuối bài được dùng khi `evidencePlan.quiz.feasible=true`, nhưng không thay thế các điểm
tự kiểm trong thân bài.
4. **Thao tác phải tự kiểm được.** Mỗi phần `Thử ngay`, đoạn mã có thể chạy, câu hỏi dự đoán hoặc
   bài tập phải nói rõ: người học cần làm gì, kết quả mong đợi là gì, cách nhận biết mình làm đúng và
   ít nhất một gợi ý khi kết quả khác dự kiến. Đáp án/phản hồi phải giải thích lý do, không chỉ báo
   `đúng` hoặc `sai`.
5. **Hình và sơ đồ phục vụ một quyết định.** Trước khi thêm hình, xác định câu hỏi mà hình giúp trả
   lời, chẳng hạn “dữ liệu đi đâu?”, “hai cách khác nhau ở điểm nào?” hoặc “bước nào xảy ra trước?”.
   Không dùng hình chỉ để lặp lại đoạn văn hay trang trí. Caption và nhãn phải tự đủ nghĩa theo §6.1;
   không dùng riêng màu sắc, biểu tượng hoặc vị trí để truyền một ý quan trọng vì người học có thể
   không phân biệt được chúng.
6. **Kết thúc tạo đà đi tiếp.** Phần cuối cần chốt: người học vừa làm/hiểu được gì, một bẫy đáng nhớ,
   và kiến thức này sẽ được dùng ở bài tiếp theo hoặc tình huống nào. Chỉ liên kết sang bài sau khi
   mối nối thật sự tự nhiên; không dùng lời hứa mơ hồ kiểu “phần sau còn nhiều điều thú vị”.
7. **Giọng người phải trung thực.** Có thể dùng góc nhìn gần gũi, tình huống đời thường và lỗi phổ
   biến để tạo kết nối. Không bịa trải nghiệm cá nhân như “mình từng gặp” nếu không có cơ sở; một ví
   dụ giả định phải nói rõ đó là tình huống minh hoạ.

### 6.9 Bằng chứng học, kiểm chứng kỹ thuật và chất lượng phát hành (BẮT BUỘC)

Một bài không được coi là hoàn chỉnh chỉ vì prose dễ đọc và MDX build được. Bài phải chứng minh
được rằng mục tiêu đã được dạy, người học có chỗ luyện đúng năng lực, ví dụ kỹ thuật đáng tin và
trải nghiệm không mất nghĩa khi đổi thiết bị.

#### 6.9.1 Mục tiêu, phạm vi và kiến thức tiên quyết

1. **Lập bản đồ mục tiêu → nội dung → luyện tập → đánh giá.** Mỗi năng lực trong `Bạn sẽ học được gì`
   phải trỏ được tới một phần giảng cụ thể, ít nhất một ví dụ/tự kiểm/thực hành và một câu hỏi hoặc
   challenge đánh giá đúng năng lực đó. Không để mục tiêu “treo”; không hỏi trong quiz nội dung chưa
   được dạy; không thêm hoạt động hấp dẫn nhưng không phục vụ mục tiêu.
2. **Giới hạn một bài ở 1–3 năng lực đầu ra chính.** Phần core (phần bắt buộc trên lộ trình) hướng tới
   nhịp học khoảng 10–20 phút. Đây là tiêu chí chia nhỏ, không phải lý do cắt kiến thức. Nếu không thể
   đạt mà vẫn dạy đủ, tách thành nhiều bài nối tiếp và cập nhật checklist roadmap để toàn bộ phạm vi
   gốc vẫn được bao phủ.
3. **Nêu và kiểm tra tiên quyết.** Chỉ sử dụng kiến thức đã được dạy ở bài/chặng trước hoặc giải thích
   đủ nền ngay trong bài. Nếu người học cần công cụ, tài khoản, hệ điều hành, file mẫu hoặc quyền truy
   cập cụ thể, phải nêu trước khi họ bắt đầu thao tác. Core và phần đào sâu/elective phải được phân
   biệt rõ để kiến thức mở rộng không chặn đường học chính.

#### 6.9.2 Kiểm chứng ví dụ, phiên bản và nguồn

1. **Chạy thử ví dụ kỹ thuật khi môi trường cho phép.** Code, lệnh, truy vấn, cấu hình và output mẫu
   phải được kiểm tra trong môi trường phù hợp trước khi bàn giao. Không được tự viết output “trông
   có vẻ đúng”. Nếu không thể chạy vì thiếu dịch vụ, thiết bị hoặc quyền truy cập, phải ghi rõ giới
   hạn trong ghi chú biên soạn và kiểm chứng bằng tài liệu kỹ thuật gốc.
2. **Phân biệt code chạy được với nội dung minh hoạ.** Pseudocode (mã giả dùng để giải thích ý tưởng),
   output rút gọn, dữ liệu giả và mô phỏng phải có nhãn rõ. Không trình bày chúng như lệnh hoặc chương
   trình có thể sao chép rồi chạy nguyên trạng.
3. **Khóa phạm vi phiên bản khi hành vi có thể thay đổi.** Với API, SDK, framework, hệ điều hành,
   công cụ dòng lệnh hoặc tiêu chuẩn có khác biệt theo phiên bản, ghi rõ phiên bản/phạm vi áp dụng và
   ngày kiểm chứng trong ghi chú nghiên cứu hoặc metadata phù hợp. Trước khi hoàn tất, kiểm tra các
   link ở `Đọc thêm / Tài liệu tham khảo` còn mở được và đúng với nội dung được viện dẫn.

#### 6.9.3 Chất lượng quiz, challenge và phản hồi

1. **Mỗi câu hỏi đo một năng lực đã dạy.** Không hỏi mẹo, chi tiết vụn vặt, kiến thức ngoài bài hoặc
   bắt học viên nhớ nguyên văn. Số lượng theo rubric sư phạm; chất lượng và độ phủ mục tiêu quan trọng
   hơn việc thêm câu cho đủ số.
2. **Phản hồi phải giúp sửa hiểu lầm.** Mỗi câu cần giải thích vì sao đáp án đúng; với lựa chọn sai
   dễ nhầm, giải thích hiểu lầm hoặc bước suy luận sai nằm ở đâu. Không chỉ hiện `đúng`/`sai`.
3. **Lựa chọn sai phải có lý do tồn tại.** Distractor (lựa chọn sai dùng để phát hiện hiểu lầm) nên
   xuất phát từ lỗi người mới thường mắc, không phải đáp án vô lý để làm câu hỏi dễ giả tạo.
4. **Challenge có điều kiện hoàn thành quan sát được.** Nêu đầu vào, sản phẩm/kết quả cần tạo, tiêu
   chí pass, cách tự kiểm và gợi ý phục hồi. Challenge phải map trực tiếp tới skill node hoặc năng lực
   đầu ra của bài/chặng.

#### 6.9.4 QA trực quan, khả năng tiếp cận và đa nền tảng

1. **Render và xem thật.** Sau kiểm tra cú pháp, mở bài ở kích thước desktop và mobile để rà chữ tràn,
   bảng/sơ đồ bị cắt, nhãn quá nhỏ, khoảng trắng bất thường và thứ tự đọc. `npm run lint:mdx` không
   thay thế bước QA trực quan.
2. **Có đường hiểu bằng chữ.** Hình, sơ đồ và tương tác truyền kiến thức quan trọng phải có caption,
   mô tả hoặc phần giải thích chữ tương đương. Người không nhìn rõ hình vẫn phải hiểu được kết luận
   cốt lõi. Không dùng riêng màu, biểu tượng, chuyển động hay vị trí để phân biệt đúng/sai hoặc trạng thái.
3. **Không chặn bàn phím và công nghệ hỗ trợ.** Tương tác phải dùng được bằng bàn phím, có thứ tự
   focus hợp lý và nhãn dễ hiểu. Nội dung chuyển động không được là cách duy nhất truyền kiến thức.
4. **Có fallback khi nền tảng không hỗ trợ tương tác.** Nếu normalizer biến component thành `stub`
   trên mobile/runtime, phần fallback phải giữ được mục tiêu học, dữ liệu chính, kết quả mong đợi và
   cách tự kiểm; không được biến một bước bắt buộc thành hộp trống hoặc lời nhắn “hãy mở web”.

#### 6.9.5 Kiểm chứng với người học và cải thiện sau phát hành

1. **Walkthrough theo góc nhìn người mới trước phát hành.** Với bài mới hoặc thay đổi lớn, người soạn
   phải đi lại toàn bộ luồng mà không dùng kiến thức ngoài phần tiên quyết: đọc hook, làm điểm tự kiểm,
   thử thao tác, làm quiz và kiểm tra kết bài. Với bài/chặng quan trọng, ưu tiên nhờ một người đúng
   trình độ mục tiêu học thử; ghi lại chỗ họ dừng, hiểu sai hoặc cần tra ngoài.
2. **Không tuyên bố giữ chân chỉ từ cảm giác.** Khi đã có dữ liệu hợp lệ và tuân thủ quyền riêng tư,
   dùng tỷ lệ rời bài, hoàn thành bài, bắt đầu/hoàn thành thực hành, hoàn thành quiz và câu hỏi bị sai
   nhiều để tìm điểm cần sửa. Dữ liệu hành vi là tín hiệu để điều tra, không phải lý do tự động rút
   gọn kiến thức hoặc tối ưu bằng thủ thuật gây nghiện.
3. **Lặp lại vòng cải thiện.** Nếu nhiều người dừng hoặc sai tại cùng một điểm, kiểm tra theo thứ tự:
   tiên quyết → thuật ngữ → độ dài/nhịp → ví dụ → phản hồi → lỗi giao diện. Cập nhật bài và đánh giá
   lại; không đổ lỗi mặc định cho người học.

### 6.10 Checklist agent / người soạn (trước merge)

- [ ] Rà viết tắt (PR, CI, CD, CVE, K8s, VM, IaC, SLI, SLO, SLA, SRE, IAM, DORA, CNCF, OWASP…): mỗi
      cái đã có nghĩa lần đầu?
- [ ] Mọi thuật ngữ khó với người mới đã có nghĩa tiếng Việt dễ hiểu ngay trong ngoặc (§6.1)?
- [ ] Phần giải nghĩa nói được “là gì/dùng làm gì”, không định nghĩa vòng tròn bằng jargon khác (§6.1)?
- [ ] Đã rà riêng từng bảng, sơ đồ, card, callout, caption và quiz như một khối độc lập (§6.1)?
- [ ] Tiêu đề/nhãn dùng tiếng Việt trước; không còn nhãn Anh–Việt nén kiểu ghi chú nội bộ (§6.1)?
- [ ] Không còn `Có/Không/Cao/Thấp/Không chuẩn` mà thiếu tiêu chí hoặc hệ quả cụ thể (§6.1, §6.2)?
- [ ] Bảng ≥4 cột hoặc bảng dày jargon đã được tách thành component/khối dễ đọc (§6.2)?
- [ ] Frontmatter `id` chỉ có chữ thường, số, gạch ngang và không bị chèn phần giải nghĩa (§6.1.1)?
- [ ] Không sửa slug, URL, path, prop định danh hoặc code khi humanize/giải nghĩa (§6.1.1)?
- [ ] Tên tag HTML/JSX trong câu đã bọc backtick; code nhiều dòng đã vào code fence (§6.1.2)?
- [ ] Mọi prop/component MDX đóng đủ quote, ngoặc và tag (§6.1.2)?
- [ ] Không còn `HOLD…`, ký tự NUL hoặc placeholder nội bộ (§6.1.2)?
- [ ] `npm run lint:mdx` đã chạy thành công sau lần sửa cuối (§6.1.2)?
- [ ] Không còn đoạn “một câu = cả pipeline”?
- [ ] Mọi quy trình ≥3 bước đã là sơ đồ?
- [ ] Học viên đọc to được luồng mà **không** cần Google viết tắt?
- [ ] Không có mục/card meta hoặc “trống nghĩa” (§6.3)?
- [ ] Mọi câu chuyện/ví dụ có **thông điệp + bối cảnh + bước** (§6.4), ưu tiên sơ đồ?
- [ ] Mọi mục tiêu đầu bài đều được dạy đủ trong thân bài (§6.5)?
- [ ] Mỗi khái niệm chính có cơ chế, ví dụ áp dụng và bẫy/ranh giới cần biết (§6.5)?
- [ ] Cơ chế/luồng/trạng thái đã có mô tả trực quan: đầu vào → biến đổi → đầu ra (§6.5)?
- [ ] Không còn câu trừu tượng kiểu “xử lý”, “tối ưu”, “quản lý”, “kết nối” mà thiếu chủ thể và kết quả cụ thể (§6.5)?
- [ ] Không có placeholder, định nghĩa lướt hoặc đoạn viết chỉ để bài trông dài (§6.5)?
- [ ] Người học kết thúc bài có thể giải thích lại và làm được một việc cụ thể (§6.5)?
- [ ] Tên/link nguồn bên thứ ba chỉ nằm trong **Đọc thêm / Tài liệu tham khảo** (§6.6)?
- [ ] Không còn câu “theo/dựa trên/lấy từ roadmap, nguồn, tài liệu…” trong phần giảng dạy (§6.6)?
- [ ] Nếu có link lộ trình do người dùng cung cấp: đã lập danh mục đủ chặng/chủ đề/bài/mục con trước
      khi soạn (§6.7)?
- [ ] Danh mục có trạng thái và đã được đối chiếu trước mỗi đợt soạn; không còn mục nào bị bỏ/gộp
      mất ý nghĩa (§6.7)?
- [ ] Mọi mục roadmap chưa có link đã được chủ động kiểm chứng bằng tài liệu chính thống, đáng tin
      cậy; không có mục nào bị bỏ vì thiếu link (§6.7)?
- [ ] Mọi thay đổi phạm vi hoặc thứ tự lớn so với lộ trình gốc đều có xác nhận rõ ràng của người dùng
      (§6.7)?
- [ ] Mở bài có tình huống/vấn đề thực tế, nêu rõ năng lực đầu ra và không bắt đầu bằng định nghĩa khô
      (§6.8)?
- [ ] Mỗi phần chỉ trả lời một câu hỏi học tập chính; kiến thức đào sâu đã tách rõ khỏi phần cần biết
      ngay (§6.8)?
- [ ] Mỗi ý lớn có điểm dự đoán, tự kiểm hoặc áp dụng trong thân bài; không dồn toàn bộ tương tác vào
      `QuizBox` cuối bài (§6.8)?
- [ ] Mọi thao tác/bài tập nêu đủ việc cần làm, kết quả mong đợi, cách tự kiểm và gợi ý khi sai (§6.8)?
- [ ] Mỗi hình/sơ đồ trả lời một câu hỏi học tập cụ thể, có caption tự đủ nghĩa và không chỉ truyền ý
      bằng màu sắc/vị trí (§6.8)?
- [ ] Kết bài chốt năng lực, một bẫy và mối nối tự nhiên tới bài sau hoặc tình huống áp dụng (§6.8)?
- [ ] Không có trải nghiệm cá nhân bị bịa; tình huống giả định đã được nói rõ là minh hoạ (§6.8)?
- [ ] Mỗi năng lực đầu ra đã map đủ tới phần giảng, ví dụ/thực hành và quiz/challenge tương ứng
      nếu `evidencePlan` đánh dấu tương tác đó khả thi; nếu không thì có tự kiểm bằng chữ (§6.9.1)?
- [ ] Bài có 1–3 năng lực chính; nếu core vượt nhịp 10–20 phút đã được tách bài mà không mất phạm vi
      roadmap (§6.9.1)?
- [ ] Kiến thức, công cụ, tài khoản và quyền truy cập tiên quyết đã được nêu; không giả định phần chưa
      dạy (§6.9.1)?
- [ ] Code/lệnh/truy vấn/cấu hình và output mẫu đã được chạy thử khi có thể; phần không chạy được có
      giới hạn và căn cứ kiểm chứng rõ (§6.9.2)?
- [ ] Mã giả, dữ liệu giả, output rút gọn và mô phỏng đã được gắn nhãn; phạm vi phiên bản đã được xác
      định khi hành vi có thể thay đổi (§6.9.2)?
- [ ] Link trong `Đọc thêm / Tài liệu tham khảo` còn truy cập được và dẫn đúng tài liệu cần thiết
      (§6.9.2)?
- [ ] Quiz chỉ hỏi nội dung đã dạy; giải thích lý do đúng và hiểu lầm sau các lựa chọn sai đáng chú ý
      (§6.9.3)?
- [ ] Challenge có đầu vào, kết quả cần tạo, tiêu chí pass, cách tự kiểm và map đúng năng lực/skill
      node (§6.9.3)?
- [ ] Bài đã được render và kiểm tra trực quan ở desktop lẫn mobile, không có chữ/sơ đồ/bảng tràn hoặc
      bị cắt (§6.9.4)?
- [ ] Hình và tương tác quan trọng có đường hiểu tương đương bằng chữ; thao tác dùng được bằng bàn
      phím và không phụ thuộc riêng vào màu/chuyển động (§6.9.4)?
- [ ] Component bị `stub` trên mobile/runtime có fallback giữ đủ mục tiêu học và cách tự kiểm
      (§6.9.4)?
- [ ] Đã walkthrough toàn bài như người mới; với bài quan trọng đã ưu tiên học thử và ghi nhận điểm
      dừng/hiểu sai (§6.9.5)?
- [ ] Nếu đã có dữ liệu sau phát hành, các điểm rời bài/sai nhiều đã được điều tra và cập nhật theo
      vòng cải thiện, không dùng thủ thuật gây nghiện (§6.9.5)?
- [ ] Nội dung đã được viết lại độc lập bằng tiếng Việt, không kể quy trình biên soạn (§6.6)?

**Chốt bàn giao:** agent phải tự đọc lại phần prose **và quét riêng nội dung trong bảng/JSX props**.
Nếu còn một thuật ngữ khó chưa giải nghĩa, một nhãn tiếng Anh nén, hoặc một kết luận mơ hồ không có
hệ quả, agent **không được báo hoàn thành**.
