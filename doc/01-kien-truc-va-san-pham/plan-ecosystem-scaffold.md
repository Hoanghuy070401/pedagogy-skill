**Status (2026-08-11): đã dựng bộ khung kỹ thuật cho cả 3 repo và kiểm tra luồng
đọc/ghi tệp; chưa kiểm chứng chất lượng tạo bài, chất lượng đánh giá giáo dục,
khả năng sử dụng của giáo viên hoặc hiệu quả trong lớp học; chưa commit.** Xem
"Implementation notes" ở cuối tài liệu.

> Tài liệu này ghi lại phạm vi scaffold ban đầu. Kế hoạch triển khai tiếp theo đã
> chuyển sang [`plan-xay-dung-he-sinh-thai.md`](plan-xay-dung-he-sinh-thai.md),
> ưu tiên hợp đồng dữ liệu và vertical slice kỹ thuật; thẩm định giáo viên tạm
> thời không phải blocker.

# Plan — Scaffold the 3-repo educational AI ecosystem

Source: gap analysis of `doc/01-kien-truc-va-san-pham/startdoc.md` against the current state of
`pedagogy-skill`, `lessonforge`, `EduEvals` (2026-08-11).

## Current state (2026-08-11, after scaffold implementation)

| Repo | State | Gap vs. `startdoc.md` |
|---|---|---|
| `pedagogy-skill` | Có bộ quy tắc soạn bài tiếng Việt và scope note | Chưa có taxonomy đầy đủ theo môn/cấp học và chưa có benchmark nghiệp vụ |
| `lessonforge` | Có scaffold CLI, provider interface và luồng tạo `lesson.md` | Chưa có generation nghiệp vụ cho lesson package hoàn chỉnh; chưa thử với giáo viên |
| `EduEvals` | Có scaffold runner và cấu trúc thư mục kết quả | Scorer vẫn là placeholder; chưa đo chất lượng giáo dục |

Các thay đổi scaffold hiện chưa commit. Bảng này mô tả trạng thái file đang có
trong working tree, không phải trạng thái của commit gần nhất.

### Historical baseline before scaffold

Trước vòng implementation ngày 2026-08-11, `lessonforge` và `EduEvals` là repo
rỗng; chưa có `.gitignore`, `.local/`, env-var API key handling hoặc provider
interface. Baseline này giải thích phạm vi của plan nhưng không còn là trạng
thái hiện tại.

## Goal

Stand up the minimum real structure in all three repos so they match the
local-first / git-backed architecture in `startdoc.md`, without over-building
ahead of actual lesson-generation or eval logic.

## Scope

**In scope:**
1. `lessonforge` — initial scaffold: CLI entry point, provider-agnostic AI
   interface (OpenAI / Ollama / LM Studio / vLLM), `lesson.yaml` input shape,
   local output writing (`lesson.md`, `worksheet.md`, `quiz.json`,
   `rubric.json`), env-var API key handling, `.gitignore` + `.local/`.
2. `EduEvals` — initial scaffold: `runs/<date>-<model>/` output convention
   (`config.json`, `results.jsonl`, `summary.json`, `report.md`), env-var API
   key handling, `.gitignore` + `.local/`.
3. `pedagogy-skill` — add a short note in `README.md` clarifying it is
   currently scoped to lesson-authoring rules (not the full
   `frameworks/subjects/curriculum/schemas` taxonomy from `startdoc.md`), so
   the gap is documented rather than silent. Add `.gitignore` for consistency.

**Out of scope (defer):**
- Actual lesson-generation logic / prompting in `lessonforge`.
- Actual eval suites / scoring logic in `EduEvals`.
- Expanding `pedagogy-skill` into the full taxonomy (`frameworks/`,
  `subjects/`, `curriculum/`, `schemas/`) — real content work, not scaffolding.
- Community PR/review workflow (schema validation, CI) — needs real schemas
  first.
- Any centralized backend/DB — explicitly against the architecture.

## Proposed structure

### `lessonforge`

```
lessonforge/
  README.md
  .gitignore
  pyproject.toml (or package.json — TBD, see open question)
  src/lessonforge/
    cli.py                  # typer entry point: lessonforge generate lesson.yaml
    models.py                # pydantic models for lesson.yaml, outputs
    providers/
      base.py                # AIProvider interface
      openai_provider.py
      ollama_provider.py
      lmstudio_provider.py
      vllm_provider.py
    pipeline.py              # lesson.yaml -> pedagogy-skill markdown -> provider -> outputs
  examples/
    lesson.yaml              # sample input
  .local/                    # gitignored — generated lessons land here by default
```

`AIProvider` interface: `generate(prompt: str, **params) -> str`, reads API
key from `os.environ`, never accepts a key as a YAML/JSON field.

### `EduEvals`

```
EduEvals/
  README.md
  .gitignore
  pyproject.toml
  src/eduevals/
    cli.py                   # typer entry point: eduevals run --config config.json
    models.py                 # pydantic models for config.json, results
    runner.py                # writes results.jsonl, summary.json, report.md
  examples/
    config.json               # sample eval config
  .local/
    runs/                     # gitignored by default; user opts in per-run to commit
```

### `pedagogy-skill`

No structural change. Add to `README.md`:

> Scope note: this repo currently holds the lesson-authoring rule set only.
> The broader `frameworks/ subjects/ curriculum/ schemas/` taxonomy described
> in the ecosystem doc is not built yet — see `doc/01-kien-truc-va-san-pham/plan-ecosystem-scaffold.md`
> in `AI_foreducation` for the gap and sequencing.

Add a minimal `.gitignore` (`.local/`, `.env*`) for consistency with the other
two repos, even though nothing currently needs it.

### Shared `.gitignore` (lessonforge, EduEvals, pedagogy-skill)

```gitignore
.local/
.env
.env.*
*.key
*.pem
cache/
tmp/
```

## Sequencing

1. `lessonforge` scaffold first — it's the piece with the clearest spec in
   `startdoc.md` (explicit input/output shapes) and the one other repos don't
   depend on.
2. `EduEvals` scaffold second — same pattern, independent of `lessonforge`.
3. `pedagogy-skill` README note — 5-minute change, can happen anytime.

## Decisions

- **Language/runtime**: Python (`pyproject.toml`) for both `lessonforge` and
  `EduEvals`. CLI framework: `typer` (pairs well with `pydantic` for parsing
  `lesson.yaml` / `config.json` into typed models).
- **pedagogy-skill coupling**: provider-agnostic. `lessonforge` reads
  `pedagogy-skill/SKILL.md` and `references/*.md` as plain markdown and
  injects the relevant sections into whatever provider prompt it builds
  (OpenAI / Ollama / LM Studio / vLLM). It does not shell out to Claude Code
  or depend on the Skill format at runtime — `pedagogy-skill` stays a
  content repo, not a runtime dependency.

## Non-goals

- No centralized DB or backend, per `startdoc.md`'s core rule.
- No mandatory user accounts or telemetry.
- No API keys committed anywhere, ever.

## Implementation notes (2026-08-11)

Đã cài các package vào một môi trường thử, chạy CLI và kiểm tra việc tạo tệp đầu
ra. Đây là **kiểm thử luồng kỹ thuật**, không phải kiểm thử sản phẩm giáo dục.
Chưa có bài học hoàn chỉnh để giáo viên thẩm định và chưa thử trong lớp:

| Thành phần | Đã xây | Đã kiểm thử kỹ thuật | Đã thử với giáo viên | Đã thử trong lớp |
|---|---|---|---|---|
| `lessonforge` scaffold | Có | Một phần; chưa tạo thành công bài hoàn chỉnh | Chưa | Chưa |
| `EduEvals` scaffold | Có | Có ở mức ghi file bằng scorer placeholder | Chưa | Chưa |
| `pedagogy-skill` rule set | Có nội dung ban đầu | Chưa có benchmark nghiệp vụ | Chưa | Chưa |

- **`lessonforge`**: `AIProvider` interface + `OpenAIProvider`/`OllamaProvider`/
  `LMStudioProvider`/`VLLMProvider` (last three share an
  `OpenAICompatibleProvider` base since they all speak the OpenAI-compatible
  API). Pipeline reads `pedagogy-skill/SKILL.md` + `references/*.md` as plain
  markdown from the sibling repo, builds a prompt, calls the provider, writes
  `lesson.md` under `.local/output/`. Đã thử gọi một Ollama instance local;
  request tới bước gọi mạng nhưng không tạo được nội dung vì máy
  chưa có model `llama3`. Vì vậy chưa thể kết luận chất lượng generation.
  **Found and fixed a real bug**: Typer
  collapses a single `@app.command()` into the top-level command, so
  `lessonforge generate file.yaml` doesn't parse — corrected CLI usage to
  `lessonforge file.yaml --provider ...` (README updated to match).
- **`EduEvals`**: `EvalConfig`/`EvalResult`/`EvalSummary` pydantic models,
  `run_eval()` with a pluggable `Scorer`, default placeholder scorer (passes
  non-empty items) để kiểm tra luồng ghi file. Một lần chạy thử đã tạo
  `runs/2026-08-11-gpt-4o-mini/{config.json,results.jsonl,summary.json,report.md}`
  under `.local/runs/` matching `startdoc.md`'s file convention. Kết quả này chỉ
  chứng minh runner ghi được file; placeholder scorer chưa đo chất lượng giáo
  dục. Typer single-command behavior applied here too — CLI is
  `eduevals --config config.json`, no `run` subcommand needed.
- **`pedagogy-skill`**: added scope note to `README.md` + `.gitignore` for
  consistency with the other two repos.

**Not yet done:** none of the changes are committed in any of the three repos
— `git status` in each shows the new/modified files as untracked/modified,
waiting on your go-ahead.
