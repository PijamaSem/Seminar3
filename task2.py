# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a=[2, 3, 4, 5, 6]
if len(a)%2 ==0: # четное
    middle=int(len(a)/2)
else:
    middle = int((len(a) / 2)+1)
print(middle)
result_list=[]
for i in range (0,middle):
    result_list.append(a[i]*a[-(i+1)])
print(result_list)