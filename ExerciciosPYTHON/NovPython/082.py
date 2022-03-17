from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

path = os.path.dirname(__file__)

file_text = ['    A mythical monster like a giant reptile. In European tradition the dragon is typically ', 'fire-breathing and tends to symbolize chaos or evil, whereas in East Asia it is usually', 'a beneficent symbol of fertility, associated with water and the heavens.']
img = path+r'\Dragon.webp'


def mm(v):
    return v / 0.352777


def create_pdf():
    try:
        pdf = canvas.Canvas(path+r'\dragons.pdf', pagesize=A4)
        
        pdf.setFont('Courier', 35)
        pdf.setTitle('Dragons')
        pdf.drawCentredString(mm(105), mm(285), 'Dragons')
        
        pdf.line(mm(10), mm(272), mm(200), mm(272))
        pdf.setFont('Courier-Oblique', 25)
        pdf.drawCentredString(mm(105), mm(265), 'Carnivore Winged Reptile')
        pdf.line(mm(10), mm(262), mm(200), mm(262))
        
        pdf.setFont('Helvetica', 15)
        text = pdf.beginText(mm(10), mm(245))
        for line in file_text:
            text.textLine(line)
        pdf.drawText(text)
        
        pdf.drawInlineImage(img, mm(0), mm(65))
        
        pdf.save()
    except Exception as error:
        messagebox.showerror('PDF Creation Error', f'Failed to create PDF file.\nERROR: {error}')
    else:
        messagebox.showinfo('PDF Created', 'PDF file was successfully created!')

app = Tk()
app.title('PDF file')
app.geometry('500x400')

btn_create = Button(app, text='Create PDF', command=create_pdf, bg='darkorange')
btn_create.pack(pady=100)

app.mainloop()
