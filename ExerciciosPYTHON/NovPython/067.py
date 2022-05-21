from tkinter import *
from tkinter import messagebox

def show_msg():
    messagebox.showinfo('Samuel', 'José')

app = Tk()
app.title('Frame e Label')
app.geometry('700x400')
app.configure(background='#dde')

entry = StringVar()

fr_quadro1 = Frame(app, borderwidth=1, relief='solid')
fr_quadro1.place(x=10, y=10, width=300, height=100)

lb = Label(fr_quadro1, text='Mensagem', anchor='w')
lb.place(x=1, y=10)
op = Entry(fr_quadro1, textvariable=entry)
op.place(x=1, y=30)

btn = Button(fr_quadro1, text='Mostrar Mensagem', command=show_msg)
btn.place(x=1, y=50)

fr_quadro2 = Frame(app, borderwidth=1, relief='solid', background='black')
fr_quadro2.place(x=10, y=120, width=300, height=100)

lb2 = Label(fr_quadro2, text='Jeanne D\'arc', background='black', foreground='white', font=('Comic Sans', 15))
lb2.pack(side='left', fill=X, expand=True)

app.mainloop()
