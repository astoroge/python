# empty_list = []
# friends = ['Max','Leo','Kate']
# print(type(friends))
# print('Второй друг: ', friends[1])
# print('Первый друг с концом: ', friends[-1])
# print(friends[1:2])
# print(friends[:2])
# print(friends[1:])
# print(len(friends))
# friends.append('Ron')
# print(friends)
# print(friends.pop())
# friends.remove('Max')
# del friends[0]
# print(friends)
# friends.clear()
# print(friends)

# hero = 'Superman'
# if hero.find('man') != -1: # не равно минус один, значит если есть; равно минус один тоже самое что нету
#     print('Есть')
# if 'man' in hero:
#     print('Есть')

# goals = ['стать гуру языка python', 'здоровье', 'накормить кота']
# if 'здоровье' in goals:
#     print('Все хорошо')

# Кортеж - не изменяемый список

from itertools import count
from unittest import result

print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name)
    i -= 1 # i = i - 1
print('В соревновании участвовали: ', members)

members.reverse()

result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)