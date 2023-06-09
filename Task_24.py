#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
#причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
#  Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
#  на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве
#  внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких
#  собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий
#модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint, randrange

numbers = []
n = int(input("Введите количество кустов в окружности: "))
for i in range(n):
    a = randint(1, 20)            # Заполняем список рандомными числами от 1 до 20
    numbers.insert(i, a)
    i += 1
print(*numbers)

result=sorted(numbers)
print(*result)                    # Сортируем список по возрастанию

sumOfEl=0
for i in range(len(result)-3, len(result)):
    sumOfEl=sumOfEl+result[i]
    i +=1
print(f"Максимальное количество ягод за 1 раз: {sumOfEl}")