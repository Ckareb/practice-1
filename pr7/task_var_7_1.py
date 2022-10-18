def function(lst):
    global t,p
    for i in range(10):
        lst.append(int(input('Введите 10 чисел: ')))
        if lst[i] % 2 == 0:
            p += lst[i]
        if lst[i] % 2 != 0:
            t *= lst[i]

lst = []
p = 0
t = 1

function(lst)
print('Сумма четный: ', p)
print('Произведение нечетный: ', t)