def cycle():
    global n, count
    if n <= 9:
        for i in range(1,n):
            x = str(i)
            count = count + x
            print(count)
    else: print('Слишком большое число')

n = int(input('Количество переменных '))
count = ''
str(count)

cycle()
