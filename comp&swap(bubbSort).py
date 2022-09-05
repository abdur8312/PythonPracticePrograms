def swap(a,i,j):
    if(a[i]>a[j]):
        a[i],a[j]=a[j],a[i]
a=[10,2,6,7]
n=len(a)
for i in range(0,n):
    i,j=i,i+1
    if(j==5):
        break
        swap(a,i,j) 
for i in range(0,3):
    i,j=i,i+1
    if(j==4):
        break
    swap(a,i,j)
for i in range(0,2):
    i,j=i,i+1
    if(j==3):
        break
    swap(a,i,j)
print(a)

