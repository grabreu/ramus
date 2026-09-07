# ramus

## Repository

A single Python package published as [`ramus`](https://pypi.org/project/ramus/): a cross-platform `tree`/`find`-style CLI for exploring directory structures.

Read `README.md` before making changes — it documents the actual public CLI (usage, flags).

## General Rules

- Keep changes scoped to the requested change.
- Prefer existing patterns over introducing new abstractions.
- Do not add dependencies unless they are necessary.
- Run formatting, linting, typecheck, and tests after changes.
- Do not change CI/CD configuration unless explicitly required.
- Do not claim a validation command passed unless it was actually run.
- Do not fill gaps with assumptions when the user hasn't given the information — ask, or mark it as pending.
- Code, comments, commit messages, and documentation are always written in English.

## Source

No source code yet — package layout and entry point are still to be scaffolded.

## Validation

- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run mypy .`
- `uv run pytest`

## Git

Follow the conventions defined in `CONTRIBUTING.md` for branches, commits, and pull requests.

- Do not create or switch branches unless explicitly requested by the user.
- Do not create commits unless explicitly requested by the user.
- Do not push changes unless explicitly requested by the user.
- Keep commits focused on the requested change.

## Releases

Versioning, changelog, and PyPI publish are automated by [release-please](https://github.com/googleapis/release-please) — see `CONTRIBUTING.md` for how commit types map to version bumps. Do not hand-edit `version` in `pyproject.toml` or `.release-please-manifest.json`; release-please owns both after the initial `1.0.0` bootstrap.

## Documentation

Follow the documentation conventions below when creating or updating project documentation.

### Audience

Write for a developer evaluating whether to install this CLI.

Keep documentation concise and skimmable. Do not write onboarding tutorials unless explicitly requested.

### README Structure

`README.md` — badges, one-line description, install, `Why` (with a runnable example), usage/flags, `Development`, `License`.

Keep the existing README structure unless there is a clear reason to change it.

### Content Rules

- State facts concisely. Avoid unnecessary explanations or trailing rationale.
- Do not document information that is already obvious from the repository structure or configuration.
- Do not invent features, API shapes, or future direction.
- Document a capability only after it is implemented and verified.
- Use proper Markdown headings (`##`, `###`, etc.), not bold text as headings.
