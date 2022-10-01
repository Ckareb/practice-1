def cycle():
    x = 1 
    global n, count_1, count_2
    for i in range(2,n):
        x = count_1 + count_2
        count_1 = count_2
        count_2 = x
        print(count_2)


n = int(input('Количество переменных '))
count_1 = count_2 = 1

cycle()
