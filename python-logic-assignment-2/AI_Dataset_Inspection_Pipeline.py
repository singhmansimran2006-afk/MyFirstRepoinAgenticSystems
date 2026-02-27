import pandas as pd

df = pd.read_csv("employee.csv")

a = df.head()
print("First 5 Rows:" ,"\n", a, "\n")

b = df.tail()
print("Last 5 Rows:" ,"\n", b, "\n")

print("Information:")
print(df.info(), "\n")

d = df.describe()
print("Description:" , "\n", d, "\n")

single_column = df["name"]
print("Name Column: ", "\n", single_column, "\n")

multiple_columns = df[["age" , "department"]]
print("Age and Department:", "\n", multiple_columns, "\n")

filtering = df[df["age"] > 30]
print("Filtered:", "\n", filtering, "\n")

# I added CSV file from main folder to this assginment folder