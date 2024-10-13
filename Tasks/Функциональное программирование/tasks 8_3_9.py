# Алгоритм быстрого возведения в степень
# Реализуйте рекурсивный алгоритм быстрого возведения в степень. Если нам требуется возвести некоторое число 𝑎 в степень 𝑛, где 𝑛 — положительное целое число, мы можем руководствоваться следующими принципами:
#
# если 𝑛 четное, то мы можем представить результат 𝑎 в степени 𝑛 как
#
# a**n = a**(n/2)*a**(n/2)=a**((n/2)**2)
#
# если 𝑛 нечетное, то 𝑎 в степени 𝑛 можно найти как
#
# a**n = (a**(n-1))*a
#
# При этом  𝑛−1 гарантированно станет четным числом и тогда на следующем этапе можно будет воспользоваться формулой выше для четных 𝑛.
# Базовым случаем для операции возведения в данной задаче будет являться нулевая степень числа. Любое число в нулевой степени равно 1.
#
# Напишите рекурсивную функцию quick_power, которая реализует алгоритм быстрого возведения в степень
#
# Для проверки правильности работы вашего алгоритма выведите в самом начале функции quick_power состояние параметров a и n  в следующем формате
#
# State: a=<value>, n=<value>
# Sample Input 1:
#
# print(quick_power(3, 4))
# Sample Output 1:
#
# State: a=3, n=4
# State: a=3, n=2
# State: a=3, n=1
# State: a=3, n=0
# 81
# Sample Input 2:
#
# print(quick_power(2, 24))
# Sample Output 2:
#
# State: a=2, n=24
# State: a=2, n=12
# State: a=2, n=6
# State: a=2, n=3
# State: a=2, n=2
# State: a=2, n=1
# State: a=2, n=0
# 16777216
# Sample Input 3:
#
# print(quick_power(1, 1000))
# Sample Output 3:
#
# State: a=1, n=1000
# State: a=1, n=500
# State: a=1, n=250
# State: a=1, n=125
# State: a=1, n=124
# State: a=1, n=62
# State: a=1, n=31
# State: a=1, n=30
# State: a=1, n=15
# State: a=1, n=14
# State: a=1, n=7
# State: a=1, n=6
# State: a=1, n=3
# State: a=1, n=2
# State: a=1, n=1
# State: a=1, n=0
# 1


def quick_power(val, p):
    print(f'State: a={val}, n={int(p)}')
    if p<0:
        return quick_power(1 / val, -p)
    if p==0:
        return 1
    if p % 2 == 0:
        return quick_power(val, p / 2) ** 2
    else:
        return quick_power(val, p - 1) * val


print(quick_power(2, 24))
