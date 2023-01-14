import json
def add_book(book_data):
    with open("books.json","r") as file:
        data = json.load(file)
        name = book_data.pop("name").title()
        data[name] = book_data

    with open("books.json","w") as file:
        json.dump(data, file, indent=4)

def get_book_data(book):
    pass

add_book({"name": "Monte Cristo ASD",
  "desc": "DESCRIPTION",
  "genre": "Dog",
  "age": "18+",
  "length": 0})