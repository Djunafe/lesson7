"""Вычисление среднего арифметического списка. В случаи, если список пустой, то выбрасывать исключение ValueError("list is empty")"""

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = []


def arithmetic_mean(list=int):
    if len(list) > 0:
        print(sum(list) / len(list))
    else:
        raise ValueError('List is empty!')


arithmetic_mean(my_list_1)
arithmetic_mean(my_list_2)
