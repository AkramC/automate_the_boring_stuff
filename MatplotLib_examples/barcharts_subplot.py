import matplotlib.pyplot as plt
import  pandas as pd

df=pd.read_csv('barcharts-us-music-sales-by-genre.csv',index_col='Year')
ax1,ax2 = df[['Jazz','Rock']].plot.bar(subplots=True)
fig3=plt.gcf()
fig3.set_size_inches(12,4)
plt.show()