import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('barchart-divorcerates.csv')

fig,ax=plt.subplots(figsize=(12,4))
w,l,v= ax.pie(x='Women',labels='Age',data=df,autopct='%1.1f%%',explode=(0,0,0,0.1,0))
ax.legend(bbox_to_anchor=(0,1),loc=1)

ax.set_aspect('equal')
'''for t in ax.texts:
    t.set_color('white')
    t.set_size(11)
colors=['red','blue','green','orange','yellow']

for w,c in zip(ax.patches,colors):
    w.set_facecolor(c)
    w.set_ls('dotted')
    w.set_edgecolor('white')
    w.set_lw(2)'''

#to add circle in middle donout chart

from matplotlib.patches import Circle

circle=Circle((0,0),0.3,facecolor='white')
ax.add_artist(circle)
plt.show()