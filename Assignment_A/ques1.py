# import numpy as np
# def Create_Array(*args):
#     n = len(args)
#     arr = np.zeros((n,n), dtype='i');
#     for i in range(n):
#         arr[i,i] = args[i]
#     return arr
# print(Create_Array(1,2,3,4))

import numpy as np
def Create_Array(li):
    arr = np.diag(li)
    return arr
print(Create_Array([2,3,4,5,6,7]))
    