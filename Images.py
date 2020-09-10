from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn GUI')
# only ico files, convert jpg files to ico
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')


my_img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\download.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\download2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\download3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\download4.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text = 'Image 1 of 4', bd = 1, relief = SUNKEN, anchor = E)

mylabel = Label(image = my_img1)
mylabel.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global mylabel
    global button_forward
    global button_back

    mylabel.grid_forget()#grid deletes what ever was present (predefined function)
    mylabel = Label(image = image_list[image_number])
    button_forward = Button(root, text='>>', command = lambda: forward(image_number+1))
    button_back = Button(root, text = '<<', command = lambda: back(image_number))

    if(image_number == 3):
        button_forward = Button(root, text ='>>', state = DISABLED)

    mylabel.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

    ig_no = 1+image_number
    status = Label(root, text = 'Image %s of 4'%(str(ig_no)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

def back(image_number):
    global mylabel
    global button_forward
    global button_back

    mylabel.grid_forget()#grid deletes what ever was present (predefined function)
    mylabel = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text='>>', command = lambda: forward(image_number))
    button_back = Button(root, text = '<<', command = lambda: back(image_number-1))

    if(image_number == 1):
        button_back = Button(root, text ='<<', state = DISABLED)

    mylabel.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

    ig_no = image_number
    status = Label(root, text = 'Image %s of 4'%(str(ig_no)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

button_back = Button(root, text = '<<', command = back, state = DISABLED)
button_exit = Button(root, text = 'Exit Program', command = root.quit)
button_forward = Button(root, text = '>>', command = lambda: forward(1))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 5)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

root.mainloop()