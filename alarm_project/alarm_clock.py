from tkinter import *
from tkinter import messagebox

condition = False
hour = 0
hour_alarm = 0
minutes = -1
minutes_alarm = 0
time1 = '00:00'
time2 = '00:00'
time_alarm = '00:00'


def set_time(test):
    global hour, hour_alarm, minutes, minutes_alarm, time1, time2, time_alarm

    if condition:
        if test == "hour":
            hour_alarm += 1
            if hour_alarm < 10 and minutes_alarm < 10:
                time_alarm = f"0{hour_alarm}:0{minutes_alarm}"

            elif hour_alarm == 24 and minutes_alarm < 10:
                time_alarm = f"00:0{minutes_alarm}"
                hour_alarm = 0

            elif hour_alarm == 24 and minutes_alarm >= 10:
                time_alarm = f"00:{minutes_alarm}"
                hour_alarm = 0

            elif hour_alarm >= 10 and minutes_alarm >= 10:
                time_alarm = f"{hour_alarm}:{minutes_alarm}"

            elif hour >= 10 and minutes_alarm < 10:
                time_alarm = f"{hour_alarm}:0{minutes_alarm}"

            elif hour < 10 and minutes_alarm >= 10:
                time_alarm = f"0{hour_alarm}:{minutes_alarm}"

            clock.config(text=time_alarm)

        else:
            minutes_alarm += 1
            if minutes_alarm < 10 and hour_alarm < 10:
                time_alarm = f"0{hour_alarm}:0{minutes_alarm}"

            elif minutes_alarm == 60 and hour_alarm >= 10:
                hour_alarm += 1
                time_alarm = f"{hour_alarm}:00"
                minutes_alarm = 0

            elif minutes_alarm == 60 and hour_alarm < 10:
                hour_alarm += 1
                time_alarm = f"0{hour_alarm}:00"
                minutes_alarm = 0

            elif minutes_alarm >= 10 and hour_alarm >= 10:
                time_alarm = f"{hour_alarm}:{minutes_alarm}"

            elif minutes_alarm >= 10 and hour_alarm < 10:
                time_alarm = f"0{hour_alarm}:{minutes_alarm}"

            elif minutes_alarm < 10 and hour_alarm >= 10:
                time_alarm = f"{hour_alarm}:0{minutes_alarm}"

            clock.config(text=time_alarm)
    else:

        if test == "hour":
            hour += 1
            if hour < 10 and minutes < 10:
                time1 = f"0{hour}:0{minutes}"
                time2 = time1
            elif hour == 24 and minutes < 10:
                time1 = f"00:0{minutes}"
                hour = 0
                time2 = time1
            elif hour == 24 and minutes >= 10:
                time1 = f"00:{minutes}"
                hour = 0
                time2 = time1

            elif hour >= 10 and minutes >= 10:
                time1 = f"{hour}:{minutes}"
                time2 = time1

            elif hour >= 10 and minutes < 10:
                time1 = f"{hour}:0{minutes}"
                time2 = time1

            elif hour < 10 and minutes >= 10:
                time1 = f"0{hour}:{minutes}"
                time2 = time1
            clock.config(text=time2)

        else:
            minutes += 1
            if minutes < 10 and hour < 10:
                time1 = f"0{hour}:0{minutes}"

            elif minutes == 60 and hour >= 10:
                hour += 1
                time1 = f"{hour}:00"
                minutes = 0

            elif minutes == 60 and hour < 10:
                hour += 1
                time1 = f"0{hour}:00"
                minutes = 0

            elif minutes >= 10 and hour >= 10:
                time1 = f"{hour}:{minutes}"


            elif minutes >= 10 and hour < 10:
                time1 = f"0{hour}:{minutes}"


            elif minutes < 10 and hour >= 10:
                time1 = f"{hour}:0{minutes}"
            time2 = time1
            clock.config(text=time2)


def tick():
    global hour, time2, minutes

    """
        Проверка будильника
    """

    if time_alarm == time2 and time_alarm != '00:00':
        messagebox.showinfo("ALARM", "ALARM ALARM ALARM")

    if condition:
        if hour == 0 and minutes == -1:
            minutes += 1
            time2 = f"0{hour}:0{minutes}"

        elif hour < 10 and minutes < 9:
            minutes += 1
            time2 = f"0{hour}:0{minutes}"

        elif hour < 10 and minutes >= 9 and minutes < 59:
            minutes += 1
            time2 = f"0{hour}:{minutes}"

        elif hour >= 10 and minutes == 59:
            minutes = 0
            hour += 1
            time2 = f"{hour}:00:"
        elif hour < 10 and minutes == 59:
            minutes = 0
            hour += 1
            time2 = f"0{hour}:00"

        elif hour >= 10 and minutes < 9:
            time2 = f"{hour}:0{minutes}"
            minutes += 1
        elif hour >= 10 and minutes >= 9:
            time2 = f"{hour}:{minutes}"
            minutes += 1
    else:
        if hour == 0 and minutes == 0:
            minutes += 1
            time2 = f"0{hour}:0{minutes}"

        elif hour < 10 and minutes < 9:
            minutes += 1
            time2 = f"0{hour}:0{minutes}"

        elif hour < 10 and minutes >= 9 and minutes < 59:
            minutes += 1
            time2 = f"0{hour}:{minutes}"

        elif hour >= 10 and minutes == 59:
            minutes = 0
            hour += 1
            time2 = f"{hour}:00"
        elif hour < 10 and minutes == 59:
            minutes = 0
            hour += 1
            time2 = f"0{hour}:00"

        elif hour >= 10 and minutes < 9:
            time2 = f"{hour}:0{minutes}"
            minutes += 1

        elif hour >= 10 and minutes >= 9:
            minutes += 1
            time2 = f"{hour}:{minutes}"
        clock.config(text=time2)
    clock.after(60000, tick)



def set_alarm():
    global condition, time_alarm
    if not condition and time_alarm == '00:00':
        condition = True
        clock.config(text=time_alarm)
    elif not condition and time_alarm != '00:00':
        condition = False
        time_alarm = '00:00'
        clock.config(text=time2)
    else:
        condition = False
        clock.config(text=time2)




def set_hours():
    set_time("hour")

def set_minutes():
    set_time("minute")



root = Tk()
root.title("Будильник")
root.geometry('400x180')

frame1 = Frame(root, width=300, height=130,  background="#343434")
frame2 = Frame(root, width=300, height=30, background="#343434")

frame1.place(x=50, y=20)
frame2.place(x=50, y=150)

clock = Label(frame1, font=('Pixel Cyr', 70), bg='#343434', fg='white')
clock.config(text=time1)
clock.place(x=38, y=18)

buttonH = Button(frame2, text="H", width=5, bg='#0067BD', fg='white', command=set_hours)
buttonH.place(x=40, y=1)

buttonM = Button(frame2, text="M", width=5, bg='#0067BD', fg='white', command=set_minutes)
buttonM.place(x=120, y=1)

buttonA = Button(frame2, text="A", width=5, bg='#0067BD', fg='white', command=set_alarm)
buttonA.place(x=200, y=1)


tick()

root.resizable(width=False, height=False)

root.mainloop()
