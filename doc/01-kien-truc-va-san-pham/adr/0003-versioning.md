# ADR 0003 — Versioning: schema_version theo từng file, semantic versioning theo từng repo, chưa xây migration vì mới có 1 version

**Trạng thái:** Chấp nhận (một phần — chính sách migration còn để ngỏ, xem "Việc chưa làm")
**Ngày:** 2026-08-11
**Liên quan:** Milestone 1; `open-lesson-spec/src/open_lesson_spec/models.py`

## Bối cảnh

3 repo (`open-lesson-spec`, `lessonforge`, `EduEvals`) và 1 pack tri thức
(`pedagogy-skill`) tiến hoá độc lập nhưng phải đọc/ghi cùng 1 định dạng
package. Plan mục 11 đã chốt mặc định "semantic versioning" nhưng chưa nói cụ
thể versioning nằm ở đâu.

## Quyết định

1. **Mỗi model cấp file** trong `open_lesson_spec.models` (`ProjectManifest`,
   `SourceManifest`, `Brief`, `ClaimMap`, `ArtifactMeta`, `Quiz`, `AnswerKey`,
   `Rubric`, `Provenance`, `BuildManifest`, `ExtractedSource`, `EvalSummary`)
   có field riêng `schema_version: str = "0.1.0"` — versioning theo TỪNG FILE,
   không phải 1 version chung cho cả package. Lý do: các file này tiến hoá
   không đồng đều (ví dụ thêm `ArtifactMeta.approved` ở Milestone 3 không cần
   đổi version của `quiz.json`).
2. **`build-manifest.json` lưu thêm `package_schema_version`** — đây MỚI là
   version của toàn bộ "hình dạng" package (tập hợp file bắt buộc + cách chúng
   liên kết với nhau, tức `REQUIRED_FILES` trong `package_io.py`), tách biệt
   với `schema_version` của riêng `build-manifest.json`.
3. **Package Python `open-lesson-spec` có version riêng trong `pyproject.toml`
   (`0.1.0`)** — đây là version của CODE (Pydantic models + hàm), độc lập với
   `package_schema_version` của DỮ LIỆU. Trong giai đoạn 0.x, 2 con số này cố
   ý được giữ đồng bộ (cùng `0.1.0`) để dễ theo dõi, nhưng không có ràng buộc
   kỹ thuật bắt chúng phải luôn khớp nhau.
4. **pedagogy-skill được version qua chuỗi định danh `"<tên>@<semver>"`**
   (ví dụ `"pedagogy-skill@0.1.0"`), lưu trong `Brief.pedagogy_pack` và
   `ProvenanceRecord.prompt_version` — không phải version riêng của
   `open-lesson-spec`, vì pedagogy-skill là nội dung/quy tắc, không phải code.

## Việc chưa làm (cố ý hoãn, không phải thiếu sót)

Plan mục 4.1 yêu cầu "quy tắc tương thích giữa các phiên bản" và Giai đoạn A
liệt kê "migration" — hiện tại **CHƯA có code migration nào** vì toàn bộ hệ
thống mới chỉ có đúng 1 version dữ liệu (`0.1.0`). Viết migration logic bây
giờ sẽ là đoán trước hình dạng của version kế tiếp mà không có bằng chứng cần
thiết — vi phạm nguyên tắc "không thiết kế cho yêu cầu giả định". Quyết định:
migration path (`open_lesson_spec.migrate.upgrade(root, from_version,
to_version)` hoặc tương đương) sẽ được thiết kế khi có version `0.2.0` thật sự
cần thiết, dựa trên đúng những field thay đổi tại thời điểm đó — không thiết
kế trước.

## Hệ quả

- Khi 1 field mới được thêm với giá trị mặc định hợp lý (như
  `ArtifactMeta.approved: bool = False` ở Milestone 3), package cũ đọc được mà
  KHÔNG cần bump `schema_version` hay viết migration — Pydantic tự điền
  default. Đây là lý do vì sao ADR này ghi rõ: chỉ bump `schema_version` khi
  thay đổi phá vỡ khả năng đọc ngược (đổi kiểu field, xoá field bắt buộc, đổi
  enum), không bump cho mọi thay đổi.
- Hệ quả phụ đã gặp thật: thêm field mới làm lệch hash đã lưu trong
  `build-manifest.json` của các fixture cũ (vì hash tính trên byte JSON, và
  JSON giờ có thêm 1 key) — đã phải ghi lại `valid-minimal` và
  `vat-ly-10-co-nang-v0.1` bằng `write_package()`. Đây KHÔNG phải lỗi
  migration (dữ liệu vẫn đọc đúng), mà là hệ quả tất yếu của việc hash bám
  theo byte thay vì theo ngữ nghĩa — chấp nhận được vì hash trong
  `build-manifest.json` có mục đích phát hiện thay đổi nội dung, không phải
  định danh ổn định lâu dài.
