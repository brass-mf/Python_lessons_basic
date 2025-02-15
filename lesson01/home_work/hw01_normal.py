
__author__ = 'Афонин Сергей Сергеевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

var_input = int(input('Введите целое беззнаковое число: '))
i = 0
max = 0
if var_input == 0:
    max = var_input
elif var_input > 0:
    while var_input > 0:
        i = var_input % 10
        if i > max:
            max = i
        var_input = var_input // 10
print(max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

var_user1 = input('Первое значение: ')
var_user2 = input('Второе значение: ')
var_user1, var_user2 = var_user2, var_user1
print ('Первое значение: ', var_user1, 'Второе значение: ', var_user2)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math

const_a = int(input('Введите а: '))
const_b = int(input('Введите b: '))
const_c = int(input('Введите c: '))


var_d = const_b*const_b - 4*const_a*const_c
if var_d > 0:
    x1 = (math.sqrt(var_d) - const_b) / (2*const_a)
    x2 = (-const_b - math.sqrt(var_d)) / (2*const_a)
    print (x1,' ',x2)
elif var_d ==0:
    x1 = (-const_b) / 2*const_a
    print(x1)
else:
    print('Корней нет!')