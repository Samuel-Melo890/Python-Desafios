from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def insert_char():
    if e_name.get() == '' or e_age.get() == '':
        messagebox.showinfo('Dados Incompletos', 'Por favor preencha todos os dados.')
    else:
        c = cursor.execute(f'INSERT INTO characters (T_Name, I_Age) VALUES("{e_name.get()}", "{e_age.get()}")')
        conn.commit()
        
        tv.delete(*tv.get_children())
        charac = cursor.execute('SELECT * FROM characters').fetchall()
        for c in charac:
            tv.insert('', 'end', values=(c[0], c[1], c[2]))
        
        e_name.delete(0, END)
        e_age.delete(0, END)
        e_name.focus()

def search_name(name):
    if name == '':
        messagebox.showinfo('Dados Incompletos', 'Por favor preencha todos os dados.')
    else:
        s_name = cursor.execute(f'SELECT * FROM characters WHERE T_Name LIKE "%{name}%"').fetchall()
        
        tv.delete(*tv.get_children())
        for i in s_name:
            tv.insert('', 'end', values=(i[0], i[1], i[2]))
        
        e_searchname.delete(0, END)
        e_searchname.focus()

def show_all():
    tv.delete(*tv.get_children())
    
    charac = cursor.execute('SELECT * FROM characters').fetchall()
    
    for c in charac:
        tv.insert('', 'end', values=(c[0], c[1], c[2]))
    app.update()

conn = sqlite3.connect(r'C:\Users\saymu\Desktop\ExerciciosPYTHON\NovPython\Banco\Characters.db')
cursor = conn.cursor()

app = Tk()
app.title('Treeview com Banco de Dados')
app.geometry('600x400')

lf_table = LabelFrame(app, text='Characters', borderwidth=1, relief='solid')
lf_insert = LabelFrame(app, text='Insert Character', borderwidth=1, relief='solid')
lf_search = LabelFrame(app, text='Search Character', borderwidth=1, relief='solid')

lf_table.place(x=50, y=0, width=500, height=250)
lf_insert.place(x=50, y=260, width=500, height=60)
lf_search.place(x=50, y=330, width=500, height=60)

tv = ttk.Treeview(lf_table, columns=('id', 'name', 'age'), show='headings')
tv.column('id', minwidth=0, width=40)
tv.column('name', minwidth=0, width=150)
tv.column('age', minwidth=0, width=150)

tv.heading('id', text='ID')
tv.heading('name', text='Character\'s Name')
tv.heading('age', text='Character\'s Age')

charac = cursor.execute('SELECT * FROM characters').fetchall()
for c in charac:
    tv.insert('', 'end', values=(c[0], c[1], c[2]))

tv.pack()

lb_name = Label(lf_insert, text='Name:')
e_name = Entry(lf_insert)

lb_age = Label(lf_insert, text='Age:')
e_age = Entry(lf_insert)

btn_insert = Button(lf_insert, text='Insert Character', command=insert_char)

lb_name.grid(column=0, row=0, pady=10, sticky='w')
e_name.grid(column=1, row=0, padx=10, pady=10)

lb_age.grid(column=2, row=0, pady=10, sticky='w')
e_age.grid(column=3, row=0, padx=10, pady=10)

btn_insert.grid(column=4, row=0, pady=10)

lb_searchname = Label(lf_search, text='Name:')
e_searchname = Entry(lf_search)

btn_searchname = Button(lf_search, text='Search', command=lambda: search_name(e_searchname.get()))
btn_showall = Button(lf_search, text='Show All', command=show_all)

lb_searchname.grid(column=0, row=0, pady=10, sticky='w')
e_searchname.grid(column=1, row=0, padx=10, pady=10)

btn_searchname.grid(column=2, row=0, pady=10, sticky='w')
btn_showall.grid(column=3, row=0, padx=10, pady=10)

app.mainloop()
