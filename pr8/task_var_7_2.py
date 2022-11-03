def octal(A):
    M = ""
    if A < 1000000000:
        while  A != 0:
            M = str(A % 8)  + M
            A //= 8
        return "{0:0>10}".format(M)
    else: print('Неверный формат')
    

N = int(input('Введите целое не отрицательное число '))

print(octal(N))