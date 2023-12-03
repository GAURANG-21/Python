from cmath import inf


# li = [1,2,3,4,5]
# se = {2,3,4,5,6}
# tu = (3,4,5,6,7)

def sumi(var):
    sum = 0
    for i in range(len(var)):
        sum = sum + var[i];
    return sum;

def maxi(var):
    maximum = -inf
    for i in range(len(var)):
        if(maximum<var[i]):
            maximum = var[i];
    return maximum

def mini(var):
    minimum = inf
    for i in range(len(var)):
        if(minimum>var[i]):
            minimum = var[i]
    return minimum

if(__name__ == "__main__"):
    print("my_module is now available");
else:
    print("Not my module")
    
# print(sum(li))
# print(sum(list(se)))
# print(sum(tu))
