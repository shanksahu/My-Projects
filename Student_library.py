class Library():
    data = []

    def __init__(self, books):
        self.books = books #ye books hi hmara list rhega

    def ShowListOfBooks(self):
        for books in self.books:
            print(" *", books)

    def BorrowBook(self,BookName):
        if BookName in self.books:
            print(f"The book {BookName} has been issued to you. Please return on time. Enjoy the book!")
            self.books.remove(BookName)
            self.data.append(f"The book '{BookName}' has been issued.")
            return self.books
        else:
            print("Sorry! This book is either not available or alrady has been issued to someone. Please  wait untill avaible or return")

    def ReturnBook(self, BookName):
        print("The book has been return/add sucessfully. Thank You!")
        self.books.append(BookName)
        if BookName in self.data:
            self.data.remove(BookName)
        return self.books
    
    def __str__(self):
        return self.Library

class student():
 
    def request(self):
        self.book = input("Enter the Book name you want to borrow: ")
        return self.book
    
    def ReturnBook(self):
        self.book = input("Enter the Book name With  you want to return/add: ")
        return self.book

    def __str__(self):
        return self.userList
    
msg='''\n*****Welcome to IAS Library******
    press 1 for see the avaible books
    press 2 for borrow the book
    press 3 for return/add book
    press 4 to see issued books 
    press 5 for Main menu '''

  
        

lib=Library(["mom","com","MP","MP-2","metology","M1","M2","M3","english"])
stu = student()

while(True):
    print(msg)
    a = input("Enter Your choise: ")
    try:
        a=int(a)
        if a==1:
            lib.ShowListOfBooks()
        elif a==2:
            lib.BorrowBook(stu.request())
        elif a==3:
            lib.ReturnBook(stu.ReturnBook())
        elif a==4:
            if lib.data == []:
                print("No Book has been issued")
            else:
                for items in lib.data:
                    print(items)
            
        else:
            print("Please enter valid choice")

    except:
         print("Please enter valid choice")