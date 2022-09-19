# СТРОКИ

friend = 'Тимур'
print(type(friend))
print(len(friend))
print(friend[0])
print(friend[-2])
print(friend[1:4])
print(friend[:4])
print(friend[1:])
print(friend.split('у'))
print(friend.upper())
print(friend.lower())
print(friend.find('и'))

name = 'Leo'
age = 30

hello_str = 'Привет, ' + name + ' тебе ' + str(age) + ' лет'
print(hello_str)

hello_str = 'Привет %s тебе %d лет'%(name, age)
print(hello_str)

hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)

top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start: end]
result = 'Поздравляем {} c успехом!'.format(top3.upper())
print(result)