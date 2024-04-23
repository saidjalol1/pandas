import pandas as pd

data = "../pandas_csv/customers-100.csv"

df = pd.read_csv(data)

print(df.head(10)) # returns the specified number of rows from the top
print(df.tail()) # returns 5 rows from the bottom, if the numbers of rows is specified it returns them
print(df.info()) # gives the info about the dataset

