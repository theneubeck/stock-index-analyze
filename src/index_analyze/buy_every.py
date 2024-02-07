from pathlib import Path
import sys

import pandas as pd

from index_analyze.lib.read_data import load_directory
from index_analyze.lib.analyze import analyze_result

def run(directory):
    result = pd.DataFrame()
    raw_data = load_directory(directory)

    years = 5

    data = build_analyze_matrix(raw_data, years)
    result = analyze_result(data, years)
    return result.sort_values(by=["median"], ascending=False).dropna()


def build_analyze_matrix(data, years=5):
    shares = mean_shares(calc_shares(data), years)
    result = shares.mul(data)
    return result.dropna(how="all")


def calc_shares(prices):
    return 1 / prices

def mean_shares(shares, years=5, min_periods=None):
    min_periods = min_periods or 12*years+1
    return shares.rolling(f"{366 * years}d", min_periods=min_periods).mean()


if __name__ == "__main__":
    with pd.option_context("display.max_rows", None):
        if len(sys.argv) > 1 and sys.argv[1] == "-h":
            print("In a buy every month for 5 years scenario:")
            print("mean - mean of times money value")
            print("median - median of times money value")
            print("min - worst of times money value")
            print("max - best of times money value")
            print()
        print(run(Path("./data/monthly")))
