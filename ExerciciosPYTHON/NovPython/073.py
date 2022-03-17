from tkinter import *
from tkinter import ttk

app = Tk()
app.title('Abas a Notebook')
app.geometry('600x400')
app.configure(background='lightgrey')

nb = ttk.Notebook(app)
nb.place(x=0, y=0, width=400, height=200)

fr1 = Frame(nb)
fr2 = Frame(nb)
fr3 = Frame(nb)

nb.add(fr1, text='Games')
nb.add(fr2, text='Animes e Mangás')
nb.add(fr3, text='Pinturas')

lb1 = Label(fr1, text='Minecraft')
lb1.pack()

lb2 = Label(fr2, text='Berserk')
lb2.pack()

lb3 = Label(fr3, text='Shion Esboço')
lb3.pack()

app.mainloop()
