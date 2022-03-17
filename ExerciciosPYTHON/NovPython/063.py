from tkinter import *
import os

paste = os.path.dirname(__file__)

def teste():
    print('')

def new_cont():
    exec(open(paste+r'\062.py').read(), {'x':1})

app = Tk()
app.title('Menu de Opções')
app.geometry('700x450')
app.configure(background='#dde')

barra_de_menu = Menu(app)
menu_contatos = Menu(barra_de_menu, tearoff=0)
menu_contatos.add_command(label='Novo Contato', command=new_cont)
menu_contatos.add_command(label='Pesquisar Contato', command=teste)
menu_contatos.add_command(label='Deletar Contato', command=teste)
menu_contatos.add_separator()
menu_contatos.add_command(label='Sair', command=app.quit)
barra_de_menu.add_cascade(label='Contatos', menu=menu_contatos)

menu_manutencao = Menu(barra_de_menu, tearoff=0)
menu_manutencao.add_command(label='Banco de Dados', command=teste)
barra_de_menu.add_cascade(label='Manutenção', menu=menu_manutencao)

menu_sobre = Menu(barra_de_menu, tearoff=0)
menu_sobre.add_command(label='Samuel Tkinter', command=teste)
barra_de_menu.add_cascade(label='Sobre', menu=menu_sobre)

app.config(menu=barra_de_menu)

app.mainloop()
