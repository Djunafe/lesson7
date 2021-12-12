n_list = [1, 3, 4, 8, 3, 4, 8, 2, 4, 44, 67, 3, 5, 3]


def del_x():
    x = int(input('Enter what do you want to delete: '))
    while x in n_list:
        n_list.remove(x)
    return n_list


print(del_x())
