def count():
    global a
    while a > b:
        a = a - 1
        if a % 2 != 0 :
            print(a)

a = int(input('Введите число a '))

b = int(input('Введите число b '))

count()