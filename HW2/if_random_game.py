# Упражнение 2.1
import random

machine = (random.randint(0, 10))
user = int(input("Загадайте число от 1 до 4: "))

if machine == user:
    print("Победа!")
else:
    print("Повторите еще раз!")
    if machine > user:
        print('Результат больше введенного числа')
    else:
        print("Результат меньше введенного числа")
