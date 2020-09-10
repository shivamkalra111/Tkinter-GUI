from tkinter import *

root = Tk()

def click():
    mylabel = Label(root, text = "Clicked the button!!")
    mylabel.pack()

#click the button again and again the text comes up multiple times
#can also use x color codes
mybutton = Button(root, text = "Click me", padx = 50, pady = 50, command = click, fg = 'yellow', bg = '#000000')
mybutton.pack()

root.mainloop()