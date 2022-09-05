def Pyramid(n):
    for i in range(0,n,2):
        a=n-(i+1)
        for j in range(0,a):
            print(" ",end="")
        for k in range(0,i+1):
            print(" *",end="")
        print("\r")
n=9
Pyramid(n)
