import pandas as pd
import numpy as np

data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
print(df,"\n")


print("Missing Data:\n",df.isnull(),"\n")


mean = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean)
print("Filling missing values with mean:\n",df,"\n")


drop = df.drop(columns=["Temporary_Notes"])
print("Dropped Temporary_Notes column:\n",drop,"\n")


rename = df.rename(columns={"Salary" : "Annual_Salary"})
print("Rename of column Salary:\n", rename, "\n")


summary = df.groupby("Department").agg({
    "Salary" : ["mean"],
    "Employee" : ["count"]
})
print("Final summary:\n", summary, "\n")
