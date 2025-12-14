import random


def generate_phone_number():
    # Список операторов с кодами
    operators = {
        'МегаФон': ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919'],
        'МТС': ['911', '912', '913', '914', '915', '916', '917', '918', '919'],
        'Tele2': ['900', '901', '902', '903', '904', '905', '906', '907', '908', '909']
    }

    # Выбираем случайного оператора
    operator = random.choice(list(operators.keys()))

    # Выбираем случайный код оператора
    code = random.choice(operators[operator])

    # Генерация случайных чисел для номера
    number_part1 = random.randint(100, 999)
    number_part2 = random.randint(10, 99)
    number_part3 = random.randint(10, 99)

    # Формируем номер в нужном формате
    phone_number = f"+7 ({code}) {number_part1}-{number_part2}-{number_part3}"

    return phone_number


# Пример использования
phone = generate_phone_number()
print(phone)

