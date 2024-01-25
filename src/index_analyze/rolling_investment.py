import os
import pandas as pd
from pathlib import Path

def merge(contents):
    data = pd.DataFrame()
    for c in contents:
         data = pd.merge(data, c, how="outer", left_index=True, right_index=True)

    return data

def run(directory):
    contents = []

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            with open(os.path.join(directory, filename)) as f:
                contents.append(pd.read_csv(f, parse_dates=['Date'], date_format="%Y-%m").set_index('Date'))
                # data = pd.merge(data, content, how="outer", left_index=True, right_index=True)
    data = merge(contents)
    print(data)

def analyze(data):
    pass

if __name__ == "__main__":
    run(Path("./data/curvo"))