import tkinter
from booksearch import *
bookid=True
# THIS CODE BELONGS TO F127290-DAVID IDOWU
def checkout(memberid,bookid,frame3):
    '''the checkout function takes in 3 parameters, the memberid,
    bookid and frame which is where it is placed in tkinter
    by rewriting into the logfile and database file,
    it changes the data in the the check_out date column to today's data
    and changes the member_id in database file to the memberid input'''

    csvlog=database.openfile('logfile.txt') #logfile
    csvdata=database.openfile('database.txt') #database file

    for row in csvdata:
        #if the bookid is in the databasefile and the memberid isnt an entry(string),
        #then rewrite the memberid and then change checkout date to today's date
        #in the log file
        if bookid == row['ID'] and row['Member Id']=='0':
            row['Member Id']=memberid
            log={'book_id':bookid,'Checkout_Date':datetime.datetime.today().strftime('%d/%m/%Y'),
                 'Return_Date':'0','Member_id':memberid}
            csvlog.append(log)
            database.logwrite(csvlog)#writes into log file
            database.bookwrite(csvdata)#writes into database file
            #display checkout is successful if requirements are met
            tkinter.Label(frame3, text="CHECKOUT SUCCESSFUL")\
                 .place(relx=0.5, rely=0.6, anchor='center')

            break
        #if the bookid isnt in the database file, then display the label info
        else:
            if bookid not in row['ID']:
                tkinter.Label(frame3, text="BOOKID ISN'T IN DATABASE") \
                .place(relx=0.5, rely=0.6, anchor='center')


#testing the checkout function
if __name__=='__main__':

    root = tkinter.Tk()
    checkout("fave", "7",root)
    root.mainloop()










