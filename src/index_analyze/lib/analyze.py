import math
import pandas as pd

def analyze_result(data, years):
    analyze = pd.DataFrame(columns=["name"], data=data.columns).set_index("name")
    analyze["years"] = years
    analyze["years_of_data"] = data.apply(calculate_date_difference)

    analyze["mean"] = data.mean().array
    analyze["median"] = data.median().array
    analyze["min"] = data.min().array
    analyze["max"] = data.max().array
    analyze["yearly"] = analyze["mean"].apply(lambda x: x ** (1 / years))
    analyze["yearly_median"] = analyze["median"].apply(lambda x: x ** (1 / years))
    return analyze.sort_values(by=["median"], ascending=False)


# Define a function to calculate the date difference for a column
def calculate_date_difference(column):
    first_date = column.first_valid_index()
    last_date = column.last_valid_index()
    if not first_date or not last_date:
        return 0
    return math.ceil((last_date - first_date).days/ 365.25)
