import json


class Book:
    def __init__(self):
        with open("books.json", "r") as file:
            self.__book_database = json.load(file)

    def __database_update(self):
        with open("books.json", "w") as file:
            json.dump(self.__book_database, file, indent=4)
        with open("books.json", "r") as file:
            self.__book_database = json.load(file)
            return self.__book_database

    def book_add(self, book_data):
        book_data["name"].title()

        self.__book_database[book_data["name"]] = book_data

        for i in ["tags", "genres"]:  # Add tags/genres to the GENERAL list of tags/genres
            for count in range(len(book_data[i])):  # Formats tags/genres
                book_data[i][count] = book_data[i][count].title()

            for ele in book_data[i]:
                if ele not in self.__book_database["GENERAL"][i]:
                    self.__book_database["GENERAL"][i].append(ele)

        self.__database_update()
        return "200"

    def book_get(self, book):
        if book in self.__book_database:
            return self.__book_database[book]
        return "404"

    def book_has_tag(self, book, tag):
        return tag in self.__book_database[book]["tags"]

    def book_has_genre(self, book, genre):
        return genre in self.__book_database[book]["genres"]

    def tag_list_get(self):
        return self.__book_database["GENERAL"]["tags"]

    def tag_exists(self, tag):
        return tag in self.__book_database["GENERAL"]["tags"]

    def genre_exists(self, genre):
        return genre in self.__book_database["GENERAL"]["genres"]

    def genre_list_get(self):
        return self.__book_database["GENERAL"]["genres"]


c = Book()
c.book_add({"name": "Pantheon",
            "desc": "OwO so hot",
            "genres": ["Leagueoflegos"],
            "age": 18123111,
            "length": 123,
            "tags": ["Tag122222", "SecondTag"]})
