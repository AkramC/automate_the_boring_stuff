import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('df-weed.csv')
fig,ax=plt.subplots(figsize=(15,3))
#ax.hist('HighQ',data=df,bins=50,alpha=1)
df.plot.hist(ax=ax,alpha=0.7,bins=20)
bc=ax.containers[0]
for b in bc.patches:
    b.set_facecolor('red')
ax.legend()

plt.show()