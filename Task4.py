procceds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

result = procceds-costs

print(int(result))

if result == 0:
    print('Ваша прибыль нулевая. ')
if result < 0:
    print(f'Ваш убыток составил {int(result* -1)}')

elif result > 0:
    print(f'Ваша прибыль составляет {int(result)}')
    profitability = result / procceds
    print(f'Рентабельность выручки составляет {round(profitability)}')
    staff = int(input('Введите численность сотрудников фирмы: '))
    profitStaf = result / staff
    print(f'Прибыль фирмы в расчете на одного сотрудника {profitStaf}')