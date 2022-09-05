for i in range(1,2000):
    a=str(i)
    temp=0
    n=len(a)
    for j in range(0,n):
        b=int(a[j])**n
        temp+=b
    if(temp==int(a)):
        print(a,"is a armstrong number")