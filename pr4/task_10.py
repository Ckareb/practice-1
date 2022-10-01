def cycle():
    x = 1 
    global n, count_1, count_2, k
    for i in range(2,n):
        i = count_1 + count_2
        count_1 = count_2
        count_2 = i 
        print(count_2)


n = int(input('Количество переменных '))
k = int(input('Начать с '))
count_1 = count_2 = 1

cycle()