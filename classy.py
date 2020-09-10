from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn GUI')
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')
root.geometry("400x400")


class Elder:

    def __init__(self, master):
        self.myFrame = Frame(master)
        self.myFrame.pack()

        self.mybutton = Button(master, text = 'Click me', command = self.clicker)
        self.mybutton.pack()

    def clicker(self):
        print('Clicked the button')

e = Elder(root)

mainloop()