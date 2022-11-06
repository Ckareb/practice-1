def inMat():
    for i in range(N):
        Y = []
        for i in range(N):
            Y.append(int(input('Внести значение в массив ')))
        X.append(Y)
    for i in range(N):
        for j in range(N):
            print(X[i][j], end=' ')
        print()


def Mas():
    for i in range(N):
        for j in range(N):
            if (i == j) | (i + j == N - 1):
                A.append(X[i][j])
    print(A)

def sumMas():
    C = len(A)
    D = 0
    for i in range(C):
        D += A[i]  
    print(D)
    return D
   

def Trans(D):
    for i in range(N):
        for j in range(N):
            if i % 2 == 0:
                X[i][j] = X[i][j] / D

    for i in range(N):
        for j in range(N):
            print(X[i][j], end=' ')
        print()

N = int(input('Введите количество столбцов и строк квадратной матрицы '))
X = []
inMat()

A = []
Mas()

Trans(sumMas())            