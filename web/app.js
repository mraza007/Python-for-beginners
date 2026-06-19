/* Python for Beginners — interactive course front-end.
 *
 * Reads the same Markdown lessons that live in ../course/<dir>/README.md,
 * renders them, turns example code blocks into editable + runnable cells,
 * and loads the exercise/solution .py files on demand. Python runs entirely
 * in the browser via Pyodide.
 */

"use strict";

// ---- Course manifest -------------------------------------------------------
// Every module is just a folder under ../course/ with a README.md.
// Add a module here and it shows up automatically (greyed out until it exists).
const COURSE_ROOT = "../course";
const MODULES = [
  { part: "Part 1 — Fundamentals", num: "01", dir: "01-variables",        title: "Variables" },
  { part: "Part 1 — Fundamentals", num: "02", dir: "02-data-types",       title: "Data Types & Numbers" },
  { part: "Part 1 — Fundamentals", num: "03", dir: "03-strings",          title: "Strings" },
  { part: "Part 1 — Fundamentals", num: "04", dir: "04-booleans",         title: "Booleans & Comparison" },
  { part: "Part 1 — Fundamentals", num: "05", dir: "05-operators",        title: "Operators & Expressions" },
  { part: "Part 1 — Fundamentals", num: "06", dir: "06-conditionals",     title: "Conditionals" },
  { part: "Part 1 — Fundamentals", num: "07", dir: "07-loops",            title: "Loops" },
  { part: "Part 1 — Fundamentals", num: "08", dir: "08-input-output",     title: "Input & Output" },

  { part: "Part 2 — Data Structures", num: "09", dir: "09-lists",         title: "Lists" },
  { part: "Part 2 — Data Structures", num: "10", dir: "10-tuples-and-sets", title: "Tuples & Sets" },
  { part: "Part 2 — Data Structures", num: "11", dir: "11-dictionaries",  title: "Dictionaries" },
  { part: "Part 2 — Data Structures", num: "12", dir: "12-comprehensions", title: "Comprehensions" },

  { part: "Part 3 — Functions & Modules", num: "13", dir: "13-functions", title: "Functions" },
  { part: "Part 3 — Functions & Modules", num: "14", dir: "14-lambdas",   title: "Lambdas & map/filter" },
  { part: "Part 3 — Functions & Modules", num: "15", dir: "15-modules",   title: "Modules & Standard Library" },
  { part: "Part 3 — Functions & Modules", num: "16", dir: "16-iterators-generators", title: "Iterators & Generators" },

  { part: "Part 4 — Real-World Python", num: "17", dir: "17-exceptions",  title: "Exceptions & Error Handling" },
  { part: "Part 4 — Real-World Python", num: "18", dir: "18-file-handling", title: "File Handling" },
  { part: "Part 4 — Real-World Python", num: "19", dir: "19-debugging",   title: "Debugging" },

  { part: "Part 5 — Object-Oriented Programming", num: "20", dir: "20-classes-and-objects", title: "Classes & Objects" },
  { part: "Part 5 — Object-Oriented Programming", num: "21", dir: "21-encapsulation", title: "Encapsulation" },
  { part: "Part 5 — Object-Oriented Programming", num: "22", dir: "22-static-class-members", title: "Static & Class Members" },

  { part: "Capstone Projects", num: "P1", dir: "01-number-guessing-game", base: "../projects/01-number-guessing-game", title: "Number Guessing Game" },
  { part: "Capstone Projects", num: "P2", dir: "02-mad-libs",              base: "../projects/02-mad-libs",              title: "Mad Libs Story" },
  { part: "Capstone Projects", num: "P3", dir: "03-todo-list",            base: "../projects/03-todo-list",            title: "To-Do List" },
];

// Where a module's files live (course modules vs capstone projects).
function moduleBase(mod) {
  return mod.base || `${COURSE_ROOT}/${mod.dir}`;
}

// ---- Pyodide (lazy) --------------------------------------------------------
let _pyodidePromise = null;

function setStatus(state, label) {
  const el = document.getElementById("py-status");
  el.className = "py-status" + (state ? " " + state : "");
  el.querySelector(".label").textContent = label;
}

function getPyodide() {
  if (!_pyodidePromise) {
    _pyodidePromise = (async () => {
      setStatus("loading", "Python: loading…");
      const py = await loadPyodide();
      // Wire input() to the browser's prompt dialog.
      py.runPython(`
import builtins
from js import window as _window
def _web_input(prompt=""):
    r = _window.prompt(str(prompt))
    return "" if r is None else str(r)
builtins.input = _web_input
`);
      setStatus("ready", "Python: ready");
      return py;
    })().catch((err) => {
      setStatus("error", "Python: failed to load");
      _pyodidePromise = null; // allow a retry
      throw err;
    });
  }
  return _pyodidePromise;
}

// Run code, returning { text, isError }. stdout + stderr are captured;
// a Python exception is appended as a (trimmed) traceback.
async function runPython(code) {
  const py = await getPyodide();
  py.runPython(`
import sys, io
_saved_out, _saved_err = sys.stdout, sys.stderr
sys.stdout = sys.stderr = io.StringIO()
`);
  let isError = false;
  let errText = "";
  try {
    py.runPython(code);
  } catch (e) {
    isError = true;
    errText = String(e.message || e);
    // Pyodide prepends JS framing; keep from the Python "Traceback" onward.
    const i = errText.indexOf("Traceback (most recent call last)");
    if (i >= 0) errText = errText.slice(i);
  }
  const out = py.runPython("sys.stdout.getvalue()");
  py.runPython("sys.stdout, sys.stderr = _saved_out, _saved_err");
  const text = (out || "") + (isError ? (out ? "\n" : "") + errText : "");
  return { text, isError };
}

// ---- Interactive code cell -------------------------------------------------
function autosize(ta) {
  ta.style.height = "auto";
  ta.style.height = Math.min(ta.scrollHeight + 2, 600) + "px";
}

function makeCell(initialCode, { tag = "python" } = {}) {
  const cell = document.createElement("div");
  cell.className = "cell";

  const bar = document.createElement("div");
  bar.className = "cell-bar";
  bar.innerHTML =
    `<span class="tag">${tag}</span><span class="spacer"></span>` +
    `<button class="btn-ghost btn-reset">Reset</button>` +
    `<button class="btn-run">▶ Run</button>`;

  const ta = document.createElement("textarea");
  ta.value = initialCode;
  ta.spellcheck = false;
  ta.setAttribute("autocomplete", "off");
  ta.setAttribute("autocapitalize", "off");

  const output = document.createElement("div");
  output.className = "output";
  const outPre = document.createElement("pre");
  output.appendChild(outPre);

  cell.append(bar, ta, output);

  // Sizing
  requestAnimationFrame(() => autosize(ta));
  ta.addEventListener("input", () => autosize(ta));

  // Tab inserts 4 spaces instead of leaving the field.
  ta.addEventListener("keydown", (e) => {
    if (e.key === "Tab") {
      e.preventDefault();
      const s = ta.selectionStart, en = ta.selectionEnd;
      ta.value = ta.value.slice(0, s) + "    " + ta.value.slice(en);
      ta.selectionStart = ta.selectionEnd = s + 4;
    }
    if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
      e.preventDefault();
      run();
    }
  });

  const runBtn = bar.querySelector(".btn-run");
  async function run() {
    runBtn.disabled = true;
    const prev = runBtn.textContent;
    runBtn.textContent = "Running…";
    output.classList.add("show");
    outPre.className = "";
    outPre.innerHTML = '<span class="empty">Running…</span>';
    try {
      const { text, isError } = await runPython(ta.value);
      outPre.className = isError ? "error" : "";
      if (text.trim() === "") {
        outPre.innerHTML = '<span class="empty">✓ ran — no output</span>';
      } else {
        outPre.textContent = text.replace(/\n$/, "");
      }
    } catch (err) {
      outPre.className = "error";
      outPre.textContent = "Could not start Python.\n" + (err.message || err);
    } finally {
      runBtn.disabled = false;
      runBtn.textContent = prev;
    }
  }
  runBtn.addEventListener("click", run);
  bar.querySelector(".btn-reset").addEventListener("click", () => {
    ta.value = initialCode;
    autosize(ta);
    output.classList.remove("show");
  });

  return cell;
}

// ---- Lesson rendering ------------------------------------------------------
async function fetchText(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`${res.status} for ${path}`);
  return res.text();
}

function isCheatSheetHeading(text) {
  const t = (text || "").toLowerCase();
  return t.includes("cheat-sheet") || t.includes("recap");
}

// Replace each runnable python <pre> with an interactive cell, except those
// in the recap/cheat-sheet section (which contain pseudo-code).
function enhanceCodeBlocks(container) {
  let inCheat = false;
  // Walk a static list since we mutate the DOM as we go.
  Array.from(container.children).forEach((node) => {
    if (node.tagName === "H2") {
      inCheat = isCheatSheetHeading(node.textContent);
      return;
    }
    if (node.tagName === "PRE") {
      const code = node.querySelector("code");
      const cls = code ? code.className : "";
      if (code && /python/i.test(cls) && !inCheat) {
        const cell = makeCell(code.textContent.replace(/\n$/, ""));
        node.replaceWith(cell);
      }
    }
  });
}

// Pull "exercises/NN_name.py" paths out of the raw markdown, in order.
function extractExercisePaths(md) {
  const re = /exercises\/[\w.\-]+\.py/g;
  const seen = new Set();
  const out = [];
  let m;
  while ((m = re.exec(md)) !== null) {
    if (!seen.has(m[0])) { seen.add(m[0]); out.push(m[0]); }
  }
  return out;
}

async function buildExercises(mod, md, container) {
  const paths = extractExercisePaths(md);
  if (paths.length === 0) return;

  const section = document.createElement("section");
  section.className = "exercises";
  const h = document.createElement("h2");
  h.textContent = "✏️ Exercises — try them here";
  section.appendChild(h);
  const note = document.createElement("p");
  note.innerHTML = "Edit the code, hit <strong>▶ Run</strong>, and check it against the expected output in each task. Peek at the solution only after you've given it a go.";
  section.appendChild(note);

  container.appendChild(section);

  for (const exPath of paths) {
    const fullEx = `${moduleBase(mod)}/${exPath}`;
    const fullSol = fullEx.replace("/exercises/", "/solutions/");
    let starter;
    try {
      starter = await fetchText(fullEx);
    } catch {
      continue; // skip if the file isn't there
    }

    const card = document.createElement("div");
    card.className = "ex-card";
    const head = document.createElement("div");
    head.className = "ex-head";
    head.innerHTML =
      `<span class="ex-tag">Exercise</span>` +
      `<span class="ex-name">${exPath.split("/").pop()}</span>`;
    const body = document.createElement("div");
    body.className = "ex-body";

    body.appendChild(makeCell(starter.replace(/\n$/, "")));

    const solBtn = document.createElement("button");
    solBtn.className = "sol-toggle";
    solBtn.textContent = "Show solution";
    let solCell = null;
    solBtn.addEventListener("click", async () => {
      if (solCell) {
        const showing = solCell.style.display !== "none";
        solCell.style.display = showing ? "none" : "block";
        solBtn.textContent = showing ? "Show solution" : "Hide solution";
        return;
      }
      solBtn.textContent = "Loading…";
      try {
        const sol = await fetchText(fullSol);
        solCell = makeCell(sol.replace(/\n$/, ""), { tag: "solution" });
        body.appendChild(solCell);
        solBtn.textContent = "Hide solution";
      } catch {
        solBtn.textContent = "Solution unavailable";
        solBtn.disabled = true;
      }
    });
    body.appendChild(solBtn);

    card.append(head, body);
    section.appendChild(card);
  }
}

async function loadModule(mod) {
  const content = document.getElementById("content");
  content.innerHTML = '<p class="loading-note">Loading lesson…</p>';
  window.scrollTo(0, 0);
  setActiveNav(mod.dir);
  closeSidebar();

  let md;
  try {
    md = await fetchText(`${moduleBase(mod)}/README.md`);
  } catch {
    content.innerHTML =
      `<h1>${mod.num} · ${mod.title}</h1>` +
      `<p class="loading-note">This lesson hasn't been written yet — check back soon!</p>`;
    return;
  }

  const article = document.createElement("article");
  article.innerHTML = marked.parse(md);
  content.innerHTML = "";
  content.appendChild(article);

  enhanceCodeBlocks(article);
  await buildExercises(mod, md, content);

  location.hash = mod.dir;
}

// ---- Navigation / sidebar --------------------------------------------------
function setActiveNav(dir) {
  document.querySelectorAll(".nav-item").forEach((a) => {
    a.classList.toggle("active", a.dataset.dir === dir);
  });
}

function buildNav() {
  const nav = document.getElementById("nav");
  let currentPart = "";
  MODULES.forEach((mod) => {
    if (mod.part !== currentPart) {
      currentPart = mod.part;
      const label = document.createElement("div");
      label.className = "part-label";
      label.textContent = mod.part;
      nav.appendChild(label);
    }
    const a = document.createElement("a");
    a.className = "nav-item";
    a.dataset.dir = mod.dir;
    a.href = "#" + mod.dir;
    a.innerHTML = `<span class="num">${mod.num}</span><span class="t">${mod.title}</span>`;
    a.addEventListener("click", (e) => {
      e.preventDefault();
      loadModule(mod);
    });
    nav.appendChild(a);
  });
}

// Grey out modules whose README isn't present yet.
async function markAvailability() {
  await Promise.all(MODULES.map(async (mod) => {
    const a = document.querySelector(`.nav-item[data-dir="${mod.dir}"]`);
    if (!a) return;
    try {
      const res = await fetch(`${moduleBase(mod)}/README.md`, { method: "HEAD" });
      if (!res.ok) throw new Error();
    } catch {
      a.classList.add("pending");
      const soon = document.createElement("span");
      soon.className = "soon";
      soon.textContent = "soon";
      a.appendChild(soon);
      a.addEventListener("click", (e) => e.preventDefault(), true);
    }
  }));
}

function renderWelcome() {
  const content = document.getElementById("content");
  content.innerHTML = `
    <div class="welcome">
      <div class="hero">
        <h1>Learn Python, hands-on 🐍</h1>
        <p>Read a lesson, then edit and run real Python right here in your browser —
        no installation, nothing to set up. Your code never leaves your machine.</p>
      </div>
      <div class="cards">
        <div class="card"><h3>📖 Clear lessons</h3><p>Plain-English explanations with small, focused examples.</p></div>
        <div class="card"><h3>▶ Runnable code</h3><p>Every example is editable — change it, run it, see what happens.</p></div>
        <div class="card"><h3>✏️ Exercises</h3><p>Practice in each lesson, with solutions a click away.</p></div>
        <div class="card"><h3>🧩 Built in order</h3><p>Start at Variables and work down — each lesson builds on the last.</p></div>
      </div>
      <button class="cta" id="start-btn">Start with 01 · Variables →</button>
    </div>`;
  document.getElementById("start-btn").addEventListener("click", () => loadModule(MODULES[0]));
}

// ---- Mobile sidebar --------------------------------------------------------
function openSidebar() {
  document.getElementById("sidebar").classList.add("open");
  document.getElementById("scrim").classList.add("show");
}
function closeSidebar() {
  document.getElementById("sidebar").classList.remove("open");
  document.getElementById("scrim").classList.remove("show");
}

// ---- Boot ------------------------------------------------------------------
function boot() {
  buildNav();
  markAvailability();

  document.getElementById("menu-toggle").addEventListener("click", () => {
    const open = document.getElementById("sidebar").classList.contains("open");
    open ? closeSidebar() : openSidebar();
  });
  document.getElementById("scrim").addEventListener("click", closeSidebar);

  const hash = location.hash.replace("#", "");
  const start = MODULES.find((m) => m.dir === hash);
  if (start) {
    loadModule(start);
  } else {
    renderWelcome();
  }
}

boot();
