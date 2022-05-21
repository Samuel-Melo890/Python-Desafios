from tkinter import *

def showName():
    name = sb_valores.get()
    print(f'Name: \033[32m{name}\033[m')

app = Tk()
app.title('SpinBox')
app.geometry('600x400')

l_names = ['Jeanne', 'Astolfo', 'Samuel', 'Gustavo', 'Golias', 'Veda', 'André', 'Noelle']

#sb_valores = Spinbox(app, from_=0, to=10)
sb_valores = Spinbox(app, values=l_names)
sb_valores.pack()

btn_sb = Button(app, text='Show Name', command=showName)
btn_sb.pack()

app.mainloop()
