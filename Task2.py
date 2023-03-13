'''Написать программу, которая при вводе пользователем числа в секундах будет выводить это число
в консоль в формате - чч:мм:сс'''

n = int(input('Введите число секунд: '))

if n < 0:
    print('Введите положительное число секунд')

if n >= 0:
    h = n//3600
    m = (n-h*3600)//60
    s = (n-h*3600)%60
    print(f"{int(h)}:{int(m)}:{int(s)}")
#print(f"{int(h)}:{int(m)}")