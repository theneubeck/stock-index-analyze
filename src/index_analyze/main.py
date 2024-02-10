import sys

import pandas as pd

from index_analyze.lib.investor import Investor


def parse_input(format="csv"):
    if format == "csv":
        return pd.read_csv(sys.stdin, parse_dates=["Date"], date_format="%b %d, %Y")
    elif format == "csv-curvo":
        return pd.read_csv(sys.stdin, parse_dates=["Date"], date_format="%Y-%m")
    return pd.read_json(sys.stdin)


def run(data):
    investor = Investor("stdin")
    for _, row in data.iterrows():
        investor.buy(row["Date"], row["Close"], 100)
    return investor


def main():
    result = run(parse_input("json"))
    print(result.inspect())


if __name__ == "__main__":
    main()
