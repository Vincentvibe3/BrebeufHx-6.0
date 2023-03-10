
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
import recommendations
from uuid import uuid4
import os
import binascii
from fastapi.middleware.cors import CORSMiddleware

validTokens = []
data = Book()

auth_data = TinyDB('auth.json')
Q = Query()

hasher = PasswordHasher()

app = FastAPI()

origins = [
    "http://localhost",
    os.environ["FRONTEND_ORIGIN"]
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
print(os.environ["FRONTEND_ORIGIN"])

def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()

@app.post("/testpost")
async def testpost(params:dict):
    return params

@app.get("/")
async def hello_world():
    return "helloworld"

@app.post("/get_recommendation")
async def get_recommendation(userData:dict):
   return [ value for value in recommendations.get_everything(userData,3).values()]

@app.get("/get_tags")
async def get_tags():
    return data.tag_list_get()

@app.post("/add_book")
async def add_book(book_data:dict):
    return data.book_add(book_data)  # Returns OK or 69420

@app.get("/book/{book_id}")
async def book(book_id):
    if book_id == "ALL":
        return data.data
    book_data = data.book_get(book_id)
    return book_data

@app.post("/register")
async def register(request: Request, username:str=Form(), password:str=Form()):
    referer = request.headers["referer"]
    print(referer)
    hashed_password = hasher.hash(password)
    print(auth_data.search(Q.username == username))
    if auth_data.search(Q.username == username) == []:
        auth_data.insert({"username": username, "pass_hash": hashed_password})
        validTokens.append(generate_key())
        return RedirectResponse(f"{referer}/callback?token={generate_key()}", status_code=302)
    return RedirectResponse(f"{referer}register?failed", status_code=302)

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
        validTokens.append(generate_key())
        return RedirectResponse(f"{referer}callback?token={generate_key()}", status_code=302)
    except Exception:
        return RedirectResponse(f"{referer}login?failed", status_code=302)

@app.post("/logout")
async def logout(self, request:Request):
    token=request.cookies.get("token")
    validTokens.remove(token)    
    logout(request)
    return RedirectResponse(f"{referer}logout successful")