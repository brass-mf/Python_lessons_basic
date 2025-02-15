# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
input_list = [1,100,10,0,1,65,44,33,60]
output_list = [item*item for item in input_list]
print(output_list)



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['ананас','банан','кокос','персик','яблоко','фейхоа']
fruits2 = ['ананас','нектарин','кокос','персик','авокадо','фейхоа']

output_list = [item for item in fruits1 if item in fruits2]
print(output_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

input_list = [1,100,-10,0,-1,65,44,33,60]
output_list = [item for item in input_list if (item > 0 and item%3==0 and item%4!=0)]
print(output_list)
