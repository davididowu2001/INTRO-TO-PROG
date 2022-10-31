import csv
import datetime


def openfile(file):
    '''this function reads any file and is accessed in the search function'''
    book = open(file, 'r')
    read_doc = list(csv.DictReader(book))
    book.close()
    return read_doc

def bookwrite(records):
    '''function writes into the database file'''
    book=open('database.txt', 'w')
    headers='ID,Genre,Title,Author,Purchase Date,Member Id'
    book.write(headers+'\n')
    for record in records:
        rec=""
        for attribute in headers.split(','):
            rec=rec + record[attribute]+','
        rec=rec[:-1]+'\n'
        book.write(rec)
    book.close()
    return bookwrite

def logwrite(records):
    '''this function rewrites the logfile, pls dont rerun this '''
    book=open('logfile.txt', 'w')
    heads='book_id,Checkout_Date,Return_Date,Member_id'
    book.write(heads+'\n')
    for record in records:
        rec=""
        for attribute in heads.split(','):
            rec=rec + record[attribute]+','
        rec=rec[:-1]+'\n'
        book.write(rec)
    book.close()
    return bookwrite

def dateconverter(date):
    '''this function is used to calculate dates which was used for loan periods'''
    days,month,year=date.split("/")
    datecon=datetime.date(year=int(year),month=int(month) ,day=int(days))
    return datecon


