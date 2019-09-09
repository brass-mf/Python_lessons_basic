#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
class Card:
    def __init__(self, name):
        '''
        :param name: Имя игрока
        '''
        self.card = ([], [], [])
        self.name = name
        for i, item in enumerate(random.sample(range(1, 90), 16)):
            if i > 0 and i <= 5:
                self.card[0].append(item)
            elif i > 5 and i <= 10:
                self.card[1].append(item)
            elif i > 10 and i <= 16:
                self.card[2].append(item)
        self.card = (sorted(self.card[0]), sorted(self.card[1]), sorted(self.card[2]))

    def __str__(self):
        '''
        Перегружаем print карточки в красивом виде
        :return:
        '''
        return '\nКарточка игрока: '+str(self.name)+'\n-----------------------\n'+str(self.card[0])+'\n'+str(self.card[1])+'\n'+str(self.card[2])+'\n-----------------------'

    def num_exists(self,num,cross_out=True):
        '''

        :param num: Число для проверки
        :param cross_out: Зачеркнуть ли если оно есть?
        :return: Есть или нет число в карточке
        '''
        result = False
        i=0
        y=0
        while i < len(self.card):
            while y < len(self.card[i]):
                if str(num) == str(self.card[i][y]):
                    result = True
                    if cross_out==True:
                        self.card[i][y]='-'
                y+=1
            y=0
            i+=1
        return result


#основной блок
card_human = Card('Сергей')
card_comp = Card('Computer')
n=90 #число бочонков
cross_out = None
for i, item in enumerate(random.sample(range(1, n+1), n)):
    print ('Выпало число:',str(item),' Осталось:',n-i-1)
    print(card_human)
    print(card_comp)

    while cross_out not in ('Y','N'):
        cross_out = input('Зачеркнуть цифру? (y/n):').upper()

    print (cross_out)
    if cross_out=='Y':
        if card_human.num_exists(item,True):
            card_comp.num_exists(item,True)
        else:
            print ('Игра окончена, нет такого числа в карте')
            exit()
    elif cross_out=='N':
            if card_human.num_exists(item, False):
                print ('Игра окончена, в карте есть число',item)
                exit()
            else:
                card_comp.num_exists(item, True)