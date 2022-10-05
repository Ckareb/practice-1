n = int(input('Введите число '))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)