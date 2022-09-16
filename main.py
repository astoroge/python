while True:
    user_number = int(input('Введите число: '))
    if 0 < user_number < 10:
        print(f'Результат: {user_number ** 2}')
        break
    else:
        print(f'Число не верное. Диапазон допустимых значений от 0 до 10.')