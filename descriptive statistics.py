import pandas as pd
marks = [65, 70, 75, 80, 85, 90, 72, 68, 88, 95]
df = pd.DataFrame({"Marks": marks})
print(df.describe())