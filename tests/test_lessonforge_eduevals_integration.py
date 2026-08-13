import json
import shutil
from pathlib import Path

from eduevals.evaluator import evaluate_package
from lessonforge.package import generate_lesson_package
from lessonforge.providers.base import AIProvider
from open_lesson_spec import read_package

REPO_ROOT = Path(__file__).resolve().parents[1]
LESSON_SPEC = REPO_ROOT / "lessonforge" / "examples" / "lesson.yaml"
VAT_LY_10_FIXTURE = (
    REPO_ROOT / "open-lesson-spec" / "fixtures" / "vat-ly-10-co-nang-v0.1"
)


class FakeProvider(AIProvider):
    def __init__(self, model: str = "fake-model"):
        self.model = model

    def generate(self, prompt: str, **params) -> str:
        return "# Bài học giả lập\n\nNội dung do FakeProvider trả về.\n"


def test_lessonforge_package_passes_eduevals_validation(tmp_path):
    package_root = generate_lesson_package(
        LESSON_SPEC, FakeProvider(), tmp_path / "package"
    )

    eval_dir = evaluate_package(package_root)

    summary = json.loads((eval_dir / "summary.json").read_text(encoding="utf-8"))
    assert summary["errors"] == 0
    assert summary["passed"] is True
    assert (eval_dir / "results.jsonl").exists()
    assert (eval_dir / "report.md").exists()

    package = read_package(package_root)
    assert package.build_manifest.eval_summary_ref is None, (
        "eval/ was written after build-manifest.json; ref only reflects state at "
        "write_package() time, not a live pointer"
    )


def test_vat_ly_10_pilot_fixture_passes_eduevals_validation(tmp_path):
    package_root = tmp_path / "vat-ly-10-co-nang-v0.1"
    shutil.copytree(VAT_LY_10_FIXTURE, package_root)

    eval_dir = evaluate_package(package_root)

    summary = json.loads((eval_dir / "summary.json").read_text(encoding="utf-8"))
    results = [
        json.loads(line)
        for line in (eval_dir / "results.jsonl").read_text(encoding="utf-8").splitlines()
    ]

    assert summary["errors"] == 0, [r for r in results if r["severity"] == "error"]
    assert summary["passed"] is True

    package = read_package(package_root)
    assert package.project.project_id == "co-nang-va-su-chuyen-hoa-nang-luong"
    assert len(package.claims.claims) == 7
    assert len(package.artifacts.quiz.questions) == 8
    rejected = [q for q in package.artifacts.quiz.questions if q.status == "rejected"]
    assert [q.question_id for q in rejected] == ["q8"]
