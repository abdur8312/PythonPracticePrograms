
#if(a[0]>a[1]):
 #   swap(a,0,1)
#if(a[1]>a[2]):
 #   swap(a,1,2)
#if(a[2]>a[3]):
#     swap(a,2,3)

# if(a[0]>a[1]):
#     swap(a,0,1)
# if(a[1]>a[2]):
#     swap(a,1,2)

# if(a[0]>a[1]):
#    swap(a,0,1)
    
# for i in range(0,n-1):
#     j=i+1
#     if(a[i]>a[j]):
#         swap(a,i,j)
# for i in range(0,n-2):
#     j=i+1
#     if(a[i]>a[j]):
#         swap(a,i,j)
# for i in range(0,n-3):
#     j=i+1
#     if(a[i]>a[j]):
#         swap(a,i,j)

def swap(a,j,k):
        a[j],a[k]=a[k],a[j]
a=[28,27,99,199,6,13,299,10]
n=len(a)
for i in range(1,n-1):
    for j in range(0,n-i):
        k=j+1
        if(a[j]>a[k]):
            swap(a,j,k)
print(a)
        