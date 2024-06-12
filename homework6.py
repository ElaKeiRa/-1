my_dict = {'Elly': 1996, 'Soll': 1997, 'Dania': 2016}
print(my_dict)
print(my_dict['Soll'])
print(my_dict.get('Sania', 'Такого пользователя нет'))
my_dict['Evi'] = 1994
my_dict['Katlyn'] = 1999
print(my_dict)
my_dict.pop('Evi')
print(my_dict)

my_set = {166, 186, 98, 76, 166, 98, 'local', 'singl', 'time', 'Экспресс', 'singl', 'local'}
print(my_set)
my_set.add('total')
my_set.add(5)
my_set.remove(186)
print(my_set)
