#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

from random import randint

x = randint(1, 1000)
y = randint(1, 1000)
print(f"Петя загадал {x} и {y}")
sum=x+y
print(f"Сумма чисел: {sum}")
multy=x*y
print(f"Произведение чисел: {multy}")

for i in range(1000):
    for g in range(1000):
        if i+g==sum and i*g==multy:
            print(i, g)
