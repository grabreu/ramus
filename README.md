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

Windows' built-in `tree` command only supports `/F` (list files) and `/A` (ASCII characters) — no depth limit, no filtering, nothing else. Linux's `tree`/`find` cover that gap; ramus brings the same behavior to a `pip install`-able package.

```
$ ramus
.
├── README.md
├── src
│   ├── app.py
│   └── app.pyc
└── tests
    └── test_app.py

2 directories, 4 files
```

## Usage

```
$ ramus -I "*.pyc"
.
├── README.md
├── src
│   └── app.py
└── tests
    └── test_app.py

2 directories, 3 files
```

| Flag | | |
|---|---|---|
| `-L N` | `--level` | Limit recursion to `N` levels |
| `-I PATTERN` | `--exclude` | Exclude entries matching a glob pattern (repeatable) |
| `-P PATTERN` | `--pattern` | Include only entries matching a glob pattern (directories are always shown so matching descendants stay reachable) |
| `-a` | `--all` | Include hidden files and directories |
| `-d` | `--dirs-only` | List directories only |
| `-f` | `--full-path` | Print each entry's full path instead of just its name |

Symlinked directories are listed but not followed. Plain text output, no color.

## Development

```bash
uv sync --dev
uv run pytest
uv run ruff format .
uv run ruff check .
uv run mypy .
```

Releases (versioning, changelog, and PyPI publish) are automated via [release-please](https://github.com/googleapis/release-please) in CD.

## License

Licensed under the [MIT License](LICENSE).
