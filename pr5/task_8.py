def output(): 
    global n, a, c
    while a >= 1:
        k = int(input('Введите число: '))
        if a < k:
            n = k  
        if k == a:
            c = n
        a = k
    else: print('наибольшее число подряд повторяется:',c)

a = int(input('Введите число: '))

n = 0
c = 0
output()