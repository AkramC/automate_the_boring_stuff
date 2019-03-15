import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import StrMethodFormatter

df=pd.read_csv('index.csv',index_col='Year')
a='Federal Funds Target Rate'
b='Unemployment Rate'
fig,ax=plt.subplots(figsize=(12,4))
p=ax.scatter(a,b,data=df)

mf=StrMethodFormatter("{x} %")
ax.xaxis.set_major_formatter(mf)
ax.yaxis.set_major_formatter(mf)


p.set_alpha(0.5)
p.set_sizes(df[a].dropna()**2.8)
p.set_color(['white','yellow'])
plt.show()