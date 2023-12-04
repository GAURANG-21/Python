l1 = list(int(x) for x in input("Enter numbers seperated by spaces: ").split())

def reverse_num(val):
    l = []
    for i in range(len(val)):
        x = val[i];
        rev = 0;
        while(x!=0):
            rev = (rev*10)+(x%10)
            x = x//10
        l.append(rev)
    return l;

print(reverse_num(l1))