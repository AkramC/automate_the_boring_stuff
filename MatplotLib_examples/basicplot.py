import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
import numpy as np

fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
plt.plot(x,np.sinc(x),color='lightblue',linestyle='-.')
plt.plot(x,np.sinc(x),'-.b')
plt.xlim(-1,11)
plt.ylim(-1.5,1.5)
plt.axis('tight')
#ax.plot(x,np.sinc(x))
plt.show()