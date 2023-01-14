
import requests
import base64
from argon2 import PasswordHasher
from tinydb.storages import JSONStorage
from tinydb import TinyDB, Query
import argon2
from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from book import Book
from fastapi.responses import RedirectResponse

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
    print("called")
    return data.book_add(book_data)  # Returns OK

@app.get("/book/{book_name}")
async def book(book_name):
    book_data = data.book_get(book_name)
    return book_data

@app.post("/register")
async def register(request: Request, username:str=Form(), password:str=Form()):
    referer = request.headers["referer"]
    print(referer)
    hashed_password = hasher.hash(password)
    print(auth_data.search(Q.username == username))
    if auth_data.search(Q.username == username) == []:
        auth_data.insert({"username": username, "pass_hash": hashed_password})
        return RedirectResponse(f"{referer}/callback?token=abc", status_code=302)
    return RedirectResponse(f"{referer}noot noot", status_code=302)

@app.post("/login")
async def login(request: Request,username:str=Form(), password:str=Form()):  # Logs in and identifies the user
    referer = request.headers["referer"]
    print(referer)
    if auth_data.search(Q.username == username) == []:
        return RedirectResponse(f"{referer}login failed", status_code=302)
    hash_pass = auth_data.search(Q.username == username)[0]["pass_hash"]
    print(hash_pass)
    try:
        hasher.verify(hash_pass, password)
        # Generate Token
        return RedirectResponse(f"{referer}callback?token=abc", status_code=302)
    except Exception:
        return RedirectResponse(f"{referer}login failed", status_code=302)