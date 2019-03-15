from matplotlib import pyplot as plt
from matplotlib import style

plt.bar([1,3,4,2,5],[5,2,4,3,5],label='Example One')
plt.bar([1,4,2,1,3],[3,2,4,2,1],label='Example Two',color='g')
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Info")
plt.show()
