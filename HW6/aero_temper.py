# Упражнение 10.2

with open("temper.stat.txt", 'r') as file:
    contents = file.read()

lst = []
for i in contents.split():
    lst.append(float(i))

max1 = max(lst)
min1 = min(lst)
mean1 = sum(lst) / len(lst)

rare = 0
for i in lst:
    if lst.count(i) == 1:
        rare += 1
print("Максимальная температура: ", max1, "Минимальная температура", min1, "Средняя температура: ", int(mean1), "Количество уникальных температур: ", rare, sep="\n")








