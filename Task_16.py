#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
# 1 2 3 4 5
#6
#-> 5

from random import randint, randrange

numbers = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    a = randint(1, 20)            # Заполняем список рандомными числами от 1 до 20
    numbers.insert(i, a)
    i += 1
print(numbers)

goal = int(input("Введите нужное число: "))
result = 0
for i in range(len(numbers)):
    if abs(goal-numbers[i])<goal-result:
        result = numbers[i]
print(f"Ближайшее число: {result}")