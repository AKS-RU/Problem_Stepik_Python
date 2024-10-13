# Превращаем вложенный список в плоский
# Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из
# списков, внутри которых также могут быть списки. Задача функции flatten вернуть новый линейный список, составленный
# из элементов входного списка, в котором уже отсутствует какая-либо вложенность. Элементы в плоском списке должны
# располагаться в том же порядке, как они следовали в исходном списке. Вот несколько примеров вызова функции flatten:
#
# flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
# flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
# flatten([[[[9]]], [1, 2], [[8]]]) => [9, 1, 2, 8]
# Ваша задача только написать определение функции flatten
#
# Разбор Youtube Patreon Boosty
#
# Sample Input 1:
#
# print(flatten([1, [2, 3], [[2], 5], 6]))
# Sample Output 1:
#
# [1, 2, 3, 2, 5, 6]
# Sample Input 2:
#
# print(flatten([[[[9]]], [1, 2], [[8]]]))
# Sample Output 2:
#
# [9, 1, 2, 8]
# Sample Input 3:
#
# print(flatten([[1, 2, 3], [4, [5, [6]]], 7]))
# Sample Output 3:
#
# [1, 2, 3, 4, 5, 6, 7]
# Sample Input 4:
#
# print(flatten([[[[[[[[[4]]]]]], [[[[[[[5, 6, 7, [5, [4]]]]]]]]]]]]))
# Sample Output 4:
#
# [4, 5, 6, 7, 5, 4]


def flatten(lst: list) -> list:
    result = []
    for value in lst:
        if isinstance(value, list):
            result += flatten(value)
        else:
            result.append(value)
    return result


print(flatten([1, [2, 3], [[2], 5], 6]))
