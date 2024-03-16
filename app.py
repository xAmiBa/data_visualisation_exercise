import csv
import pandas as pd
import plotly.express as px


with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

# 2. All of the sales from each month in a single list. I used for loop.
    print('Sales for every month:')
    for row in spreadsheet:
        sales = dict(row)['month'] + '  £ ' + dict(row)['sales']
        print(sales)
print('\n')

#3. Output the total sales across all months
data = pd.read_csv('sales.csv')
sales_sum = data['sales'].sum()
print('Total sales across all months are: £ {}'.format(sales_sum))

#empty line to make the report more readable
print('\n')

#PROJECT EXTENSION: PROFIT ACROSS ALL MONTHS
# substracts expediture from sales values and add new colum
df = pd.read_csv('sales.csv')
profit_data = df['sales'] - df['expenditure']
df['profit'] = df['sales'] - df['expenditure']
profit = df['profit']
new_column = df['profit']
data_new = pd.read_csv('sales.csv')
data_new['profit'] = new_column
data_new.to_csv('sales.csv', index=False)
print('\n')

#PROJECT EXTENSION: OUTPUT OF PROFIT VALUES ACROSS ALL MONTHS. For loop used.
import csv
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    print('Profit for every month:')
    for row in spreadsheet:
        profit_print = dict(row)['month'] + '  £ ' + dict(row)['profit']
        print(profit_print)

#PROJECT EXTENSION: SUM OF TOTAL PROFIT ACROSS ALL MONTHS
# Pandas dataframe. constructor
data = pd.read_csv('sales.csv')
profit_sum = data['profit'].sum()
print('Total profit across all months is: £ {}'.format(profit_sum))
print('\n')


#PROJECT EXTENSION: MAXIMUM AND MINIMUM INCOME AND SALES ACROSS ALL MONTHS
maximum_sales = df['sales'].max()
print('The maximum monthly sales across all months was: £', maximum_sales)

maximum_profit = df['profit'].max()
print('The maximum monthly profit across all months was: £', maximum_profit)

minimum_sales = df['sales'].min()
print('The minimum monthly sales across all months was: £', minimum_sales)

minimum_profit = df['profit'].min()
print('The minimum monthly profit across all months was: £', minimum_profit)
print('\n')

#Print of the whole dataframe defined earlier
print(df)

#PROJECT EXTENSION: Graph showing profits across all months
graph_data = pd.read_csv('sales.csv')
graph = px.line(graph_data, x = 'month', y = 'profit', title = 'Company profits graph')
graph.show()
print('\n')

#PROJECT EXTENSION: Graphs for different rows of data - on demand
#if yes - prints sales graph
yes_sales_graph = input('Would you like me to display the \'Company sales graph\'? y/n ')
if yes_sales_graph == 'y':
    graph_data = pd.read_csv('sales.csv')
    graph = px.line(graph_data, x = 'month', y = 'sales', title = 'Company sales graph')
    graph.show()
else:
    print('No worries, thank you!')

#if yes - prints expenditure graph
yes_expenditure_graph = input('Would you like me to display the \'Company expenditure graph\'? y/n ')
if yes_expenditure_graph == 'y':
    graph_data = pd.read_csv('sales.csv')
    graph = px.line(graph_data, x='month', y='sales', title='Company expenditure graph')
    graph.show()
else:
    print('No worries, thank you!')