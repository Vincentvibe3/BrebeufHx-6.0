import requests
import json
dictionary = {"name": "Monte PP",
            "desc": "DESCRIPTIONASD",
            "genres": ["Dog", "Cat", "Chicken", "Penis", "LeaGUEOFLEGENDS"],
            "age": 18123,
            "length": 0,
            "tags": ["Tag1", "SecondTag"]}
c = requests.post("http://127.0.0.1:5000/add_book", json = dictionary)
c = requests.get("http://127.0.0.1:5000/book/Pantheossssn")

print(c.text)

