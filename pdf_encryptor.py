from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import os

root=Tk()
root.title('PDF Encryption Application')
f=Frame(root,height=1000,width=500)
f.pack()

filename=''
password=''
pwd=''

def end():
 messagebox.showinfo('App Ended','ThankYou!!')
 root.destroy()

def encrypt():
 global filename
 global password
 newname=os.path.splitext(f"{filename}")[0]
 pfw = PdfFileWriter()
 file =  PdfFileReader(filename)
 n = file.numPages
 for idx in range (n):
  page = file.getPage(idx)
  pfw.addPage(page)
  
 password = pwd.get()
 print(password)
 pfw.encrypt(password)
 
 with open(f'{newname}_encrypted.pdf','wb') as ef:
  pfw.write(ef)
  
 messagebox.showinfo('Done','File Successfully Encrypted!!!')

def select_file():
  global filename
  global pwd
  filename = filedialog.askopenfilename()
  file_label = tk.Label(f, text=f'Selected File: {filename}',bg='lime')
  file_label.grid(row = 1, column = 0)
  
  pwd_label = tk.Label(f, text='Enter Password for Encryption:')
  pwd_label.grid(row = 2, column = 0)
  
  pwd = Entry(f, width = 50)
  pwd.grid(row = 2, column = 1)
  
  encrypt_button = ttk.Button(f,text='Encrypt', command = encrypt)
  encrypt_button.grid(row = 3, column = 0)
  
  quit_button = ttk.Button(f,text='Quit',command = end)
  quit_button.grid(row = 4, column = 0)
  
  return filename

tk.Label(f, text='Pdf Encryptor').grid(row = 0, column = 0)
ttk.Label(f, text='Select file:').grid(row = 1, column = 0)
choose=ttk.Button(f, text='Choose File', command = select_file)
choose.grid(row = 1, column = 1)

root.mainloop()
