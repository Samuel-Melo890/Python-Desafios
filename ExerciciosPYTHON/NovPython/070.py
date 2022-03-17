from tkinter import *
from tkinter import ttk

def getgame():
    game = cb_games.get()
    scale = sc_scale.get()
    print(f'{game} : {scale}% carregado')

app = Tk()
app.title('ComboBox')
app.geometry('600x400')
app.configure(background='lightgrey')

list_games = ['Rimworld', 'Legends of Runeterra', 'Minecraft']

lb_games = Label(app, text='Games')
lb_games.pack()

cb_games = ttk.Combobox(app, values=list_games)
cb_games.set('Rimworld')
cb_games.pack()

sc_scale = Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_scale.set(50)
sc_scale.pack()

btn = Button(app, text='Get Game', command=getgame)
btn.pack()

app.mainloop()
