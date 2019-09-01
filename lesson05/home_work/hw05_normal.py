# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy
def getdirname():
    return (input('Введите имя папки:'))

def menu():
    return (input(
    '1 ->Перейти в папку\n'\
    '2 ->Просмотреть содержимое текущей папки\n'\
    '3 ->Удалить папку\n'\
    '4 ->Создать папку\n'\
    ))

choice = menu()
if choice=='1':

elif choice =='2':
    print(hw05_easy.lsfiles())
elif choice=='3':
    print(hw05_easy.rm_dir(getdirname()))
elif choice=='4':
    print(hw05_easy.create_dir(getdirname()))
else:
    exit()