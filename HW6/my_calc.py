# Упражнение 10.1

x = input("Input the first number: ")
y = input("Input the second number: ")
z = input("Choose the operand: ")

def simple_calc(x, y, z):
    x = int(x)
    y = int(y)
    z = str(z)

    dictionary = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "^": lambda x, y: x ** y
    }
    return dictionary[z](x,y)
try:
    print(simple_calc(x ,y, z))
except ValueError:
    print("Вы ввели строку, введите число.")
except ZeroDivisionError:
    print("На ноль делить нельзя.")