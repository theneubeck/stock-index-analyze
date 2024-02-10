import numpy as np
import pandas as pd
from pathlib import Path
from index_analyze.lib.read_data import load_directory, merge
from index_analyze.lib.analyze import analyze_result

def run(directory):
    years = 5
    raw_data = load_directory(directory)
    total = analyze_matrix(compare_matrix(raw_data["MSCI World"], raw_data))

    result = rolling_outperformance(raw_data["MSCI World"], raw_data, years)
    rolling = analyze_result(result, years, raw_data).drop(["yearly", "yearly_median"], axis=1)
    return merge([rolling, total]).sort_values(by=["median"], ascending=False)

def compare_matrix(index, data):
    index_change = index.pct_change(fill_method=None).dropna(how='all')
    percentage_change = data.pct_change(fill_method=None).dropna(how='all')
    result = percentage_change.ge(index_change, axis=0).astype(int)
    # repopulate the NaN values
    return result.where(percentage_change.notna(), np.nan)

def rolling_outperformance(index, data, years):
    cmp = compare_matrix(index, data)
    min_periods = 12 * years + 1
    return cmp.rolling(f"{366 * years}d", min_periods=min_periods).mean()

def analyze_matrix(df):
    analyze = pd.DataFrame(columns=["name"], data=df.columns).set_index("name")
    analyze["total_outperforming"] = df.mean() * 100
    analyze["months_of_cmp"] = df.count()
    return analyze.sort_values(by=["total_outperforming"], ascending=False)

if __name__ == "__main__":
    with pd.option_context("display.max_rows", None):
        print(run(Path("./data/monthly")))
