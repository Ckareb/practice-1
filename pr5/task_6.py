def output(): 
    global n, a, c
    while a >= 1:
        c += a
        n += 1
        a = int(input('Введите число: '))
    else: print('количество членов последовательности:',n, 'Среднее значение' , c/n )

n = 0

c = 0

a = int(input('Введите число: '))

output()