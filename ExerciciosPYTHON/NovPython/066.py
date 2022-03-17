from tkinter import *
from tkinter import messagebox

def show_msg(type, msg: str):
    if type == '1':
        messagebox.showinfo(title='Mensagem Importante', message=msg)
    elif type == '2':
        messagebox.showerror(title='Erro Importante', message=msg)
    elif type == '3':
        messagebox.showwarning(title='Aviso Importante', message=msg)
    else:
        print('\033[31mERRO! Por favor insira um número entre 1 e 3!\033[m')

def resetarTB():
    res = messagebox.askyesno('Resetar Text Box', 'Confirma reset do Text Box?')
    if res == True:
        op.delete(0, END)
        op.insert(0, '1')

app = Tk()
app.title('MessageBox')
app.geometry('700x400')
app.configure(background='#dde')

caixa_num = StringVar()
caixa_num.set(1)

Label(app, text='Tipo de caixa (1, 2, 3)', anchor='center').pack()
op = Entry(app, textvariable=caixa_num)
op.pack()

btn_1 = Button(app, text='Mostrar Mensagem', command=lambda: show_msg(caixa_num.get(), 'Skull Knight'))
btn_1.pack()

btn_2 = Button(app, text='Resetar Text Box', command=resetarTB)
btn_2.pack()

app.mainloop()
