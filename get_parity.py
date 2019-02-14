# Упражнение 2.3

num = int(input("Введите целое число: "))

def get_parity(x):
    if x % 2 == 0:
        print("Число", x, "четно")
    else:
        print("Число", x, "нечетно")

get_parity(num)
