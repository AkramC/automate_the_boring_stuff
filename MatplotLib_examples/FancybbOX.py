from matplotlib import  pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

x=list(range(1,5))
y = x
fig,ax = plt.subplots(figsize=(15,5))

def makeFancyBBox(ax,x,y,w):
    for x,y in zip(x,y):
        fbox=FancyBboxPatch((x,0),w,y,boxstyle='round')
        ax.add_patch(fbox)

makeFancyBBox(ax,x,y,0.3)
ax.autoscale()
plt.show()

