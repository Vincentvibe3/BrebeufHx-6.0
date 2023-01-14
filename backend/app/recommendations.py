import json
import random as RNGesus
import numpy as np
from book import Book

#with open('answers.json') as preferences:
#    answers = json.load(preferences)


user = {
    "age": 66,
    "length": "medium",
    "tags": ['Awesome','NewTag'],
    "date": "contemporary"
}

    
#probs easier if books were ID'd with a number instead of title
def get_everything(answers, num):
    
    book = Book()
    book_data = book.data

    books = {}

    for i in book_data:
        name = i["name"]
        books[f"{name}"] = i
    
    ratings = {}
    #ratings = dict()
    for x in books:
        rating = 0

        if answers["age"] <= books[x]["age"] - 20 and answers["age"] >= books[x]["age"] + 20:
            rating +=1

            

        #tags preference
        tagsAns = list(answers["tags"])
        tagsBooks = list(books[x]["tags"])
        for i in range (len(tagsAns)):
            for j in range(len(tagsBooks)):
                if tagsAns[i] == tagsBooks[j]:
                    rating += 1

                
        #length preference
        #answers["length"] = 'short', 'medium', 'long'
        #books["length"] = int page
        #short = 0-100; medium = 101-400; long = 401+
        lengthPref = 0
        bl = books[x]["length"]
        al = answers["length"]
        if bl <= 100 and al == 'short':
            rating += 1
        elif bl > 100 and bl <= 400 and al == 'medium':
            rating += 1
        elif bl > 400 and al == 'long':
            rating += 1
        #stfu bl isn't yaoi


        #era preference
        #answers["date"] = 'contemporary', modern', 'renaissance', 'gothic', 'baroque', 'middle ages', 'antiquity', etc.
        #books["date"] = int date
        #source : wikipedia and history class in high school
        dateprefs = list(answers["date"])
        bd = books[x]["yearPublished"]
        if bd < 476 and 'antiquity' in dateprefs:
            rating += 1
        if bd >= 476 and bd < 1492 and 'middle ages' in dateprefs:
            rating += 1
        if bd >= 1300 and bd < 1700 and 'renaissance' in dateprefs:
            rating += 1
        if bd >= 1150 and bd <= 1450 and 'gothic' in dateprefs:
            rating += 1
        if bd >= 1600 and bd <= 1750 and 'baroque' in dateprefs:
            rating += 1
        if bd >= 1492 and bd < 1793 and 'modern' in dateprefs:
            rating += 1
        if bd > 1793 and 'contemporary' in dateprefs:
            rating += 1
        
        #this cannot be efficient...

        #origin of book preference
        #answers["origin"] = str[] origin(s)
        #books["origin"] = str origin
        #originPref = 0
        #if books[x]["origin"] in list(answers["origin"]):
        #    originPref = 1

        #language preference
        #answers["language"] = str[] language(s)
        #books["language"] = str language
        #languagePref = 0
        #if books[x]["language"] in list(answers["language"]):
            #languagePref = 1


        #final update of dict ratings
    
        ratings.update({x:rating})

    print(ratings)
    sorted_ratings = sorted(ratings, key=ratings.get, reverse=True)[:num]
    print(sorted_ratings)
    #sorted_ratings = reversed(sorted_ratings)

    #highest rated book(s)
    #def highest_value_titles(num):
    v = list(ratings.values())
    k = list(ratings.keys())
    #s = sort_index(v)[:num]
    booklist = {}
    #for i in range(len(ratings)-num):
    #sorted_ratings.pop(0)
            #booklist.append(books[sorted_ratings[num]]["name"])
    for i in sorted_ratings:
        booklist.update({i:books[i]})
    return booklist
    #or return book ID ig...

    #h = k[v.index(max(v))]       (old code but could be useful if ever we revert)
    #return books[h]["name"]
    
print(get_everything(user, 3))