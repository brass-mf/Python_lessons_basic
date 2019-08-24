# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    result = number*(10**(ndigits*2))//10**ndigits
    var_ostatok = number*(10**(ndigits*2))%10**ndigits/(10**(ndigits-1))
    if var_ostatok>4:
       result = result +1
    return(result/(10**(ndigits)))

print(my_round(2.1234567, 0))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(0.9999917, 5))
print(my_round(9999917111.000023321, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    var_len = round(len(str(ticket_number))/2+0.4)
    first = ticket_number//10**var_len
    second = ticket_number%10**var_len
    print(first)
    print(second)
    sum_first = 0
    sum_second = 0
    while first > 0:
        i = first % 10
        sum_first = sum_first + i
        first = first // 10

    while second > 0:
        i = second % 10
        sum_second = sum_second + i
        second = second // 10
    if sum_first == sum_second:
        return True
    else: return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(111222))
