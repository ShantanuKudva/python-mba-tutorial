# 00 — Setup

Goal: a working Python + VSCode + git environment in under an hour. Do this **once**, before week 1.

If anything goes wrong: read the error, search it, then move on. You can always come back.

---

## 1. Install Python 3.12

### macOS

1. Open Terminal (Cmd+Space → "Terminal").
2. Install Homebrew if you don't have it: https://brew.sh/
3. Then:

   ```bash
   brew install python@3.12
   ```

4. Verify:

   ```bash
   python3 --version
   ```

   You should see `Python 3.12.x`.

### Windows

1. Go to https://www.python.org/downloads/
2. Download **Python 3.12.x** for Windows.
3. **CRITICAL:** during install, check the box **"Add Python to PATH"**. Without this you'll fight the terminal forever.
4. Open PowerShell and verify:

   ```powershell
   python --version
   ```

---

## 2. Install VSCode

- Download: https://code.visualstudio.com/
- Open it.
- Install these extensions (left sidebar → squares icon → search):
  - **Python** (by Microsoft)
  - **Jupyter** (by Microsoft)
  - **Pylance** (usually auto-installs with Python)

---

## 3. Install git

### macOS

```bash
brew install git
git --version
```

### Windows

- Download: https://git-scm.com/download/win
- Use defaults during install.
- Open "Git Bash" from Start menu and run:

  ```bash
  git --version
  ```

Tell git who you are (one-time):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## 4. Get this repository onto your computer

```bash
# pick a folder, e.g.:
cd ~/Documents
git clone <URL-of-this-repo> python-excel-mba
cd python-excel-mba
```

(If your instructor/mentor sent this as a zip, just unzip it instead.)

Open the folder in VSCode:

```bash
code .
```

---

## 5. Create your virtual environment

A virtual environment is a private "sandbox" of Python packages just for this project. It keeps things tidy.

From inside the project folder:

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell complains about execution policy, run once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

After activation, your prompt should start with `(.venv)`.

---

## 6. Install all course packages

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will take a few minutes the first time. Go make tea.

---

## 7. Verify everything works

Run the verifier:

```bash
python 00-setup/verify.py
```

You should see something like:

```
✅ Python 3.12.x
✅ pandas 2.x
✅ numpy 1.x
✅ matplotlib 3.x
✅ groq SDK installed
🎉 You're ready for Week 1.
```

If anything is `❌`, re-run `pip install -r requirements.txt` and read the error.

---

## 8. (Later, week 11) Install Node.js

Only needed when you start the capstone frontend. **Skip for now.**

- Download: https://nodejs.org/ → "LTS" version (20.x or higher).
- Verify: `node --version` and `npm --version`.

---

## Common problems

**`python: command not found` (macOS)**
On macOS, use `python3` and `pip3` instead of `python`/`pip`.

**VSCode is using the wrong Python**
Bottom-right of VSCode shows the active interpreter. Click it, choose the one inside `.venv`.

**`pip install` is super slow**
That's normal the first time. Subsequent installs are cached.

**`ModuleNotFoundError` after install**
You forgot to activate `.venv`. Check the prompt has `(.venv)`.

---

Once `verify.py` passes, you are done with setup. Open [`../01-foundations/week-1/README.md`](../01-foundations/week-1/README.md) and start the course.
