import numpy as np

def array_form(n):
    arr= np.arange(1,n*n*2,2).reshape(n,n)
    return arr

def return_diag(arr):
    li = []
    for i in range(len(arr)):
        li.append(arr[i,i])
    return np.array(li)

n = int(input("Enter n: "))
arr = array_form(n)
print(arr)
arr = return_diag(arr)
print(arr)