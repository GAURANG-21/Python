import matplotlib.pylab as plt

fobj = plt.figure(figsize=(10,10), facecolor='r')
fobj.patch.set_alpha(0.5)

sobj1 = fobj.add_subplot(1,2,1)
v = [0.04,0.08,0.14,0.22,0.26,0.34]
i = [2.11,2.42,2.44,2.73,2.90,3.25]
sobj1.plot(v,i,color='c', linewidth=0.4,linestyle='dotted', marker='o')
sobj1.set_title("Experiment")
sobj1.set_ylabel("Current")
sobj1.set_xlabel("Voltage")


sobj2 = fobj.add_subplot(1,2,2)
v = [0.04,0.08,0.14,0.22,0.26,0.34]
i = [2.11,2.42,2.44,2.73,2.90,3.25]
sobj2.plot(v,i,color='c', linewidth=0.4,linestyle='dotted', marker='o')
sobj2.set_title("Experiment")
sobj2.set_ylabel("Current")
sobj2.set_xlabel("Voltage")

plt.show()