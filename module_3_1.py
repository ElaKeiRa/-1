 # пространство имен  локальное - имена,которые мы используем  внутри функций, глабольное - целиком се что есть,
 # не включая локальное , встроеноое - именна -  встроенных функций.
# a = 5                     # глобальное простанство имен
# b = 10
#def printer():
    # global a, b
    # a = 'Str'
    # b = 'Str 2'
    # c = 15                        # локальное пространсво имен( используется только внутри функций)
    # d = 20
    # print(c, d, 'local')
    # print(a, b, 'global')
# print(a, b)
# printer()
# print(a, b)
calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
     count_calls()
     return string.upper() in [a.upper() for a in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # UrbaN ~ URBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)