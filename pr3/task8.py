def fin():
    if number1 == number2 == number3:
        print('3')
    elif number1 == number2:
        print('2')
    elif number2 == number3:
        print('2')
    elif number1 == number3:
        print('2')
    else: print('0')


number1 = int(input('Число один '))
number2 = int(input('Число два '))
number3 = int(input('Число три '))

fin()
