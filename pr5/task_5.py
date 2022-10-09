def output(): 
    global n
    while int(input('Введите число: ')) >= 1:
        n += 1
    else: print('количество членов последовательности:',n)

n = 0

output()