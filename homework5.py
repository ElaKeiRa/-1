immutable_var_tuple_ = (16,66,'Pink','Red')
print(immutable_var_tuple_)
# immutable_var_tuple_[1] = 175
# кортеж используют в качестве хранлища, например если нам нужно чтобы данные внутри него не изменялись.

mutable_list = ['Трюфель','Апельсин','Бирюза','Сетка']
print(mutable_list)
print(mutable_list[0])
mutable_list[0] = 'Мухомор'
print(mutable_list)