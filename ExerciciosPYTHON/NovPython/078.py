from tkinter import *
from tkinter import messagebox

def convert_time():
    try:
        global time
        sec = int(time_s.get())
        
        if 0 <= sec < 60:
            time['text'] = f'{sec} segundos'
        
        elif sec >= 60 and sec < 3600:
            min = sec // 60
            sec = sec - (min * 60)
            
            if sec == 0:
                time['text'] = f'{min} minutos'
            else:
                time['text'] = f'{min} minutos e {sec} segundos'
        
        elif sec >= 3600:
            hour = sec // 3600
            sec = sec - (hour * 3600)
            
            if sec >= 60:
                min = sec // 60
                sec = sec - (min * 60)
                
                if sec == 0:
                    time['text'] = f'{hour} horas e {min} minutos'
                else:
                    time['text'] = f'{hour} horas, {min} minutos e {sec} segundos'
            else:
                if sec == 0:
                    time['text'] = f'{hour} horas'
                else:
                    time['text'] = f'{hour} horas e {sec} segundos'
    except Exception as error:
        messagebox.showerror('Valor Não Numérico', 'Por favor insira um valor numérico.')
        print(error)
        time_s.delete(0, END)
    else:
        time_s.delete(0, END)

app = Tk()
app.title('Conversor de Tempo')
app.geometry('600x400')
app.configure(background='black')

frame1 = Frame(app, background='orange', relief='raised', borderwidth=1)
lb1 = Label(frame1, text='Conversor de Tempo', font=('Comic Sans', 11), foreground='white', background='orange')
lb2 = Label(app, text='Tempo em Segundos', background='orange', foreground='white')
time_s = Entry(app)

frame1.grid(columnspan=2, row=0, ipadx= 50)
lb1.pack(pady=10)
lb2.grid(column=0, row=1, sticky='w', pady=5)
time_s.grid(column=1, row=1, ipady=1, sticky='w')

btn_time = Button(app, text='Converter', command=convert_time)
btn_time.grid(columnspan=2, row=2)

time = Label(app, text='', background='white', anchor='w', borderwidth=1)
time.grid(columnspan=2, row=3, ipadx=10, ipady=1, pady=5)

app.mainloop()
