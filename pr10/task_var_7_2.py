def readFile():
    global N
    file = open('E:\\work\\practice-1\\pr10\\budkov_Y-222_vvod.txt', 'r')
    N = int(file.read(1))
    file.close()

def inMat():
    file = open('E:\\work\\practice-1\\pr10\\budkov_Y-222_vvod.txt', 'r')
    for i in range(N):
        Y = []
        for i in range(N):
            Y.append(int(file.readline(2)))
        X.append(Y)
    for i in range(N):
        for j in range(N):
            print(X[i][j], end=' ')
        print()
    file.close()


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


readFile()

#file = open('E:\\work\\practice-1\\pr10\\budkov_Y-222_vivod.txt', 'w')
#file.write(str(X[i][j]))
#file.close()
X = []
inMat()

A = []
Mas()

Trans(sumMas())            