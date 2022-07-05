"""
A program that stores book information:
Title, Author
Year, ISBN

User can:
View all records
Search for an entry
Add an entry
Update an entry
Delete an entry
Close the app
"""

from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple, l5
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    global l5
    l5.destroy()
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
    l5 = Label(window, text="Displaying all records")
    l5.grid(row=2, column=1)

def search_command():
    global l5
    l5.destroy()
    list1.delete(0, END)
    for row in backend.search( title_text.get(), author_text.get(), year_text.get(), isbn_text.get() ):
        list1.insert(END, row)
    if list1.size():
        l5 = Label(window, text="Matching records found")
        l5.grid(row=2, column=1)
    else:
        l5 = Label(window, text="No records found")
        l5.grid(row=2, column=1)


def insert_command():
    global l5
    l5.destroy()
    ### Insert item
    backend.insert( title_text.get(), author_text.get(), year_text.get(), isbn_text.get() )
    ### Show new entry
    list1.delete(0, END)
    for row in backend.search( title_text.get(), author_text.get(), year_text.get(), isbn_text.get() ):
        selected_tuple = row
    list1.insert( END, ( selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) )
    l5 = Label(window, text="Your entry has been added")
    l5.grid(row=2, column=1)
    ### Clear fields
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def update_command():
    global l5
    l5.destroy()
    backend.update( selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get() )
    l5 = Label(window, text="Update successful")
    l5.grid(row=2, column=1)

def delete_command():
    global l5
    l5.destroy()
    backend.delete(selected_tuple[0])
    list1.delete(0, END)
    l5 = Label(window, text="Entry ID {0} has been deleted".format(selected_tuple[0]))
    l5.grid(row=2, column=1)
    for row in backend.view():
        list1.insert(END, row)
        
        
window = Tk()
window.title('Book Store Catalog')


### Create labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

l5 = Label(window, text="")
l5.grid(row=2, column=1)

### Create entry boxes
title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

### Create scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=4, sticky=N+S+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

### Detects listbox selection events
list1.bind('<<ListboxSelect>>', get_selected_row)

### Create buttons
b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.quit)
b6.grid(row=7, column=3)


window.mainloop()