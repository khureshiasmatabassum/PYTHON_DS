import pandas as pd
d1={
"name":["jaya","asma","sudha"],
"age":[28,60,80]
}
d2=pd.DataFrame(d1)
print(d2)
print(d2["age"].mean())