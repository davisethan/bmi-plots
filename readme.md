# Bayesian Motor Imagery (BMI) Plots

## Conda setup

```bash
# Create environment
conda create -n bmi-plots python=3.12

# Delete environment
conda env remove -n bmi-plots

# List environments
conda env list

# Activate environment
conda activate bmi-plots

# Deactivate environment
conda deactivate

# Save environment
conda env export > environment.yml

# Recreate environment
conda env create -f environment.yml
```

## Environment variables

Create `.env` file in root of git repository.

```bash
DATA_PATH=/path/to/data
```

## File format & linting

```bash
# Format files
ruff format /path/to/software

# Fail if files not formatted
ruff format --check /path/to/software

# Lint files
ruff check --fix /path/to/software

# Fail if files not linted
ruff check /path/to/software
```
