from tkinter import *
from DataProcessing import Database

#Initialize Database Object
database = Database("library.db")

#Retrieve data from selected row in library UI
def getSelection(event):
    try:
        global selectedTuple
        selectedTuple = dataListBox.get(dataListBox.curselection()[0])
        titleEntry.delete(0,END)
        titleEntry.insert(END,selectedTuple[1])
        authorEntry.delete(0, END)
        authorEntry.insert(END,selectedTuple[2])
        yearEntry.delete(0, END)
        yearEntry.insert(END,selectedTuple[3])
        isbnEntry.delete(0, END)
        isbnEntry.insert(END,selectedTuple[4])
    except IndexError:
        pass

#List all books currently in library
def viewExecute():
    dataListBox.delete(0,END)
    for row in database.view():
        dataListBox.insert(END, row)

#List book that matches certain search criteria
def searchExecute():
    dataListBox.delete(0,END)
    for row in database.search(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get()):
        dataListBox.insert(END, row)

#Add book to library
def addExecute():
    if titleValue.get() != '' and not titleValue.get().isspace() :
        database.insert(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
        dataListBox.delete(0,END)

#Delete book from library
def deleteExecute():
    try:
        database.delete(selectedTuple[0])
    except:
        pass

#Update book fields
def updateExecute():
    try:
        database.update(selectedTuple[0],titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
    except:
        pass


#Create UI for Library App using tkinter
database.view()
window = Tk()

window.wm_title("Library")

titleLabel = Label(window, text = "Title")
titleLabel.grid(row = 0, column = 0)
authorLabel = Label(window, text="Author")
authorLabel.grid(row=0, column=3)
yearLabel = Label(window, text="Year")
yearLabel.grid(row=1, column=0)
isbnLabel = Label(window, text="ISBN")
isbnLabel.grid(row=1, column=3)

titleValue = StringVar()
titleEntry = Entry(window, textvariable=titleValue)
titleEntry.grid(row=0, column=1)

authorValue = StringVar()
authorEntry = Entry(window, textvariable=authorValue)
authorEntry.grid(row=0, column=4)

yearValue = StringVar()
yearEntry = Entry(window, textvariable=yearValue)
yearEntry.grid(row=1, column=1)

isbnValue = StringVar()
isbnEntry = Entry(window, textvariable=isbnValue)
isbnEntry.grid(row=1, column=4)


dataListBox = Listbox(window, height = 6, width = 35)
dataListBox.grid(row = 3, column = 0, rowspan = 6, columnspan = 2)

dataScrollBar = Scrollbar(window)
dataScrollBar.grid(row = 3, column = 2, rowspan = 6)

dataListBox.configure(yscrollcommand = dataScrollBar.set)
dataScrollBar.config(command = dataListBox.yview)

dataListBox.bind('<<ListboxSelect>>', getSelection)


viewAllButton = Button(window, text = "View All", width = 12, command = viewExecute)
viewAllButton.grid(row = 3, column = 4)

searchButton = Button(window, text="Search Entry", width=12, command = searchExecute)
searchButton.grid(row=4, column=4)

AddButton = Button(window, text="Add Entry", width=12, command = addExecute)
AddButton.grid(row=5, column=4)

updateButton = Button(window, text="Update", width=12, command = updateExecute)
updateButton.grid(row=6, column=4)

deleteButton = Button(window, text="Delete", width=12, command = deleteExecute)
deleteButton.grid(row=7, column=4)

closeButton = Button(window, text="Close", width=12, command = window.destroy)
closeButton.grid(row=8, column=4)

window.mainloop()
