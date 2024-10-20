# Давайте на практике применим метод подсчета
#
# На вход вашей программе поступает положительное целое число n, а ваша задача вывести в порядке возрастания все цифры, которые встречались в этом числе, и напротив каждого также необходимо вывести сколько раз данная цифра встречалась в числе n
#
# Разбор Youtube Patreon Boosty
#
# Sample Input 1:
#
# 45654
# Sample Output 1:
#
# 4 2
# 5 2
# 6 1
# Sample Input 2:
#
# 11111
# Sample Output 2:
#
# 1 5

a = list(input())

count = [0] * 10

for i in a:
    b = int(i)
    count[b] += 1

for i in range(10):
    if count[i] > 0:
        print(i, count[i])
