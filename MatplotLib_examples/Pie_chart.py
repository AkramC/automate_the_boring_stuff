from matplotlib import pyplot as plt

slices=[7,3,4,5]
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=180,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%'

      )

plt.title("Pie Chart")
plt.savefig('piedraw.png')
plt.show()