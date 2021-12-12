"""Создайте функцию, которая принимает список из елементов типа int, а возвращает новый список из строковых значений исходного массива. 
Добавить аннотацию типов для входных и результирующих значений функции"""

from typing import List


def int_func(variable: List[int]) -> List[str]:
    str_list = [str(i) for i in variable]
    return str_list


list_1 = [1, 2, 3, 9, 9, 9, 3, 2, 1]
list_2 = int_func(list_1)
print(list_1)
print(type(list_1[0]))
print(int_func([1, 9, 5, 'word', 7]))
print(type(list_2[0]))
