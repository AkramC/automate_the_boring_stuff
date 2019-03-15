from matplotlib import  pyplot as plt
from matplotlib import style

style.use("ggplot")

plt.plot([1,2,3],[4,5,1],'y',label='line one',linewidth=5)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Info")
plt.legend()
plt.grid(True,color='c')
plt.show()