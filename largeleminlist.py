a=[1222,2,56,47,96,344,111]
n=len(a)
small=a[0]
for i in range(0,n):
    if(a[i]<small):
        small=a[i]
print(small)