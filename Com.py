import pandas as pd 
df = pd.read_csv("ECommerce.csv")
print(df)
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print(df["Product"])
print(df.loc[0])
print(df.loc[df["Price"].idxmax()])
print(df.loc[df["Price"].idxmin()])
print(df["Rating"].mean())
print(df.groupby("Category")["Product"].count())

df["Inventory Value"] = df["Price"] * df["Quantity"]
print(df["Inventory Value"].sum())