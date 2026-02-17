# Statistics Course - Python Practicals

Python implementations and visualizations for practical exercises in Statistics.

## Project Overview

This repository contains solutions and educational examples for Statistics course practicals (TDs - Travaux Dirigés). Each module focuses on different statistical concepts with practical implementations using Python, including data analysis, visualization, and quantitative methods.

## Repository Structure

```
Statistics_cours-python-/
├── README.md                 # Project documentation
├── LICENSE                   # License information
├── Td4_Dzhafarov.py         # TD4: Statistical measures and box plots
```

## Course Topics

The repository covers the following statistical topics:

### TD4: Quartiles, Box Plots, and Distribution Analysis

#### Functions Overview

| Function | Description |
|----------|-------------|
| `example()` | Basic introduction to quartiles (Q1, Q2, Q3) calculation and box plot visualization for two datasets. |
| `ex1()` | Demonstrates the impact of outliers on mean vs. median through comparison with visual indicators. |
| `ex2()` | Advanced box plot with quartiles, median, and mean reference lines overlaid for two data series. |
| `mediane_quartiles_avec_effectifs1(values)` | Calculates quartiles from frequency-weighted data using NumPy's quantile method. Handles (value, frequency) pairs. |
| `mediane_quartiles_avec_effectifs2(values)` | Alternative quartile calculation using the (n+1)/4 interpolation method for weighted data. |
| `ex3()` | Compares two quartile calculation methods (NumPy vs. (n+1)/4) side-by-side with visual representation. |
| `exercice4(classes, values)` | Calculates quartiles from grouped/classified data (intervals with frequencies). Returns Q1, median, Q3. |
| `exercice4_tests()` | Test cases for grouped data quartile calculation with real-world examples and SLA evaluation. |
| `probleme1()` | Complex analysis of French population age distribution (1991-2023) using pandas, including mean/median trends and population aging insights. |

#### Function Details

**Basic Exercises (example, ex1, ex2)**
- Focus on direct quartile and median calculation
- Demonstrate box plot visualization
- Show impact of outliers on statistical measures

**Frequency-Weighted Data (mediane_quartiles_avec_effectifs1, mediane_quartiles_avec_effectifs2, ex3)**
- Handle data with frequency counts
- Compare different quartile interpolation methods
- Validate calculation approaches

**Grouped Data Analysis (exercice4, exercice4_tests)**
- Calculate statistics from binned/classified data
- Apply interpolation formulas for continuous distributions
- Include SLA (Service Level Agreement) evaluation examples

**Advanced Analysis (probleme1)**
- Uses pandas for data manipulation
- Time-series analysis of demographic data
- Comprehensive statistical reporting with visualizations



## Requirements

- Python 3.7+
- numpy
- matplotlib
- pandas

## Installation

Clone the repository:

```bash
git clone https://github.com/Gog2006/Statistics_cours-python-.git
cd Statistics_cours-python-
```

Install dependencies:

```bash
pip install numpy matplotlib pandas
```

## Usage

Each TD module contains executable functions demonstrating different statistical concepts.

### Running TD4 Exercises

Import and run specific exercises from TD4:

```python
from Td4_Dzhafarov import example, ex1, ex2, ex3, exercice4_tests, probleme1

# Run basic examples
example()          # Quartiles and box plots
ex1()              # Mean vs median with outliers
ex2()              # Detailed statistical analysis and visualization

# Run frequency-weighted data analysis
ex3()              # Compare quartile calculation methods

# Run grouped data analysis
exercice4_tests()  # Quartiles from classified data with SLA evaluation

# Run advanced analysis
probleme1()        # French population age analysis (requires CSV data)
```

### Output

Visualizations are saved to the Downloads folder in PNG format with high resolution (200+ DPI).

## Contributing

Contributions and improvements to existing solutions are welcome. Please ensure code follows the project structure for scalability.

## License

See [LICENSE](LICENSE) file for details.
