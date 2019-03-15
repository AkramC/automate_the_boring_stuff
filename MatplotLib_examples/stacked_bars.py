import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('barcharts-us-music-sales-by-genre.csv',index_col='Year')
fig,ax=plt.subplots(figsize=(12,4))
df[['Country','Rock','Jazz']].plot.bar(stacked=True,rot=0,ax=ax)
plt.show()