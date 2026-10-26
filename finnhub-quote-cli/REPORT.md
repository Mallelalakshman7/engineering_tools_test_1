# Finnhub Quote CLI — Assignment Report

## 1. Environment and `uv`

### What is `$PATH`?

`PATH` is an operating-system environment variable containing directories searched when a command is executed. When I run a command such as `python` or `uv`, the operating system searches the directories listed in `PATH` to locate the executable.

### What is `sys.prefix`?

In Python, `sys.prefix` identifies the prefix associated with the active Python installation or virtual environment. When the project runs inside its `.venv` environment, it helps identify that environment.

### Why use `uv`?

`uv` manages Python project dependencies, virtual environments, lockfiles, and package builds. It makes the project setup reproducible and simplifies dependency installation.

## 2. API and Configuration

The application retrieves stock quote data from the Finnhub API.

- API endpoint: `https://finnhub.io/api/v1/quote`
- The API key is loaded from a local `.env` file.
- `.env.template` documents the required environment variable without containing the real API key.
- `.gitignore` excludes `.env` and `.venv` from Git tracking.
- Configuration validation raises a clear error if the API key is missing or still contains a known placeholder.
- HTTP requests use a timeout and check for HTTP errors.

## 3. Dependencies and Semantic Versioning

### Dependency Tree Analysis

The project uses `uv` to manage dependencies and `uv.lock` to record resolved versions.

The dependency tree from `uv tree` is:

```text
finnhub-quote-cli v0.1.0
├── python-dotenv v1.2.4
├── requests v2.34.2
│   ├── certifi v2026.10.23
│   ├── charset-normalizer v3.5.2
│   ├── idna v3.20
│   └── urllib3 v2.8.0
└── pytest v9.1.1 (group: dev)
    ├── colorama v0.4.6
    ├── iniconfig v2.3.1
    ├── packaging v26.3
    ├── pluggy v1.7.0
    └── pygments v2.21.0
```

### Direct Dependencies

- `requests` is a runtime dependency used to send HTTP requests to the Finnhub API.
- `python-dotenv` is a runtime dependency used to load configuration from the local `.env` file.
- `pytest` is a development dependency used to execute automated tests.

### Transitive Dependencies

Transitive dependencies are packages installed because another dependency requires them.

- `requests` depends on `certifi`, `charset-normalizer`, `idna`, and `urllib3`.
- `pytest` depends on `colorama`, `iniconfig`, `packaging`, `pluggy`, and `pygments` in this resolved environment.

Keeping development dependencies separate from runtime dependencies avoids requiring test tools when users install the application for normal use.

### SemVer Scenario Examples

The following examples demonstrate how version numbers should change according to the type of modification.

| Scenario | Version change | Reason |
|---|---|---|
| Fix a bug without changing existing public behavior | `1.2.3` → `1.2.4` | PATCH release |
| Add a backward-compatible feature | `1.2.3` → `1.3.0` | MINOR release |
| Introduce a breaking change to the public API | `1.2.3` → `2.0.0` | MAJOR release |

These examples assume the package has reached version `1.2.3` and follows Semantic Versioning.

## 4. Build and Distribution

The project defines a command-line entry point in `pyproject.toml`:

```toml
[project.scripts]
finnhub-quote = "finnhub_quote_cli.cli:main"
```

The command `uv build` successfully generated a wheel and a source distribution in the `dist` directory. The CLI was tested using `uv run finnhub-quote NVDA`.

The package was successfully published to TestPyPI. Both the wheel and source distribution were uploaded, and version 0.1.0 is visible on the public project page.

## 5. Professional Debugging Investigation

### Issue Investigated

The CLI accepts a stock symbol as a command-line argument. Empty or whitespace-only symbols must be rejected before an API request is made.

### Debugging Method

I configured the Python debugger in VS Code using `launch.json` and launched the CLI with an empty symbol argument. I used a breakpoint to pause execution and inspect the program as it ran, rather than adding temporary print statements.

### Variable Inspection

The relevant variable is `symbol` in `get_quote()` in `client.py`. The code normalizes the input using `strip()` and `upper()`. An empty or whitespace-only input becomes an empty string after normalization.

### Root Cause and Fix

The issue is that an empty symbol is not a valid stock ticker. The function checks the normalized symbol and raises a clear `ValueError` when it is empty, preventing an unnecessary API request.

### Call Stack

The Call Stack shows the active chain of function calls that led to the current execution point. In this application, the CLI entry point in `main()` calls `get_quote()`, which validates the symbol before making an HTTP request.

### Verification

The automated test suite contains five tests, all of which passed. These tests cover missing or placeholder API keys and empty or whitespace-only stock symbols. The live Finnhub API call and CLI were also tested successfully.

## 6. TestPyPI Deployment

**Package name:** `finnhub-quote-cli`

**Published version:** `0.1.0`

**TestPyPI project page:** https://test.pypi.org/project/finnhub-quote-cli/

**Distribution artifacts:**
- Wheel: `finnhub_quote_cli-0.1.0-py3-none-any.whl`
- Source distribution: `finnhub_quote_cli-0.1.0.tar.gz`

Both distribution files were successfully uploaded to TestPyPI. The public project page displays version `0.1.0`.

### Debugging approach

A professional debugging workflow includes reproducing the error, inspecting relevant variables and program state, checking the traceback, and examining the Call Stack to understand how execution reached the failing code. After applying a fix, rerun the relevant tests to confirm the issue is resolved.
