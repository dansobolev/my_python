# задание 4
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cvar1 = tkinter.BooleanVar()
        self.cvar1.set(0)

        self.cvar2 = tkinter.BooleanVar()
        self.cvar2.set(0)

        self.cvar3 = tkinter.BooleanVar()
        self.cvar3.set(0)

        self.cvar4 = tkinter.BooleanVar()
        self.cvar4.set(0)

        self.cvar5 = tkinter.BooleanVar()
        self.cvar5.set(0)

        self.cvar6 = tkinter.BooleanVar()
        self.cvar6.set(0)

        self.cvar7 = tkinter.BooleanVar()
        self.cvar7.set(0)

        self.check_button1 = tkinter.Checkbutton(text='Замена масла - 300$', variable=self.cvar1)
        self.check_button1.pack()

        self.check_button2 = tkinter.Checkbutton(text='Смазочные работы - 20$', variable=self.cvar2)
        self.check_button2.pack()

        self.check_button3 = tkinter.Checkbutton(text='Промывка радиатора - 40$', variable=self.cvar3)
        self.check_button3.pack()

        self.check_button4 = tkinter.Checkbutton(text='Замена жидкости в трансмиссии - 100$', variable=self.cvar4)
        self.check_button4.pack()

        self.check_button5 = tkinter.Checkbutton(text='Осмотр - 35$', variable=self.cvar5)
        self.check_button5.pack()

        self.check_button6 = tkinter.Checkbutton(text='Замена глушителя выхлопа - 200$', variable=self.cvar6)
        self.check_button6.pack()

        self.check_button7 = tkinter.Checkbutton(text='Перестановка шин - 20$', variable=self.cvar7)
        self.check_button7.pack()





        self.button1 = tkinter.Button(self.bottom_frame,
                                      text='Показать стоимость',
                                      command=self.show_price)
        self.button2 = tkinter.Button(self.bottom_frame,
                                      text='Выйти',
                                      command=self.main_window.destroy)




        self.button1.pack(side='left')
        self.button2.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_price(self):
        rez = 0
        if self.cvar1.get():
            rez += 300
        if self.cvar2.get():
            rez += 20
        if self.cvar3.get():
            rez += 40
        if self.cvar4.get():
            rez += 100
        if self.cvar5.get():
            rez += 35
        if self.cvar6.get():
            rez += 200
        if self.cvar7.get():
            rez += 20
        tkinter.messagebox.showinfo('Общая стоимость', f"Ваши затраты равны = {rez}")




my_gui1 = MyGUI()