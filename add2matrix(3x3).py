def printMatrix(e):
    print(e[0])
    print(e[1])
    print(e[2])
a=[[1,2,3],
    [4,5,6],
    [7,8,9]]
b=[[9,8,7],
   [6,5,4],
   [3,2,1]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        result[i][j]=a[i][j]+b[i][j]
printMatrix(a)
printMatrix(b)
printMatrix(result)


