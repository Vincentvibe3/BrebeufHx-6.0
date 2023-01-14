import requests
import json
dictionary = {"name": "Pantheo232a3aaaaaaan",
            "desc": "OwO so hot",
            "age": 18123111,
            "length": 123,
            "yearPublished":1984,
            "tags": ["Tag122222", "SecondTag"],
            "author":"MEMEMEMEME",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQiICxX7SNshiebtkyqGDBlFSsj6nd4pz7fIJcXwAc&s"}


c = requests.post("http://127.0.0.1:8080/add_book", json = dictionary)

print(c.text)

