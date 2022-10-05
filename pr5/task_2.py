n = int(input('Натуральное число >2: '))

k =  n



while k >= 2:
    if n % k == 0:
        print('Число: ', k)
    k -= 1
