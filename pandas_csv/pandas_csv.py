import pandas as pd

pd.options.display.max_rows = 105
pd.options.display.max_columns = 25

data = pd.read_csv("customers-100.csv")

print(data)
# print()