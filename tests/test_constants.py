from pathlib import Path

from mypy_boto3_builder.constants import StaticStubsPath, TemplatePath, TEMPLATES_PATH


class TestConstants:
    def test_template_path(self) -> None:
        for key in dir(TemplatePath):
            if key.startswith("_"):
                continue

            path: Path = getattr(TemplatePath, key)
            assert path.is_absolute()
            assert path.exists()
            assert path.relative_to(TEMPLATES_PATH)

    def test_static_stubs_path(self) -> None:
        for key in dir(StaticStubsPath):
            if key.startswith("_"):
                continue
            path: Path = getattr(StaticStubsPath, key)
            assert path.is_absolute()
            assert path.exists()