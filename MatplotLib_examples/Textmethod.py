from matplotlib import  pyplot as plt
from matplotlib.text  import Text
from matplotlib.patches import FancyBboxPatch
txt1=Text(x=0.5,y=0.5,text='dude')
txt2=Text(x=0.2,y=0.4,text="The other dude")
fig,ax=plt.subplots()

t1=ax._add_text(txt1)
t2=ax._add_text(txt2)

t1.set_color('red')
t1.set_size(24)
t1.set_alpha(0.8)
t1.set_family('sans-serif')
t1.set_rotation(45)
t1.set_style('italic')
t1.set_weight('bold')
t1.set_bbox(dict(facecolor='black',boxstyle='darrow',alpha=0.7))

plt.show()