# Упражнение 4.1
import math

x = int(input('Введите натуральное целое число: '))
q = math.pi
def func_num(x):
    return '{q:.{}f}'.format(x, q=math.pi)
print(func_num(x))