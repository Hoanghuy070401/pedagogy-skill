# Integration tests

Test tích hợp xuyên `open-lesson-spec` → `lessonforge` → `EduEvals`, xác nhận package do
`lessonforge` sinh ra được `EduEvals` đọc và validate mà không cần chuyển đổi thủ công
(điều kiện hoàn thành của Milestone 1 trong
`doc/01-kien-truc-va-san-pham/plan-xay-dung-he-sinh-thai.md`).

Mỗi sub-project (`open-lesson-spec/`, `lessonforge/`, `EduEvals/`, `lesson-studio/`) có
`.venv` riêng cho test nội bộ của nó. Test ở đây cần cả bốn cài chung một venv:

```bash
cd /Volumes/Disk_1/AI/AI_foreducation
python3 -m venv .venv-integration
source .venv-integration/bin/activate
pip install -e "open-lesson-spec[dev]" -e "lessonforge[dev]" -e "EduEvals[dev]" -e "lesson-studio[dev]"
```

Chạy TỪNG bộ test bằng 1 lệnh `pytest` RIÊNG cho mỗi thư mục, KHÔNG gộp chung 1 lệnh
`pytest` duy nhất — 4 sub-project đều có `tests/conftest.py` không đặt trong package
(không có `__init__.py`), nên khi pytest nạp chung cả 4 trong 1 lần chạy, các file
`conftest.py`/`test_*.py` trùng tên (ví dụ mỗi nơi đều dễ có 1 file dùng chung tên biến)
tranh chấp cùng 1 khoá module `conftest`/`test_x` trong `sys.modules`, làm sai lệch việc
`from conftest import ...` — không phải lỗi logic, chỉ là giới hạn cách pytest nạp module
không-phải-package. Chạy tách theo từng thư mục né hoàn toàn vấn đề này mà không cần sửa
lại 4 bộ test đã pass độc lập:

```bash
pytest open-lesson-spec/tests -q
pytest lessonforge/tests -q
pytest EduEvals/tests -q
pytest lesson-studio/tests -q
pytest tests -q
```

Hoặc dùng vòng lặp:

```bash
for d in open-lesson-spec lessonforge EduEvals lesson-studio .; do
  pytest "$d/tests" -q || echo "FAILED: $d"
done
```
