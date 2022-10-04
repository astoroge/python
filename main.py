######################################################
# number_list = [] 
# for i in range(3):
#     num = int(input(f'Введите {i+1} число: '))
#     number_list.append(num)
# min_number = min(number_list)
# max_number = max(number_list)
# result = min_number + max_number
# print(result)
######################################################
# def print_sep(sep, count):
#     return sep * count
# sep = print_sep('+' , 23)
# text = 'Hello {} func {}'.format(sep, sep)
# print(text)
######################################################
# def greeting(say,*args):
#     print(say, args)
# greeting('Hello', 'Max', 'Kate')
#
# def get_person(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# get_person(name='Leo', age=20, year=2000)
######################################################

# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. 
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
#
# name = input('Введите имя: ')
# age = input('Введите возраст: ')
# city = input('Введите город проживания: ')
#
# def info(name, age, city):
#     result = f'{name}, {age} год(а), проживает в городе {city} '
#     return result
#
# print(info(name, age, city))

# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
#
# num_1 = input()
# num_2 = input()
# num_3 = input()
#
# def num_max(num_1, num_2, num_3):
#     result = max([num_1, num_2, num_3])
#     return result
#
# max = num_max(num_1, num_2, num_3)
# print(max)

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь 
# ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
# ### Поэкспериментируйте с значениями урона и жизней по желанию. 
# ### Теперь надо создать функцию attack(person1, person2). 
# Примечание: имена аргументов можете указать свои. 
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
# ### В теле функция должна получить параметр damage атакующего 
# и отнять это количество от health атакуемого. 
# Функция должна сама работать со словарями и изменять их значения.
#
# player_name = input('Введите имя игрока: ')
# enemy_name = input('Введите имя врага: ')
#
# player = { 'name': player_name, 'health': 100, 'damage': 50}
# enemy = { 'name': enemy_name , 'health': 50, 'damage': 30}
#
# def attack(person1, person2):
#     person1['health'] -= person2['damage']
#
# attack(player, enemy)
# print(player)

# 4: Давайте усложним предыдущее задание. 
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный
# урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона 
# и вычитания его из здоровья персонажа. 
#
# player_name = 'Вася'
# enemy_name = 'Петя'
#
# player = { 'name': player_name, 'health': 100, 'armor' : 1.2, 'damage': 50 }
# enemy = { 'name': enemy_name, 'health': 50, 'armor' : 1, 'damage': 30 }
#
# def get_damage(damage, armor):
#     return damage / armor
#
# def attack(person1, person2):
#     damage = get_damage(person1['damage'], person2['armor'])
#     person1['health'] -= damage
#
# attack(enemy, player)
# print(enemy)
