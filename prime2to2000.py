for i in range(2,2000):
    a=i
    if(a==2):
        print("not prime number")
    if(a>2):
        for j in range(2,a):
            b=a%j
            if(b==0):
                break
        if(b==0):
            print("Not a prime number")
        else:
            print("prime number")
            
            
            
