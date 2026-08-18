# Part 2 - Advanced Session (Shared Computing Cluster)

Run these notebooks on the SCC, ideally through **SCC OnDemand** (see notebook 8), so you have access to GPU nodes and your own Python environment. Students should already be added to the SCC project before this session.

## Notebooks, in order

0. **00_Setup_on_SCC_OnDemand.ipynb** - log in through SCC OnDemand, create a personal project folder, clone the workshop repository, and set up the `energize` conda environment with the workshop packages and PyTorch.
1. **01_Advanced_Data_Structures.ipynb** - sets, set/dict comprehensions, sorting with a custom key, `zip()`, `namedtuple`.
2. **02_Advanced_Dictionary_Usage.ipynb** - `.get()`, `defaultdict`, `Counter`, merging dictionaries, nested dictionaries and JSON.
3. **03_NumPy_for_Performance.ipynb** - vectorization vs. Python loops (with timing), broadcasting, basic linear algebra, views vs. copies.
4. **04_Advanced_Pandas.ipynb** - merging DataFrames, multi-column grouping/aggregation, pivot tables, `.apply()`.
5. **05_CPU_vs_GPU_Computing.ipynb** - why GPUs are fast for array math, PyTorch CPU vs. GPU benchmark, moving data between CPU and GPU. **Requires a GPU node.**
6. **06_Submitting_Jobs_CPU_vs_GPU.ipynb** - anatomy of a `qsub` batch script, CPU vs. GPU job examples, interactive sessions, monitoring jobs, array jobs.
7. **07_Virtual_Environments_on_SCC.ipynb** - `venv` and conda environments on the SCC, requirements files, using an environment in a batch job or as a Jupyter kernel.
8. **08_Jupyter_Notebooks_on_SCC.ipynb** - running Jupyter on a compute node via SCC OnDemand (or a manual SSH tunnel), requesting a GPU for a notebook session.

## Data

- `tensile_test_data.csv` - the same sample dataset from Part 1.
- `material_properties.csv` - a small reference table (density, Young's modulus) used to demonstrate merging in notebook 4.

## Suggested Flow

Cover notebooks 1-4 (advanced language/data-science topics) first, then move to 5-8 (SCC/GPU-specific topics), ending with students launching their own Jupyter session on a GPU node via OnDemand.
