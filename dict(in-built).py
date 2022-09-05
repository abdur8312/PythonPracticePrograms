#A=[]
#n=int(input("Enter range:"))
# for i in range(n):
#     a=input("Enter the values:")
#     A.append(a)
#A=[1,1,2,2,2,2,5,5,5]
A=[2,2,5,5,5,5,1,1,1,20]
value=None
mydict={}
for i in range(len(A)):
    if(A[i] in mydict):
        value=mydict.get(A[i])
        value+=1
        key=A[i]
        mydict[key]=value
    else:
        key=A[i]
        value=1
        mydict[key]=value
print(mydict)


# def swap(b,j,k):
#     b[j],b[k]=b[k],b[j]
# b=list(mydict.items())
# n=len(mydict)
# for l in range(1,n):
#     for j in range(0,n-l):
#         i=1
#         k=j+i
#         if(b[j][i]<b[k][i]):
#             swap(b,j,k)
# print(b)
# for m in range(n):
#     print(b[m][0])


#5,2,1 (by key)
#4,3,2(by value)
#2:4,5:3,1:2(by key&value)
#5:4,1:3,2:2,20:1
#5,1,2,20