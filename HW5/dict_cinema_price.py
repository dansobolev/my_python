# Упражнение 2.5 с использованием словаря

friday = {12: 250, 16: 350, 20: 450}
champions = {10: 250, 13: 350, 16: 350}
squad = {10: 350, 14: 450, 18: 450}
movies = {"Пятница": friday, "Чемпионы": champions, "Пернатая банда": squad}

film = str(input("Введите название фильма: "))
day = str(input("Введите дату (сегодня или завтра): "))
time = int(input("Выберите время: "))
amount = int(input("Укажите количество билетов: "))


def cinema_day(day_disc):
    if day_disc == "сегодня":
        return 1
    else:
        return 0.95

def amount_person(amount_disc):
    if amount_disc > 20:
        return 0.8
    else:
        return 1
    
    
def all_price(film, day, time, amount):
    return movies[film][time]*amount*amount_person(amount)*cinema_day(day)
    

if film and day and time and amount:
    if film in movies:
        if day == "сегодня" or day == "завтра":
            if time in movies[film]:
                print("Фильм:", film, "День:", day, "Время:", time, "Количество билетов:", amount)
                print("Результат:", all_price(film, day, time, amount))
            else:
                print("Ошибка ввода.")
        else:
            print("Ошибка ввода.")
    else:
        print("Ошибка ввода.")
else:
    print("Ошибка ввода.")




