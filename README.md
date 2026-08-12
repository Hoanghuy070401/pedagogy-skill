# soan-bai-hoc — skill soạn tài liệu giáo dục từ nguồn

Bản mang đi được của bộ kỹ năng soạn bài trong SchoolAI Studio (`schoolAI-deploy/website`).
Trích ngày 10/08/2026 từ `STUDIO-AGENT-RULES.md`, `HUONG-DAN-SOAN-BAI.md`, `STUDIO-ASSET-RULES.md`.

## Cấu trúc và thứ tự áp dụng

```
soan-bai-hoc/
  SKILL.md                          ← router + thứ tự ưu tiên bất biến
  references/
    00-rule-set-agent.md            ← hợp đồng tương thích SchoolAI Studio
    01-huong-dan-soan-bai.md        ← tài liệu đầy đủ, chỉ đọc khi cần tra cứu
    02-quy-tac-asset.md             ← quy tắc trực quan và khả năng tiếp cận
    03-van-phong-humanize.md        ← chống văn AI sau khi nội dung đã đủ sâu
    04-checklist-truoc-merge.md     ← checklist review toàn diện
    05-lap-ke-hoach-chieu-sau.md    ← claim → cơ chế → ví dụ → ranh giới → chuyển giao
    06-profile-theo-artifact.md     ← hợp đồng riêng cho từng loại đầu ra
    07-cong-giu-nguyen-ngu-nghia.md ← khóa claim, số liệu, công thức, đáp án, citation
    08-role-voice-profile.md         ← giọng người dùng và vai được thiết kế
    09-mach-lap-luan-va-diem-nhan.md ← xương sống, cầu nối và hệ phân cấp điểm nhấn
    10-quy-chuan-ui-hoc-lieu.md      ← layout, responsive, trạng thái, motion và UI-QA
  assets/
    mau-bai-khai-niem.md            ← khung một bài để copy
    mau-design-system-hoc-lieu.md   ← Master + page overrides cho UI sinh ra
    component-kit.md                ← nhu cầu trực quan → cách map sang stack khác
```

## Cài vào dự án khác

**Claude Code — dùng cho một dự án:**

```bash
mkdir -p <du-an>/.claude/skills
cp -R /Volumes/Disk_1/AI/skill/soan-bai-hoc <du-an>/.claude/skills/
```

**Dùng cho mọi dự án:**

```bash
cp -R /Volumes/Disk_1/AI/skill/soan-bai-hoc ~/.claude/skills/
```

Sau đó gọi `/soan-bai-hoc`, hoặc để Claude tự nhận diện khi bạn nhắc "soạn bài", "viết bài học",
"review bài giảng".

**Agent/tool khác:** nạp `SKILL.md` làm router, sau đó chỉ nạp các reference đúng loại artifact.
Không ghép toàn bộ thư mục vào mọi prompt. `lessonforge` đã có bảng định tuyến tương ứng trong
`src/lessonforge/pipeline.py`.

## Cập nhật khi bản gốc đổi

Các file gốc SchoolAI nằm ở `schoolAI-deploy/website/`. Khi chúng đổi, chỉ đồng bộ
`references/00–02`; giữ riêng `03–10` và `SKILL.md`, vì đây là lớp dùng chung đã được tổ chức theo
pipeline nguồn → chiều sâu → artifact → giọng → giữ nghĩa.

## Phạm vi hiện tại

Repo này hiện chỉ chứa bộ quy tắc soạn bài học (lesson-authoring). Sơ đồ
`frameworks/ subjects/ curriculum/ schemas/` rộng hơn được mô tả trong tài
liệu kiến trúc hệ sinh thái chưa được xây — xem `doc/01-kien-truc-va-san-pham/plan-ecosystem-scaffold.md`
trong repo `AI_foreducation` (thư mục cha) để biết khoảng cách và thứ tự dự kiến.

## Giấy phép và nguồn tham chiếu

- Quy trình humanize adapt từ [humanize-writing-skill](https://github.com/lguz/humanize-writing-skill) (MIT).
- Quy chuẩn UI tham khảo workflow design-system, UX priority và pre-delivery checks từ
  [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT), rồi siết lại cho
  học liệu đọc dài và giao diện giáo viên.
- Nội dung còn lại là quy tắc nội bộ của SchoolAI, dùng lại tự do trong các dự án của bạn.
