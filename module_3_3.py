def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(a = 2, b = 3, c = 3)
print_params(b = 1, a = 2)

values_list = [66, "kod", True]
values_dict = {'a': 1, 'b': 'срока', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [58.7, 'tom']

print_params(*values_list_2, 42)
