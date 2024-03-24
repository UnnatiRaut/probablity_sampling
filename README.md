# Ratio Analysis README

## Overview
This Python script conducts a ratio analysis on a dataset to identify upregulated and downregulated genes based on certain thresholds. The script takes a CSV file named `PIC Approach1.csv` containing gene expression data and generates a new CSV file named `Ratio Counts and Percentages PIC_1.csv` with counts and percentages of upregulated and downregulated genes.

## Requirements
- Python 3.x
- pandas
- itertools

## Usage
1. Place the `PIC Approach1.csv` file in the same directory as the script.
2. Run the script.
3. Find the output in a file named `Ratio Counts and Percentages PIC_1.csv` in the same directory.

## Description
- `File1.csv`: Input CSV file containing gene expression data.
- `Ratio Counts and Percentages PIC_1.csv`: Output CSV file containing counts and percentages of upregulated and downregulated genes.
- `upregulated_count`: Number of genes with expression ratios greater than 2.
- `downregulated_count`: Number of genes with expression ratios less than 0.5.
- `upregulated_percentage`: Percentage of genes that are upregulated.
- `downregulated_percentage`: Percentage of genes that are downregulated.
