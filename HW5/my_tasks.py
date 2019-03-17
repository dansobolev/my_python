def todo_list():
    print("Простой todo:", "    1. Добавить задачу.", "    2. Вывести список задач.",
          "    3. Выход.", sep="\n")

a = True

lst = []

while a == True:
    todo_list()
    inp = int(input("Укажите число: "))
    dictionary = {}
    if inp == 1:
        task = input("Сформулируйте задачу: ")
        dictionary["task"] = task
        category = input("Добавьте категорию к задаче: ")
        dictionary["category"] = category
        time = input("Добавьте время к задаче: ")
        dictionary["time"] = time
        lst.append(dictionary)
    elif inp == 2:
        for i in lst:
            print("Задача:", i["task"], " Категория:", i["category"], " Дата:", i['time'])
    else:
        a = False





