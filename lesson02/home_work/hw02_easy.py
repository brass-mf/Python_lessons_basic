__author__ = 'Афонин Сергей Сергеевич'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
max_num=0
max_str=0
fruits = ['банан','киви','грейпфрут1111111111111111111111','апельсин']
for idx, item in enumerate(fruits):
    if len(str(idx))> max_num:
        max_num=len(str(idx))
    if len(item)> max_str:
        max_str=len(item)
format_fruits = ''
for idx, item in enumerate(fruits):
    format_fruits = format_fruits+ str(idx).ljust(max_num+1) + item.rjust(max_str+1) +'\n'
print(format_fruits)

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1 = list('Произвольный список №1!')
list2 = list('Произволный список №2!')
ltemp = list1[:]
for i in list1:
    if i in list2:
        ltemp.remove(i)
list1 = ltemp
print(list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lnum1 = [1,2,3,4,5,6]
lnum2 = list()
for i in lnum1:
    if i % 2 == 0:
        lnum2.append(i / 4)
    else:
        lnum2.append(i * 2)
print(lnum2)