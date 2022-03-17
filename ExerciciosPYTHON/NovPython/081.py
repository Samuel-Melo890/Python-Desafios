from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

paste = os.path.dirname(__file__)

def mp(mm):
    return mm/0.352777


def create_pdf():
    try:
        cnv = canvas.Canvas(r'C:\Users\saymu\Desktop\Teste_arq\book.pdf', pagesize=A4)
        cnv.drawString(mp(85), mp(290), 'First Test With PDF')
        cnv.drawImage(image=paste+r'\anime_gif_sleep.gif', x=mp(10), y=mp(180))
        cnv.circle(mp(105), mp(140), mp(25))
        cnv.save()
    except:
        messagebox.showerror('Error PDF Creation', 'Error to create PDF file, check if the file is not already open.')
    else:
        messagebox.showinfo('PDF Created', 'PDF was successfully created!')


app = Tk()
app.title('PDF\'s with Reportlab')
app.geometry('600x450')

btn_pdf = Button(app, text='Create PDF', bg='darkorange', fg='black', command=create_pdf)
btn_pdf.grid(columnspan=3, row=0, sticky='s')

app.mainloop()
