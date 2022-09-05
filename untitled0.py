#ZOHO - Q1
# n = int(input("Enter no.of elements in array:"))
# a = []#[3,6,4,8,5,5]
# for i in range(n):
#     b = int(input("Enter value:"))
#     a.append(b)
# print(a)
# Sum = a[0]
# for i in range(1,n):
#     if(a[i]%2 != 0 and a[i-1]%2 == 0):
#         continue
#     else:
#         Sum += a[i]
# print(Sum)

#ZOHO - Q2
a = [1,2,3,4]
unique = max(a)
n = len(a)
one = 0
for i in range(n):
    one += a[i]*2
    if(one <= unique):
        print(unique)
    else:
        print("-1")
    one = 0
    
    



    