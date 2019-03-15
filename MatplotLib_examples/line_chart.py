import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#np.random.seed(44)
#x=np.linspace(10,24,10)
#y=np.random.randn(10)

df=pd.read_csv('iris.csv')

fig,ax=plt.subplots(figsize=(12,4))

ax.plot('Sepal length',data=df , label='Sepal')
ax.plot('Petal length',data=df,label='Petal')
ax.legend()

ax.set_title('Iris')
ax.set_xlabel('Index',size=14)
ax.set_ylabel('Length',size=14)
ax.tick_params(axis='both',labelsize=12,labelcolor='green')

line1=ax.lines[0]
line1.set(marker='o',markevery=5,markerfacecolor='white')
legend=ax.legend_
legend.set_bbox_to_anchor([0.2,0.7])
legend.legendPatch.set_boxstyle('round,pad=0.5,rounding_size=1')
f1=legend.get_lines()[0]
f1.set_marker('o')


val = df['Petal length'].values
p_min=val.min()
p_max=val.max()
x_min=val.argmin()
x_max=val.argmax()
ax.axvline(x_min,color='red',ls='dashed')
ax.axvline(x_max,color='blue',ls='dashed')

min_annote=ax.annotate(str(p_min),xy=(x_min,p_min),xytext=(x_min+10,p_min+2),arrowprops=dict(arrowstyle='->'))
min_annote.set(size=22,color='green')
min_annote.set_bbox(dict(facecolor='red',boxstyle='round,pad=0.4',lw=0))
plt.show()