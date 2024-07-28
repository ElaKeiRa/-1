stone_2 = int(input('Введите число от 1 до 20: '))
numbers = list(range(1, 21))
password_list = []
for i in numbers:
    for j in numbers:
        if i < j and stone_2 % (i + j) == 0 and i + j <= stone_2:
            password_list.append([i, j])
        elif i < j and i + j > stone_2:
            break
        else:
            continue

print(password_list)