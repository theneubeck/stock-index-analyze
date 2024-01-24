import os
import sys
import json
import pandas as pd
from pathlib import Path
from index_analyze.main import Investor

def run(directory, filename):
    name = Path(filename).stem
    investor = Investor(name)
    with open(os.path.join(directory, filename)) as f:
        data = pd.read_csv(f, parse_dates=['Date'], date_format="%Y-%m")
        for _, row in data.iterrows():
            investor.buy(row['Date'], row.iloc[1], 100)

    return investor

def compound(directory):
    investors = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            investors.append(run(directory, filename))

    results = map(lambda x: x.inspect(), investors)
    #print(json.dumps(sorted(results, key=lambda x: x["total_yearly"])))
    print(pd.DataFrame(data = results).set_index("name").sort_values(by=["total_yearly"], ascending=False))


if __name__ == "__main__":
    compound(sys.argv[1])

