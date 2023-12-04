from numpy import linalg as ld
import numpy as np

sol = np.array([[2488],[2852]])
print(sol)

arr = np.array([[30,26],[35,51]])
print(arr)

arr = ld.inv(arr)
print(arr)

print(arr@sol)
arr = np.matmul(arr,sol)
print(arr)