import matplotlib.pylab as plt
import numpy as np
mp = {"INC": 114, "BJP": 15, "Independent": 4, "Others": 3}
raj = {"INC": 99, "BJP": 73, "Independent": 3, "Others": 14}

fobj = plt.figure(figsize=(10,10), facecolor='r')
fobj.patch.set_alpha(0.5)

sobj1 = fobj.add_subplot(2,2,1)
plt.title("Madhya Pradesh", fontsize = 15)
plt.pie([x for x in mp.values()], labels=[x for x in mp.keys()], autopct="%0.1f%%", explode = [0.2,0,0,0])

sobj2 = fobj.add_subplot(2,2,2)
plt.title("Rajasthan", fontsize = 15)
plt.pie([x for x in raj.values()], labels=[x for x in raj.keys()], autopct="%0.1f%%")

sobj3 = fobj.add_subplot(2,2,3)
width = 0.3
p= np.arange(len(mp))
p1=[j+width for j in p]
plt.bar(p,[x for x in mp.values()],width, color='c', alpha=0.5)
plt.bar(p1,[x for x in raj.values()], width, color='g', alpha= 0.5)
plt.xticks(p+width/2,[ x for x in mp.keys()])

plt.show()