# Setting Up Python, Jupyter, and VS Code

Before the workshop, please install and test the following on your own laptop. This only needs to be done once. If you run into trouble, bring your laptop to the start of the session and we will help you get set up.

## 1. Install Python

We recommend installing Python from the official source (rather than only relying on the version built into macOS).

### macOS
1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest **Python 3** installer for macOS.
2. Run the downloaded `.pkg` installer and follow the prompts.
3. Verify the install by opening the **Terminal** app (search for it with Spotlight, `Cmd+Space`) and running:
   ```bash
   python3 --version
   ```
   You should see something like `Python 3.12.x`.

### Windows
1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest **Python 3** installer for Windows.
2. Run the installer. **Important**: on the first install screen, check the box **"Add python.exe to PATH"** before clicking Install.
3. Verify the install by opening **Command Prompt** or **PowerShell** (search for it in the Start menu) and running:
   ```powershell
   python --version
   ```
   You should see something like `Python 3.12.x`.

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

## 4. Install Jupyter and Key Packages

1. In VS Code, open a new terminal: menu **Terminal > New Terminal** (or `` Ctrl+` ``).
2. Install Jupyter and the packages used in this workshop by running:

   **macOS**
   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install jupyter numpy pandas matplotlib
   ```

   **Windows**
   ```powershell
   python -m pip install --upgrade pip
   python -m pip install jupyter numpy pandas matplotlib
   ```

## 5. Open and Run a Notebook in VS Code

1. In VS Code, go to **File > Open Folder...** and open the `ENERGIZE` folder (the one containing `Part1` and `Part2`).
2. In the Explorer sidebar, open `Part1/01_Python_Basics_and_Data_Structures.ipynb`.
3. VS Code will show the notebook with its cells. In the top-right corner, click **Select Kernel**, then choose the Python interpreter you just installed (e.g., `Python 3.12.x`).
4. Click the ▷ (Run) button next to the first cell, or press `Shift+Enter` to run a cell and move to the next one.
5. If a cell runs successfully and shows output below it, your setup is working correctly.

## 6. Quick Test

Create a new file called `test.py` anywhere in the `ENERGIZE` folder with this content:

```python
import numpy as np
print("Setup successful! NumPy version:", np.__version__)
```

Run it from the VS Code terminal:

```bash
python3 test.py   # macOS
python test.py    # Windows
```

You should see a message confirming the NumPy version. If this works, you're ready for the workshop!

## Troubleshooting

- **`python3`/`python` not recognized**: re-run the installer and make sure the "Add to PATH" option was checked, then restart your terminal (or your computer).
- **`pip` not recognized**: try `python3 -m pip ...` (macOS) or `python -m pip ...` (Windows) instead of calling `pip` directly.
- **VS Code doesn't show "Select Kernel"**: make sure the Jupyter extension is installed and that you have a `.ipynb` file open, not a `.py` file.
- **Still stuck?** Bring your laptop to the workshop - we'll help you get set up before we start. Or email help@scc.bu.edu and set up a meeting with the SCC support team.
