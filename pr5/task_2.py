def output(): 
    global d, n, k
    while k >= 2:
        if n % k == 0:
            d = k
        k -= 1
    else: print('Наименьший делитель: ', d)

n = int(input('Натуральное число >2: '))

k =  n

output()
