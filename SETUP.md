# Setup — Install Python & Run Your First Program

You have **two ways** to use this course. Pick whichever suits you.

---

## Option A — No install (run in your browser) ✨

The fastest way to start. The course has a built-in interactive site that runs
real Python in your browser — nothing to install.

From the project folder, start a tiny local web server:

```bash
python3 -m http.server 8000
```

…then open **http://localhost:8000/web/** in your browser. Read a lesson and
click **▶ Run** on any code block.

> "But that needs Python to run the server!" — true. If you don't have Python yet,
> follow Option B first (you'll want it installed anyway).

---

## Option B — Install Python (recommended for real practice)

### 1. Install Python 3.10 or newer

**Windows**
1. Go to <https://www.python.org/downloads/> and download the latest Python.
2. Run the installer and **tick "Add python.exe to PATH"** before clicking Install.
3. Verify in a new terminal (Command Prompt or PowerShell):
   ```bash
   python --version
   ```

**macOS**
- Easiest: install [Homebrew](https://brew.sh), then:
  ```bash
  brew install python
  python3 --version
  ```
- Or download the installer from <https://www.python.org/downloads/>.

**Linux (Debian/Ubuntu)**
```bash
sudo apt update && sudo apt install python3
python3 --version
```

> On macOS/Linux the command is usually `python3`. On Windows it's usually
> `python`. Use whichever prints a version number.

### 2. (Optional) Pick an editor
[VS Code](https://code.visualstudio.com/) with the Python extension is a great,
free choice. Any text editor works too.

### 3. Run your first program
Create a file called `hello.py` with one line:

```python
print("Hello, Python!")
```

Run it from the terminal, in the folder where you saved it:

```bash
python hello.py      # or: python3 hello.py
```

You should see:

```
Hello, Python!
```

🎉 That's it — you're running Python.

---

## How the course is organised

```
course/      the lessons, in order (01, 02, 03, …)
  NN-topic/
    README.md      the lesson — read this first
    examples/      runnable example scripts
    exercises/     practice files with TODOs
    solutions/     worked answers
projects/    capstone projects that combine skills
web/         the interactive in-browser version
```

### Working through a lesson
1. Read `course/01-variables/README.md`.
2. Run the examples: `python course/01-variables/examples/01_first_variable.py`.
3. Do the exercises in `course/01-variables/exercises/` — edit the file, then run it.
4. Compare with the matching file in `course/01-variables/solutions/`.
5. Move on to `02-data-types`, and so on.

Start here → **[course/01-variables/](course/01-variables/)**
