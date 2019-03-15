import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.legend import Legend

rec1=Rectangle((0.1,0),0.1,0.3,label='Day1')
rec2=Rectangle((0.3,0),0.1,0.6,label='Day2')
rec3=Rectangle((0.5,0),0.1,0.9,label='Day3')

fig,ax=plt.subplots()

ax.add_patch(rec1)
ax.add_patch(rec2)
ax.add_patch(rec3)

colors=['red','black','green']

for x,c in zip(ax.patches,colors):
    x.set_color(c)
#ax.legend()
handles,labels=ax.get_legend_handles_labels()
legend=Legend(ax,handles=handles,labels=labels)
ax.add_artist(legend)
#ax.legend()
plt.show()