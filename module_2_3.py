my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
init_value = 0
while init_value < len(my_list):
    if my_list[init_value] == 0:
        init_value += 1
        continue
    elif my_list[init_value] > 0:
        print(my_list[init_value])
        init_value += 1
    elif my_list[init_value] <= -1:
        break
