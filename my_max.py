# Упражнение 2.2

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

def max(num1,num2):
    if num1 > num2:
        print("Наибольшее:",num1)
    else:
        print("Наибольшее:", num2)

max(num_1, num_2)
