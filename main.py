#############################################
# Тернарный оператор
# is_russian = False
# print('Привет' if is_russian else 'Hello')
#############################################
# Обработка исключительных ситуаций(ошибок)
# number = int(input('Введите число: '))
# try:
#     result = 100 / number
# except:
#     print('Ошибка. Деление на 0.')
# print('Конец')
#
# Обработка конкретных исключительных ситуаций(ошибок)
# number = int(input('Введите число: '))
# try:
#     result = 100 / number
# except ZeroDivisionError:
#     print('Попытка деления на 0.')
# except Exception:
#     print('Неизвестная ошибка.')
#
# Чтобы посмотреть информацию об исключении
# number = int(input('Введите число: '))
# try:
#     result = 100 / number
# except ZeroDivisionError as e:
#     print('Попытка деления на 0.')
#     print('Информация об исключении', e)
# except Exception as e:
#     print('Неизвестная ошибка.')
#     print('Информация об исключении', e)
#############################################