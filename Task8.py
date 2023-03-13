a = int(input('Введите размер долек ширины шоколадки : '))
b = int(input('Введите размер долек длины шоколадки: '))
c = int(input('Введите количество долек : '))

if c < a and c < b:
    print('no')
elif c==a or c==b:
    print('yes')
elif c%a == 0 or c%b == 0:
    print('yes')
else:
    print('no')