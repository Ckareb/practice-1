def output(): 
    global c, n, k
    while n > c:
        c += 1
        k *= 2
    else: print('Показатель степени:', c, 'Сама степень:', k)

n = int(input('Введите число '))

c = 0

k = 1

output()