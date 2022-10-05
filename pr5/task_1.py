def output(): 
    global c, n, k
    while n > c:
        print('Числа: ', c)
        k +=1
        c = k**2

n = int(input('Введите число '))

k = c = 0

output()
    