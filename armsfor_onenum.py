Input=str(153) #input("Enter a number to check ARMSTRONG:")
temp=0
n=len(Input)
for i in range(0,n):
    b=int(Input[i])**n
    temp+=b
if(temp==int(Input)):
    print(Input,"is a armstrong number")
else:
    print(Input,"is not a armstrong number")