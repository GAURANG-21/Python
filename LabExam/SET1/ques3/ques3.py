import numpy as np
import math
import matplotlib.pylab as plt

n = int(input("Enter n: "))
k = int(input("Enter number of values: "))

arr = list(np.random.randint(10, n, k))

def primes(n):
    count = 0
    for i in range(2,n):
        if(n%i==0):
            count = count+1
            if(count>2):
                return False
    return True

def c_p(arr):
    composite = []
    prime = []
    for x in arr:
        if(primes(x)):
            prime.append(x);
        else:
            composite.append(x);
    l = []
    l.append(composite)
    l.append(prime)
    return l

arr = c_p(arr)
composite = arr[1]
prime = arr[0]

squares = list(map(lambda x: x*x, prime))
square_root = list(map(lambda x: math.sqrt(x), composite))

fobj = plt.figure(figsize=(10,10), facecolor='r')
fobj.patch.set_alpha(0.5)

sobj1 = fobj.add_subplot(1,2,1)
plt.scatter(prime, squares,marker='D')

sobj2 = fobj.add_subplot(1,2,2)
plt.scatter(composite, square_root, marker="o")

plt.show()