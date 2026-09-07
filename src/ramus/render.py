"""Turns a walked entry list into printable, tree-style lines."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from ramus.walker import Entry


def render(root: Path, entries: Sequence[Entry], *, full_path: bool, dirs_only: bool) -> list[str]:
    """Render `entries` as tree-style lines, with a root header and a summary footer."""
    lines = [str(root)]
    lines.extend(_render_entry(entry, full_path=full_path) for entry in entries)
    lines.append("")
    lines.append(_summary(entries, dirs_only=dirs_only))
    return lines


def _render_entry(entry: Entry, *, full_path: bool) -> str:
    prefix = "".join("    " if last else "│   " for last in entry.ancestors_last)
    branch = "└── " if entry.is_last else "├── "
    label = str(entry.path) if full_path else entry.path.name
    return f"{prefix}{branch}{label}"


def _summary(entries: Sequence[Entry], *, dirs_only: bool) -> str:
    dirs = sum(1 for entry in entries if entry.is_dir)
    dir_word = "directory" if dirs == 1 else "directories"
    if dirs_only:
        return f"{dirs} {dir_word}"
    files = len(entries) - dirs
    file_word = "file" if files == 1 else "files"
    return f"{dirs} {dir_word}, {files} {file_word}"
