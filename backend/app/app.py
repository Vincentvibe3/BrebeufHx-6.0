import flask
import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)
bp_home = Blueprint('home', __name__, url_prefix='/')
#bp_add_book = Blueprint("add_book", __name__, url_prefix='/add_book')
def create_app():
    app = app = Flask(__name__)
    app.register_blueprint(bp_home)
    return app

@bp_home.route('/', methods=('GET', 'POST'))
def auth():
    return "Hello World"

@bp_home.route('/', methods=('GET', 'POST'))
def auth():
    if request.method == "GET":
        return "Formulaire"

    if request.method == "POST":
        

    return "Hello World"
