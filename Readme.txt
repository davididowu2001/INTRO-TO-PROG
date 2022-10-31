# THIS CODE BELONGS TO F127290-DAVID IDOWU
My library management system works similar to online libraries i have used previously.


Searchtab: as you type it automatically searches, when you clear the entry bar, it displays all books,
feel free to scroll and books overdue are displayed in Red(IF IT DOESNT SHOW , ITS PROBABLY DUE TO YOUR PYTHON BEING A OLD VERSION)
There is a clock and date is displayed on screen

Checkout menu works as described in spec
Return Menu; is a bit different, you can return multiple books by Ctrl+click and books that need to
be retruned are displayed on the screen. to retrun, click on the book and click the button
Recommend Menu ; displays two graphs after the Member Id has been entered, 1 displays books read
and the other displays Genre red. if the user is new obviously, no genre will be displayed but most popluar books will be on the graph

the table below shows recommended books

I also have two extra tabs , the logfile tab, displays the log and has a refresh button, which refreshes the logfile on the screen
as i couldn't do that previously

the booklist file contains all books in the database

test code is at the end of each file,IF YOU RUN EACH FILE AND IT SHOWS A MENU, ITS BECAUSE TKINTER IS IMPLEMENTED IN THE TEST CODE,I'LL SAY OPEN THE FILE WITH AN IDE
AND CHANGE THE BOOKID TO CHECK OUT ANOTHER BOOK IN THE TEST CODE
