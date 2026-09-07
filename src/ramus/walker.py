"""Directory tree walking: builds a filtered, sorted list of Entry objects."""

from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Entry:
    """A single entry in the walked tree, with enough context to render it."""

    path: Path
    depth: int
    is_dir: bool
    is_last: bool
    ancestors_last: tuple[bool, ...]


def walk(
    root: Path,
    *,
    level: int | None = None,
    excludes: tuple[str, ...] = (),
    pattern: str | None = None,
    show_hidden: bool = False,
    dirs_only: bool = False,
) -> list[Entry]:
    """Walk `root` and return its filtered, sorted entries (root itself excluded)."""
    return _walk(
        root,
        depth=1,
        ancestors_last=(),
        level=level,
        excludes=excludes,
        pattern=pattern,
        show_hidden=show_hidden,
        dirs_only=dirs_only,
    )


def _walk(
    directory: Path,
    *,
    depth: int,
    ancestors_last: tuple[bool, ...],
    level: int | None,
    excludes: tuple[str, ...],
    pattern: str | None,
    show_hidden: bool,
    dirs_only: bool,
) -> list[Entry]:
    children = _list_children(
        directory,
        excludes=excludes,
        pattern=pattern,
        show_hidden=show_hidden,
        dirs_only=dirs_only,
    )

    entries: list[Entry] = []
    last_index = len(children) - 1
    for index, child in enumerate(children):
        is_last = index == last_index
        is_dir = child.is_dir()
        entries.append(
            Entry(
                path=child,
                depth=depth,
                is_dir=is_dir,
                is_last=is_last,
                ancestors_last=ancestors_last,
            )
        )
        if is_dir and not child.is_symlink() and (level is None or depth < level):
            entries.extend(
                _walk(
                    child,
                    depth=depth + 1,
                    ancestors_last=(*ancestors_last, is_last),
                    level=level,
                    excludes=excludes,
                    pattern=pattern,
                    show_hidden=show_hidden,
                    dirs_only=dirs_only,
                )
            )
    return entries


def _list_children(
    directory: Path,
    *,
    excludes: tuple[str, ...],
    pattern: str | None,
    show_hidden: bool,
    dirs_only: bool,
) -> list[Path]:
    children: list[Path] = []
    for child in directory.iterdir():
        name = child.name
        if not show_hidden and name.startswith("."):
            continue
        if any(fnmatch(name, exclude) for exclude in excludes):
            continue
        is_dir = child.is_dir()
        if dirs_only and not is_dir:
            continue
        if pattern is not None and not is_dir and not fnmatch(name, pattern):
            continue
        children.append(child)
    return sorted(children, key=lambda p: p.name.lower())
