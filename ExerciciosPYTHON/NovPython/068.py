from tkinter import *
import os

pastaApp = os.path.dirname(__file__)

def goblin_clicado():
    vg = gs_var.get()
    if vg == 1:
        print('Goblin')
def black_clicado():
    vb = bc_var.get()
    if vb == 1:
        print('Black Knight')
def jojo_clicado():
    vj = jj_var.get()
    if vj == 1:
        print('Joseph')

app = Tk()
app.title('PhotoImage')
app.geometry('700x400')
app.configure(background='lightgrey')

gs_var = IntVar()
bc_var = IntVar()
jj_var = IntVar()

quadro1 = Frame(app, borderwidth=1, relief='flat', background='lightgrey')
quadro1.place(x=0, y=0, width=545, height=350)

img = PhotoImage(file=pastaApp+r'\anime_gif_sleep.gif')
lb_img = Label(quadro1, image=img, background='lightgrey')
lb_img.place(x=0, y=0)

cb_goblins = Checkbutton(quadro1, text='Goblin', variable=gs_var, onvalue=1, offvalue=0, command=goblin_clicado)
cb_goblins.place(x=0, y=310, width=155)

cb_blackc = Checkbutton(quadro1, text='Black', variable=bc_var, onvalue=1, offvalue=0, command=black_clicado)
cb_blackc.place(x=160, y=310, width=155)

cb_jojoj = Checkbutton(quadro1, text='Joseph', variable=jj_var, onvalue=1, offvalue=0, command=jojo_clicado)
cb_jojoj.place(x=320, y=310, width=155)

app.mainloop()
