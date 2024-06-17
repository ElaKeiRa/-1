one = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while one < len(my_list):
    if my_list[one] == 0:
        one += 1
    elif my_list[one] < 0:
        break
    else:
        print(my_list[one])
        one += 1
