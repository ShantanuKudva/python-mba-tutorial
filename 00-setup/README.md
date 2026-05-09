# 00 — Setup

## The fast path (recommended)

**Double-click `index.html`.** It opens in your browser. That's it.

Every lesson and exercise from Week 1 through Week 9 runs entirely in the browser — no Python, no VSCode, no terminal. Python executes locally via [Pyodide](https://pyodide.org/) (WebAssembly), so nothing leaves your machine and nothing needs to be installed.

Use the sidebar to navigate lessons, click `▶` links to open exercises, and hit **Run** to execute code.

> If markdown was edited and content looks stale, ask Shantanu to run `python build_site.py` once to regenerate the bundle.

---

## When you will need a local Python install

A local Python install is only required for:

| Week | Why |
|---|---|
| Week 10 — Groq AI | Needs a `.env` file with your API key; browser sandbox can't load local secrets. |
| Weeks 11–12 — Capstone | FastAPI server must run locally (or be deployed). |

If you are on Week 1–9, skip everything below and open `index.html`.

---

## Advanced: local Python install (optional)

Do this only when you reach Week 10, or if you want to run scripts from the terminal.

### 1. Install Python 3.12

**Windows**

1. Go to https://www.python.org/downloads/
2. Download **Python 3.12.x** for Windows.
3. **CRITICAL:** during install, check **"Add Python to PATH"**. Without this the terminal won't find Python.
4. Open PowerShell and verify:

   ```powershell
   python --version
   ```

**macOS**

1. Open Terminal (Cmd+Space → "Terminal").
2. Install Homebrew if you don't have it: https://brew.sh/
3. Then:

   ```bash
   brew install python@3.12
   python3 --version
   ```

---

### 2. Install VSCode (optional editor)

- Download: https://code.visualstudio.com/
- Install extensions (sidebar → squares icon → search):
  - **Python** (by Microsoft)
  - **Jupyter** (by Microsoft)

---

### 3. Install git (optional, for saving your work)

**Windows:** https://git-scm.com/download/win — use defaults. Open "Git Bash" and verify:

```bash
git --version
```

**macOS:**

```bash
brew install git
git --version
```

Tell git who you are (one-time):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

### 4. Get the repository (if you don't have it yet)

```bash
cd ~/Documents
git clone <URL-of-this-repo> python-excel-mba
cd python-excel-mba
```

Or just unzip the folder Shantanu sent.

---

### 5. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell complains about execution policy, run once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

After activation your prompt starts with `(.venv)`.

---

### 6. Install course packages

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

First run takes a few minutes. Subsequent installs are cached.

---

### 7. Verify

```bash
python 00-setup/verify.py
```

Expected output:

```
✅ Python 3.12.x
✅ pandas 2.x
✅ numpy 1.x
✅ matplotlib 3.x
✅ groq SDK installed
🎉 You're ready for Week 1.
```

If anything shows `❌`, re-run `pip install -r requirements.txt` and read the error message.

---

### 8. Node.js (capstone frontend only — Week 11)

**Skip until Week 11.**

- Download: https://nodejs.org/ → LTS version (20.x or higher).
- Verify: `node --version` and `npm --version`.

---

## Common problems (local install)

**`python: command not found` (macOS)**
Use `python3` and `pip3` instead of `python`/`pip`.

**VSCode picks the wrong Python**
Bottom-right of VSCode shows the active interpreter. Click it, choose the one inside `.venv`.

**`ModuleNotFoundError` after install**
You forgot to activate `.venv`. Check the prompt has `(.venv)`.

---

Once `verify.py` passes, open [`../01-foundations/week-1/README.md`](../01-foundations/week-1/README.md) and start the course — or just open `index.html` and click Week 1 in the sidebar.
