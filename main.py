
# Import Module
from tkinter import *


def clicked():
    res = "You wrote" + txt.get()
    lbl.configure(text=res)
    if check_var.get() == 1:
        print("Check box is checked")
    else:
        print("Check box is not checked")


# create root window
root = Tk()
check_var = IntVar()
check_box = Checkbutton(root, text="Check me", variable=check_var)
check_box.grid(column=0, row=1)
# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text="Are you a Geek?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)


# function to display user text when
# button is clicked
def clicked():
    res = "You wrote" + txt.get()
    lbl.configure(text=res)


# button widget with red color text inside
btn = Button(root, text="Click me",
             fg="red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()
