# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    item = 2
    lst = [1,1]
    while item <= m:
        lst.append(lst[item-2]+lst[item-1])
        item+=1
    return lst[n:m+1]

print(fibonacci(3,9))
print(fibonacci(0,0))
print(fibonacci(2,20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for j in range(0,len(origin_list)-1,1):
        f = 0
        for i in range(0,len(origin_list)-j-1,1):
             if origin_list[i+1]<origin_list[i]:
                 origin_list[i+1],origin_list[i] = origin_list[i],origin_list[i+1]
                 f = 1
               #  print('смена j=', j, ' i=',i,' элемент [i]: ',origin_list[i])
        if f==0:
            break
    return origin_list

print(sort_to_max([2, 1, -12, 2.5, 20, -11, 1, 4, -20]))



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def func_filter(in_function, in_lst):
    result = []
    for i in in_lst:
        if in_function(i):
            result.append(i)
    return result

print(func_filter(lambda x: x<10,[1,2,12,14,15,0]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_top(list):
    if list[0][0]+list[1][0]==list[2][0]+list[3][0] and list[0][1]+list[1][1]==list[2][1]+list[3][1]:
        result = True
    elif list[0][0]+list[2][0]==list[1][0]+list[3][0] and list[0][1]+list[2][1]==list[1][1]+list[3][1]:
        result = True
    elif list[0][0]+list[3][0]==list[1][0]+list[2][0] and list[0][1]+list[3][1]==list[1][1]+list[2][1]:
        result = True
    else:
        result = False
    return result

print(is_top(([3,1],[2,5],[7,1],[6,5])))


