from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn GUI')
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')
root.geometry('400x400')

def show():
    myLabel = Label(root, text = var.get()).pack()

var = StringVar()

c = Checkbutton(root, text = 'Check box, Hahaha', variable = var, offvalue = "Not selected", onvalue = "Selected")
c.deselect()#Using onvalue and offvalue makes the ckeck box checked already and it does not work without using this line
c.pack()

mybutton = Button(root, text = 'Click me to update', command = show).pack()

root.mainloop()