quantity_tickets = int(input('Введите сколько билетов Вы хотите приобрести: '))
person = quantity_tickets
sum = 0

while person != 0:
    age = int(input('Укажите для какого возраста приобретается билет: '))
    if age < 18:
        print('Билет бесплатный')
    elif 25 > age >= 18:
        sum += 990
        print('Стоимость билета: 990 руб.')
    else:
        sum += 1390
        print('Стоимость билета: 1390 руб.')
    person -= 1

if quantity_tickets > 3:
    sale = sum - ((sum / 100) * 10)
    print(f'Сумма к оплате {sum} руб., 10% скидка за покупку более 3 билетов')
else:
    print(f'Сумма к оплате {sum} руб.')