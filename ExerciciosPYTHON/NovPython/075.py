from tkinter import *

app = Tk()
app.title('Grid')
app.geometry('600x300')

lb_anime = Label(app, text='Dragon Ball')
lb_name = Label(app, text='Character\'s Name')
lb_age = Label(app, text='Character\'s Age')

e_name = Entry(app)
e_age = Entry(app)

btn = Button(app, text='Dragon Ball')

lb_anime.grid(column=0, row=0, columnspan=2, pady=5)
lb_name.grid(column=0, row=1, padx=10, sticky='w')
lb_age.grid(column=1, row=1, padx=10, sticky='w')

e_name.grid(column=0, row=2, padx=10)
e_age.grid(column=1, row=2, padx=10)

btn.grid(column=0, row=3, columnspan=2, pady= 10)

app.mainloop()
