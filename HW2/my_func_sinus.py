# Упражнение 3.2
import math

x = float(input("Введите любое вещественное число: "))
def func_sinus(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1

print(func_sinus(x))


