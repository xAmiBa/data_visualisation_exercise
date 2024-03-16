# Sales and Profit Analysis Project

This project is designed to analyze sales data from a CSV file, calculate profits, and visualize the data to provide insights into the sales and profit trends over time.

## Libraries Used

- `csv`: For reading and writing CSV files.
- `pandas`: Used for data manipulation and analysis.
- `plotly.express`: For creating interactive charts and graphs for data visualization.

## Overview
![graph example](/Screenshot%202024-03-16%20at%2000.04.50.png)
The project performs several key operations on the sales data:

1. Reads sales data from a CSV file.
2. Calculates total sales across all months.
3. Extends the project to calculate profit (sales - expenditure) for each month, adding this data as a new column in the CSV.
4. Calculates the total profit across all months.
5. Identifies the maximum and minimum sales and profit values across all months.
6. Visualizes the profit across all months using a line graph.
7. Offers the option to display additional graphs for sales and expenditure on demand.

## Data Visualization

This project uses Plotly Express to create dynamic and interactive visualizations. Specifically, it features:

- A line graph showing profits across all months, which helps in understanding the profit trends over time.
- On-demand generation of line graphs for sales and expenditure, allowing for a deeper dive into the financial performance of the company.

## Running the Project

Ensure you have the required libraries installed:

```bash
pip install pandas plotly
```

Run the script in a Python environment. The script will prompt you to choose whether you want to display additional graphs for sales and expenditure.

## Data File

The script operates on a `sales.csv` file, which must include the columns `month`, `sales`, and `expenditure`. Ensure this file is in the same directory as the script for it to run correctly.

## Conclusion

This project offers a comprehensive analysis and visualization of sales data, providing valuable insights into the company's financial performance over time.
