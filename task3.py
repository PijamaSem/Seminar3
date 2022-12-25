# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list=[1.1, 1.2, 3.1, 5, 10.01]
list_float=[]
for i in range (len(list)):
    if list[i]%1 != 0:
        #list_float.append(round(list[i]-int(list[i]),2))
        list_float.append(list[i] - int(list[i]))
max_flac=max(list_float)
min_flac=min(list_float)
result=max_flac-min_flac
print (round(result,5))