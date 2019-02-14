# Упражнение 2.6



#Исходные данные:
#Фильм «Пятница», 
#сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб. 
#Фильм «Чемпионы», 
#сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб. 
#Фильм «Пернатая банда», 
#сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб.


list_friday = ['12 часов', '16 часов', '20 часов']
list_champion = ['10 часов', '13 часов', '16 часов']
list_crue = ['10 часов','14 часов','18 часов']
 


film = str(input("Введите название фильма ('Пятница'/'Чемпионы'/'Пернатая банда'): "))
day = str(input("Введите дату (сегодня или завтра): "))
time = str(input("Выберите время (например, 12 часов): "))
amount = int(input("Укажите количество билетов: "))



def cinema_day(d):
    global discount_1 #скидка за день
    discount_1 = 1
    if "С" in d or "с" in d:
        discount_1 = discount_1
    else:
        discount_1 = 0.95
    


def amount_person(a):
    global discount_2 #Скидка за количество
    discount_2 = 1
    if a >= 20:
        discount_2 = 0.8
    else:
        discount_2 = discount_2


def film_friday(t):
    global price
    price = 0
    if t == "12 часов":
        price = 250
    elif t == '16 часов':
        price = 350
    elif t == '20 часов':
        price = 450

def film_champion(t):
    global price
    price = 0
    if t == '10 часов':
        price = 250
    elif t == '13 часов':
        price = 350
    elif t == '16 часов':
        price = 350
       

def film_crue(t):
    global price
    price = 0
    if t == '10 часов':
        price = 350
    elif t == '14 часов':
        price = 450
    elif t == '18 часов':
        price = 450

def cinema_price(f):
    if 'Пятница' in f:
        cinema_day(day)
        film_friday(time)
        amount_person(amount)
        all_price = price*amount*discount_1*discount_2
        if all_price == 0:
            print('Вы выбрали неверное время или дату.')
            print('Пожалуйста внимательно ознакомьтесь с расписанием: ',*list_friday)
        else:
            print('Вы выбрали фильм:', film,'День:',day, 'Время',time, 'Количество билетов:', amount)
            print('С вас',all_price,'р')
            
    elif 'Чемпионы' in f:
        cinema_day(day)
        film_champion(time)
        amount_person(amount)
        all_price = price*amount*discount_1*discount_2
        if all_price == 0:
            print('Вы выбрали неверное время или дату.')
            print('Пожалуйста внимательно ознакомьтесь с расписанием: ',*list_champion)
        else:
            print('Вы выбрали фильм:', film,'День:',day, 'Время',time, 'Количество билетов:', amount)
            print('С вас',all_price,'р')
            
    elif 'Пернатая банда' in f:
        cinema_day(day)
        film_crue(time)
        amount_person(amount)
        all_price = price*amount*discount_1*discount_2
        if all_price == 0:
            print('Вы выбрали неверное время или дату.')
            print('Пожалуйста внимательно ознакомьтесь с расписанием: ',*list_crue)
        else:
            print('Вы выбрали фильм:', film,'День:',day, 'Время',time, 'Количество билетов:', amount)
            print('С вас',all_price,'р')
        
        

cinema_price(film)


        


        
