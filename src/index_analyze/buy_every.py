from pathlib import Path

import pandas as pd

from index_analyze.read_data import load_directory
from index_analyze.analyze import analyze_result

def run(directory):
    result = pd.DataFrame()
    raw_data = load_directory(directory)

    years = 5

    data = build_analyze_matrix(raw_data, years)
    result = analyze_result(data, years)
    return result.sort_values(by=["median"], ascending=False).dropna()


def build_analyze_matrix(data, years=5):
    shares = sum_shares(calc_shares(data), years)
    result = shares.div(12*years+1).mul(data)
    return result.dropna(how="all")


def calc_shares(prices):
    return 1 / prices

def sum_shares(shares, years=5):
    return shares.rolling(f"{366 * years}d", min_periods=12*years+1).sum()


if __name__ == "__main__":
    with pd.option_context("display.max_rows", None):
        print(run(Path("./data/monthly")))