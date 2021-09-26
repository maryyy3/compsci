from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Julies party hire')
root.geometry("900x600")

# add style and theme
style = ttk.Style()
style.configure("Treeview",
                background="lightblue",
                foreground="black",
                rowheight=25,
                fieldbackground="silver"
                )
# theme
style.theme_use('default')

# change selected colour
style.map('Treeview',
          background=[('selected', 'grey')])

# creating a frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

#creating gui using treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

#config scroll bar
tree_scroll.config(command=my_tree.yview)


# defining columns
my_tree['columns'] = ("Full name", "Receipt number", "Item being hired", "Amount of items")

# formatting columns
my_tree.column("#0", width=0, stretch=NO, minwidth=25)
my_tree.column("Full name", anchor=W, width=140)
my_tree.column("Receipt number", anchor=CENTER, width=100)
my_tree.column("Item being hired", anchor=W, width=140)
my_tree.column("Amount of items", anchor=E, width=90)

# creating headings for columns
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Full name", text="Full name", anchor=CENTER)
my_tree.heading("Receipt number", text="Receipt number", anchor=CENTER)
my_tree.heading("Item being hired", text="Item being hired", anchor=CENTER)
my_tree.heading("Amount of items", text="Amount", anchor=CENTER)

# add test data
data = [
    ["mary", 1782, "tables", 78],
    ["john", 3822, "chairs", 125]
]

# create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0
count += 1

# adding data
# my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]))

# pack to screen
my_tree.pack(pady=20)


# labels and entry boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

nl = Label(data_frame, text="Full name")
nl.grid(row=0, column=0, padx=10,pady=10)
nl_box = Entry(data_frame)
nl_box.grid(row=1, column=0)

rl = Label(data_frame, text="Receipt number")
rl.grid(row=0, column=1, padx=10, pady=10)
rl_box = Entry(data_frame)
rl_box.grid(row=1, column=1, padx=10,pady=10)

il = Label(data_frame, text="Item being hired")
il.grid(row=0, column=2, padx=10, pady=10)
il_box = Entry(data_frame)
il_box.grid(row=1, column=2, padx=10,pady=10)

al = Label(data_frame, text="Amount")
al.grid(row=0, column=3, padx=10,pady=10)
al_box = Entry(data_frame)
al_box.grid(row=1, column=3,padx=10,pady=10)


# add record
def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text="",
                   values=(nl_box.get(), rl_box.get(), il_box.get(), al_box.get()))
    count += 1

    # clear boxes
    nl_box.delete(0, END)
    rl_box.delete(0, END)
    il_box.delete(0, END)
    al_box.delete(0, END)


# remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


# remove one selected
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)



# creating buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

# add record
add_record = Button(button_frame, text="Add record", command=add_record)
add_record.grid(row=0, column=1, padx=10, pady=10)

#update record
update_record = Button(button_frame, text="Update record")
update_record.grid(row=0, column=2, padx=10, pady=10)

#move records up
move_up = Button(button_frame, text="Move Up" )
move_up.grid(row=0, column=3, padx=10, pady=10)

#move records down
move_down = Button(button_frame, text="Move Down" )
move_down.grid(row=0, column=4, padx=10, pady=10)


# remove all
remove_all = Button(button_frame, text="Remove all records", command=remove_all)
remove_all.grid(row=0, column=5, padx=10, pady=10)

# remove only one
remove_one = Button(button_frame, text="Remove one selected", command=remove_one)
remove_one.grid(row=0, column=6, padx=10, pady=10)

root.mainloop()
