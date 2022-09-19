seconds = input()

minute = int(seconds)//60
houres = minute//60
dayes = houres//24

print('Дней',dayes, 'Часов', houres, 'Минут', minute, 'Секунд', seconds)


if int(seconds)//60 == 0:
    print('Секунд',seconds)
else: 
    minute = int(seconds)//60
    seconds = int(seconds)%60
    houres = 0


if minute//60 == 0:
    print( 'Минут', minute, 'Секунд', seconds)
else: 
    houres = minute//60
    minute = minute%60
    dayes = 0
    

if houres//24 == 0:
    print( 'Часов', houres, 'Минут', minute, 'Секунд', seconds)
else: 
    dayes = houres//24
    houres = houres%60
    print('Дней',dayes, 'Часов', houres, 'Минут', minute, 'Секунд', seconds)