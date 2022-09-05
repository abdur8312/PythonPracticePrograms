a='baba'  #input("Enter a letter:")
n=len(a)
b=[None]*n
for i in range(0,n):
    b[i]=a[n-(i+1)]
b=''.join(map(str,b))
if(a==b):
    print(a,"is palindrome")
else:
    print(a,"is not palindrome")
    
    
#another method
string = 'malayalam'
rev_string = string[::-1]
print(rev_string)
if(string == rev_string):
    print("Palindrome")
else:
    print("not Palindrome")
    