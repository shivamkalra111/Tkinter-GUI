from tkinter import *
from PIL import ImageTk, ImageTk

root = Tk()
root.title("Learning GUI")
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')
root.geometry('400x400')

def slide(variable):
    my_label = Label(root, text = horizontal.get()).pack()

horizontal = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL, command = slide)
horizontal.pack()

mylabel = Label(root, text = horizontal.get()).pack()

#vertical = Scale(root, from_ = 0, to = 100)
#vertical.pack()



root.mainloop()