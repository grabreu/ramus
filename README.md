# ramus

[![CI](https://github.com/grabreu/ramus/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/grabreu/ramus/actions/workflows/ci.yml)
[![CD](https://github.com/grabreu/ramus/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/grabreu/ramus/actions/workflows/cd.yml)
[![PyPI](https://img.shields.io/pypi/v/ramus.svg?style=flat-square&logo=pypi&label=ramus)](https://pypi.org/project/ramus/)
[![License](https://img.shields.io/github/license/grabreu/ramus?style=flat-square)](LICENSE)

A cross-platform `tree`/`find`-style CLI for exploring directory structures.

```bash
pip install ramus
```

## Why

Windows' built-in `tree` command only supports `/F` (list files) and `/A` (ASCII characters) — no depth limit, no filtering, nothing else. Linux's `tree`/`find` cover that gap; ramus brings the same to a `pip install`-able package.

```bash
ramus                                # tree of the current directory
ramus -L 2                           # limit depth to 2 levels
```

## Usage

```bash
ramus -I "*.pyc" -I "__pycache__"    # exclude patterns
ramus -P "*.py"                      # include only matching pattern
ramus -a                             # include hidden files/folders
ramus -d                             # directories only
ramus -f                             # print full paths instead of just names
```

Plain text output, no color.

## Development

```bash
uv sync --all-extras --dev
uv run pytest
uv run ruff format .
uv run ruff check .
uv run mypy .
```

Releases (versioning, changelog, and PyPI publish) are automated via [release-please](https://github.com/googleapis/release-please) in CD.

## License

Licensed under the [MIT License](LICENSE).
