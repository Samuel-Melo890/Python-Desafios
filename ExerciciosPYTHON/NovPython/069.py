from tkinter import *

def mostrasenha():
    print(f'Senha digitada:{senha.get()}')

app = Tk()
app.title('Password')
app.geometry('700x300')
app.configure(background='lightgrey')

senha = StringVar()

p_senha = Entry(app, textvariable=senha, show='*')
p_senha.pack()

btn = Button(app, text='Mostra Senha', command=mostrasenha)
btn.pack()

app.mainloop()
