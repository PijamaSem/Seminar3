# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


num = int(input())
list_positive = [0,1]
for i in range (2,num+1):
    list_positive.append(list_positive[i-1]+list_positive[i-2])
list_neagative=list.copy(list_positive)
for i in range (2,num+1):
    list_neagative[i]*=(-1)**(i-1)                              # Формирование Негафибоначи из обычной
list_neagative.reverse()                                        # разворот списка
list_positive.remove(0)                                         # удаление первой позиции, чтобы избежать 2 нулей
list_neagative.extend(list_positive)                            # к негафибоначи присоединяем обычную
print(list_neagative)