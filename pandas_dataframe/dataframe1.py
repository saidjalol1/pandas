import pandas as pd


data = {
    "calories" :  [420, 380, 390],
    "durations" : [380, 390, 360]
}

df = pd.DataFrame(data) # with index argument we cn specify the custom index to every rows
print(df)
print(df.loc[[0, 0]]) 

