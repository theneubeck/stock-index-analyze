import pandas as pd

def analyze_result(data, years):
    analyze = pd.DataFrame(columns=["name"], data=data.columns)
    analyze["years"] = years
    analyze["mean"] = data.mean().array
    analyze["median"] = data.median().array
    analyze["min"] = data.min().array
    analyze["max"] = data.max().array
    analyze["yearly"] = analyze["mean"].apply(lambda x: x ** (1 / years))
    analyze["yearly_median"] = analyze["median"].apply(lambda x: x ** (1 / years))
    return analyze.sort_values(by=["median"], ascending=False)