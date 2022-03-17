from tkinter import *
from tkinter import ttk
from time import sleep

def value_bar():
    for n in range(0, 100):
        v = pro_var.get()
        pro_var.set(v + 1)
        app.update()
        sleep(0.0005)

app = Tk()
app.title('Progress Bar')
app.geometry('600x300')
app.configure(bg='lightgrey')

pro_var = DoubleVar()
pro_var.set(0)

pb = ttk.Progressbar(app, variable=pro_var, maximum=100)
pb.place(x=10, y=10, width=200, height=10)

btn = Button(app, text='Increase Bar', command=value_bar)
btn.place(x=60, y=25, width=100)

app.mainloop()
