# Introduction to Python Training Session

**Audience:** Colleagues with little to no Python experience. Mixed OS: some on macOS with normal terminal access, many on Windows with locked-down machines (no terminal access at all, even inside the IDE).
**Duration:** 4 hours (including breaks)
**Goal:** By the end, attendees can confidently set up any Python project in the company (pyenv + venv + pip) and understand core language fundamentals well enough to read, write, and test simple Python code following good practices.

**Setup approach:** everyone learns and types the *same* terminal commands in Part 1 — there's no separate GUI track. macOS/unlocked attendees use their local terminal. Windows/locked-down attendees use a real terminal running in the browser via [mybinder.org](https://mybinder.org) (launches a JupyterLab environment from a public GitHub repo, no signup, includes a genuine bash terminal tab where `venv`/`pip` behave exactly as on a Mac). This keeps the taught commands and mental model identical for the whole room — only the window they're typing into differs.


Materials repo:
https://github.com/computerise-afsl/python-training

Binder link:



> **⚠️ Action items before this session:**
> 1. Launch and **pre-launch the Binder link 10–15 minutes before the session starts** — cold builds can take a minute or more, and you don't want everyone hitting a slow build simultaneously at 0:10.
> 2. Do **not** point Binder at any real company repo, code, or data — mybinder.org is public shared infrastructure. Use it only for the generic training exercises in this plan.
> 3. Binder sessions are ephemeral (destroyed after ~10 min idle or when the tab closes) — anything attendees want to keep, they should copy out (e.g. into a scratch file or the exercise repo) before the session ends.
> 4. pyenv version-switching won't be meaningfully demonstrable inside Binder (the container ships with one fixed Python version) — for the Windows/Binder group, frame pyenv as "here's the concept and the commands; venv and pip are what you'll actually use hands-on" rather than skipping it, so the terminal commands still transfer to real machines later.

---

## Session Overview

| Time | Block | Topic |
|---|---|---|
| 0:00 – 0:10 | Intro | Welcome and Goals |
| 0:10 – 1:30 | Part 1 | Environment & dependency management (pyenv, pip, venv) |
| 1:30 – 1:40 | Break | |
| 1:40 – 3:10 | Part 2 | Python fundamentals |
| 3:10 – 3:20 | Break | |
| 3:20 – 3:50 | Part 3 | Best practices for writing solid Python |
| 3:50 – 4:00 | Wrap-up | Recap, resources, Q&A |

---

## 0:00 – 0:10 — Introduction

- Welcome and session goals: "leave today able to set up and work confidently in any Python codebase at the company"
- Quick poll: who has any Python/programming experience?
- Housekeeping: prerequisites check (terminal access OR the Binder link open and loaded, GitHub/company repo access)
- Set expectation: this is hands-on — everyone follows along, typing the same commands, either in their local terminal or in the Binder browser terminal
- Windows/locked-down attendees: confirm their Binder tab is loaded and showing a terminal *before* 0:10 — flag anyone still on a build screen immediately

**Prerequisite check (ideally sent out before the session):**
- macOS/unlocked attendees: terminal access (Terminal.app / iTerm / Git Bash), Git installed
- Windows/locked-down attendees: the Binder link (sent in advance), opened in a browser tab, with the JupyterLab **Terminal** tab open — confirm this loads successfully *before* the session, not during it
- Company repo access (if using a real internal project later) — not applicable inside Binder, generic exercises only

---

## 0:10 – 1:30 — Part 1: Environment & Dependency Management (80 min)

**Objective:** Every attendee can install a specific Python version with pyenv, create an isolated venv, and install/manage packages with pip — for any project, on demand. Everyone types the same commands; Windows/locked-down attendees do it in their Binder browser terminal instead of a local shell.

### 1.1 Why this matters (5 min)
- The "it works on my machine" problem
- Why we don't install packages globally / system Python
- Mental model: **pyenv** = which Python interpreter, **venv** = isolated project sandbox, **pip** = packages inside that sandbox
- Quick check: everyone has a terminal prompt in front of them (local or Binder) before moving on

### 1.2 pyenv — managing Python versions (25 min)
- What pyenv does and why (multiple projects, multiple Python versions, no sudo/global installs)
- Key commands:
  - `pyenv install --list` / `pyenv install 3.12.4`
  - `pyenv versions`
  - `pyenv global 3.12.4`
  - `pyenv local 3.12.4` (per-project `.python-version` file)
  - `pyenv which python`
- **Exercise:** Install a Python version, set it as local for a scratch folder, confirm with `python --version`
- Common gotchas: shell not picking up pyenv (`eval "$(pyenv init -)"` in shell rc file), PATH ordering
- **Binder/Windows note:** the Binder container ships with a single fixed Python version, so `pyenv install` of a *second* version may be slow or unnecessary — it's fine to just run `pyenv versions`/`pyenv local` against the one that's there to see the commands work, and treat real multi-version installs as something they'll do back on a real machine later

### 1.3 venv — isolated environments (25 min)
- Why isolate per-project (dependency conflicts between projects)
- Creating and activating:
  - `python -m venv .venv`
  - `source .venv/bin/activate` (macOS/Linux, and Binder's terminal is Linux too, so this is the one everyone in the Binder group uses) / `.venv\Scripts\activate` (only relevant for someone on native Windows *with* shell access)
  - `deactivate`
- How to tell you're in a venv (prompt prefix, `which python`)
- Convention: `.venv` folder name + add to `.gitignore`
- **Exercise:** Create a project folder, set local pyenv version, create and activate a venv, confirm isolation

### 1.4 pip — managing dependencies (20 min)
- `pip install <package>`, `pip uninstall`, `pip list`, `pip show`
- Pinning and reproducibility: `pip freeze > requirements.txt`
- Installing from a requirements file: `pip install -r requirements.txt`
- Brief mention of `pip install -e .` for local/editable installs (if relevant to company projects)
- Note on lockfile-based alternatives (Poetry/uv/pip-tools) — mention they exist, out of scope today
- **Exercise:** Install `requests` and `pytest`, freeze requirements, delete venv, recreate from `requirements.txt` to prove reproducibility

### 1.5 Putting it together (5 min)
- Walk through the full "new project" checklist end-to-end:
  1. `pyenv local <version>`
  2. `python -m venv .venv && source .venv/bin/activate`
  3. `pip install -r requirements.txt`
- Point to where this is documented for company projects (README convention, if one exists)
- Close the loop for the Binder group: **this session's environment disappears when the tab closes** — back on their real Windows machine, the same three commands are what they'll reach for, terminal access permitting; if their real machine still has no terminal at all, that's a separate follow-up with IT, not something this session can solve today

---

## 1:30 – 1:40 — Break (10 min)

---

## 1:40 – 3:10 — Part 2: Python Fundamentals (90 min)

**Objective:** Attendees can read and write basic Python scripts, understand functions, classes, modules, and know how to run a simple unit test.

### 2.1 Scripts and the REPL (10 min)
- Running a `.py` file: `python script.py`
- Using the REPL / `python -i` for quick experiments
- `if __name__ == "__main__":` — what it means and why it's there

### 2.2 Variables and core data types (15 min)
- Dynamic typing, variables as names/bindings
- Core types: `int`, `float`, `str`, `bool`, `None`
- Collections: `list`, `dict`, `tuple`, `set` — when to use which
- f-strings for formatting
- **Exercise:** Small script manipulating a list of dicts (e.g. filter/transform a list of "employees")

### 2.3 Control flow (10 min)
- `if`/`elif`/`else`, `for`, `while`
- Comprehensions (list/dict) — brief intro, not overused
- **Exercise:** Extend previous script with a loop + conditional

### 2.4 Functions (15 min)
- Defining functions, parameters, default args, `*args`/`**kwargs` (brief)
- Return values, multiple returns via tuples
- Type hints as documentation (`def foo(x: int) -> str:`)
- Docstrings convention
- **Exercise:** Refactor earlier script logic into a function

### 2.5 Modules and imports (10 min)
- Splitting code across files, `import`, `from x import y`
- What makes something a module/package (`__init__.py` brief mention)
- Standard library highlight tour (`os`, `pathlib`, `datetime`, `json`) — just enough to know they exist
- **Exercise:** Move the function from 2.4 into a separate module and import it in the script

### 2.6 Classes and objects (20 min)
- Why classes (bundling data + behaviour), vs. just using dicts/functions
- `class`, `__init__`, `self`, instance attributes/methods
- Simple example (e.g. a `Trade` or `Order` class relevant to the business domain)
- Brief mention: dataclasses as a lighter-weight alternative for simple data containers
- **Exercise:** Write a small class with 2–3 methods and instantiate it

### 2.7 Unit testing (10 min)
- Why tests matter, especially before refactoring
- `pytest` basics: test discovery, `test_*.py`, `assert`
- Writing one test for a function/class from earlier exercises
- Running tests: `pytest`, `pytest -v`
- **Exercise:** Write and run 2–3 tests against the module built in 2.5/2.6

---

## 3:10 – 3:20 — Break (10 min)

---

## 3:20 – 3:50 — Part 3: Writing Solid Python — Best Practices (30 min)

**Objective:** Attendees leave with a checklist of habits that will make their code readable, safe, and consistent with company standards.

- **Style & readability**
  - PEP 8 basics, why consistency matters
  - Formatters/linters: `black`, `ruff` (or whatever the company standardises on) — run once, don't argue about style
- **Naming & structure**
  - Descriptive names over comments
  - Small functions, single responsibility
  - Avoid deep nesting; prefer early returns
- **Error handling**
  - `try`/`except` — catch specific exceptions, not bare `except:`
  - Fail loudly vs. silently swallowing errors
- **Dependencies & environments**
  - Always work inside a venv (tie back to Part 1)
  - Pin dependencies, keep `requirements.txt` up to date
- **Testing habits**
  - Write tests for logic, not for the sake of coverage numbers
  - Test edge cases, not just the happy path
- **Version control hygiene**
  - `.gitignore` for `.venv`, `__pycache__`, `.env`
  - Never commit secrets/credentials — use environment variables or a secrets manager
- **Documentation**
  - Docstrings for public functions/classes
  - A good README: how to set up the venv, install deps, run tests
- **Where to go next**
  - Type checking (`mypy`) for larger codebases
  - Logging vs. `print()` for anything beyond a script
  - Pointer to company style guide / template repo, if one exists

---

## 3:50 – 4:00 — Wrap-up (10 min)

- Recap the end-to-end workflow: pyenv → venv → pip → write code → test → lint
- Share resources:
  - Session materials / exercise repo
  - Official Python docs, Real Python tutorials
  - Company-specific onboarding docs / template repos
- Q&A
- Ask what follow-up topics would be useful (e.g. async, packaging, a specific company framework) for a future session

---

## Materials to Prepare Beforehand

- [ ] Create a small **public** GitHub repo for Binder to launch from — minimal, e.g. just a README and a `runtime.txt`/`environment.yml` pinning a Python version, so the build is fast. Confirm `pyenv`, `python -m venv`, and `pip` all work as expected inside the resulting container terminal
- [ ] Generate the Binder launch link (`https://mybinder.org/v2/gh/<org>/<repo>/HEAD`) and send it to Windows/locked-down attendees ahead of time, with instructions to open it and click into the **Terminal** tile
- [ ] **Pre-launch the Binder link yourself 10–15 min before the session** to confirm it builds cleanly, and keep that tab open as a live fallback/demo
- [ ] Confirm with IT how Python is provisioned on the Windows image, purely so you can address "will this work on my actual laptop after today" questions accurately
- [ ] Pre-session email: prerequisites (terminal + Git for macOS/unlocked attendees; the Binder link, opened and loaded, for locked-down Windows attendees)
- [ ] Starter repo/folder with exercise skeletons for each section
- [ ] `requirements.txt` example for the pip exercise
- [ ] Slides or a shared doc with the command cheat-sheet (pyenv/venv/pip commands) — same cheat-sheet for everyone, since commands are now identical across the room
- [ ] A small, relatable domain example (e.g. "Order"/"Trade" class) for the classes section
- [ ] Solutions branch/gist for each exercise, shared after the session

## Risk / Time Buffer Notes

- **Binder cold-start latency:** a fresh build can take anywhere from ~30 seconds to several minutes depending on the repo's dependencies. Pre-warming the link before the session (see Materials) mitigates this, but have attendees open their Binder link 5 minutes before 0:10 as a buffer, not at 0:10 itself.
- **Binder is public shared infrastructure, not authorised for company code or data** — keep it strictly to the generic exercises in this plan; don't let anyone paste in real project code "just to try it."
- **Binder sessions are ephemeral** — idle timeout (~10 min) or closing the tab destroys the environment and anything unsaved in it. Remind attendees mid-session if there's a natural break where idle timeout could bite (e.g. during a long Part 2 discussion after Part 1 wraps).
- Environment setup (Part 1) is still the most likely place to overrun, given individual machine/network differences (corporate proxy/VPN blocking installs on the local-terminal side, slow/blocked Binder builds on the browser side). Consider having a co-presenter free to help anyone stuck on either path while the main presenter keeps moving.
- Keep Part 2 exercises short and code-along rather than independent, to stay on schedule — save deeper independent practice for after the session
- Part 2 onward (fundamentals, testing, best practices) works identically whether attendees are in a local terminal/editor or in the Binder JupyterLab environment — scripts run and pytest works the same way in both
