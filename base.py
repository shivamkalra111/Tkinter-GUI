from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn GUI')
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')

def open():
    global my_img
    top = Toplevel()
    #label = Label(top, text = 'Hey there!').pack()
    my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\download.jpg"))
    label = Label(top, image = my_img).pack()
    button2 = Button(top, text = 'Close', command = top.destroy)
    button2.pack()


button = Button(root, text = 'Clck to open the image', command = open)
button.pack()



mainloop()