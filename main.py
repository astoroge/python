# Во множестве не могут быть двух одинаковых элементов

# cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']

# print(type(cities))
# print(cities)

# cities = set(cities)

# print(type(cities))
# print(cities)

# cities = {'Las Vegas', 'Paris', 'Moscow'}
# print(cities)
# cities.add('Burma')
# print(cities)

# cities.remove('Moscow')
# print(cities)

# print(len(cities))

# print('Paris' in cities)

# for city in cities:
#     print(city)

max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты',}

kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

print(max_things | kate_things) # объединение списков с неповторяющийся последовательностью

print(max_things & kate_things) # выводит пересечение списков

print(max_things - kate_things) # вычитает из первого списка второй и выводит уникальные вещи первого списка в сравнение со сторым списком

