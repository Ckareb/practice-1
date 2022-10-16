def change(S):
    n = len(S)
    global string
    for i in range(n):
        if (S[i] == 'п') and (i < n//2):
            t = S[i].replace('п','*')
            string += t
        else: string += S[i]


S = str(input('Введите строку '))
string = ''
change(S)

print('Замена "п" в первой половине строки ',string)