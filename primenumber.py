a=int(input("Enter a number:"))
b=None
if(a==1):
    print("1 is not a prime number according to google")
if(a==2):
    print("prime number")
if(a>2):
    for i in range(2,a):
        b=a%i
        if(b==0):
            break
    if(b==0):
        print("not a prime number")
    else:
        print("prime number")