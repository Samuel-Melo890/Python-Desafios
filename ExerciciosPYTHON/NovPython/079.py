from tkinter import *
import datetime

def time_now():
    global hour, min, secs, time
    
    hour = datetime.datetime.today().hour
    min = datetime.datetime.today().minute
    secs = datetime.datetime.today().second
    
    if hour < 10:
        hour = f'0{hour}'
    if min < 10:
        min = f'0{min}'
    if secs < 10:
        secs = f'0{secs}'
    
    time = f'{hour}:{min}:{secs}'
    virtual_clock['text'] = time
    
    global id_a
    id_a = clock.after(ms=1000, func=time_now)

def stop(id):
    clock.after_cancel(id)

clock = Tk()
clock.title('Relógio Digital')
clock.geometry('600x400')

hour = datetime.datetime.today().hour
min = datetime.datetime.today().minute
secs = datetime.datetime.today().second

time = StringVar()
time = f'{hour}:{min}:{secs}'

virtual_clock = Label(clock, text=time, font=('Arial', 30))
virtual_clock.pack(pady=150)

btn = Button(clock, text='Stop', command=lambda: stop(id_a), font=('Arial', 20))
btn.pack()

clock.after(ms=1000, func=time_now)

clock.mainloop()
