import requests
import json
dictionary = {"name": "Monte PP",
            "desc": "DESCRIPTIONASD",
            "genres": ["Dog", "Cat", "Chicken", "Penis", "LeaGUEOFLEGENDS"],
            "age": 18123,
            "length": 0,
            "tags": ["Tag1", "SecondTag"]}


c = requests.post("http://127.0.0.1:5000/add_book", json = dictionary)

c = requests.post("http://127.0.0.1:5000/register", json = {"username":"username1","password":"mypass"})

c = requests.post("http://127.0.0.1:5000/login", json = {"username":"username1","password":"mypass2"})
print(c.text)

