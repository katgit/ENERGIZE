# Setting Up Python, Jupyter, and VS Code

Before the workshop, please install and test the following on your own laptop. This only needs to be done once. If you run into trouble, bring your laptop to the start of the session and we will help you get set up.

We recommend using **Anaconda**, which installs Python, Jupyter, and the scientific packages used in this workshop (NumPy, pandas, Matplotlib) all at once, along with a graphical **Anaconda Navigator** for managing environments.

## 1. Install Anaconda

### macOS
1. Go to [anaconda.com/download](https://www.anaconda.com/download) and download the **Anaconda Distribution** installer for macOS (choose the graphical `.pkg` installer for your Mac's chip - Apple Silicon or Intel).
2. Run the downloaded `.pkg` installer and follow the prompts, accepting the default options.
3. Open a **new** Terminal window (search for it with Spotlight, `Cmd+Space`) so the installer's changes take effect, and verify the install:
   ```bash
   conda --version
   python3 --version
   ```

### Windows
1. Go to [anaconda.com/download](https://www.anaconda.com/download) and download the **Anaconda Distribution** installer for Windows.
2. Run the installer, accepting the default options (install "just for me" when prompted).
3. Open **Anaconda Prompt** from the Start menu (search for it) and verify the install:
   ```powershell
   conda --version
   python --version
   ```

## 2. Install VS Code

1. Go to [code.visualstudio.com](https://code.visualstudio.com/) and download **Visual Studio Code** for your operating system (macOS or Windows).
2. Run the installer (on Windows, keep the default options, including **"Add to PATH"**; on macOS, drag the app into your `Applications` folder).
3. Open VS Code once to confirm it launches.

## 3. Install the VS Code Extensions

Inside VS Code:

1. Click the **Extensions** icon in the left sidebar (it looks like four squares), or press `Cmd+Shift+X` (macOS) / `Ctrl+Shift+X` (Windows).
2. Search for **"Python"** (published by Microsoft) and click **Install**.
3. Search for **"Jupyter"** (published by Microsoft) and click **Install**.

These two extensions let VS Code run `.py` scripts and `.ipynb` (Jupyter) notebooks directly, with a built-in interactive Python session.

## 4. Create the Workshop Conda Environment

Anaconda already includes a `base` environment with Jupyter, NumPy, pandas, and Matplotlib. For this workshop, we'll create a separate, dedicated environment named `energize` so it doesn't interfere with anything else on your machine.

Open a terminal (macOS: Terminal app; Windows: **Anaconda Prompt** from the Start menu) and run:

```bash
conda create -n energize python=3.14 jupyter numpy pandas matplotlib ipykernel -y
```

Activate it:

```bash
conda activate energize
```

Your terminal prompt should now start with `(energize)`. Any `python`, `pip`, or `jupyter` command you run now uses this environment. To leave the environment later, run `conda deactivate`.

### Register the Environment as a Jupyter Kernel

So VS Code (and Jupyter) can find and use this environment:

```bash
python -m ipykernel install --user --name energize --display-name "Python (energize)"
```

> **Prefer a graphical tool?** You can do the same steps using **Anaconda Navigator** (installed alongside Anaconda): open Navigator, go to the **Environments** tab, click **Create**, name it `energize`, and select Python 3.12. Then use the environment's package list (or the **Home** tab) to install/launch Jupyter.

## 5. Open and Run a Notebook in VS Code

1. In VS Code, go to **File > Open Folder...** and open the `ENERGIZE` folder (the one containing `Part1` and `Part2`).
2. In the Explorer sidebar, open `Part1/01_Python_Basics_and_Data_Structures.ipynb`.
3. VS Code will show the notebook with its cells. In the top-right corner, click **Select Kernel**, then choose **"Python (energize)"** (or select the `energize` conda environment directly from the interpreter list).
4. Click the ▷ (Run) button next to the first cell, or press `Shift+Enter` to run a cell and move to the next one.
5. If a cell runs successfully and shows output below it, your setup is working correctly.

## 6. Quick Test

Create a new file called `test.py` anywhere in the `ENERGIZE` folder with this content:

```python
import numpy as np
print("Setup successful! NumPy version:", np.__version__)
```

Run it from the VS Code terminal, with the `energize` environment activated:

```bash
python test.py
```

You should see a message confirming the NumPy version. If this works, you're ready for the workshop!

## Troubleshooting

- **`conda` not recognized**: close and reopen your terminal after installing Anaconda (on Windows, use **Anaconda Prompt** from the Start menu), or re-run the installer and allow it to modify your PATH / shell profile.
- **`python`/`python3` not recognized**: make sure you opened a new terminal (or Anaconda Prompt) after installing, and that the `energize` environment is activated (`conda activate energize`).
- **VS Code doesn't show "Select Kernel"**: make sure the Jupyter extension is installed and that you have a `.ipynb` file open, not a `.py` file.
- **"Python (energize)" doesn't appear as a kernel**: make sure you ran the `ipykernel install` command *while* the `energize` environment was activated, then restart VS Code.
- **Still stuck?** Bring your laptop to the workshop - we'll help you get set up before we start. Or email help@scc.bu.edu and set up a meeting with the SCC support team.
