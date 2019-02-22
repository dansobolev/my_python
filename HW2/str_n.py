# Упражнение 4.3

s = str(input("Введите какую нибудь строку: "))
n = int(input("Введите целое число: "))

def str_fun(s,n):
    if len(s) > n:
        return s.upper()
    else:
        return s

print(str_fun(s,n))


