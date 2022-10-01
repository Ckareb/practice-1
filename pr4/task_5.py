def cycle():
    global n, count
    for i in range(1,n):
        count = count + i**3

n = int(input('Количество переменных '))
count = 0
n = n + 1
cycle()
print(count)