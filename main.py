# friend = {
#     'name': 'Max',
#     'age': 23
# }

# print(friend)
# print(type(friend))
# print(friend['name'])

# friend['has_car'] = True
# print(friend)

# friend['has_car'] = False
# print(friend)

# del friend['age']
# print(friend)

# if 'has_car' in friend:
#     print('Есть тачка')

friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True,
}

for key in friend.keys():
    print(key)
    print(friend[key])

for val in friend.values():
    print(val)

for key, val in friend.items():
    print(key)
    print(val)