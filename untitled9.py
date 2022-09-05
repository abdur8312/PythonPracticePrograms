def isArmstrong(A,arm):
    if(A==arm):
        return True
    else:
        return False
A=str(153)
n=len(A)
arm=0
for i in A:
    a=int(i)
    b=a**n
    arm+=b
A=int(A)
ARMSTRONG=isArmstrong(A,arm)
print(ARMSTRONG)