# Local-First & Git-Backed Architecture

> **Đối tượng:** tài liệu kiến trúc dành cho đội phát triển. Giáo viên và người
> đọc không chuyên kỹ thuật nên bắt đầu từ
> [`gioi-thieu-cho-giao-vien.md`](gioi-thieu-cho-giao-vien.md).

## Core Design Principle

The ecosystem is designed around a **local-first architecture**.

Educational content, evaluation results, credentials, project files, and other working data remain under the user's control and are processed on the user's own machine whenever possible.

The core tools should not require:

- A centralized database
- A hosted backend
- A mandatory user account system
- Central telemetry
- Server-side storage of project data
- Server-side storage of API keys or credentials

> **Local-first by design. Cloud optional.**

---

## Git-Backed by Default

Skills, curricula, lessons, benchmarks, evaluation definitions, and other reusable educational resources should be stored as human-readable files such as:

- Markdown
- YAML
- JSON
- JSONL

Git is used as the primary versioning and collaboration layer.

This provides:

- Version history
- Diff tracking
- Branching
- Pull requests
- Peer review
- Rollback
- Tags and releases
- Community collaboration

> **Git-backed by default:** Skills, curricula, lessons, and benchmarks are plain-text, version-controlled artifacts that users can inspect, modify, fork, and share.

---

## Recommended Ecosystem Architecture

```text
                     GitHub
                       │
                Skills / Updates
                       │
                       ▼

                 User Machine
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼

   Pedagogy Skill  LessonForge    Edu-Evals

         │             │             │
         └─────────────┼─────────────┘
                       │
                       ▼

                   Local Files
                       │
                       ▼
                      Git
```

The ecosystem does not require a centralized backend for its core functionality.

---

## Repository Responsibilities

### Pedagogy Skill

Stores pedagogical knowledge and teaching rules as version-controlled files.

Examples:

```text
skills/
frameworks/
subjects/
curriculum/
examples/
schemas/
```

Typical formats:

```text
.md
.yaml
.json
```

The repository should be fully usable without a database.

---

### LessonForge

Runs lesson generation on the user's machine.

Typical workflow:

```text
lesson.yaml
     ↓
Pedagogy Skill
     ↓
LLM Provider
     ↓
lesson.md
worksheet.md
quiz.json
rubric.json
```

Generated content should be stored locally.

Users decide whether they want to commit and share the generated content through Git.

---

### Edu-Evals

Runs educational-content evaluation locally.

Example output structure:

```text
runs/
└── 2026-08-11-model-name/
    ├── config.json
    ├── results.jsonl
    ├── summary.json
    └── report.md
```

Benchmark results remain local by default.

Users may voluntarily publish selected benchmark results through Git.

---

## Public vs Private Data

Repositories should clearly separate shareable resources from local/private data.

Recommended structure:

```text
repository/
│
├── skills/
├── curriculum/
├── examples/
├── benchmarks/
│
└── .local/
    ├── secrets/
    ├── cache/
    ├── sessions/
    └── private-data/
```

Recommended `.gitignore`:

```gitignore
.local/

.env
.env.*
*.key
*.pem

cache/
tmp/

private/
student-data/
```

Sensitive information must never be committed by default.

---

## API Key Security

API keys should never be stored inside committed project files.

Do not use:

```yaml
openai_api_key: sk-xxxx
```

Prefer environment variables:

```bash
export OPENAI_API_KEY="..."
```

Applications can read them locally:

```python
import os

api_key = os.environ.get("OPENAI_API_KEY")
```

If `.env` files are supported, they must be excluded from Git:

```gitignore
.env
.env.*
```

---

## AI Provider Architecture

The ecosystem should remain provider-agnostic.

```text
AI Provider Interface
│
├── OpenAI
├── Ollama
├── LM Studio
├── vLLM
└── Custom OpenAI-Compatible API
```

Cloud providers are optional.

When using a cloud provider:

```text
User Machine
     │
     │ HTTPS
     ▼
Cloud AI Provider
```

The ecosystem should avoid routing requests through a project-owned central server.

---

## Full Local Mode

For stronger privacy, users should be able to use local AI providers.

Example:

```text
User Machine
     │
     ▼
LessonForge
     │
     ▼
Ollama / LM Studio / vLLM
     │
     ▼
Local Model
```

In this mode, educational data can remain entirely on the user's machine.

---

## Community Collaboration Model

Git becomes the collaboration mechanism for reusable educational knowledge.

Example workflow:

```text
Community Member
      ↓
Create / Improve Skill
      ↓
Commit
      ↓
Pull Request
      ↓
Schema Validation
      ↓
Pedagogy Evaluation
      ↓
Human Review
      ↓
Merge
      ↓
Release
```

Users receive updates through normal Git workflows.

---

## Why This Architecture

This architecture provides several benefits:

### Privacy

Users retain control of lessons, educational materials, evaluation results, and private project data.

### Security

The project does not need to centrally store user API keys or sensitive educational data.

### Transparency

Most core resources are plain-text files that can be inspected and audited.

### Portability

Users can clone the repositories and work independently.

### Offline Capability

With local AI models, much of the ecosystem can operate without cloud services.

### Community Ownership

Skills and curricula can be forked, modified, reviewed, and improved through Git.

### Reduced Infrastructure Complexity

The core open-source project does not require operating a centralized database or backend service.

---

## Architectural Rule

A useful rule for future development is:

> **If a feature can work locally without a centralized service, it should work locally by default.**

Centralized infrastructure should only be introduced when it provides clear value that cannot reasonably be achieved through local files and Git.

---

## Privacy Statement

> **Local-first architecture:** Educational content, evaluation results, credentials, and project data remain under the user's control. The core tools require no centralized database or hosted backend.

> **Git-backed by default:** Skills, curricula, lessons, and benchmarks are plain-text, version-controlled artifacts that users can inspect, modify, fork, and share.

> **Cloud optional:** Users can connect to cloud AI providers when desired, while local providers such as Ollama, LM Studio, or vLLM can be used for workflows that require stronger privacy.

---

## Final Direction

The core ecosystem should follow this model:

```text
Pedagogy Skill
      ↓
Local pedagogical knowledge

LessonForge
      ↓
Local educational content generation

Edu-Evals
      ↓
Local educational quality evaluation

Git
      ↓
Versioning + collaboration

Cloud AI
      ↓
Optional provider

Local AI
      ↓
Privacy-first provider
```

### Guiding Statement

> **Build an open-source educational AI ecosystem that runs on the user's machine, stores knowledge as version-controlled files, keeps private data under user control, and treats cloud infrastructure as optional rather than mandatory.**
