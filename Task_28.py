#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#*Пример:*
#2 2
#   4

def sum1(a, b):
    if b==0:
        return a
    else:
        return sum1(a+1, b-1)
    
print(sum1(3, 6))