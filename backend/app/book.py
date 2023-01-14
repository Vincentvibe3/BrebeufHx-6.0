import json
def add_book(book_data):
    with open("books.json","r") as file:
        data = json.load(file)
        data[f"{len(data)}"] = book_data

    with open("books.json","w") as file:
        json.dump(data, file, indent=4)



add_book({"name": "Monte Cristo",
  "desc": "DESCRIPTION",
  "genre": "Dog",
  "age": "18+",
  "length": 0})