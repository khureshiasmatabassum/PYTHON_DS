import pandas as pd
import numpy as np
data = {
"name":["rahul","aman","priya","neha"],
"marks":[85,np.nan,91,np.nan]
}
df=pd.DataFrame(data)
print("student data:")
print(df)
print("\nmissing values:")
print(df.isnull())
print("\nnumber of missing values:")
print(df.isnull().sum())
clean_data = 