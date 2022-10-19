# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Примите на вход два числа, которе будут обозначать позиции.
# Найдите произведение элементов на указанных позициях.
import functools

n = int(input('Введите число N: '))
my_list = [n for n in range(-n, n+1)]
print(f'Список промежутка [-{n}, {n}]: ', my_list)
pos_1, pos_2 = int(input('Введите индекс первой позиции: ')), int(input('Введите  индекс второй позиции: '))
res=[]
for count, i in enumerate(my_list):
    if count== pos_1 or count== pos_2:
        res.append(i)
print(functools.reduce(lambda a, b : a * b, res))