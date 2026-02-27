import pandas as pd

df = pd.read_csv("students.csv")

print("Single Column:","\n", df["name"], "\n")
print("Multiple Columns:","\n", df[["score", "passed"]], "\n")

print("First 3 rows with iloc:","\n", df.iloc[0:3], "\n")

df.index = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print("Using loc:","\n", df.loc["a"],"\n")

print("High Performing Students:", "\n", df[df["score"] > 85], "\n")

print("High Performing Students and Result:", "\n")
result = df[(df["score"] > 85) & (df["passed"] == True)]
print(result, "\n")

sorting = result.sort_values(["score"] , ascending = False)
print("Sorted Result:" , "\n",sorting, "\n")

chained = df[(df["score"] > 70) | ~(df["category"] == "C")] \
            .sort_values(["score"], ascending = False)
print("Chained Operation:" , "\n" ,chained, "\n")


# I added CSV file from main folder to this assginment folder