import main

while(True):
    n = int(input("Enter choice: "))
    if(n==1):
        main.initialize();
    elif(n==2):
        main.show();
    elif(n==3):
        main.modify()
    elif(n==0):
        break;
    else:
        print("Wrong choice entered\n")



