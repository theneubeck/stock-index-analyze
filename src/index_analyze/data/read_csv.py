import sys
import pandas as pd
import pandas as pd

df = pd.read_csv(sys.stdin, parse_dates=['Date'], date_format="%b %d, %Y")
print(df)