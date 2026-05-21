# Design Note Example: CSV Trend Plot

## Problem

Create a small Python script that reads a CSV file containing `date` and `sales` columns and produces a monthly sales trend plot.

## Scope

Included:
- load one CSV file from disk
- parse the `date` column into real dates
- sort rows chronologically
- aggregate by month
- save a single line chart as an image

Excluded:
- web UI
- database storage
- multiple file uploads
- forecasting future sales

## Inputs

- CSV file path
- a CSV with at least two columns: `date` and `sales`

Example input rows:

```csv
date,sales
2026-01-05,120
2026-01-20,180
2026-02-01,150
```

## Outputs

- one saved chart image, for example `monthly_sales.png`
- optional console message confirming where the chart was written

## Constraints

- use Python
- prefer standard libraries plus `pandas` and `matplotlib`
- fail clearly if required columns are missing
- do not mutate the original CSV file
- keep the script understandable for beginners

## Validation

- the script runs on a small sample CSV without crashing
- the months appear in chronological order
- the plot contains one point per month
- missing columns produce a clear error message
