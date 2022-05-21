from tkinter import *
import sqlite3

def imprimir():
    if vnome.get() != '' and vemail.get() != '' and vfone.get() != '' and vtexto.get('1.0', END) != '':
        con = sqlite3.connect(r'C:\Users\saymu\Documents\MyRepository\Python-Desafios\ExerciciosPYTHON\NovPython\Banco\AgendaTkinter.sqlite')
        cursor = con.cursor()
        cursor.execute(f'''INSERT INTO bancoagenda (T_Name, T_Email, T_Telefone, T_Texto)
                            VALUES ("{vnome.get()}", "{vemail.get()}", "{vfone.get()}", "{vtexto.get('1.0', END)}")''')
        con.commit()
        cursor.close()
        
        vnome.delete(0, END)
        vemail.delete(0, END)
        vfone.delete(0, END)
        vtexto.delete("1.0", END)
    else:
        Label(app, text='Dados não fornecidos! Por favor preencha todos os dados!', background='#dde', foreground='#ff0000', anchor='w').place(x=10, y=370, width=350, height=20)

app = Tk()
app.title('Janela Tkinter')
app.geometry('700x400')
app.configure(background='#dde')

Label(app, text='Ola! Seja bem-vindo a sua interface grafica! Qual o seu nome?', background='#dde', foreground='#000', anchor='w').place(x=10, y=10, width=400, height=20)
vnome = Entry(app)
vnome.place(x=10, y=40, width=275, height=20)

Label(app, text='Qual o seu email?', background='#dde', foreground='#000', anchor='w').place(x=10, y=80, width=400, height=20)
vemail = Entry(app)
vemail.place(x=10, y=110, width=275, height=20)

Label(app, text='Qual o seu telefone?', background='#dde', foreground='#000', anchor='w').place(x=10, y=150, width=400, height=20)
vfone = Entry(app)
vfone.place(x=10, y=180, width=275, height=20)

Label(app, text='Texto sobre voce:', background='#dde', foreground='#000', anchor='w').place(x=10, y=220, width=400, height=20)
vtexto = Text(app)
vtexto.place(x=10, y=250, width=275, height=50)

Button(app, text='Imprimir Dados', command=imprimir, background='#00ffff', foreground='#000', anchor='center').place(x=10, y=310, width=150, height=40)

app.mainloop()
