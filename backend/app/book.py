import json
class Book:
    def __init__(self):
        with open("books.json", "r") as file:
            self.book_database = json.load(file)

    def database_update(self):
        with open("books.json", "w") as file:
            json.dump(self.book_database, file, indent=4)
        with open("books.json", "r") as file:
            self.book_database = json.load(file)
            return self.book_database

    def book_add(self,book_data):
        name = book_data.pop("name").title()
        self.book_database[name] = book_data

        for i in "tags","genres":  # Adds unadded tags/genres to the GENERAL list of tags/genres
            for ele in book_data[i]:
                if ele not in self.book_database["GENERAL"][i]:
                    self.book_database["GENERAL"][i].append(ele)
        self.database_update()

    def book_get(self,book):
        if book in self.book_database:
            return self.book_database[book]
        return "BOOK DOESN'T EXIST"

    def tag_list_get(self):
        return self.book_database["GENERAL"]["tags"]

    def tag_exists(self,tag):
        return tag in self.book_database["GENERAL"]["tags"]

    def genre_exists(self,genre):
        return genre in self.book_database["GENERAL"]["genres"]

    def genre_list_get(self):
        return self.book_database["GENERAL"]["genres"]

c = Book()
c.book_add({"name": "Monte Cristo ASASDAD",
  "desc": "DESCRIPTIONASD",
  "genres": ["Dog","Cat","Chicken","Penis"],
  "age": 18123,
  "length": 0,
  "tags":["Tag1","SecondTag"]})