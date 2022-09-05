matrix1 =[[9,8,7],[6,5,4],[3,2,1]]
matrix2 =[[1,2,3],[4,5,6],[7,8,9]]
rmatrix = [[0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]
for r in rmatrix:
    print(r)