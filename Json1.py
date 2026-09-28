#java script on notation

import pandas as pd
data = {
"Name": ["Rahul", "Aman", "Priya"],"Marks": [85,
72, 91]
}
df = pd.DataFrame(data)
df.to_json("students.json", orient="records", indent=4)
print("JSON file created successfully.")
new_df = pd.read_json("students.json")
print("\nData read from JSON:")
print(new_df)