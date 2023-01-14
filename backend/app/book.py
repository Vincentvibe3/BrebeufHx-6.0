import json
import supabase
import os
from supabase import create_client
class Book:
    def __init__(self):
        self.__book_database = create_client(os.environ["SUPA_URL"],os.environ["SUPA_KEY"])
        self.data = self.__book_database.table("books").select("*").execute().data

    def book_add(self, book_data):
        book_data["name"] = book_data["name"].title()

        for count in range(len(book_data["tags"])):  # Formats tags
            book_data["tags"][count] = book_data["tags"][count].title()

        existing_tags = self.__book_database.table("tags").select("*").execute().data
        existing_tags = [i["name"] for i in existing_tags]

        try:
            book_name_list = [i["name"] for i in self.__book_database.table("books").select("name").execute().data]
            if book_data["name"] in book_name_list:
                x = 5/0
            self.__book_database.table("books").insert(book_data).execute()
        except:
            return "69420: book already exists"

        for ele in book_data["tags"]:
            if ele not in existing_tags:
                self.__book_database.table('tags').insert({"name":ele}).execute()

        self.data = self.__book_database.table("books").select("*").execute().data
        return "200"

    def book_get(self, book_id):
        for i in self.data:
            if str(i["id"]) == str(book_id):
                return i
        return "404"

    '''def book_has_tag(self, book, tag):
        return tag in self.__book_database[book]["tags"]'''

    '''    def book_has_genre(self, book, genre):
        return genre in self.__book_database[book]["genres"]
    '''

    def tag_list_get(self):
        ans = []
        for i in self.__book_database.table('tags').select("name").execute().data:
            ans.append(i['name'])
        return ans
'''
    def tag_exists(self, tag):
        return tag in self.__book_database["GENERAL"]["tags"]'''

'''    def genre_exists(self, genre):
        return genre in self.__book_database["GENERAL"]["genres"]

    def genre_list_get(self):
        return self.__book_database["GENERAL"]["genres"]
'''
'''

c.book_add({"name": "Pantheon",
            "desc": "OwO so hot",
            "age": 18123111,
            "length": 123,
            "yearPublished":1984,
            "tags": ["Tag122222", "SecondTag"]})
'''
'''c = Book()
c.book_add({"name": "Pantheo2323aaaaaaan",
            "desc": "OwO so hot",
            "age": 18123111,
            "length": 123,
            "yearPublished":1984,
            "tags": ["Tag122222", "SecondTag"],
            "author":"MEMEMEMEME",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQiICxX7SNshiebtkyqGDBlFSsj6nd4pz7fIJcXwAc&s"})
print(c.tag_list_get())
print(c.data)
c = Book()
c.book_add({"name": "Pantheo2323aaa2aaaanaaaaaa",
            "desc": "OwO so hot",
            "age": 18123111,
            "length": 123,
            "yearPublished":1984,
            "tags": ["Tag122222", "SecondTaggggggg"],
            "author":"MEMEMEMEME",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQiICxX7SNshiebtkyqGDBlFSsj6nd4pz7fIJcXwAc&s"})
'''