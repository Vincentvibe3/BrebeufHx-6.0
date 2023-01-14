import requests
import json
dictionary = {"name": "Pantheon",
            "desc": "OwO so hot",
            "age": 18123111,
            "length": 123,
            "yearPublished":1984,
            "tags": ["Tag122222", "SecondTag"]}


c = requests.post("http://127.0.0.1:8080/add_book", json = dictionary)

print(c.text)

