
import requests
import base64
from argon2 import PasswordHasher
from tinydb.storages import JSONStorage
from tinydb import TinyDB, Query
import argon2
from fastapi import FastAPI

from book import Book

data = Book()

auth_data = TinyDB('auth.json')
Q = Query()

hasher = PasswordHasher()


app = FastAPI()

@app.post("/testpost")
async def testpost(params:dict):
    return params

@app.get("/")
async def hello_world():
    return "helloworld"

@app.get("/get_recommendation")
async def get_recommendation():
    pass

@app.get("/get_stats")
async def get_stats():
    return {"tags": data.tag_list_get(), "genres": data.genre_list_get()}

@app.post("/add_book")
async def add_book(book_data:dict):
    return data.book_add(book_data)  # Returns OK

@app.get("/book/{book_name}")
async def book(book_name):
    book_data = data.book_get(book_name)
    return book_data

@app.post("/register")
async def register(request:dict):
    username = request["username"]
    password = request["password"]
    hashed_password = hasher.hash(password)
    if auth_data.search(Q.username == username) == []:
        auth_data.insert({"username": username, "pass_hash": hashed_password})
        return "200"
    return "69420"

@app.post("/login")
async def login(request:dict):  # Logs in and identifies the user
    username = request["username"]
    password = request["password"]
    if auth_data.search(Q.username == username) == []:
        return "69420: user doesn't exist"
    hash_pass = auth_data.search(Q.username == username)[0]["pass_hash"]
    try:
        hasher.verify(hash_pass, password)
        # Generate Token
        return "login token goes here"
    finally:
        return "69420: Login failed"