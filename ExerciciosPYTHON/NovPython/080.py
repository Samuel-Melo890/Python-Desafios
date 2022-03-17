from tkinter import *

def showLan(language):
    lan = language.get()
    if lan == 'Python':
        message['text'] = 'print("Hello World")'
    elif lan == 'Java':
        message['text'] = 'System.out.println("Hello World")'
    elif lan == 'CSharp':
        message['text'] = 'std::cout << "Hello World" << std::endl'

language = Tk()
language.title('Language Label')
language.geometry('600x400')

program_lan = StringVar()

frame1 = Frame(language, borderwidth=1, relief='sunken', bg='slategrey')
frame1.pack()

Label(frame1, text='Language Selection', bg='yellow', fg='black', relief='raised', borderwidth=1).grid(columnspan=3, row=0, sticky='n', ipadx=50)

python = Radiobutton(frame1, text='Python', value='Python', variable=program_lan)
python.grid(column=0, row=1, sticky='w', padx=10, pady=10)

java = Radiobutton(frame1, text='Java', value='Java', variable=program_lan)
java.grid(column=1, row=1, sticky='w', pady=10)

csharp = Radiobutton(frame1, text='CSharp', value='CSharp', variable=program_lan)
csharp.grid(column=2, row=1, sticky='w', padx=10, pady=10)

btn_confirm = Button(frame1, text='Confirm', command=lambda: showLan(program_lan), bg='limegreen')
btn_confirm.grid(columnspan=3, row=2, sticky='n')

message = Label(frame1, text='', bg='lightyellow', borderwidth=1, relief='solid', anchor='w', width=30)
message.grid(columnspan=3, row=3, sticky='n', pady=20)

language.mainloop()
