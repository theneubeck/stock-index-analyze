import sys
import pandas as pd
import pandas as pd

df = pd.read_csv(sys.stdin, parse_dates=['Date'], date_format="%Y-%m-%d").set_index("Date")
name = df.columns[0]
df[name] = df[name].apply(lambda x: float(x.replace(",","")))
print(df.to_csv(date_format="%Y-%m"))