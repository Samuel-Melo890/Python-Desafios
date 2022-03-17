from tkinter import *

def imprimir():
    if op_esportes.get() == 'Futebol':
        print('Futebol foi selecionado!')
    elif op_esportes.get() == 'Vôlei':
        print('Vôlei foi selecionado!')
    elif op_esportes.get() == 'Basquete':
        print('Basquete foi selecionado!')
    else:
        print('Selecione um esporte!')

app = Tk()
app.title('Option Menu')
app.geometry('700x400')
app.configure(background='#dde')

lista_esportes = ['Futebol', 'Vôlei', 'Basquete']

op_esportes = StringVar()
op_esportes.set(lista_esportes[0])#Valor Padrão!

t_esportes = Label(app, text='Esportes')
t_esportes.pack()

es_esportes = OptionMenu(app, op_esportes, *lista_esportes)
es_esportes.pack()

btn_esporte = Button(app, text='Esporte Selecionado', command=imprimir)
btn_esporte.pack()

app.mainloop()
