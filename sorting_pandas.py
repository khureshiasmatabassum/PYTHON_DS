import pandas as pd

data = {
    "name": ["rahul", "aman", "priya", "neha", "rohan"],
    "marks": [85, 72, 91, 88, 76]
}

df = pd.DataFrame(data)

#result = df[df["marks"] >= 80]
df["result"] = df["marks"] >=50
#print("Students scoring 80 or more:")
#print(result)
print(df)
df["bonus"] = 5
df["final marks"] = df["marks"] + df["bonus"]
print(df)
df["college"] = "AP"
print(df)
df = df.drop("result",axis=1)
print("\nAfter Removing Result:")
print(df)
df = df.drop("bonus",axis=1)
print("\nAfter Removing bonus:")
print(df)
df = df.drop("college",axis=1)
print("\nAfter Removing college:")
print(df)
df["college"] = "AP"
print(df)
df.insert(0,"Date", "01-Aug-2026")
print(df)
sorted_df = df.sort_values("marks", ascending=False)
print("Students sorted by marks:")
print(sorted_df)
print(df.describe())