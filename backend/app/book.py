import json
import supabase
import os
from supabase import create_client
class Book:
    def __init__(self):
        self.__book_database = create_client(os.environ["SUPA_URL"],os.environ["SUPA_KEY"])
        self.__data = self.__book_database.table("books").select("*").execute().data[0]

    def book_add(self, book_data):
        book_data["name"] = book_data["name"].title()

        for count in range(len(book_data["tags"])):  # Formats tags
            book_data["tags"][count] = book_data["tags"][count].title()

        existing_tags = self.__book_database.table("tags").select("*").execute().data
        existing_tags = [i["name"] for i in existing_tags]

        try:
            self.__book_database.table("books").insert(book_data).execute()
        except:
            return "69420: book already exists"

        for ele in book_data["tags"]:
            if ele not in existing_tags:
                self.__book_database.table('tags').insert(ele).execute()

        self.__data = self.__book_database.table("books").select("*").execute().data[0]
        return "200"

    def book_get(self, book):
        for i in self.__data:
            if i["name"] == book:
                return i
        return "404"

    '''def book_has_tag(self, book, tag):
        return tag in self.__book_database[book]["tags"]'''

    '''    def book_has_genre(self, book, genre):
        return genre in self.__book_database[book]["genres"]
    '''

    '''def tag_list_get(self):
        return self.__book_database["GENERAL"]["tags"]

    def tag_exists(self, tag):
        return tag in self.__book_database["GENERAL"]["tags"]'''

'''    def genre_exists(self, genre):
        return genre in self.__book_database["GENERAL"]["genres"]

    def genre_list_get(self):
        return self.__book_database["GENERAL"]["genres"]
'''
'''
#c = Book()
#c.book_add({"name": "Pantheon",
            "desc": "OwO so hot",
            "age": 18123111,
            "length": 123,
            "yearPublished":1984,
            "tags": ["Tag122222", "SecondTag"]})
'''