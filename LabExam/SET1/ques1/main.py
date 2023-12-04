def my_zip(empName, empCode, empSalary, homog):
    l = []
    if(len(empCode)==len(empName)==len(empSalary)):
        homog = True
    if(homog):
        for i in range(len(empCode)):
            l.append(tuple((empName[i], empCode[i], empSalary[i])));
    else:
        for i in range(min(len(empName),len(empCode),len(empSalary))):
            l.append(tuple((empName[i], empCode[i], empSalary[i])));
    return l

def sort(empName, empCode, empSalary, val):
    for i in range(len(val)):
        for j in range(len(val)-i-1):
            if(val[j][2]>val[j+1][2]):
                val[j],val[j+1] = val[j+1], val[j]
    print(val);
    
empName = list(x for x in input("Enter names: ").split());
empCode = list(int(x) for x in input("Enter code: ").split());
empSalary = list(int(x) for x in input("Enter salary: ").split());
print(empName,empCode,empSalary)
t = my_zip(empName, empCode, empSalary, False)
sort(empName, empCode, empSalary, t)