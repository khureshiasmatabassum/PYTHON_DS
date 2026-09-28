import pandas as pd
data = {
"Department": ["BCA", "BCA", "BBA", "BBA", "BCA"],
"Student": ["Rahul", "Aman", "Priya", "Neha", "Rohan"],
"Marks": [80, 70, 90, 85, 75]
}
df = pd.DataFrame(data)
print("Student Data:")
print(df)
average_marks=df.groupby("Department")["Marks"].mean()
print("\nAverage Marks by Department:")
print(average_marks)




import pandas as pd
data = {
"Department": ["BCA", "BCA", "BBA", "BBA", "BCA"],
"Marks": [80, 70, 90, 85, 75]
}
df = pd.DataFrame(data)
result = df.groupby("Department")["Marks"].agg(
["count", "mean", "min", "max", "sum"]
)
print(result)




import pandas as pd
df1 = pd.DataFrame(
{
"Name": ["Rahul", "Aman"],"Marks": [80, 75]
})
df2 = pd.DataFrame(
{
"Name": ["Priya", "Neha"],"Marks": [90, 85]
})
result = pd.concat([df1, df2], ignore_index=True)
print("First DataFrame:")
print(df1)
print("\nSecond DataFrame:")
print(df2)
print("\nConcatenated DataFrame:")
print(result)



import pandas as pd
students = pd.DataFrame(
{
"ID": [1, 2, 3],"Name": ["Rahul", "Aman", "Priya"]
})
marks = pd.DataFrame(
{
"ID": [1, 2, 3],"Marks": [85, 72, 91]
})
result = pd.merge(students, marks, on="ID")
print("Students:")
print(students)
print("\nMarks:")
print(marks)
print("\nMerged Data:")
print(result)
