def printMatrix(c,n):
    for i in range(0,n):
        print(c[i])
n=int(input("Enter the order of matrix:"))
def inputMatrix(n):
    b=[]
    print("Enter the value of Matrix:")
    for i in range(n):
        row=[]
        for j in range(n):
            e=int(input())
            row.append(e)
        b.append(row)
    return b
def createZeroMatrix(n):
    c=[]
    for i in range(n):
        row=[]
        for j in range(n):
            e=0
            row.append(e)
        c.append(row)
    return c

A=inputMatrix(n)
B=inputMatrix(n)
printMatrix(A,n)
print("\n")
printMatrix(B,n)
print("\n")
prinT=createZeroMatrix(n)
printMatrix(prinT,n)
print("\n")

for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            prinT[i][j]+=A[i][k]*B[k][j]
printMatrix(prinT,n)
