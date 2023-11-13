import tempfile
from pathlib import Path
from unittest.mock import patch

from mypy_boto3_builder.utils.path import print_path, walk_path


class TestPath:
    def test_init(self) -> None:
        with patch.object(Path, "cwd") as cwd_mock:
            cwd_mock.return_value = Path("/absolute/")
            assert print_path(Path("./relative")) == "./relative"
            assert print_path(Path("/absolute/path/test")) == "path/test"
            assert print_path(Path("/absolute/path")) == "./path"
            assert print_path(Path("/absolute")) == "/absolute"
            assert print_path(Path("/")) == "/"
            assert print_path(Path(".")) == "."

    def test_walk(self) -> None:
        with tempfile.TemporaryDirectory() as output_dir:
            output_path = Path(output_dir)
            (output_path / "one.txt").touch()
            (output_path / "two.txt").touch()
            result = list(walk_path(output_path))
            assert len(result) == 2
            result = list(walk_path(output_path, [output_path / "one.txt"]))
            assert len(result) == 1
            assert result[0] == output_path / "two.txt"