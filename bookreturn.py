import database
import tkinter
import datetime
loan_period=0
# THIS CODE BELONGS TO F127290-DAVID IDOWU
def returnbook(frame5,bookid):
    '''Returnbook function takes in the bookid and checks
     if book hasnt been returned yet. loan period is also calculated.
     if the return date is 0, then it replaces
     it with the member id of who checked the book. also displays a warning
     message if loan period is more than 60 days'''
    bookid=str(bookid)#makes bookid a string so i can input in the tkinter file
    av=False#av is created as an indicator to display labels
    csvlog = database.openfile('logfile.txt')#open logfile
    csvdata=database.openfile('database.txt')#open databasefile

    for data in csvdata:
        # change memberid to 0 in the database file if the bookid is matched
        if data['ID']==bookid:
            data['Member Id']='0'
            database.bookwrite(csvdata)
            break
    for r in csvlog:
        #if bookisnt returned , change return date to today's date.
        if r['Return_Date']=='0' and r['book_id']==bookid:
            r['Return_Date']=datetime.datetime.today().strftime("%d/%m/%Y")
            return_date=database.dateconverter(r['Return_Date'])
            checkoutdate=database.dateconverter(r['Checkout_Date'])
            av = True
            # loan period is calculated,and if its more than
            # 60days then show warning
            loan_period=(return_date-checkoutdate).days
            if loan_period>60:
                tkinter.Label(frame5,text="Loan period is more than "
                                          "60 days.loan period: "+
                                          str(loan_period))\
                    .place(relx=0.5, rely=0.6,anchor='center')#warning message
            return database.logwrite(csvlog)#rewrite log file
    if av== False:
            #if r['Return_Date']!='0' and bookid in r['book_id']:
        tkinter.Label(frame5, text="CHECK BOOKID AGAIN " )\
        .place(relx=0.5, rely=0.6, anchor='center')


#testing return function
if __name__=='__main__':
    'this test code returns abook' \
    'by filing in the parameters, right now it displays an ' \
    'error message telling the user that book is already present in db'

    root = tkinter.Tk()
    returnbook(root, "7")
    root.mainloop()













