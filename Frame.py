from tkinter import *
from PIL import ImageTk, ImageTk

root = Tk()
root.title('Learn GUI')
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')

frame = LabelFrame(root, text = 'This is a frame', padx = 50, pady = 50)
frame.pack(padx = 10, pady = 10)

b = Button(frame, text = 'Acha beta')
b.grid(row = 0, column = 0)
b = Button(frame, text = 'Areee bhai mat')
b.grid(row = 1, column = 1)

root.mainloop()