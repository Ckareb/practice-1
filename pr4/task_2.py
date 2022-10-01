def count_1():
    global a
    while a > b:
        print(a)
        a = a - 1
        if a == b:
            print(b)

def count_2():
    global a
    while a < b:
        print(a)
        a = a + 1
        if a == b:
            print(b)

a = int(input('Введите число a '))

b = int(input('Введите число b '))

count_1()

count_2()