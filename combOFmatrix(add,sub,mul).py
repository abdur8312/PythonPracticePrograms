n=int(input("Enter the order of matrix:"))
def printMatrix(d,n):
    for i in range(n):
        print(d[i])
def createZeroMatrix(n):
    f=[]
    for i in range(n):
        g=[]
        for j in range(n):
            h=0
            g.append(h)
        f.append(g)
    return f
def inputMatrix(m,n):
    for i in range(n):
        for j in range(n):
            m[i][j]=int(input())
    return m
def multiPlication(A,B,n):
    mult=createZeroMatrix(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mult[i][j]+=A[i][k]*B[k][j]
    return mult
def addiTion(A,B,n):
    add=createZeroMatrix(n)
    for i in range(n):
        for j in range(n):
            add[i][j]=A[i][j]+B[i][j]
    return add
def subTraction(A,B,n):
    sub=createZeroMatrix(n)
    for i in range(n):
        for j in range(n):
            sub[i][j]=A[i][j]-B[i][j]
    return sub
A=createZeroMatrix(n)
A=inputMatrix(A,n)
print("A=",end="")
printMatrix(A,n)
print("\n")
B=createZeroMatrix(n)
B=inputMatrix(B,n)
print("B=",end="")
printMatrix(B,n)
print("MATRIX MULTIPLICATION:")
mult=multiPlication(A,B,n)
printMatrix(mult,n)
print("MATRIX ADDITION:")
add=addiTion(A,B,n)
printMatrix(add,n)
print("MATRIX SUBTRACTION:")
sub=subTraction(A,B,n)
printMatrix(sub,n)

