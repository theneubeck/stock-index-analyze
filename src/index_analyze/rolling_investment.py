from pathlib import Path
import pandas as pd
from index_analyze.read_data import load_directory


def run(directory):
    result = pd.DataFrame()
    raw_data = load_directory(directory)

    for years in range(1,11):
        data = build_analyze_matrix(raw_data, years)
        result = pd.concat([result, analyze(data, years)])
    return result.sort_values(by=["median"], ascending=False).dropna()

def analyze(data, years):
    analyze = pd.DataFrame(columns=["name"], data=data.columns)
    analyze["years"] = years
    analyze["mean"] = data.mean().array
    analyze["median"] = data.median().array
    analyze["min"] = data.min().array
    analyze["max"] = data.max().array
    analyze["yearly"] = analyze["mean"].apply(lambda x: x**(1/years))
    analyze["yearly_median"] = analyze["median"].apply(lambda x: x**(1/years))
    return analyze.sort_values(by=["median"], ascending=False)

def build_analyze_matrix(data, years = 5):
    values_5_years_ago = data.shift(periods=1, freq=pd.DateOffset(years=years))
    result = data.div(values_5_years_ago)
    return result.dropna(how="all")

def mean_of_all_years(data):
    group = data.groupby("name")
    analyze = pd.DataFrame()
    analyze["yearly_mean"] = group["yearly"].mean()
    analyze["yearly_median_mean"] = group["yearly_median"].mean()
    return analyze.sort_values(by=["yearly_median_mean"], ascending=False)

if __name__ == "__main__":
    with pd.option_context('display.max_rows', None):
        baz  = run(Path("./data/monthly"))
        print(baz)
        # print(mean_of_all_years(baz))
