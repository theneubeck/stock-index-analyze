import numpy as np
import pandas as pd
from pathlib import Path
from index_analyze.lib.read_data import load_directory

def run(directory):
    raw_data = load_directory(directory)
    result = compare_matrix(raw_data["MSCI World"], raw_data)
    print(analyze_matrix(result))

def compare_matrix(index, data):
    index_change = index.pct_change(fill_method=None).dropna(how='all')
    percentage_change = data.pct_change(fill_method=None).dropna(how='all')
    result = percentage_change.ge(index_change, axis=0).astype(int)
    # repopulate the NaN values
    return result.where(percentage_change.notna(), np.nan)

def analyze_matrix(df):
    analyze = pd.DataFrame(columns=["name"], data=df.columns).set_index("name")
    analyze["outperforming_months"] = (df.sum() / df.count()) * 100
    analyze["months"] = df.count()
    return analyze.sort_values(by=["outperforming_months"], ascending=False)

if __name__ == "__main__":
    with pd.option_context("display.max_rows", None):
        print(run(Path("./data/monthly")))
