import datetime
import database
# THIS CODE BELONGS TO F127290-DAVID IDOWU

def Searchbook(search):
    '''The Searchbook function opens the database file, logfile
    and loops through each line in the database file and searches for
    books based on their title or author. I figured out it will be
    more efficient to search for a book based on author also rather
    then just title. it also displays all information about the book
    including the loan period if it is currently on loan.
    '''
    search = search.lower()#allows capital or small letter entries
    listt = [] #created to contain details of the book
    csv_reader = database.openfile('database.txt')#opens database file
    csv_log = database.openfile('logfile.txt')#opens logile
    current_date = database.dateconverter(datetime.datetime.today()
                                          .strftime('%d/%m/%Y')) #today's date
    length=len(search)
    for row in csv_reader: # this iterates through database file
        title=row["Title"].lower() #allows capital or small letter entries
        author=row["Author"].lower()#allows capital or small letter entries
        if title[:length]  == search or author[:length]==search:
            #if the search has the same letters as the title or book author,
            # add book details to the list,with the number of days its on loan
            loanperiod = 0
            # iterates through log file and gets the checkout  and return date
            for date in csv_log:

                if date['book_id'] == row['ID']:
                    Checkout_Date = database.dateconverter(date['Checkout_Date'])
                    Return_Date = date['Return_Date']
            #if the book hasn't been returned then calculate the loan period
                    if Return_Date == '0':
                        loanperiod = current_date - Checkout_Date
                        loanperiod = loanperiod.days
            # if loanperiod>60:
            listt.append((row, loanperiod))
    return listt #outputs the book details


#testcode
if __name__=='__main__':
    '''test code to search for a book in db, this is the output :'''
    '''[({'ID': '1', 'Genre': 'Manga', 'Title': 'Tokyo Ghoul', 'Author': 'Kishimoto', 'Purchase Date': '12/09/1999', 'Member Id': '0'}'''

    print(Searchbook("tokyo ghoul"))