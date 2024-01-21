import yfinance as yf

def get_yearly_returns(ticker):
    data = yf.download(ticker, start="2000-01-01", end="2023-01-01")
    data['Year'] = data.index.year
    yearly_returns = data.groupby('Year')['Adj Close'].pct_change().add(1).prod() - 1
    return yearly_returns

# Define the tickers for the indices
indices = {
    'Global': '^GSPC',  # S&P 500 as a global index (you can change this to another global index)
    'Nasdaq 100': '^NDX',
    'Dow Jones': '^DJI',
    # Add more indices as needed
}

# Calculate yearly returns for each index
returns_dict = {}
for index_name, index_ticker in indices.items():
    returns_dict[index_name] = get_yearly_returns(index_ticker)

# Find the index that outperformed the global index
global_returns = returns_dict['Global']
outperformers = {index_name: returns for index_name, returns in returns_dict.items() if returns > global_returns}

# Display the results
print("Yearly Returns:")
for index_name, returns in returns_dict.items():
    print(f"{index_name}: {returns:.4f}")

print("\nIndices that outperformed the global index:")
for index_name in outperformers:
    print(index_name)
