# задание 3
import tkinter


class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label1 = tkinter.Label(self.top_frame,
                                           text='Введите количество галонов:')
        self.kilo_entry1 = tkinter.Entry(self.top_frame,
                                         width=10)

        self.prompt_label2 = tkinter.Label(self.mid_frame,
                                           text='Введите количество миль:')
        self.kilo_entry2 = tkinter.Entry(self.mid_frame,
                                         width=10)

        self.prompt_label1.pack(side='left')
        self.kilo_entry1.pack()
        self.prompt_label2.pack(side='left')
        self.kilo_entry2.pack()

        self.descr_label = tkinter.Label(self.middle_frame,
                                         text='Мили на галлон (MPG): ')

        self.value = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.middle_frame,
                                         textvariable=self.value)

        self.descr_label.pack(side='left')
        self.miles_label.pack()

        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Преобразовать',
                                          command=self.evaluate)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def evaluate(self):
        # kilo = float(self.kilo_entry.get())
        gallons_amount = int(self.kilo_entry1.get())
        miles_amount = int(self.kilo_entry2.get())

        rez = miles_amount / gallons_amount

        self.value.set(rez)


kilo_conv = KiloConverterGUI()