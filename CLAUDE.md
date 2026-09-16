# ramus

## Repository

A single Python package published as [`ramus`](https://pypi.org/project/ramus/): a cross-platform `tree`/`find`-style CLI for exploring directory structures.

Read `README.md` before making changes — it documents the actual public CLI (usage, flags).

## General Rules

- Keep changes scoped to the requested change.
- Prefer existing patterns over introducing new abstractions.
- Do not add dependencies unless they are necessary.
- Do not fill gaps with assumptions when the user hasn't given the information — ask, or mark it as pending.
- Do not claim a validation command passed unless it was actually run.
- Code, comments, commit messages, and documentation are always written in English.

## Git

- Do not create or switch branches unless explicitly requested.
- Do not create commits unless explicitly requested.
- Do not push unless explicitly requested.
- Keep commits focused on the requested change.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (`type: summary`).

## Documentation

### Audience

A developer evaluating whether to install this CLI. Not onboarding material — keep it concise and skimmable.

### Content Rules

- State facts concisely. Avoid unnecessary explanations or trailing rationale.
- Do not document information that is already obvious from the repository structure or configuration.
- Do not invent features, API shapes, or future direction — mark undecided things as TODO.
- Document a capability only after it is implemented and verified.
- Use proper Markdown headings (`##`, `###`), not bold text as headings.

---

## Project-Specific Guidelines

### Source

- `src/ramus/walker.py` - `walk`/`Entry`: recursive directory traversal with hidden/exclude/pattern/dirs-only filtering and sorting.
- `src/ramus/render.py` - `render`: turns walked entries into tree-style lines (box-drawing glyphs, full-path mode, summary footer).
- `src/ramus/cli.py` - Typer app: option parsing (`-L`/`-I`/`-P`/`-a`/`-d`/`-f`), wires `walker` → `render` → stdout, forces UTF-8 stdout so tree glyphs don't crash on legacy Windows codepages.

Every function/class should have matching coverage in `tests/`.

### Validation

Run `uv run ruff format --check .`, `uv run ruff check .`, `uv run mypy .`, and `uv run pytest` before considering a change done — CI (`.github/workflows/ci.yml`) runs the same on push/PR to `main`.
