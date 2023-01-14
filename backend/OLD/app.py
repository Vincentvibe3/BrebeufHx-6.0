import flask
import requests
import base64

from argon2 import PasswordHasher
from tinydb.storages import JSONStorage
from tinydb import TinyDB, Query
import argon2

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)
from backend.app import book
from backend.app.book import Book

data = Book()

auth_data = TinyDB('auth.json')
Q = Query()
hasher = PasswordHasher()



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

@bp_home.route('/get_recommendation')
def get_recommendation():
    #request.json will be sent from website
    #treat request.json with questionmark.py
    #return recommendation
    pass

@bp_home.route('/get_stats', methods=('GET', 'POST'))
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
@bp_book.route('/<book_name>', methods=('GET', 'POST'))
def book(book_name):
    if request.method == "GET":
        book_data = data.book_get(book_name)
        return book_data

@bp_home.route("/register", methods=('GET', 'POST'))
def register():
    username = request.json["username"]
    password = request.json["password"]
    hashed_password = hasher.hash(password)
    if auth_data.search(Q.username == username) == []:
        auth_data.insert({"username":username,"pass_hash":hashed_password})
        return "200"
    return "69420"


@bp_home.route("/login", methods=('GET', 'POST'))
def login():  # Logs in and identifies the user
    username = request.json["username"]
    password = request.json["password"]
    if auth_data.search(Q.username == username) == []:
        return "69420: user doesn't exist"
    hash_pass = auth_data.search(Q.username == username)[0]["pass_hash"]
    try:
        hasher.verify(hash_pass, password)
        # Generate Token
        return "login token goes here"
    finally:
        return "69420: Login failed"