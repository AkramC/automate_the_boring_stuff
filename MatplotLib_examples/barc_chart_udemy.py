import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('barcharts-us-music-sales-by-genre.csv',index_col='Year')
fig,ax=plt.subplots(figsize=(12,4))
width=0.3
rock=ax.bar(df.index,'Rock',data=df,label='Rock %',width=width)
jazz=ax.bar(df.index+width,'Jazz',data=df,label='Jazz %',width=width)
ax.set_xticks(df.index+width/2)
ax.set_xticklabels(df.index)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.xaxis.set_ticklabels(df['Year'].values)

for p in rock.patches:
    t=ax.annotate(str(p.get_height())+'%',(p.get_x(),p.get_height()+2))
    t.set(color='black',size=8)
    t.set_bbox(dict(facecolor='white',boxstyle='circle',lw=1,edgecolor='red'))
plt.show()