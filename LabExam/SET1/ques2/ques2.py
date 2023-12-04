import numpy as np
import matplotlib.pylab as plt

n = int(input("Enter value of n: "))
user = np.array([int(x) for x in input("Enter n*n numbers: ").split()]).reshape((n, n))
generated = np.random.randint(10, 100, n * n).reshape(n,n)
print(f"User: {user}")
print(f"Generated: {generated}")

user_new = user[np.mod(user, 5) == 0]
generated_new = generated[np.mod(generated, 4) == 0]
print(f"User_new: {user_new}")
print(f"Generated_New: {generated_new}")

row = np.concatenate([user,generated], axis=0)
column = np.concatenate([user,generated], axis = 1)

print(f"Row Concatenation: {row}")
print(f"Column Concatenation: {column}")

print(user.flatten())
fobj = plt.figure(figsize=(10,10), facecolor='r')
fobj.patch.set_alpha(0.5)

sobj1 = fobj.add_subplot(1,2,1)
plt.plot(user.flatten(), color='c')

sobj2 = fobj.add_subplot(1,2,2)
plt.plot(generated.flatten(), color='c')

plt.show()
