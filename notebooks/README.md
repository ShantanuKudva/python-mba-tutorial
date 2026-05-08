# Notebooks

Scratch space. Use this folder for any Jupyter notebook (`.ipynb`) where you experiment, plot, or explore data interactively.

## Why notebooks at all

Notebooks are great for:

- Trying out a pandas one-liner on real data without writing a full script.
- Plotting and tweaking visuals.
- Quick "what does this function actually return?" experiments.

Notebooks are bad for:

- Production code. They're not versioned cleanly, hard to test, easy to forget what cells were run in what order.

So: **explore in notebooks, ship in `.py`.**

## How to launch Jupyter

With your project `.venv` activated:

```bash
jupyter notebook
# or, more modern:
jupyter lab
```

A browser tab opens. Create a new notebook in this folder.

## VSCode alternative

VSCode opens `.ipynb` files natively. With the Jupyter extension installed (already in your week-1 setup), you can run cells right in the editor.

## Conventions

- Name notebooks with a date + topic: `2026-05-15-explore-orders.ipynb`. Future-you will thank present-you.
- Don't commit huge output cells. Click "Clear all outputs" before committing.
- If a notebook becomes useful production logic, **port it to `.py`** in the relevant week's folder.

This folder is otherwise empty. Add notebooks as you go.
