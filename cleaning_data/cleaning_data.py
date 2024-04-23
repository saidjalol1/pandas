import pandas as pd

data =  "data.csv"

df = pd.read_csv(data)

# new_df = df.fillna(130) # dropna returs new DataFrame by defoult, inplace attibute returns the original  DataFrame 

df["Calories"].fillna(130,inplace=True)
print(df)