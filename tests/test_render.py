from pathlib import Path

from ramus.render import render
from ramus.walker import Entry


def test_render_basic_tree() -> None:
    entries = [
        Entry(path=Path("root/a.txt"), depth=1, is_dir=False, is_last=False, ancestors_last=()),
        Entry(path=Path("root/sub"), depth=1, is_dir=True, is_last=True, ancestors_last=()),
        Entry(
            path=Path("root/sub/nested.txt"),
            depth=2,
            is_dir=False,
            is_last=True,
            ancestors_last=(True,),
        ),
    ]

    lines = render(Path("root"), entries, full_path=False, dirs_only=False)

    assert lines == [
        "root",
        "├── a.txt",
        "└── sub",
        "    └── nested.txt",
        "",
        "1 directory, 2 files",
    ]


def test_render_full_path() -> None:
    nested_path = Path("root/sub/nested.txt")
    entries = [
        Entry(
            path=nested_path,
            depth=1,
            is_dir=False,
            is_last=True,
            ancestors_last=(),
        ),
    ]

    lines = render(Path("root"), entries, full_path=True, dirs_only=False)

    assert lines[1] == f"└── {nested_path}"


def test_render_dirs_only_summary() -> None:
    entries = [
        Entry(path=Path("root/sub"), depth=1, is_dir=True, is_last=True, ancestors_last=()),
    ]

    lines = render(Path("root"), entries, full_path=False, dirs_only=True)

    assert lines[-1] == "1 directory"
