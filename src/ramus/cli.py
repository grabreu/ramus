"""Typer CLI entry point for ramus."""

from __future__ import annotations

import sys
from pathlib import Path

import typer

from ramus.render import render
from ramus.walker import walk

app = typer.Typer(add_completion=False)


def _ensure_utf8_stdout() -> None:
    """Force UTF-8 output so the tree glyphs don't crash on legacy Windows codepages."""
    encoding = sys.stdout.encoding
    if encoding is not None and encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]


@app.command()
def main(
    path: Path = typer.Argument(
        Path("."), exists=True, file_okay=False, help="Directory to display."
    ),
    level: int | None = typer.Option(
        None, "-L", "--level", min=1, help="Limit recursion to N levels."
    ),
    exclude: list[str] = typer.Option(
        [], "-I", "--exclude", help="Exclude entries matching this glob pattern (repeatable)."
    ),
    pattern: str | None = typer.Option(
        None, "-P", "--pattern", help="Include only entries matching this glob pattern."
    ),
    show_hidden: bool = typer.Option(
        False, "-a", "--all", help="Include hidden files and directories."
    ),
    dirs_only: bool = typer.Option(False, "-d", "--dirs-only", help="List directories only."),
    full_path: bool = typer.Option(
        False, "-f", "--full-path", help="Print the full path instead of just the name."
    ),
) -> None:
    """Print a tree of PATH (defaults to the current directory)."""
    _ensure_utf8_stdout()
    entries = walk(
        path,
        level=level,
        excludes=tuple(exclude),
        pattern=pattern,
        show_hidden=show_hidden,
        dirs_only=dirs_only,
    )
    for line in render(path, entries, full_path=full_path, dirs_only=dirs_only):
        typer.echo(line)
