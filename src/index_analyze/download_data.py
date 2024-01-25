import yfinance as yf

tickers = {
    'Global': '^GSPC',          # S&P 500 as a global index (you can change this to another global index)
    'Nasdaq 100': '^NDX',
    'Nasdaq Composite': '^IXIC',
    'Dow Jones': '^DJI',
    'S&P 500': '^GSPC',
    'FTSE 100': '^FTSE',         # UK
    'DAX': '^GDAXI',             # Germany
    'CAC 40': '^FCHI',           # France
    'NIKKEI 225': '^N225',       # Japan
    'Hang Seng': '^HSI',         # Hong Kong
    'Shanghai Composite': '000001.SS',  # China
    'Sensex': '^BSESN',          # India
    'ASX 200': '^AXJO',          # Australia
    'Brazil Bovespa': '^BVSP',   # Brazil
    'MSCI WORLD': '^990100-USD-STRD',
    "OMX 30" : '^OMX',
    "Vanguard Small Cap Index Adm": 'VSMAX'
    # Add more indices as needed
}

ticker = tickers['Nasdaq Composite']
data = yf.download(ticker, start="2023-01-01", end="2024-01-20", interval="1mo")
print(data.reset_index()[["Date", "Close"]].to_csv())
print(data.reset_index().to_json())

print(data.reset_index()[["Date", "Close"]].to_string(formatters={"Date": lambda x: x.strftime('%Y-%m')}))
