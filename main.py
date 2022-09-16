number = int(input('Введите число: '))
while 10 < number > 0:
    number = int(input('Число не верное. Введите число в диапозоне от 0 до 10: '))

print(number**2)