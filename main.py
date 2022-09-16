name = input('Введите имя: ')
lastname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
kg = int(input('Введите вес: '))

if age < 30 and 50 < kg < 120:
    print(f'{name} {lastname}, {age} лет, вес {kg} - хорошее состояние')
if age > 30 and 50 > kg or kg > 120:
    print(f'{name} {lastname}, {age} лет, вес {kg} - следует заняться собой')
if age > 40 and 50 > kg or kg > 120:
    print(f'{name} {lastname}, {age} лет, вес {kg} - следует обратится к врачу!')