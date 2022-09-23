

def hour():
    
    global minute
    if minute//60 == 0:
        print( 'Минут', minute,)
    else: 
        houres = minute//60
        minute = minute%60

    if  0 <= houres <= 23:
        print( 'Часов', houres, 'Минут', minute,)
    else: 
        ost = houres - 23
        houres = houres - ost
        print( 'Часов', houres, 'Минут', minute,)



minute = int(input('Введите минуты '))

hour()