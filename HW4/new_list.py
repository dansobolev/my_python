# Упражнение 6.2

from math import sqrt

# На основе цикла for
spisok1 = [2, 4, 9, 16, 25]
spisok2 = []
for i in range(len(spisok1)):
    spisok2.append(sqrt(spisok1[i]))


# На основе функции map
spisok = [2, 4, 9, 16, 25]
list1 = list(map(sqrt, spisok))


# В виде генератора списка
a = [sqrt(spisok[i]) for i in range(len(spisok))]
print(a)