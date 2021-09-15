from tkinter import *
from tkinter import ttk
root = Tk()

my_tree = ttk.Treeview(root)

# defining columns
my_tree['columns'] = ("Full name", "Receipt number", "Item being hired", "Amount of items")

# formatting columns
my_tree.column("#0", width=0, minwidth=25,)
my_tree.column("Full name", anchor=W, width=120)
my_tree.column("Receipt number", anchor=CENTER, width=120)
my_tree.column("Item being hired", anchor=W, width=120)
my_tree.column("Amount of items", anchor=E, width=80)

# creating headings for columns
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Full name", text="Full name")
my_tree.heading("Receipt number", text="Receipt number", anchor=W)
my_tree.heading("Item being hired", text="Item being hired", anchor=CENTER)
my_tree.heading("Amount of items", text="Amount of items", anchor=W)

# adding data
my_tree.insert(parent='', index='end', iid=0, text="Parent", values=("test", 48358, "car", "78") )
my_tree.pack(pady=20)
root.mainloop()

