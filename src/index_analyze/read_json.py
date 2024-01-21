import sys
import pandas as pd

df = pd.read_json(sys.stdin)
print(df)