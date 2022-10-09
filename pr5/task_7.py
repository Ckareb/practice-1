def output(): 
    global n, a, c
    while a >= 1:
        k = int(input('Введите число: '))
        if a < k:
            n += 1
        a = k
    else: print('количество членов последовательности больше предыдущего элемента:',n)

n = 0

a = int(input('Введите число: '))

output()