import tkinter
import random


def random_word():
    global rus
    eng, rus = random.choice(list(dictionary.items()))
    label2.config(text=eng)

def random_choice_func():
    try:
        if rus == entry.get():
            label4.config(text="Угадали!")
        else:
            label4.config(text='Ошибка')
    except Exception as ex:
        print(ex)

window = tkinter.Tk()



frame = tkinter.Frame(window)
frame.pack()

dictionary = {
    "dog": "собака",
    "cat": "кошка",
    "car": "машина",
    "ball": "мяч"
}

label = tkinter.Label(frame, text="Случайное слово:")
label.pack()

label2 = tkinter.Label(frame, text='cool')
label2.pack()

label3 = tkinter.Label(frame, text="Укажите перевод слова:")
label3.pack()

entry = tkinter.Entry(frame)
entry.pack()

label4 = tkinter.Label(frame)
label4.pack()

button1 = tkinter.Button(frame, text="Готово!", command=random_choice_func)
button1.pack()

button2 = tkinter.Button(frame,text="Выход")
button2.pack()

random_word()

window.mainloop()