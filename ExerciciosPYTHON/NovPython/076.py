from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def v_insert():
    id = e_id.get()
    name = e_name.get()
    age = e_age.get()
    if id == '' or name == '' or age == '':
        messagebox.showinfo('Dados Não Preenchidos!', 'Você deve preencher todos os dados requisitados.')
    else:
        tv.insert('', 'end', values=(id, name, age))
        e_id.delete(0, END)
        e_name.delete(0, END)
        e_age.delete(0, END)
        e_id.focus()

def v_delete():
    try:
        itemSelected = tv.selection()[0]
        tv.delete(itemSelected)
    except:
        messagebox.showerror('Item Not Selected', 'None item was selected for deletion')

def v_obtain():
    try:
        itemSelected = tv.selection()[0]
        item = tv.item(itemSelected, 'values')
        
        print(f'ID.....: {item[0]}')
        print(f'Name...: {item[1]}')
        print(f'Age....: {item[2]}')
    except:
        messagebox.showerror('Item Not Selected', 'None item was selected to be obtained.')

app = Tk()
app.title('TreeView')
app.geometry('600x400')

Label(app, text='ID:').grid(column=0, row=0, sticky='w')
e_id = Entry(app)
e_id.grid(column=0, row=1)

Label(app, text='Name:').grid(column=1, row=0, padx=10, sticky='w')
e_name = Entry(app)
e_name.grid(column=1, row=1, padx=10)

Label(app, text='Age:').grid(column=2, row=0, sticky='w')
e_age = Entry(app)
e_age.grid(column=2, row=1)

tv = ttk.Treeview(app, columns=('id', 'name', 'age'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('name', minwidth=0, width=150)
tv.column('age', minwidth=0, width=150)

tv.heading('id', text='ID')
tv.heading('name', text='Character\'s Name')
tv.heading('age', text='Character\'s Age')

tv.grid(column=0,row=2, columnspan=3, pady=5)

btn_insert = Button(app, text='Insert', command=v_insert)
btn_delete = Button(app, text='Delete', command=v_delete)
btn_obtain = Button(app, text='Obtain', command=v_obtain)

btn_insert.grid(column=0, row=3, columnspan=3, padx=50, sticky='w')
btn_delete.grid(column=1, row=3, columnspan=3, padx=50, sticky='w')
btn_obtain.grid(column=2, row=3, columnspan=3, padx=50, sticky='w')

app.mainloop()
