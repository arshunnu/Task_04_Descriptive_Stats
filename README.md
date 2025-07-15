# Task_04_Descriptive_Stats

This repository contains a research task focused on calculating descriptive statistics and analyzing performance data. The task involves analyzing various performance metrics across different campaigns, aiming to understand patterns and trends in engagement, spending, and audience targeting.

## Objective
The primary objective of this project is to:
1. Compute descriptive statistics (count, mean, min, max, std, unique values, most frequent values) using:
   - Pure Python
   - Pandas
   - Polars
2. Visualize the data using appropriate charts to help draw insights from the analysis.
3. Provide a compelling narrative based on these statistics that can be presented to senior executives or researchers.

## Methodology
The task is split into three main scripts:
1. Pure Python Script: Loads the data and computes descriptive statistics using Python’s built-in libraries.
2. Pandas Script: Loads the data using Pandas and computes descriptive statistics using tools like `DataFrame.describe()`, `value_counts()`, and `nunique()`.
3. Polars Script: Loads the data using Polars and computes descriptive statistics manually using Polars’ methods for numerical and categorical data.

### Key Analytical Steps:
1. Loading the Data: The data was loaded using Pandas (for the Pandas script) and Polars (for the Polars script).
2. Descriptive Statistics: 
   - For numeric columns, statistics like count, mean, min, max, and standard deviation were computed.
   - For categorical columns, the unique values and most common values were calculated.
3. Visualization: Visualizations such as histograms, box plots, and bar charts were created to explore data distributions and patterns.

## Visualizations
The following visualizations were created to help understand key aspects of the data:
1. Histogram for Numeric Data: Distribution of key performance metrics.
2. Boxplot for Numeric Data: Visualizing the spread and identifying outliers in the data.
3. Bar Charts for Categorical Data: Performance across different categories such as platforms or ad creators.

### Examples:
- Histogram: Shows the distribution of key metrics, such as spending or audience size, helping identify skewness and anomalies.
- Boxplot: Provides insights into the spread and distribution of numeric data, highlighting potential outliers.
- Bar Charts: Display how certain categories (e.g., platforms or ad creators) perform relative to others.

## Installation

### Dependencies
- Python 3.8+
- Libraries:
  - Pandas
  - Polars
  - Streamlit (for creating an interactive dashboard)
  - Matplotlib and Seaborn (for visualizations)

You can install the required libraries using `pip`:

```bash
pip install pandas polars streamlit matplotlib seaborn
