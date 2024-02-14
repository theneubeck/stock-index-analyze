import sys
import json
import pandas as pd

def run(file, name):
    data = json.load(file)
    df = pd.DataFrame(data=data["dataSerie"])
    df["x"] = pd.to_datetime(df["x"], unit='ms', origin='unix')
    df.set_index("x", inplace=True)
    q = df.groupby(pd.Grouper(freq="MS")).first()
    q["y"] = q["y"] + 1
    q.rename(index={0:"Date"}, columns={"y": name}, inplace=True)
    q.to_csv(f"data/{name}.csv", date_format="%Y-%m")
    return q


if __name__ == "__main__":
    print(run(sys.stdin, "dnb-tech-a"))