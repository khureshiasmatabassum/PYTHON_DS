import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df={
         "marks":[10,20,30],
         "name":['A','B','C']
}
c=pd.DataFrame(df)
#sns.lineplot(x="marks",y="name",data=df,linestyle="--")
#sns.barplot(x="marks",y="name",data=df,linestyle="--")
#sns.boxplot(x="marks",y="name",data=df,linestyle="--")
sns.scatterplot(x="marks",y="name",data=df,linestyle="--")
plt.show()