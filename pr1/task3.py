nam = input('Введите имя ')

if nam == 'Иван':
    print ('Я так и знал')
else: print('Не знаю')

six = 16
age = input( 'Введите ваш возраст ')

if int(age) <= six:
    rem =  16 - int(age) 
else:
    rem = 0


if ((int(age) <= 0) or (int(age) >= 75) ):
    print('error')
elif int(age) >= six: 
    print('Поздравляем вы поступили в ВГУИТ ',age)
else:
    print('Сначала надо доучиться ',rem,'Года')




