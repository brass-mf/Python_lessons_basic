# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

f_workers = open('data/workers','r',encoding='utf-8')
i=0
workers_list=list()
for line in f_workers:
    workers_list.append(line.split())
    i+=1
f_workers.close()

f_hours = open('data/hours_of','r',encoding='utf-8')
i=0
hours_list=list()
for line in f_hours:
    hours_list.append(line.split())
    i+=1
f_hours.close()
workers_list.pop(0)
hours_list.pop(0)

def get_salary(salary,hours,norma):
    if hours==norma:
        result=salary
    elif hours>norma:
        result=salary+(hours-norma)*2*(salary/hours)
    elif hours<norma:
        result=salary-(norma-hours)*(salary/hours)
    return result

for worker in workers_list:
    for hour in hours_list:
        if hour[0] == worker[0] and hour[1] == worker[1]:
            worker[2] = get_salary(int(worker[2]),int(worker[4]),int(hour[2]))

print(workers_list)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

f_fruits = open('data/fruits.txt','r',encoding='utf-8')
fruits_dict={}
for line in f_fruits:
    if line!='\n':
        key = line[0:1].upper()
        if key not in fruits_dict.keys():
            fruits_dict[key] = line
        else:
            #print(fruits_dict[key])
            fruits_dict[key] = fruits_dict[key]+line
f_fruits.close()
print(fruits_dict)

for item in fruits_dict:
    f_file = open('data/fruit_'+str(item)+'.txt', 'w', encoding='utf-8')
    f_file.write(fruits_dict[item])
    f_file.close()
