from matplotlib import pyplot as plt
from matplotlib.text import Annotation

annot = Annotation('Dude', xy=(0.2,0.2),xytext=(0.5,0.8),arrowprops=dict(arrowstyle='->',color='r',lw=2))

fig,ax=plt.subplots()
an1=ax._add_text(annot)
an1.set_bbox(dict(facecolor='red',boxstyle='circle',ls='dashed',lw=2))
an1.set_size(14)
arrow=an1.arrow_patch
arrow.set_linewidth(2)
arrow.set_arrowstyle('-[')
plt.show()
