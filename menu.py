import os
# THIS CODE BELONGS TO F127290-DAVID IDOWU
import time #will use this to display a clock on my tkinter menu
from tkinter import * #import all attributes of tkinter
from tkinter import ttk #this is to allow me use treeview
import csv #imports csv to access my database file
from bookcheckout import * #grants access to checkout module
from bookreturn import *#grants access to return module
from bookrecommend import *#grants access to recommend module
#today's date which will be displayed on the screen
todays_date = datetime.datetime.now()

frame = Tk()#this calls or instantiates tkinter
frame.title('D-LIBRARY') #title at the top of the menu
frame.configure(background='black')#sets the background of the menu to black
# using the notebook frames to create tabs
note_book = ttk.Notebook(frame)
note_book.pack()

# creating frames
frame1 = Frame(note_book, width=1500, height=700, bg='black')
frame2 = Frame(note_book, width=1500, height=700, bg='white')
frame3 = Frame(note_book, width=1500, height=700, bg='black')
frame4 = Frame(note_book, width=1500, height=700, bg='white')
frame5 = Frame(note_book, width=1500, height=700, bg='black')
frame6 = Frame(note_book, width=1500, height=700, bg='black')
frame7 = Frame(note_book, width=1500, height=700, bg='black')
#placing frames on screen
frame1.pack(fill='both', expand=3)
frame2.pack(fill='both', expand=3)
frame3.pack(fill='both', expand=3)
frame4.pack(fill='both', expand=3)
frame5.pack(fill='both', expand=3)
frame6.pack(fill='both', expand=3)
frame7.pack(fill='both', expand=3)

# adding Tabs to notebook

note_book.add(frame1, text='Search')
note_book.add(frame2, text='Book-list')
note_book.add(frame3, text='Check-book')
note_book.add(frame4, text='Log-list')
note_book.add(frame5, text='Book return')
note_book.add(frame6, text='Book Recommend')
note_book.add(frame7, text='Recommend Graph')

#clock on screen
def timehour(): #function to create clock
    '''this function creates a clock on my search screen
    the clock is digital and counts in seconds which can also be seen
    the librarian could use this to check how long they has been using it'''
    clock.config(text=time.strftime("%I:%M:%S"))
    clock.after(1000,timehour) #makes clock physically count on screen
    return clock
clock=Label(frame1,bg='black',fg="gold",font=("Italics",30))
clock.pack()#places clock on the screen
timehour()#calls the function


# FUNCTIONS FOR NAVIGATION BUTTONS

def foreward1(): #moves to next screen
    note_book.select(1)
def previous():#moves to previous screen
    note_book.select(0)
def previous2():#moves to previous screen
    note_book.select(1)
def forward2():#moves to next screen
    note_book.select(2)
def forward3():#moves to next screen
    note_book.select(3)
def forward4():#moves to next screen
    note_book.select(4)
def previous3():#moves to previous screen
    note_book.select(2)
def previous5():#moves to previous screen
    note_book.select(4)
def previous4():#moves to previous screen
    note_book.select(3)
def forward5():#moves to next screen
    note_book.select(5)
#NAVIGATION BUTTON CREATION
navigatebutton = Button(frame1, text='>', command=foreward1, bg='gold')#creates button
navigatebutton.place(relx=0.95, rely=0)#places on button on screen
navigatebutton = Button(frame2, text='<', command=previous, bg='gold')#creates button
navigatebutton.place(relx=0.95, rely=0)#places on button on screen
navigatebutton = Button(frame3, text='<', command=previous2, bg='gold')#creates button
navigatebutton.place(relx=0.95, rely=0)#places on button on screen
navigatebutton = Button(frame2, text='>', command=forward2, bg='gold')#creates button
navigatebutton.place(relx=0.97, rely=0)#places on button on screen
navigatebutton = Button(frame3, text='>', command=forward3, bg='gold')#creates button
navigatebutton.place(relx=0.97, rely=0)#places on button on screen
navigatebutton = Button(frame4, text='>', command=forward4, bg='gold')#creates button
navigatebutton.place(relx=0.97, rely=0)#places on button on screen
navigatebutton = Button(frame4, text='<', command=previous3)#creates button
navigatebutton.place(relx=0.95, rely=0)#places on button on screen
navigatebutton = Button(frame5, text='<', command=previous4)#creates button
navigatebutton.place(relx=0.95, rely=0)#places on button on screen
navigatebutton = Button(frame6, text='<', command=previous5)#creates button
navigatebutton.place(relx=0.95, rely=0)#places on button on screen
navigatebutton = Button(frame5, text='>', command=forward5)#creates button
navigatebutton.place(relx=0.97, rely=0)#places on button on screen

# HEADING
lab = Label(frame1, text='Welcome to D-Library ', font='100', fg='gold', bg='black')\
    .place(relx=0.5, rely=0.6, anchor='center')
# BOOKLIST
#this adds the all the books to the tkinter
tableframe = Frame(frame2, width=1500, height=700)
tableframe.pack()
#scrollbars
scrollhorizon = Scrollbar(tableframe, orient=HORIZONTAL)
scrollvert = Scrollbar(tableframe, orient=VERTICAL)
#treeview for all the books
headers = ttk.Treeview(tableframe, columns=('ID', 'Genre', 'Title', 'Author',
 'Purchase Date', 'Member Id'), height=400,selectmode="none",
#scrollbar commands
yscrollcommand=scrollvert.set,xscrollcommand=scrollhorizon.set)
scrollhorizon.config(command=headers.xview)#this sets the scroll bars in place
scrollhorizon.pack(side=RIGHT, fill=Y)
scrollvert.pack(side=BOTTOM, fill=X)
scrollvert.config(command=headers.yview)
#headers are just basically each bookdetails which will be displayed at the top
headers.heading("ID", text='ID', anchor=W)
headers.heading("Genre", text='Genre', anchor=W)
headers.heading("Title", text='Title', anchor=W)
headers.heading("Author", text='Author', anchor=W)
headers.heading("Purchase Date", text='Purchase Date', anchor=W)
headers.heading("Member Id", text='Member Id', anchor=W)

headers.column('#0', stretch=YES, width=50)
headers.column('#1', stretch=YES, width=50)
headers.column('#2', stretch=NO, width=200)
headers.column('#3', stretch=NO, minwidth=100, width=200)
headers.column('#4', stretch=NO, minwidth=100, width=200)
headers.column('#5', stretch=YES, width=200)

headers.pack()
#this opens the database file, iterates through
#and adds the, into each header (basically their details)
with open('database.txt', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ID = row['ID']
        Genre = row['Genre']
        Title = row['Title']
        Author = row['Author']
        Purhcase = row['Purchase Date']
        Memberid = row['Member Id']
        headers.insert('', 0, values=(ID, Genre, Title, Author, Purhcase, Memberid))
        for i in row:
            if loan_period>60:
                headers.insert('', 0, values=(ID, Genre, Title,
                        Author, Purhcase, Memberid),fg='green')

frame.geometry('800x700')
tags=("highlight")

##LOGFILE
#REFRESH BUTTON
def refresh():
    '''this function exists the menu screen and reopens it
    hence reloading the logfile page as it doesn't automatically do that'''
    frame.destroy()
    os.popen("menu.py")
#REFRESH BUTTON CREATION
button=Button(frame4,text="↺",command=refresh)
button.place(relx=0.9,rely=0)#display button on screen


tableframe = Frame(frame4)
tableframe.pack()

scrollvert = Scrollbar(tableframe, orient=VERTICAL)

headers = ttk.Treeview(tableframe, columns=('book_id', 'Checkout_Date',
'Return_Date', 'Member_id'), height=200,yscrollcommand=scrollvert.set)

scrollvert.pack(side=BOTTOM, fill=X)
scrollvert.config(command=headers.yview)
headers.heading("book_id", text='book_id', anchor=W)
headers.heading("Checkout_Date", text='Checkout_Date', anchor=W)
headers.heading("Return_Date", text='Return_Date', anchor=W)
headers.heading("Member_id", text='Member_id', anchor=W)

headers.column('#0', stretch=YES, width=50)
headers.column('#1', stretch=YES, width=50)
headers.column('#2', stretch=NO, width=100)
headers.column('#3', stretch=NO, minwidth=100, width=100)
headers.column('#4', stretch=NO, minwidth=100, width=200)
headers.pack()

with open('logfile.txt', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ID = row['book_id']
        CD = row['Checkout_Date']
        RD = row['Return_Date']
        MID = row['Member_id']
        headers.insert('', 0, values=(ID, CD, RD, MID))

# BOOKSEARCH
#creates date and places on screen
label = Label(frame1, text=f"{todays_date:%A, %B %d, %Y}", font="10", bg="black", fg="gold")
label.place(relx=0.8, rely=0.8, anchor='center')
#creates searchbar
searchbar = Entry(frame1, width=50, fg='blue', relief=SUNKEN, textvariable=StringVar)
searchbar.place(relx=0.5, rely=0.5, anchor='center')
searchbar.bind('<KeyRelease>', lambda _: entry()) #automatically searches for the book
#creates treeview and divides it into columns
columntitles = ttk.Treeview(frame1, columns=('ID', 'Genre', 'Title', 'Author', 'Purchase Date', 'Member Id'))
columntitles.heading("ID", text='ID', anchor=W)
columntitles.heading("Genre", text='Genre', anchor=W)
columntitles.heading("Title", text='Title', anchor=W)
columntitles.heading("Author", text='Author', anchor=W)
columntitles.heading("Purchase Date", text='Purchase Date', anchor=W)
columntitles.heading("Member Id", text='Member Id', anchor=W)
#creates cloumns
columntitles.column('#0', stretch=YES, minwidth=0, width=0)
columntitles.column('#1', stretch=YES, minwidth=0, width=50)
columntitles.column('#2', stretch=YES, minwidth=0, width=80)
columntitles.column('#3', stretch=YES, minwidth=0, width=120)
columntitles.column('#4', stretch=NO, minwidth=0, width=100)
columntitles.column('#5', stretch=NO, minwidth=0, width=100)
columntitles.pack()
columntitles.focus()



def loopbooks(individualbook):
    '''this function inserts the books into the treeview
    but if the loan period of the book is more than
    60 days , it highlights the book in a red font
    and makes it bold'''
    for book, loanperiod in individualbook:
        colour = 'black'

        if 60 < loanperiod:
            colour = 'red'#if loan period is more than 60 days

        columntitles.insert('', 'end', iid=book['ID'], tags=[colour], values=(
            book['ID'], book['Genre'], book['Title'], book['Author'], book['Purchase Date'], book['Member Id']))

    columntitles.tag_configure('red', foreground='#990000',font=("",10,"bold"))

def entry():
    '''this function iterates through each book and applies the search function
    hence searches for each book based on the users entry'''
    for book in columntitles.get_children():
        columntitles.delete(book)
    search = searchbar.get()
    books = Searchbook(search)

    loopbooks(books)


def temporarytext(e):
    '''function deletes a temporary message from an entry'''
    searchbar.delete(0,"end")

searchbar.insert(0, "Enter book name or Author ")
searchbar.bind("<FocusIn>", temporarytext)#binds text to make it temporary

# CHECKBOOK MENU
#creates date label on the screen
label = Label(frame3, text=f"{todays_date:%A, %B %d, %Y}", font="10", bg="gold")
label.place(relx=0.8, rely=0.8, anchor='center')
#creates entry for memberid
memberid = Entry(frame3, width=50, fg='blue', relief=SUNKEN)
memberid.place(relx=0.5, rely=0.5, anchor='center')
#creates labels for memberid and bookid
memblabel = Label(frame3, text='Enter memberId', bg='gold').place(relx=0.25, rely=0.5, anchor='center')
booklabel = Label(frame3, text='Enter BookId', bg='gold').place(relx=0.25, rely=0.4, anchor='center')
#creates book id Entry tab
bookid = Entry(frame3, width=50, fg='black', relief=SUNKEN)
bookid.place(relx=0.5, rely=0.4, anchor='center')#places bookid entry on screen

def checkbuttonentry():
    '''this function sets the conditions for the users entries, if the id is
    less than 4 charcters, then it displays an error, or if it is not available
    it displays an error, otherwise it checkout the book and calls the
    return_screen function which updates the return screen'''
    memberide = memberid.get()#memberid entry
    bookide = bookid.get() #boodid entry
    if len(memberide)!=4: #if memberid is not 4 characters long
        errormessage = Label(frame3, width=50, text="Member id must be 4 characters")
        errormessage.place(relx=0.5, rely=0.6,anchor='center')
    elif memberide=='0': #if book is currently on loan, display an error
        errormessage=Label(frame3,width=50,text="Book is on currently on loan")
        errormessage.place(relx=0.5, rely=0.6,anchor='center')
    else:#otherwise, checkout the book and update return screen
        output= checkout(memberide, bookide,frame3)
        returnscreen()
        return output
#creates checkout button
checkbutton = Button(frame3, text='Checkout Book', width=12, relief=RAISED, command=checkbuttonentry)
checkbutton.place(relx=0.5, rely=0.7, anchor='center')


#RETURN MENU
#displays date on menu screen
label = Label(frame5, text=f"{todays_date:%A, %B %d, %Y}", font="10", bg="gold")
label.place(relx=0.8, rely=0.8, anchor='center')
def Returnboook():
    '''function calls the returnbook function from bookreturn.py
    '''
    for b in returnview.selection():
        # displays books on screen if they need to be returned
        returnbook(frame5,b)
    returnscreen()


def refresh_return():
    '''this function refreshes the return screen after another book
    is checked out'''
    Returnboook()
    returnscreen()
#creates the refresh button
returnbutton = Button(frame5, text='Return Book', width=10, relief=RAISED, command=refresh_return)
returnbutton.place(relx=0.5, rely=0.8, anchor='center')
#creating the treeview for return books
returnview = ttk.Treeview(frame5, columns=('ID', 'Title', 'Member Id'))
returnview.heading("ID", text='ID', anchor=W)
returnview.heading("Title", text='Title', anchor=W)
returnview.heading("Member Id", text='Member Id', anchor=W)
returnview.column('#0', stretch=YES, minwidth=0, width=0)
returnview.column('#1', stretch=YES, minwidth=0, width=100)
returnview.column('#2', stretch=YES, minwidth=0, width=100)
returnview.column('#3', stretch=YES, minwidth=0, width=100)
returnview.pack()
#this inserts the books in the frame on tkinter
def returnloopbooks(individualbook):
    '''this function inserts the books into the treeview frame if and only if
    they haven't been returned'''
    for book,_ in individualbook:
        if book["Member Id"] !="0":#conditional statement for if book isnt returned
            returnview.insert('', 'end', iid=book['ID'], values=(
            book['ID'],  book['Title'], book['Member Id']))

def returnscreen():
    '''this function gets the values in the treeview .which are the main reocrds
     of the boook and clears it after a book has been returned'''
    for i in returnview.get_children():
        returnview.delete(i)
    books = Searchbook("")
    returnloopbooks(books)

returnscreen()
#Recommend
#places recommend entry on screen
recomm_memberide = Entry(frame6, width=50, fg='blue', relief=SUNKEN,
textvariable=StringVar)
recomm_memberide.place(relx=0.5, rely=0.5, anchor='center')
recomm_memberid = Label(frame6, text='Enter memberId', bg='gold').place(relx=0.25, rely=0.5, anchor='center')

# Create Label to display the Date
label = Label(frame6, text=f"{todays_date:%A, %B %d, %Y}", font="10", bg="gold")
label.place(relx=0.8, rely=0.8, anchor='center')

def select_reco():
    '''function displays the graph screen after getting member id'''
    memb = recomm_memberide.get()

    note_book.select(frame7)


def recommend():
    '''this function calls the recommend function from bookrecommend.py if and
    only if it meets the criteria for member id or else error messages are
    displayed'''
    errormessage = Label(frame6, width=50)
    errormessage.place(relx=0.5, rely=0.4, anchor='center')
    memb=recomm_memberide.get()
    recomm_memberide.delete(0,"end")
    if len(memb)==4: #if member id is up to 4 characters call select reco function
        errormessage.configure(text="")
        select_reco()

        return Recommend(frame7, memb)
    else:#display error message
        errormessage.configure(text="Member id must be 4 characters")

def temporarytext(e):
    '''function to delete temporary text on memberid entry'''
    recomm_memberide.delete(0,"end")

#recommend button created and calls the recommend function
recommendbut = Button(frame6, text='Recommend', width=10, relief=RAISED, command=recommend)
recommendbut.place(relx=0.5, rely=0.8, anchor='center')
recomm_memberide.bind()
recomm_memberide.insert(0, "Enter Memberid ") #display temporary message on entrybar
#calls the temportary function and bind it to the entry
recomm_memberide.bind("<FocusIn>", temporarytext)




frame.mainloop()

