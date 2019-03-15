from matplotlib import pyplot as plt
from matplotlib import  style

populatiion_ages=[22,55,62,45,34,44,44,33,23,21,43,55,33,22,13,44,22,45,102,105,108]
bins =[0,10,20,30,40,50,60,70,80,90,100,110]
plt.hist(populatiion_ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Histogram")
plt.show()