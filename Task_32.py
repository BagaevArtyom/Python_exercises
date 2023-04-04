#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
#заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
#Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#Диапазон от 6 до 12
#Вывод: [1, 9, 13, 14, 19]

from random import randint, randrange

numbers = []
n = int(input("Введите количество элементов: "))
for i in range(n):
    a = randint(1, 20)            # Заполняем список рандомными числами от 1 до 20
    numbers.insert(i, a)
    i += 1
print(*numbers)

def min_max_index(list1=[]):
    min_1 = int(input("Введите min: "))
    max_1 = int(input("Введите max: "))
    result =[]
    a=len(list1)
    for i in range(a):
        if min_1<list1[i]<max_1:
            result.append(i)
            i+=1
    print(*result)

min_max_index(numbers)
