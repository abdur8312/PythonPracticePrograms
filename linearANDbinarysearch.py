def LinearSearch(a, search):
    n = len(a)
    for i in range(n):
        if(search == a[i]):
            print("The element is in index",i)

# a = [10,20,30,40,50,60]
# search = 40
# LinearSearch(a, search)


def BinarySearch(a, key):
    n = len(a)
    l = 0
    h = n-1
    while(l <= h):    
        mid = (l+h)//2
        if(key == a[mid]):
            return mid
        elif(key < a[mid]):
            h = mid - 1
        elif(key > a[mid]):
            l = mid + 1

a = [1,5,10,12,14,16,20,24,29,31]
key = 200
result = BinarySearch(a, key)
if(result is None):
    print("key is not there in the list")
else:
    print("key is in index", result)