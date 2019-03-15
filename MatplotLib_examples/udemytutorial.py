from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

#rec1 = Rectangle((0.7,0),0.2,0.8)
#rec2= Rectangle((0.2,0),0.2,0.6)

#fig,ax = plt.subplots()
#ax.add_patch(rec1)
#ax.add_patch(rec2)
#plt.show()

np.random.seed(14)
x=list(range(1,6))
y=np.linspace(2,10,5)

fig,ax = plt.subplots()

def makeBars(ax,x,y,w):
    for x,y in zip(x,y):
        bar = Rectangle((x,0),w,y)
        ax.add_patch(bar)

makeBars(ax,x,y,0.4)
ax.autoscale()
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
fig.set_size_inches(10,5)

for r in ax.patches :
    r.set_edgecolor('g')
    r.set_ls('dashed')
    r.set_lw(3)
    r.set_hatch('\\')

makeBars(ax,x,y,0.8)

rec_id=range(10)
zorder=reversed(rec_id)

for r,z in zip(rec_id,zorder):
    ax.patches[r].set_zorder(z)

plt.show()