# 1 задание
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.value = tkinter.StringVar()

        self.label1 = tkinter.Label(self.top_frame,
                                    textvariable=self.value)
        self.label1.pack(side="left")

        self.button1 = tkinter.Button(self.bottom_frame, text="Показать инфо", command=self.show_info)
        self.button2 = tkinter.Button(self.bottom_frame, text="Выход", command=self.main_window.destroy)

        self.button1.pack(side="left")
        self.button2.pack()

        tkinter.mainloop()

    def show_info(self):
        text = "Стивен Маркуc" + "\n" + "274 Бейли" + "\n" + "Уэнзвиль, Северная Каролина 27990"
        self.value.set(text)


my_gui = MyGUI()