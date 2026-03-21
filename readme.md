# Bayesian Motor Imagery (BMI) Plots

## Python Guide

### Conda setup

```bash
# Create environment
conda create -n evaluation python=3.12

# Delete environment
conda env remove -n evaluation

# Clone environment
conda create --name new_evaluation --clone evaluation

# List environments
conda env list

# Activate environment
conda activate evaluation

# Deactivate environment
conda deactivate

# Save environment
conda env export > evaluation.yml

# Recreate environment
conda env create -f evaluation.yml
```

### Environment variables

Create `.env` file in root of git repository.

```bash
DATA_PATH=/path/to/data
```

### File format & linting

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

## R Guide

### Conda setup

```bash
# Create environment
conda create -n analysis -c conda-forge r-base
```

### Renv project

```bash
# Enter R shell
R

# Install renv
install.packages("renv")

# Create renv
renv::init()

# Install packages
install.packages("tidyverse")

# Save renv
renv::snapshot()

# Exit R shell
q()

## Recreate renv
renv::restore()
```

### File format & linting

```bash
# Within R shell
styler::style_dir("/path/to/software")
lintr::lint_dir("/path/to/software")
```
