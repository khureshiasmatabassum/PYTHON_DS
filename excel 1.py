import pandas as pd
data = {
"Name": ["Rahul", "Aman", "Priya"],"Marks": [85, 72, 91]
}
df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)
print("Excel file created successfully.")
new_df = pd.read_excel("students.xlsx")
print("\nData read from Excel:")
print(new_df)