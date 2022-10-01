def cycle():
    global n, count
    for i in range(n):
        c = int(input('Переменная = '))
        count = count + c

n = int(input('Количество переменных '))
count = 0
cycle()
print(count)
