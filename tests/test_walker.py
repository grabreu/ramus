from pathlib import Path

import pytest

from ramus.walker import walk


def _touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()


def test_lists_files_and_dirs_sorted(tmp_path: Path) -> None:
    _touch(tmp_path / "b.txt")
    _touch(tmp_path / "a.txt")
    (tmp_path / "sub").mkdir()

    entries = walk(tmp_path)

    assert [e.path.name for e in entries] == ["a.txt", "b.txt", "sub"]


def test_recurses_into_subdirectories(tmp_path: Path) -> None:
    _touch(tmp_path / "sub" / "nested.txt")

    entries = walk(tmp_path)

    assert [e.path.name for e in entries] == ["sub", "nested.txt"]
    assert [e.depth for e in entries] == [1, 2]


def test_level_limits_depth(tmp_path: Path) -> None:
    _touch(tmp_path / "sub" / "nested.txt")

    entries = walk(tmp_path, level=1)

    assert [e.path.name for e in entries] == ["sub"]


def test_hidden_entries_excluded_by_default(tmp_path: Path) -> None:
    _touch(tmp_path / ".hidden")
    _touch(tmp_path / "visible.txt")

    entries = walk(tmp_path)

    assert [e.path.name for e in entries] == ["visible.txt"]


def test_all_includes_hidden_entries(tmp_path: Path) -> None:
    _touch(tmp_path / ".hidden")
    _touch(tmp_path / "visible.txt")

    entries = walk(tmp_path, show_hidden=True)

    assert [e.path.name for e in entries] == [".hidden", "visible.txt"]


def test_exclude_pattern(tmp_path: Path) -> None:
    _touch(tmp_path / "keep.txt")
    _touch(tmp_path / "skip.pyc")

    entries = walk(tmp_path, excludes=("*.pyc",))

    assert [e.path.name for e in entries] == ["keep.txt"]


def test_pattern_filters_files_but_keeps_directories(tmp_path: Path) -> None:
    _touch(tmp_path / "match.py")
    _touch(tmp_path / "skip.txt")
    _touch(tmp_path / "sub" / "nested.py")

    entries = walk(tmp_path, pattern="*.py")

    assert [e.path.name for e in entries] == ["match.py", "sub", "nested.py"]


def test_dirs_only(tmp_path: Path) -> None:
    _touch(tmp_path / "file.txt")
    (tmp_path / "sub").mkdir()

    entries = walk(tmp_path, dirs_only=True)

    assert [e.path.name for e in entries] == ["sub"]


def test_symlink_to_directory_is_not_followed(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()
    _touch(target / "inside.txt")
    link = tmp_path / "link"
    try:
        link.symlink_to(target, target_is_directory=True)
    except OSError:
        pytest.skip("creating symlinks is not permitted on this platform")

    entries = walk(tmp_path)

    assert [e.path.name for e in entries] == ["link", "target", "inside.txt"]
