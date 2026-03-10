# Statistics Course - Python Practicals

Python implementations for Statistics practical sessions (TDs - Travaux Dirigés), including descriptive analysis and visualizations.

## Overview

This repository is organized by TD modules. Each TD file contains one or more functions that implement a specific statistical concept (quartiles, medians, grouped data, weighted data, and applied analysis).

## Repository Structure

```
Statistics_cours-python-/
├── README.md
├── LICENSE
├── Td4_Dzhafarov.py
├── td5/
└── td6/
	├── Td6.py
	├── s3.py
	├── s4.py
	└── s5.py
```

## Modules Index

| TD | File | Scope | Status |
|----|------|-------|--------|
| TD4 | `Td4_Dzhafarov.py` | Quartiles, box plots, grouped data, weighted data, demographic analysis | Available |
| TD6 | `td6/Td6.py`, `td6/s3.py`, `td6/s4.py`, `td6/s5.py` | Charts, descriptive statistics, outlier filtering, regression, clustering | Available |
| TD1 | _To be added_ | _To be defined_ | Planned |
| TD2 | _To be added_ | _To be defined_ | Planned |
| TD3 | _To be added_ | _To be defined_ | Planned |

## TD4 - Function Reference

### Core Exercises

| Function | Role |
|----------|------|
| `example()` | Computes quartiles for two datasets and generates a comparison box plot. |
| `ex1()` | Compares mean and median behavior under an outlier change and plots both datasets. |
| `ex2()` | Computes quartiles/median/mean for two series and overlays reference lines on box plots. |

### Frequency-Weighted Quartiles

| Function | Role |
|----------|------|
| `mediane_quartiles_avec_effectifs1(values)` | Expands `(value, frequency)` data and computes quartiles with `numpy.quantile`. |
| `mediane_quartiles_avec_effectifs2(values)` | Computes quartiles from weighted data using 
an interpolation approach based on `(n+1)/4`. |
| `ex3()` | Compares both quartile methods side-by-side with printed results and plots. |

### Grouped Data and Validation

| Function | Role |
|----------|------|
| `exercice4(classes, values)` | Calculates Q1, median, and Q3 from grouped class intervals using interpolation. |
| `exercice4_tests()` | Runs example scenarios for grouped quartiles, including an SLA-style interpretation. |

### Applied Demographic Analysis

| Function | Role |
|----------|------|
| `probleme1()` | Analyzes median/mean age trends by gender over time from CSV data and generates visual output. |

## TD6 - Function Reference

### Basic Charts (`td6/Td6.py`)

| Function | Role |
|----------|------|
| `battongrosse(valeurs)` | Draws a histogram for the provided values and saves the figure in non-interactive environments. |
| `battonfinne(valeurs, effectifs)` | Draws a bar chart from categories and frequencies. |
| `circul(listedesvaleurs, listedeffectif)` | Draws a pie chart with percentage labels. |

### Descriptive Statistics (`td6/s3.py`)

| Function | Role |
|----------|------|
| `ecarttype(...)` | Computes mean and standard deviation for a simple numeric list. |
| `interquartile(...)` | Computes interquartile range (IQR) and median with a Weibull-style quantile interpolation. |

### Applied Analysis (`td6/s4.py`)

| Function | Role |
|----------|------|
| `statresume(...)` | Chooses robust summary statistics when outliers are detected. |
| `listefilteranddisplay(listebrute, seuil, titre)` | Filters values by frequency threshold and generates summary plots. |
| `exercice1()` | Loads laptop dataset fields and produces filtered distributions for CPU, GPU, and RAM. |
| `prepare_data_mindfactory()` | Prepares raw and filtered data pairs (`display_cm`, `price_eur`) for modeling. |
| `exercice2()` | Runs linear regression on raw and filtered data and returns model parameters/predictions. |
| `exercice3()` | Performs KMeans clustering on raw and filtered data and returns cluster centers. |

### Filtering Utility (`td6/s5.py`)

| Function | Role |
|----------|------|
| `statfiltre(liste_simple, liste_a_modifier=None)` | Iteratively filters values around mean +/- 0.7*std until no strong outlier signal remains. |

## Requirements

- Python 3.8+
- numpy
- matplotlib
- pandas

Optional for advanced TD6 steps:

- scipy (preferred linear regression backend)
- scikit-learn (required for `exercice3()` clustering)

## Installation

```bash
git clone https://github.com/Gog2006/Statistics_cours-python-.git
cd Statistics_cours-python-
pip install numpy matplotlib pandas scipy scikit-learn
```

## Usage

### Run all TD4 scripts

```bash
python Td4_Dzhafarov.py
```

### Run TD6 scripts

```bash
python td6/Td6.py
python td6/s4.py
```

### Run selected functions

```python
from Td4_Dzhafarov import ex1, ex2, ex3, exercice4_tests, probleme1

ex1()
ex2()
ex3()
exercice4_tests()
# probleme1()  # Requires the expected CSV input file path used in the script
```

```python
from td6.Td6 import battongrosse, battonfinne, circul
from td6.s4 import exercice1, exercice2, exercice3

battongrosse([1, 2, 2, 3, 4])
battonfinne(["A", "B", "C"], [10, 8, 12])
circul(["A", "B", "C"], [10, 8, 12])

exercice1()
exercice2()
# exercice3()  # Requires scikit-learn
```

## Notes

- Most plots are saved as PNG files in the local Downloads directory.
- `probleme1()` depends on a CSV dataset path currently hardcoded in `Td4_Dzhafarov.py`.
- TD6 analysis scripts use `td6/mindfactory_updated.csv` when present.

## Scalability Convention for Future TDs

For each new TD file, keep the same structure:

1. Add one row in Modules Index.
2. Add a section `## TDX - Function Reference`.
3. Document each function with a short “Role” description.
4. Add a minimal usage example.

This keeps the repository documentation consistent as new practicals are added.

## License

See [LICENSE](LICENSE).
