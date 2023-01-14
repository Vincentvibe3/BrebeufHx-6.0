import json
import random as RNGesus

#with open('answers.json') as preferences:
#    answers = json.load(preferences)


with open("./backend/app/books.json","r") as works:
    books = json.load(works)
books.pop("GENERAL")


#    "age" : 18122,
#   "tags" : ["bunny", "loli", "perywinkle"],
#    "genres" : ["slice of life", "onee-chan", "hot chocolate", "Penis Penis Penis"],
#}

#probs easier if books were ID'd with a number instead of title
def get_everything(answers, num):
    ratings = {}
    #ratings = dict()
    for x in books:
        rating = 0

        #age preference
        if answers["age"] >= books[x]["age"] - 2 and answers["age"] <= books[x]["age"] + 2:
            rating += 1
        

        #tags preference
        tagsAns = list(answers["tags"])
        tagsBooks = list(books[x]["tags"])
        for i in range (len(tagsAns)):
            for j in range(len(tagsBooks)):
                if tagsAns[i] == tagsBooks[j]:
                    rating += 1

        #genre preferences T_T
        #same as tags really...
        # genreAns = list(answers["genres"])
        # genreBooks = list(books[x]["genres"])
        # for i in range (len(genreAns)):
        #     for j in range (len(genreBooks)):
        #         if genreAns[i] == genreBooks[j]:
        #             rating += 1

                
        #length preference
        #answers["length"] = 'short', 'medium', 'long'
        #books["length"] = int page
        #short = 0-100; medium = 101-400; long = 401+
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
        #answers["date"] = 'modern', 'renaissance', 'gothic', 'baroque', 'middle ages', 'antiquity', etc.
        #books["date"] = int date
        #source : wikipedia and history class in high school
        dateprefs = list(answers["date"])
        bd = books[x]["date"]
        if bd < 476 and 'antiquity' in dateprefs:
            rating += 1
        if bd >= 476 and bd < 1492 and 'middle ages' in dateprefs:
            rating += 1
        if bd >= 1300 and bd < 1700 and 'renaissance' in dateprefs:
            rating +=1
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
        #if books[x]["origin"] in list(answers["origin"]):
           #rating += 1

        #language preference
        #answers["language"] = str[] language(s)
        #books["language"] = str language
        #if books[x]["language"] in list(answers["language"]):
            #rating += 1

        if 'self-published fanfiction' in books[x]["genres"]:
            rating -= 1
        #more shit if needed like subjects, time of release (era), author, etc.
        #also pls merge genres and tags in the json

        #Gacha
        #rating += RNGesus.randint(0,69)

        #final update of dict ratings
        ratings.update({x:rating})


    #def sort_index(lst, rev=True):
    #      #index = range(len(lst))
    #    s = sorted(lst, reverse = rev)
        #key = lambda i:lst[i]
    #    return s
    sorted_ratings = sorted(ratings)

    #highest rated book(s)
    #def highest_value_titles(num):
    v = list(ratings.values())
    k = list(ratings.keys())
    #s = sort_index(v)[:num]
    booklist = {}
    for i in range(len(ratings)-num):
        sorted_ratings.pop()
            #booklist.append(books[sorted_ratings[num]]["name"])
    for i in sorted_ratings:
        booklist.update({i:books[i]})
    return booklist
    #or return book ID ig...

    #h = k[v.index(max(v))]       (old code but could be useful if ever we revert)
    #return books[h]["name"]