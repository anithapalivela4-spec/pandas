import pandas as pd 
data = { 
"Name": ["Anu", "Binnu", "Kalyani", "Reshma", "Anitha"], 
"Age": [17, 19, 21, 24, 18], 
"City": ["Rajahmundry", "Hyderabad", "Chennai", "Rajahmundry", "Hyderabad"], 
"Salary": [25000, 45000, 30000, 35000, 55000], 
"Department": ["IT", "HR", "IT", "Finance", "IT"] 
} 
df = pd.DataFrame(data) 
print(df)
result = df[df["Salary"] > 30000] 
print(result)
result = df[ 
(df["Salary"] > 30000) & 
(df["Department"] == "IT") 
] 
print(result) 
result = df[ 
(df["City"] == "Hyderabad") | 
(df["City"] == "Rajahmundry") 
] 
print(result)
result = df[df["City"].isin(["Hyderabad", "Chennai"])] 
print(result)
df.sort_values("Salary") 
df.sort_values("Salary", ascending=False) 
df.sort_values( 
["Department", "Salary"], 
ascending=[True, False] 
)
df["Bonus"] = df["Salary"] * 0.10 
print(df)
df["TotalSalary"] = df["Salary"] + df["Bonus"] 
print(df)
import numpy as np 
df["Level"] = np.where( 
df["Salary"] >= 40000, 
"Senior", 
"Junior" 
) 
print(df) 
result = df.groupby("Department")["Salary"].mean() 
print(result) 
result = df.groupby("Department")["Salary"].agg( 
["count", "sum", "mean", "min", "max"] 
) 
print(result)
result = df.groupby("City")["Salary"].mean() 
print(result)
result = df.groupby( 
["City", "Department"] 
)["Salary"].mean() 
print(result) 
print(df["Department"].value_counts())
print(df["City"].value_counts())
data = { 
"Name": ["Anu", "Binnu", "Kalyani", "Reshma"], 
"Age": [17, None, 21, 24], 
"Salary": [25000, 45000, None, 35000] 
} 
df = pd.DataFrame(data) 
print(df)
print(df.isnull())
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean()) 
df["Salary"] = df["Salary"].fillna(0)
df.drop_duplicates() 
df.drop_duplicates(subset=["Name"]) 
df.rename( 
columns={ 
"Salary": "MonthlySalary", 
"Age": "EmployeeAge" 
}, 
inplace=True 
) 
print(df) 
print(df.iloc[0]) 
print(df.loc[:, ["Name", "MonthlySalary"]])
result = df.loc[df["MonthlySalary"] > 30000] 
print(result)
print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[0:3, 0:2])