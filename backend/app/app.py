import flask
import requests

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)

from backend.app import book
from backend.app.book import Book

data = Book()
bp_home = Blueprint('home', __name__, url_prefix='/')
bp_book = Blueprint('book',__name__,url_prefix='/book')

def create_app():
    app = app = Flask(__name__)
    for i in [bp_home,bp_book]:
        app.register_blueprint(i)
    return app

@bp_home.route('/', methods=('GET', 'POST'))
def auth():  # Home page
    return "Hello World"
@bp_home.route('/get_stats')
def get_stats():
    return {"tags":data.tag_list_get(),"genres":data.genre_list_get()}

@bp_home.route('/add_book', methods=('GET', 'POST'))
def add_book():  # Adds a book to the database
    if request.method == "POST":
        book_data = request.json
        return data.book_add(book_data)  # Returns OK
    return "Not 200"

'''
@bp_home.route('/questionnaire', methods=('GET', 'POST'))
def questionnaire():
    if request.method == "POST":
        user_preferences = request.json  # answers to the questionnaires
'''
@bp_book.route('/<book_name>')
def book(book_name):
    if request.method == "GET":
        book_data = data.book_get(book_name)
        return book_data


'''
@bp_home.route("/login", methods=("GET", "POST"))
def login():  # Logs in and identifies the user
'''