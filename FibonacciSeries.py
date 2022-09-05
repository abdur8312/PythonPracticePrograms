n = 10#int(input("Enter N value:"))
if(n <= 0):
    print("Enter a positive number")
elif(n == 1):
    print("0")
elif(n >= 2):
    n1,n2 = 0,1
    for i in range(n):
        print(n1,end=" ")
        count = n1 + n2
        n1,n2 = n2,count
        