import pandas as pd
data = { 
"Name": ["A", "B", "C", "D", "E", "F"], 
"City": ["Rajahmundry", "Hyderabad", "Chennai", 
"Hyderabad", "Rajahmundry", "Chennai"], 
"Department": ["IT", "HR", "IT", "Finance", "IT", "HR"], 
"Salary": [25000, 40000, 35000, 45000, 50000, 30000], 
"Experience": [1, 3, 2, 5, 6, 2] 
} 
df = pd.DataFrame(data)
print(df)
result = df[df["Salary"] > 35000]
print(result)
result = df[df["City"] == "Hyderabad"]
print(result)
result = df[(df["City"] == "Hyderabad") & (df["Salary"] > 35000)]
print(result)
result = df.sort_values(by="Salary", ascending=False)
print(result)
average_salary = df["Salary"].mean()
print(average_salary)
result = df.groupby("Department")["Salary"].mean()
print(result)
result = df.groupby("Department")["Salary"].max()
print(result)
result = df["City"].value_counts()
print(result)
df["AnnualSalary"] = df["Salary"] * 12
print(df)
df["ExperienceLevel"] = df["Experience"].apply(
    lambda x: "Senior" if x >= 5 else "Junior"
)

print(df)