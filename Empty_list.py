my_list = []
my_list_1 = [1, 2, 3, 4, 5]


def arithmetic_mean(list=int):
    if len(list) > 0:
        print(sum(list) / len(list))
    else:
        raise ValueError('List is empty!')


arithmetic_mean(my_list_1)
arithmetic_mean(my_list)
