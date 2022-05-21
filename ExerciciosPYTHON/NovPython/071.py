from tkinter import *

def getanime():
    anime = animes_lb.get(ACTIVE)
    print(f'Anime: {anime}')

def add_anime():
    name = new_anime.get()
    animes_lb.insert(END, name)
    new_anime.delete(0, END)

app = Tk()
app.title('LabelFrame e Listbox')
app.geometry('600x400')
app.configure(background='lightgrey')

lb_animes = LabelFrame(app, text='Animes', borderwidth=1, relief='solid')
lb_animes.place(x=0, y=20, width=126, height=182)

list_anime = ['Naruto', 'Dragon Ball', 'One Piece']

animes_lb = Listbox(lb_animes)
for anime in list_anime:
    animes_lb.insert(END, anime)
animes_lb.place(x=0, y=0)

new_anime = Entry(app)
new_anime.place(x=130, y=20)

btn_new_anime = Button(app, text='Add Anime', command=add_anime)
btn_new_anime.place(x=130, y=40)

btn_anime = Button(app, text='Anime Selected', command=getanime)
btn_anime.place(x=130, y=175)

app.mainloop()
