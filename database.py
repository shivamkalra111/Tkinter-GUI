from tkinter import *
from PIL import ImageTk, Image
import sqlite3
# sqlite3 has only 5 datatypes


root = Tk()
root.title('Learn GUI')
root.iconbitmap('C:\\Users\\ealihks\\Desktop\\My Own Work\\GUI Application\\Tkinter\\icon.ico')
root.geometry("400x400")

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#create cursor
cur = conn.cursor()

'''
#create table
cur.execute("""CREATE TABLE adresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")

'''

#create submit function
def submit():

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #create cursor
    cur = conn.cursor()

    #Insert into Table
    cur.execute("Insert into adresses values (:f_name, :l_name, :address, :city, :state, :zipcode)",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
    }
    
    
    )


    #commit changes
    conn.commit()

    #close connection
    conn.close()



    #Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #create cursor
    cur = conn.cursor()

    #Insert into Table
    cur.execute("select *, oid from adresses")
    data = cur.fetchall()

    print_rec = ''
    for record in data:
        print_rec += str(record) + '\n'

    q_label = Label(root, text = print_rec)
    q_label.grid(row = 8, column = 0, columnspan = 2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()


f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)

#create text box labels

f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "First Name")
zipcode_label.grid(row = 5, column = 0)

#Create Submit Button
submit_btn = Button(root, text = "Add Record to database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#Create a query Button
query_button = Button(root, text = 'Show Records', command = query)
query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)


#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()