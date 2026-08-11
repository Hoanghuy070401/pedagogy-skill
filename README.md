# soan-bai-hoc — skill soạn bài học tiếng Việt

Bản mang đi được của bộ kỹ năng soạn bài trong SchoolAI Studio (`schoolAI-deploy/website`).
Trích ngày 10/08/2026 từ `STUDIO-AGENT-RULES.md`, `HUONG-DAN-SOAN-BAI.md`, `STUDIO-ASSET-RULES.md`.

## Cấu trúc

```
soan-bai-hoc/
  SKILL.md                          ← entry point: quy trình 5 bước + 8 luật cứng
  references/
    00-rule-set-agent.md            ← hợp đồng prompt cho agent tự soạn bài
    01-huong-dan-soan-bai.md        ← bản đầy đủ (§5 văn phong, §6.1–6.10 luật chi tiết)
    02-quy-tac-asset.md             ← minh hoạ sinh từ code trước; điều kiện dùng ảnh raster
    03-van-phong-humanize.md        ← quy trình 3 lượt + từ/cấu trúc cần tránh
    04-checklist-truoc-merge.md     ← checklist chốt trước bàn giao
  assets/
    mau-bai-khai-niem.md            ← khung một bài để copy
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

**Agent/tool khác:** nạp thẳng `SKILL.md` vào system prompt, và `references/00-rule-set-agent.md`
vào prompt của agent soạn bài. Các file `references/01–04` để agent đọc khi cần chi tiết.

## Cập nhật khi bản gốc đổi

Bốn file gốc nằm ở `schoolAI-deploy/website/`. Khi chúng đổi, copy lại `references/00–02` rồi
soát tay `03`, `04` và `SKILL.md` (đây là bản trích/rút gọn, không sinh tự động).

## Giấy phép và nguồn tham chiếu

- Quy trình humanize adapt từ [humanize-writing-skill](https://github.com/lguz/humanize-writing-skill) (MIT).
- Nội dung còn lại là quy tắc nội bộ của SchoolAI, dùng lại tự do trong các dự án của bạn.
