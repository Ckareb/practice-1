def cycle():
    global n, count
    for i in range(1,n):
        count = count * i

n = int(input('Количество переменных '))
n = n + 1
count = 1
cycle()
print(count)