#MAKING THE VERTICAL BARGRAPH

# import matplotlib.pylab as plt
# import numpy as np
# fobj = plt.figure(figsize=(10,10), facecolor='c')

# x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
# high = [32,32,22,22,32,30,30,30,30,30,31,31]
# low = [23,23,24,25,24,24,24,24,24,24,23,22]

# width = 0.4
# p = np.arange(len(x))
# p1 = [j+width for j in p]

# plt.bar(p,high,width,color='r', label='high')
# plt.bar(p1,low,width,color='g', label= 'low')

# plt.xticks(p+width/2,x, rotation=20)

# plt.legend()
# plt.show()


# MAKING THE HORIZONTAL BARGRAPH
# import matplotlib.pylab as plt
# import numpy as np
# fobj = plt.figure(figsize=(10,10), facecolor='r')
# fobj.patch.set_alpha(0.5)

# y=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
# high = [32,32,22,22,32,30,30,30,30,30,31,31]
# low = [23,23,24,25,24,24,24,24,24,24,23,22]

# width=0.4
# p = np.arange(len(y))
# p1=[j+width for j in p]

# plt.barh(p,high,width,color='c')
# plt.barh(p1,low,width, color='g', alpha=0.5)

# plt.yticks(p+width/2,y)

# plt.show();



#USING SUBPLOTS FOR MAKING THE HORIZONTAL AND VERTICAL GRAPHS SIDE-BY-SIDE
# import matplotlib.pylab as plt
# import numpy as np
# fobj = plt.figure(figsize=(15,15), facecolor='r')
# fobj.patch.set_alpha(0.5)
# fobj.suptitle("City X Temperature")

# x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
# high = [32,32,22,22,32,30,30,30,30,30,31,31]
# low = [23,23,24,25,24,24,24,24,24,24,23,22]

# sobj1 = fobj.add_subplot(1,2,1)
# sobj1.set_title("Vertical graph")
# width = 0.4
# p= np.arange(len(x))
# p1=[j+width for j in p]
# plt.bar(p,high,width, color='c', alpha=0.5)
# plt.bar(p1,low,width, color='g', alpha=0.5)
# plt.xticks(p+width/2,x)

# sobj2 = fobj.add_subplot(1,2,2)
# sobj2.set_title("Horizontal graph")
# width = 0.4
# p= np.arange(len(x))
# p1=[j+width for j in p]
# plt.barh(p,high,width, color='c', alpha=0.5)
# plt.barh(p1,low,width, color='g', alpha=0.5)
# plt.yticks(p+width/2,x)

# plt.show()