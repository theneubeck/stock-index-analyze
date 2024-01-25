import os
from pathlib import Path
from datetime import datetime
import pandas as pd


def merge(contents):
    data = pd.DataFrame()
    for c in contents:
        data = pd.merge(data, c, how="outer", left_index=True, right_index=True)

    return data


def run(directory):
    contents = []

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            with open(os.path.join(directory, filename)) as f:
                contents.append(pd.read_csv(f, parse_dates=["Date"], date_format="%Y-%m").set_index("Date"))
    data = build_analyze_matrix(merge(contents))
    print(analyze(data))

def analyze(data):
    means = pd.DataFrame(columns=["mean"], data=data.mean().transpose())
    means["median"] = data.median().array
    means["min"] = data.min().array
    means["max"] = data.max().array
    means["yearly"] = means["mean"].apply(lambda x: x**(1/5))
    means["yearly_median"] = means["median"].apply(lambda x: x**(1/5))
    return means.sort_values(by=["median"], ascending=False)

def build_analyze_matrix(data, years = 5):
    values_5_years_ago = data.shift(periods=1, freq=pd.DateOffset(years=years))
    result = data.div(values_5_years_ago)
    return result.dropna(how="all")


if __name__ == "__main__":
    run(Path("./data/monthly"))
