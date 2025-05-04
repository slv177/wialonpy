# Changelog

## [0.1.4] – 2025-05-04

### Added
- `get_wialon_units`: new function to fetch the list of units via `core/search_items`, with customizable `flags` support.
- Support for optional `row_from`, `row_to`, and `level` parameters in `wialon_select_result` for filtering and limiting report results.
- New helper function to retrieve report rows using the `core/batch` API.
- Integrated code quality tools: **Ruff**, **Mypy**, and **Bandit** for linting, type checking, and security analysis.

### Changed
- Renamed internal function `wialon_get_session_eid` to `get_session_eid` for clarity and consistency with naming conventions.


## [0.1.3] - 2025-05-04

### Changed
- Bump version to 0.1.3 to enable PyPI re-upload after 0.1.2 packaging fix

## [0.1.2] - 2025-05-04

### Added
- `wialon_select_result`: optional parameters `row_from`, `row_to`, `level`
- `wialon_select_result`: support for retrieving report result rows via `core/batch`
- `wialon_exec_report`: function to execute reports via `report/exec_report`
- `get_wialon_group_id_by_name`: group ID lookup by name with error handling and logging

### Changed
- Improved internal structure and API flexibility

---

## [0.1.1] - 2025-05-03

### Added
- `wialon_get_session_eid`: session authentication with logging and custom exception class

---

## [0.1.0] - 2025-05-02

### Initial
- Initial commit and basic project structure

