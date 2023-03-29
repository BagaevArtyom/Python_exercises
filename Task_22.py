#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# #Затем пользователь вводит сами элементы множеств.

numbers = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    a = int(input("Введите число: "))
    numbers.insert(i, a)
    i += 1
print(numbers)

numbers_2 = []
m = int(input("Введите количество чисел: "))
for j in range(m):
    b = int(input("Введите число: "))
    numbers_2.insert(j, b)
    j += 1
print(numbers_2)

count = []
for i in range(n):
    for j in range(m):
        if numbers[i] == numbers_2[j]:
            count.insert(i, numbers[i])


result=sorted(set(count))
print(*result)