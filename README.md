# Statistics Course - Python Practicals

Python implementations for Statistics practical sessions (TDs - Travaux Dirigés), including descriptive analysis and visualizations.

## Overview

This repository is organized by TD modules. Each TD file contains one or more functions that implement a specific statistical concept (quartiles, medians, grouped data, weighted data, and applied analysis).

## Repository Structure

```
Statistics_cours-python-/
├── README.md
├── LICENSE
└── Td4_Dzhafarov.py
```

## Modules Index

| TD | File | Scope | Status |
|----|------|-------|--------|
| TD4 | `Td4_Dzhafarov.py` | Quartiles, box plots, grouped data, weighted data, demographic analysis | Available |
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

## Requirements

- Python 3.8+
- numpy
- matplotlib
- pandas

## Installation

```bash
git clone https://github.com/Gog2006/Statistics_cours-python-.git
cd Statistics_cours-python-
pip install numpy matplotlib pandas
```

## Usage

### Run all TD4 scripts

```bash
python Td4_Dzhafarov.py
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

## Notes

- Most plots are saved as PNG files in the local Downloads directory.
- `probleme1()` depends on a CSV dataset path currently hardcoded in `Td4_Dzhafarov.py`.

## Scalability Convention for Future TDs

For each new TD file, keep the same structure:

1. Add one row in Modules Index.
2. Add a section `## TDX - Function Reference`.
3. Document each function with a short “Role” description.
4. Add a minimal usage example.

This keeps the repository documentation consistent as new practicals are added.

## License

See [LICENSE](LICENSE).
