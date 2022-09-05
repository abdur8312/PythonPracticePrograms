import sys
def getReverseString(orginStr):
    n=len(orginStr)
    reversedStr=""
    for i in range(n-1,-1,-1):
        b=orginStr[i]
        reversedStr+=b
    return reversedStr
def isPalindrome(revStr,orgStr):
    if(orgStr==revStr):
        return True
    else:
        return False
def printPAL(isPAL):
    if(isPAL==True):
        print("PALINDROME")
    else:
        print("NOT PALINDROME")
while(True):
    print("1.check palindrome")
    print("2.Exit")
    print("3.divides with zero(exit with error)")
    print("4.divides with zero(won't exit with error)")
    Input=int(input("Enter input:"))
    if(Input==1):
        original=input("Enter a string:")
        reverse=getReverseString(original)
        printPAL(isPalindrome(reverse,original))
    elif(Input==3):
        d=1/0
        print("abdur")
    elif(Input==4):
        try:
            d=4/0
        except ZeroDivisionError:
            print("will not show error")
        print("abdur")
    else:
        sys.exit(0)