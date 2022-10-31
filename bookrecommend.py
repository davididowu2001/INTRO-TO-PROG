import tkinter
from tkinter import ttk
import database
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from tkinter import *
# THIS CODE BELONGS TO F127290-DAVID IDOWU
def Recommend(frame7,memberid):
    '''this function takes the memberid and recommends books based on
    books previously read. if the user is new, it displays the most read books
    otherwise it displays books in the same genre that has been read
    function also creates a barchart showing user's past data on books
    they have read , making it easier for the librarian to recommend'''
    #opens both files
    csvlog = database.openfile('logfile.txt')
    csvdata = database.openfile('database.txt')
    Genre = {}#dictionary to contain Genre of books
    popular = {} #popular books
    Recommended_books = []
    popular_for_user = {}# this contains the most popular books read by people
    listt=[]
    listv=[]
    for log in csvlog:
        #this iterates through both files and gets genre of books accessed bu users
        bookid = log['book_id']
        if log['Member_id'] == memberid:
            for book in csvdata:
                if bookid == book['ID']:

                    Genre[book['Genre']] = Genre.get(book['Genre'], 0) + 1

            # adds most popular boooks to the dict popular_for_user
            popular_for_user[bookid] = popular_for_user.get(bookid, 0) + 1
        popular[bookid] = popular.get(bookid, 0) + 1
    if popular_for_user == {}:#if the user is a new user...
        collectionofbooks = popular
        tag = "ID"
        for b in collectionofbooks.keys():
            if len(listt)<10: #limiting number of books to 10
                listt.append(b)

        yaxis = listt #y axis plots IDs on the yaxis of the bar chart

        for x in collectionofbooks.values():#these are the frequeny of access of each book
            if len(listv) < 10:
                listv.append(x)

        xaxis = listv#xaxis plots the frequency of the access to books on x axis of the bar chart
    elif len(popular_for_user)<3:
        #if the user hasnt read up to 3 books then recommend as if they are a new user
        collectionofbooks = popular
        tag = "ID"
        for b in collectionofbooks.keys():
            if len(listt) < 10:
                listt.append(b)
        yaxis = listt
        for x in collectionofbooks.values():
            if len(listv) < 10:
                listv.append(x)
        xaxis = listv
    else:
        #if the user is a present user, then recommend books based on genre
        collectionofbooks = Genre #this contains genre of each book
        tag = "Genre"
        #best Genre is the genre which has been read the most, which is the most useful
        bestGenre=max((count, genre) for genre, count in Genre.items())[1]

        for book in csvdata:
            #this dispplays books that havent been read by user but are in the same genre
            if book['Genre']==bestGenre and book["ID"] not in popular_for_user:
                Recommended_books.append(book)

        yaxis = list(popular_for_user.keys())
        xaxis = list(popular_for_user.values())
    labels = sorted(collectionofbooks.items(), key=lambda t: t[1]
                    , reverse=True)  # books are sorted in most read genre
    labels = [id for id, _ in labels]


    for label in labels:
        for book in csvdata:
            # this dispplays books(but ID) that havent been read by user but are in the same genre
            if book[tag] == label and book['Title'] not in Recommended_books:
                if book not in Recommended_books:
                    Recommended_books.append(book)
    #tkinter bit
    children = frame7.winfo_children()


    if children:
        view = children[0]
        view.destroy()

    figure=Figure(figsize=(4,4), dpi=70)
    plot1 = figure.add_subplot(2,1,1)
    plot2 = figure.add_subplot(2,1,2)
    plot1.set_ylabel("Bookid")
    plot2.set_ylabel('Genre')
    columns = ('ID','Genre','Title','Author')
    recommendview = ttk.Treeview(frame7, columns=columns, show='headings')
    for column in columns:
        recommendview.heading(column, text=column, anchor=W)
    for book in Recommended_books[: 10]:
        values = [book[key] for key in columns]
        recommendview.insert('', 0, values=values)
    plot1.barh(yaxis, xaxis,color='red')
    plot2.barh(list(Genre.keys()), list(Genre.values()))
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(figure,
                               master=frame7)
    canvas.draw()
    # placing the toolbar on the Tkinter window

    canvas.get_tk_widget().place(relx=0.5,rely=0.3,width=900,height=450,anchor='center')
    recommendview.pack()
    recommendview.place(rely=0.65)

#test code
if __name__=='__main__':

    root = tkinter.Tk()
    Recommend(root, "7")
    root.mainloop()



