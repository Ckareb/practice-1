def cycle():
    x = 1 
    global n, count
    for i in range(2,n):
        print(x)
        x = x * i
        count = count + x

n = int(input('Количество переменных '))
n = n + 1
count = 1

cycle()
print(count)