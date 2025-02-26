import tkinter as tk
import PyPDF2
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import pathlib
from gtts import gTTS
import os

window = tk.Tk()

window.title("PDF File Converter (text only)")
window.wm_iconbitmap('send.ico')

#convert pdf file to docx
def converttodoc():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_file = open(file.name, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    pathlib.Path('context.doc').write_text(page_content)
    showinfo("Done", "Successfully Converted")

#convert pdf file to txt
def converttotext():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_file = open(file.name, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    pathlib.Path('context.txt').write_text(page_content)
    showinfo("Done", "Successfully Converted")

#read pdf file in english
def converttottsen():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_File = open(file.name, 'rb')
    pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
    count = pdf_Reader.numPages
    textList = []
    for i in range(count):
        try:
            page = pdf_Reader.getPage(i)
            textList.append(page.extractText())
        except:
            pass
    textString = " ".join(textList)
    language = 'en'
    myAudio = gTTS(text=textString, lang=language, slow=False)
    myAudio.save("Audio.mp3")
    os.system("Audio.mp3")

#read pdf file in vietnamese
def converttottsvie():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_File = open(file.name, 'rb')
    pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
    count = pdf_Reader.numPages
    textList = []
    for i in range(count):
        try:
            page = pdf_Reader.getPage(i)
            textList.append(page.extractText())
        except:
            pass
    textString = " ".join(textList)
    language = 'vi'
    myAudio = gTTS(text=textString, lang=language, slow=False)
    myAudio.save("Audio.mp3")
    os.system("Audio.mp3")


label = tk.Label(window, text="Convert to DOC: ")
label.grid(row=0, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=35, command=converttodoc)
button.grid(row=0, column=1, padx=5, pady=5)


label = tk.Label(window, text="Convert to TXT: ")
label.grid(row=1, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=35, command=converttotext)
button.grid(row=1, column=1, padx=5, pady=5)


label = tk.Label(window, text="Read the PDF file: ")
label.grid(row=2, column=0, padx=5, pady=5)

button = ttk.Button(window, text="English", width=10, command=converttottsen)
button.grid(row=2, column=1)
button = ttk.Button(window, text="Vietnamese", width=10, command=converttottsvie)
button.grid(row=2, columnspan=2)


label = tk.Label(window, text="Developed by Nguyễn Duy An")
label.grid(row=3, column=0, padx=5, pady=5)
label.config(font=("Courier", 7))

window.mainloop()
