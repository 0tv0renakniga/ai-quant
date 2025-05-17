import yfinance as yf
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Step 1: Fetch historical price data (past year)
ticker = 'AAPL'  # Apple stock
benchmark = '^GSPC'  # S&P 500 Index
start_date = '2023-01-01'
end_date = '2024-01-01'

# Download data from Yahoo Finance
#stock_data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
#benchmark_data = yf.download(benchmark, start=start_date, end=end_date)['Adj Close']
stock_data = yf.download(ticker, start=start_date, end=end_date)[('Close', ticker)]
benchmark_data = yf.download(benchmark, start=start_date, end=end_date)[('Close', benchmark)]
print(stock_data)


# Combine data into a single DataFrame
data = pd.DataFrame({
    'Stock': stock_data,
    'Benchmark': benchmark_data
}).dropna()

# Step 2: Calculate daily returns
returns = data.pct_change().dropna()

# Display the first few rows
print(returns.head())

# Define dependent (stock) and independent (benchmark) variables
X = returns['Benchmark']
y = returns['Stock']

# Add a constant to the independent variable for intercept term
X_const = sm.add_constant(X)

# Run regression: stock returns ~ benchmark returns
model = sm.OLS(y, X_const).fit()

# Extract Beta coefficient (slope)
beta = model.params['Benchmark']

print(f"\nComputed Beta for {ticker}: {beta:.4f}")

# Optional: Display detailed regression results
print(model.summary())

# Scatter plot of returns
plt.figure(figsize=(8, 5))
plt.scatter(X, y, alpha=0.5, color='blue', label='Daily Returns')

# Plot regression line
regression_line = model.params['const'] + beta * X
plt.plot(X, regression_line, color='red', linewidth=2, label='Regression Line')

plt.title(f"Regression of {ticker} Returns vs. S&P 500 Returns")
plt.xlabel('Benchmark Returns (S&P 500)')
plt.ylabel(f'{ticker} Returns')
plt.legend()
plt.grid(True)
plt.savefig('benchmark_returns.png')

