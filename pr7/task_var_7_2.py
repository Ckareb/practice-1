def function():
    global max,min,lst,x,y
    lst.append(int(input('Введите 10 чисел: ')))
    max = min = lst[0]
    y = x = 0
    for i in range(9):
        
        lst.append(int(input('Введите 10 чисел: ')))
        if min > lst[i+1]:
            min = lst[i+1]
            y = i + 1  
             
        
        if max < lst[i+1]:
            max = lst[i+1]
            x = i + 1

def swap():
    global x,y 
    lst.insert(y,max)
    y += 1
    lst.pop(y)
    lst.insert(x,min)
    x += 1
    lst.pop(x)
    
        
lst = []

function()
swap()
print('Массив ', lst)
print('Минимум и максимум: ', max, min)