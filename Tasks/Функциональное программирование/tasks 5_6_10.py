# Функция «Калькулятор»
# Пользуясь вложенными функциями, реализуйте простой калькулятор. Для этого необходимо реализовать функцию calculate ,
# которая принимает три параметра:
#
# обязательный числовой параметр x
# обязательный числовой параметр y
# необязательный строковый параметр operation,  по умолчанию принимает значение английской буквы a
# В данной функции должны быть реализованы следующие функции:
#
# addition - сложение двух чисел,
# subtraction - вычитание из первого переданного параметра второго;
# division - деление первого на второго,
# multiplication - умножение двух чисел.
# Каждая из этих четырёх вложенных функций должна распечатать результат математической операции и ничего не возвращать
#
# А при помощи параметра operation и условного оператора нужно выбрать какая из функций должна быть вызвана:
#
# если operation = a, вызываем функцию addition;
# если operation = s, вызываем функцию subtraction;
# если operation = d, вызываем функцию division;
# если operation = m, вызываем функцию multiplication;
# calculate(2, 5) # Печатает 7.0
# calculate(2.2, 15, 'a') # Печатает 17.2
# calculate(22, 15, 's') # Печатает 7.0
# calculate(2, 3.2, 'm') # Печатает 6.4
# calculate(10, 0.4, 'd') # Печатает 25.0
#
#
# Если operation принимает значение, отличное от перечисленных выше букв, то необходимо вывести на экран  сообщение
# «Ошибка. Данной операции не существует».
#
# Также если мы выполняем деление, то второе число (y) не должно равняться нулю, в противном случае необходимо
# вывести на экран: «На ноль делить нельзя!».
#
# Вам необходимо написать только определение функции  calculate
#
# Sample Input 1:
#
# calculate(10, 4, 's')
# Sample Output 1:
#
# 6
# Sample Input 2:
#
# calculate(10, 0, 'd')
# Sample Output 2:
#
# На ноль делить нельзя!
# Sample Input 3:
#
# calculate(10, 4, 'w')
# Sample Output 3:
#
# Ошибка. Данной операции не существует
# Sample Input 4:
#
# calculate(1, 2, 'a')
# Sample Output 4:
#
# 3
# Sample Input 5:
#
# calculate(3, 1, 'd')
# Sample Output 5:
#
# 3.0


def calculate(x: int | float, y: [int, float], a: str = 'a'):
    def addition(x, y):
        print(x+y)

    def subtraction(x, y):
        print(x-y)

    def division(x, y):
        print(x/y) if y else print('На ноль делить нельзя!')


    def multiplication(x, y):
        print(x*y)

    if a == 'a':
        addition(x, y)
    elif a == 's':
        subtraction(x, y)
    elif a == 'd':
        division(x, y)
    elif a == 'm':
        multiplication(x, y)
    else:
        print('Ошибка. Данной операции не существует')


calculate(10, 2, 'd')
