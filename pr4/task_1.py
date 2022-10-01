def count():
    global b
    while a < b:
        print(b)
        b = b - 1
        if a == b:
            print(a)
        

a = int(input('Введите число '))

b = int(input('Введите число '))
count()