import json

def todo_list():
    print("Простой todo:", "    1. Добавить задачу.", "    2. Вывести список задач.",
          "    3. Выход.", sep="\n")

def writer(something):
    try:
        with open("todo_list.json", 'w', encoding='windows-1251') as file_write:
            json.dump(something, file_write, sort_keys=False, ensure_ascii=False)
    except Exception as e:
        print(e)

a = True

lst = []

try:
    with open("todo_list.json", 'r', encoding='cp1251') as json_file:
        contents = json.load(json_file)
    for todo in contents:
        print("Задача:", todo["task"])
        print("Категория:", todo["category"])
        print("Дата:", todo["time"])
except:
    print("Текущие задачи в файле:\n[]")


while a == True:
    todo_list()
    inp = int(input("Укажите число : "))
    dictionary = {}
    if inp == 1:
        task = input("Сформулируйте задачу: ")
        dictionary["task"] = task

        category = input("Добавьте категорию к задаче: ")
        dictionary["category"] = category

        time = input("Добавьте время к задаче: ")
        dictionary["time"] = time

        lst.append(dictionary)

        writer(lst)
    elif inp == 2:
        for i in lst:
            print("Задача:", i["task"])
            print("Категория:", i["category"])
            print("Дата:", i["time"])
    else:
        print("Задача сохранены в файл!")
        a = False