from tkinter import *

root = Tk()

e = Entry(root, width = 50, borderwidth = 5)
e.pack()
e.insert(0, "Enter your name")#Default value
#e.get() # gets whatever is typed.

def myclick():
    hello = "Hello " + e.get()
    mylabel = Label(root, text = hello)
    mylabel.pack()

mybutton = Button(root, text = 'Click me!', command = myclick)
mybutton.pack()

root.mainloop()