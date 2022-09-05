def swap(b,j,k):
    b[j],b[k]=b[k],b[j]
a={2: 2, 5: 4, 1: 3, 20: 1}
b=list(a.items())
n=len(a)
for l in range(1,n):
    for j in range(0,n-l):
        i=1
        k=j+1
        if(b[j][i]<b[k][i]):
            swap(b,j,k)       
print(b)
