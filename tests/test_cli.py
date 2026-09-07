from pathlib import Path

from typer.testing import CliRunner

from ramus.cli import app

runner = CliRunner()


def _touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()


def test_cli_lists_tree(tmp_path: Path) -> None:
    _touch(tmp_path / "a.txt")

    result = runner.invoke(app, [str(tmp_path)])

    assert result.exit_code == 0
    assert "a.txt" in result.stdout
    assert "0 directories, 1 file" in result.stdout


def test_cli_dirs_only_flag(tmp_path: Path) -> None:
    _touch(tmp_path / "a.txt")
    (tmp_path / "sub").mkdir()

    result = runner.invoke(app, ["-d", str(tmp_path)])

    assert "sub" in result.stdout
    assert "a.txt" not in result.stdout


def test_cli_level_flag(tmp_path: Path) -> None:
    _touch(tmp_path / "sub" / "nested.txt")

    result = runner.invoke(app, ["-L", "1", str(tmp_path)])

    assert "sub" in result.stdout
    assert "nested.txt" not in result.stdout


def test_cli_rejects_missing_path(tmp_path: Path) -> None:
    missing = tmp_path / "missing"

    result = runner.invoke(app, [str(missing)])

    assert result.exit_code != 0
