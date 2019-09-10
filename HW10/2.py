# 2 задание
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.value = tkinter.StringVar()

        self.value_label = tkinter.Label(self.top_frame,
                                         textvariable=self.value)

        self.value_label.pack()

        self.button1 = tkinter.Button(self.bottom_frame, text="sinister", command=self.push_but_1)
        self.button2 = tkinter.Button(self.bottom_frame, text="dexter", command=self.push_but_2)
        self.button3 = tkinter.Button(self.bottom_frame, text="medium", command=self.push_but_3)

        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')

        tkinter.mainloop()

    def push_but_1(self):
        self.value.set("левый")

    def push_but_2(self):
        self.value.set("правый")

    def push_but_3(self):
        self.value.set("средний")


my_gui1 = MyGUI()