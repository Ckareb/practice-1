def inMat():
    global X, N
    for i in range(N):
        X.append([0]*N)

def Matrix():
    global X, N
    h = 0
    for i in range(N):
        for j in range(i+1,N):
            X[i][j] = A[h]
            X[j][i] = A[h]
            h += 1

def outMat():
    for i in range(N):
        for j in range(N):
            print(X[i][j], end=' ')
        print()


N = int(input('Введите количество столбцов и строк квадратной матрицы '))
K = (N * N - N) // 2 
A = [int(input('Задайте верхний треугольник матрицы ')) for i in range(K)]

X = []
inMat()

Matrix()

outMat()
