n = input('Введите номер своего билета: ')

if len(n) != 6:
    print('Введите корректный номер билета. ')

if len(n) == 6:
    left = n[:3]
    right = n[3:]

    l1 = list(left)
    r1 = list(right)

    l2 = []
    r2 = []

    for char in l1:
        l2.append(int(char))

    for char in r1:
        r2.append(int(char))

    sumLeft = 0
    for i in l2:
        sumLeft += i
    print(sumLeft)

    sumRight = 0
    for i in r2:
        sumRight += i
    print(sumRight)

    if sumLeft == sumRight:
        print('Поздравляем, ваш билет счастливый! ')

    if sumLeft != sumRight:
        print('Ваш билет простой. ')
