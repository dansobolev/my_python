#задание 5
import tkinter, tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.cvar1 = tkinter.IntVar()
        self.cvar1.set(0)


        self.radio_button1 = tkinter.Radiobutton(self.top_frame,text='Дневное время (6:00 - 17:59)',
                                                 variable=self.cvar1,
                                                 value=1)
        self.radio_button1.pack()

        self.radio_button2 = tkinter.Radiobutton(self.top_frame, text='Вечернее время (18:00 - 23:59)',
                                                 variable=self.cvar1,
                                                 value=2)
        self.radio_button2.pack()

        self.radio_button3 = tkinter.Radiobutton(self.top_frame, text='Непиковый период (00:00 - 5:59)',
                                                 variable=self.cvar1,
                                                 value=3)
        self.radio_button3.pack()

        self.label = tkinter.Label(self.top_frame, text='Введите количество минут: ')
        self.label.pack(side='left')

        self.entry = tkinter.Entry(self.top_frame, width=10)
        self.entry.pack()

        self.button_1 = tkinter.Button(self.bottom_frame, text='Показать стоимость',
                                       command=self.show_price)
        self.button_1.pack(side='left')

        self.button_2 = tkinter.Button(self.bottom_frame, text='Выйти',
                                       command=self.main_window.destroy)
        self.button_2.pack()

        tkinter.mainloop()

    def show_price(self):
        rez = 0
        if str(self.cvar1.get()) == str(1):
            rez = 10 * int(self.entry.get())
        if str(self.cvar1.get()) == str(2):
            rez = 12 * int(self.entry.get())
        if str(self.cvar1.get()) == str(3):
            rez = 5 * int(self.entry.get())

        tkinter.messagebox.showinfo("Общая стоимость",
                                    f"Ваши затраты = {rez}")

my_gui_new = MyGUI()