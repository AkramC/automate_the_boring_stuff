import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');
fig.savefig('my_figue.png')
plt.show()