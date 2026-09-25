import pandas as pd
data = { 
"Employee": ["A", "B", "C", "D", "E", "F"], 
"Department": ["IT", "HR", "IT", "Sales", "HR", "IT"], 
"Salary": [40000, 30000, 50000, 35000, 32000, 60000], 
"Experience": [2, 1, 4, 3, 2, 6] 
} 
df = pd.DataFrame(data) 
print(df)
result = df[df["Salary"] > 40000] 
print(result)
mean_salary = df["Salary"].mean()
print(mean_salary)
max_salary = df["Salary"].max()
print(max_salary)
df.loc[df["Salary"].idxmax(), "Salary"] = 70000
print(df)
result = df.groupby("Department")["Salary"].mean()
print(result)
print(df["Department"].value_counts())
print(df[df["Experience"] > 3])
df["AnnualSalary"] = df["Salary"] * 12
print(df)