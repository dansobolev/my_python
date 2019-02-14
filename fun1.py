# Упражнение 2.4

f_value = float(input("Введите желаемое значение функции: "))

def func(x):
    if -2.4 <= x <= 5.7:
        print(pow(x,2))
    else:
        print(4)

func(f_value)
