def zeroMatrix(n):
    zero = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp += [0]
        zero += [temp]
    return zero

def inputMatrix(zero, n):
    for i in range(n):
        for j in range(n):
            zero[i][j] = int(input("Enter the values:"))
    return zero

def add(result, mat_a, mat_b):
    length = len(mat_a)
    for i in range(length):
        for j in range(length):
            result[i][j] = mat_a[i][j] + mat_b[i][j]
    return result

def sub(result, mat_a, mat_b):
    length = len(mat_a)
    for i in range(length):
        for j in range(length):
            result[i][j] = mat_a[i][j] - mat_b[i][j]
    return result

def mult(result, mat_a, mat_b):
    length = len(mat_a)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
    return result

n = 2 #int(input("Enter order of Matrix:"))

mat_a = zeroMatrix(n)
mat_a = inputMatrix(mat_a, n)
print(mat_a)

mat_b = zeroMatrix(n)
mat_b = inputMatrix(mat_b, n)
print(mat_b)

res_mat = zeroMatrix(n)
res_mat = mult(res_mat, mat_a, mat_b)
print(res_mat)
