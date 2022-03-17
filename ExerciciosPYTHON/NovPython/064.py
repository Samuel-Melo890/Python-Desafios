from tkinter import *

def imprimir():
    ve = vesporte.get()
    vc = vcor.get()
    if ve == 'f':
        print(f'Futebol {vc.title()}')
    elif ve == 'v':
        print(f'Voley {vc.title()}')
    elif ve == 'b':
        print(f'Basketball {vc.title()}')
    else:
        print('Selecione um esporte e uma cor')

app = Tk()
app.title('Tkinter Radiobutton')
app.geometry('700x400')
app.configure(background='#dde')

vesporte = StringVar()
vcor = StringVar()

bl_esportes = Label(app, text='Esportes')
bl_esportes.pack()

rb_futebol = Radiobutton(app, text='Futebol', value='f', variable=vesporte)
rb_futebol.pack()

rb_voley = Radiobutton(app, text='Voley', value='v', variable=vesporte)
rb_voley.pack()

rb_basketball = Radiobutton(app, text='Basketball', value='b', variable=vesporte)
rb_basketball.pack()

rb_verde = Radiobutton(app, text='Cor Verde', value='Verde', variable=vcor)
rb_verde.pack()

rb_vermelho = Radiobutton(app, text='Cor Vermelha', value='Vermelho', variable=vcor)
rb_vermelho.pack()

rb_amarelo = Radiobutton(app, text='Cor Amarela', value='Amarelo', variable=vcor)
rb_amarelo.pack()

btn_esporte = Button(app, text='Esporte Selecionado', command=imprimir)
btn_esporte.pack()

app.mainloop()
