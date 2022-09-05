def LeftStairCase(n):
    for i in range(0,n):
        a=n-(i+1)
        for j in range(0,a):
            print(" ",end="")
        for k in range(0,i+1):
            print(" *",end="")
        print("\r")
n =5
LeftStairCase(n)
