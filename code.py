from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x500")
my_tree = ttk.Treeview(root)

# defining columns
my_tree['columns'] = ("Full name", "Receipt number", "Item being hired", "Amount of items")

# formatting columns
my_tree.column("#0", width=0, stretch=NO, minwidth=25)
my_tree.column("Full name", anchor=W, width=140)
my_tree.column("Receipt number", anchor=CENTER, width=100)
my_tree.column("Item being hired", anchor=W, width=140)
my_tree.column("Amount of items", anchor=E, width=80)

# creating headings for columns
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Full name", text="Full name")
my_tree.heading("Receipt number", text="Receipt number", anchor=W)
my_tree.heading("Item being hired", text="Item being hired", anchor=CENTER)
my_tree.heading("Amount of items", text="Amount", anchor=W)

# adding data
my_tree.insert(parent='', index='end', iid=0, text="", values=("test", 48358, "car", "78") )
# pack to screen
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

# labels
nl = Label(add_frame, text="Full name")
nl.grid(row=0, column=0)

rl = Label(add_frame, text="Receipt number")
rl.grid(row=0, column=1)

il = Label(add_frame, text="Item being hired")
il.grid(row=0, column=2)

al = Label(add_frame, text="Amount")
al.grid(row=0, column=3)

#entry boxes

name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

rl_box = Entry(add_frame)
rl_box.grid(row=1, column=1)

il_box = Entry(add_frame)
il_box.grid(row=1, column=2)

al_box = Entry(add_frame)
al_box.grid(row=1, column=3)

# creating buttons
add_record = Button(root, text="Add record", command=add_record)
add_record.pack(pady=20)

root.mainloop()

