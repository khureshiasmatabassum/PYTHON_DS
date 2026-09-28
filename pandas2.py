import pandas as pd
d1={
'name':['radha','jaya','sudha','pras','bharathi'],
'age':[100,200,300,400,500]
}
d2=pd.DataFrame(d1)
print(d2)
print()
print(d2['age'].mean())
print(d2.shape)
print(d2.columns)
print(d2.index)
print(d2.dtypes)
print(d2.size)
print(d2.head(2))
print(d2.tail(2))