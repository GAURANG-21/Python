a =0
b=0
c=0
d=0
e =0
contr =0

def initialize():
    global a,b,c,d,e,contr
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    d=int(input("Enter d: "))
    e=int(input("Enter e: "))
    contr = a + 10*b*c-5*d/e
    return contr

def show():
    print(f"a: {a}, b:{b}, c:{c}, d:{d}, e:{e}, contr: {contr}")

def modify():
    global a,b,c,d,e,contr
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    d=int(input("Enter d: "))
    e=int(input("Enter e: "))
    contr = a + 10*b*c-5*d/e
    return contr
    
    