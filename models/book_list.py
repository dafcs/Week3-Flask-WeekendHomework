from models.book import *

book_1 = Book("The Lord of the Rings: Fellowship of the ring","Tolkien","Fantasy-adventure",'such a long description oh my lord what a long description just for the example this will be a pain in the arse to go through since it does not wrap and even if it did it would just occupy the entire screen')
book_2 = Book("The Lord of the Rings: The Two Towers","Tolkien","Fantasy-adventure",'desc')
book_3 = Book("The Lord of the Rings: Return of the King","Tolkien","Fantasy-adventure",'desc')
book_4 = Book('Outlander 1','Diana Gabaldon','historical-romance','desc')
book_5 = Book('Outlander 2','Diana Gabaldon','historical-romance','desc')
book_6 = Book('Outlander 3','Diana Gabaldon','historical-romance','desc')
book_7 = Book('book1','author1','genre1','desc')
book_8 = Book('book2','author2','genre2','desc')
book_9 = Book('book3','author3','genre3','desc')
book_10 = Book('book4','author4','genre4','desc')
book_11 = Book('book5','author5','genre5','desc')
book_12 = Book('book6','author6','genre6','desc')


books = [book_1,book_2,book_3,book_4,book_5,book_6,book_7,book_8,book_9,book_10,book_11,book_12]

mybooks = []

def add_book_mybooks(book_title):
    book_add = None
    for book in books:
        if book.title == book_title:
            book_add = book
    mybooks.append(book_add)
    books.remove(book_add)

def add_to_books(book):
    books.append(book)
    
def delete_book_books(book_title):
    book_remove = None
    for book in books:
        if book.title == book_title:
            book_remove = book
            break
    books.remove(book_remove)

def remove_book_mylist(book_title):
    book_remove = None
    for book in mybooks:
        if book.title == book_title:
            book_remove = book
            break
    books.append(book_remove)
    mybooks.remove(book_remove)

            

def find_book(book_title):
    for book in books:
        if book.title == book_title:
            return book