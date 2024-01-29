import os
from pathlib import Path
from datetime import datetime
import pandas as pd

def merge(contents):
    data = pd.DataFrame()
    for c in contents:
        data = pd.merge(data, c, how="outer", left_index=True, right_index=True)

    return data

def load_directory(directory):
    contents = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            with open(os.path.join(directory, filename)) as f:
                contents.append(pd.read_csv(f, parse_dates=["Date"], date_format="%Y-%m").set_index("Date"))
    return merge(contents)
