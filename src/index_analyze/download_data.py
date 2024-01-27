import yfinance as yf
import pandas as pd

tickers = {
    'Global': '^GSPC',          # S&P 500 as a global index (you can change this to another global index)
    "Dow Jones Industrial Average": "^DJI",
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
    "Vanguard Small Cap Index Adm": 'VSMAX',

    # OMX and Nordic Country Indices
    "OMX Stockholm 30 (Sweden)": "^OMX",
    "OMX Helsinki 25 (Finland)": "^OMXH25",
    "OMX Copenhagen 20 (Denmark)": "^OMXC20",
    "OMX Iceland 8 (Iceland)": "OMXI8",
    # OMX Baltic 10 does not have a universal ticker; individual country indices or stocks may need to be referenced.
    "OMX Oslo 20 (Norway)": "^OSEAX",  # Note: Oslo Børs is not part of Nasdaq Nordic.

    # Commodities
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Crude Oil": "CL=F",
    "Brent Oil": "BZ=F",
    "Natural Gas": "NG=F",
    "Copper": "HG=F",

    # Currency Pairs
    "EUR/USD": "EURUSD=X",
    "USD/JPY": "USDJPY=X",
    "GBP/USD": "GBPUSD=X",
    "USD/CHF": "USDCHF=X",
    "AUD/USD": "AUDUSD=X",
    "USD/CAD": "USDCAD=X",

    # Interest Rates and Bonds
    "US 10-Year Treasury Yield": "^TNX",
    "US 30-Year Treasury Yield": "^TYX",
    "US 2-Year Treasury Yield": "^IRX",
    "Euro Bund": "^BUND",
    "UK Gilt 10-Year Yield": "^GSPG10YR"
}

# ticker = tickers['Nasdaq Composite']
# data = yf.download(ticker, start="2023-01-01", end="2024-01-20", interval="1mo")
# print(data.reset_index()[["Date", "Close"]].to_csv())
# print(data.reset_index().to_json())

# print(data.reset_index()[["Date", "Close"]].to_string(formatters={"Date": lambda x: x.strftime('%Y-%m')}))

def download(name, ticker):
    data = yf.download(ticker, period='max', interval='1mo')
    # data = yf.download(ticker, start="2023-01-01", end="2024-01-20", interval="1mo")
    print(data.rename(columns={"Close": name}).to_csv(date_format="%Y-%m", columns=[name]))

download("OMX", "^OMX")