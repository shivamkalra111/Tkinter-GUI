from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learn GUI')
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')

def open():
    global my_img
    
    root.filename = filedialog.askopenfilename(initialdir = "C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter",
    title = "Select a File", filetypes = (("jpg files", "*jpg"),("all files", "*.*")))

    #label = Label(root, text = root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(image = my_img).pack()

button = Button(root, text = "Open File", command = open).pack(anchor = S)

root.mainloop()