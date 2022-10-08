def output(): 
    global c, x, y
    while x < y:
        k = x*0.1
        x = x + k
        c = c + 1
    else: print('Количество дней ', c)


x = int(input('Пробежал киломентров '))
y = int(input('Должен прибежать '))

c = 0

output()