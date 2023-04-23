from flask import Flask, render_template, redirect, request
from app import app
from models.book_list import books as booklist, mybooks, delete_book_books,add_book_mybooks,add_to_books,find_book
from models.book import Book
import _datetime

@app.route('/home')
def main_page():
    return render_template('homepage.jinja',title = 'My',books = booklist)

@app.route('/home/delete/<book_title>', methods=['POST'])
def delete_item_books(book_title):
    delete_book_books(book_title)
    return redirect('/home')

@app.route('/home/remove/<book_title>')
def remove_book_mybooks(book_title):
    remove_book_mybooks(book_title)
    return redirect('home/mylist')

@app.route('/home/addmylist/<book_title>', methods=['POST'])
def add_item_mybooks(book_title):
    add_book_mybooks(book_title)
    return redirect('/home')

@app.route('/home/add', methods=['POST'])
def add_book_to_library():

    return redirect('/home')

@app.route('/home/mylist')
def mylist_page():
    return render_template('mylist.jinja',title = 'My',mybooks = mybooks)

@app.route('/home/book-action', methods=['POST'])
def handle_book_action():
    book_title = request.form['book_title']
    action = request.form['action']

    if action == 'remove':
        delete_book_books(book_title)
        return redirect('/home')
    elif action == 'add_to_list':
        add_book_mybooks(book_title)
        return redirect('/home')

@app.route('/home/<book_title>')
def change_book_page(book_title):
    book = find_book(book_title)
    return render_template('bookpage.jinja',title = 'My',book = book)