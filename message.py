from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn GUI')
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion('This is popup', 'Hello this is popup')# Title and then text
    Label(root, text = response).pack()

Button(root, text = "Popup", command = popup).pack()

root.mainloop()