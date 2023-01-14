import json
import random as RNGesus
import numpy as np

#with open('answers.json') as preferences:
#    answers = json.load(preferences)


with open('books.json') as works:
    books = json.load(works)
    books.pop("GENERAL")

    
#probs easier if books were ID'd with a number instead of title
def get_everything(answers, num):
    ratings = {}
    #ratings = dict()
    for x in books:
        #rating = 0

        #age preference
        #if answers["age"] <= books[x]["age"] - 2 and answers["age"] >= books[x]["age"] + 2:
        agepref = 0
        if books[x]["age"] == answers["age"]:
            agePref = 1
        else:
            agePref = 1.9*(1/((abs(books[x]["age"] - answers["age"])) + 1))
            
        

        #tags preference
        tagsAns = list(answers["tags"])
        tagsBooks = list(books[x]["tags"])
        tagsScore = 0
        for i in range (len(tagsAns)):
            for j in range(len(tagsBooks)):
                if tagsAns[i] == tagsBooks[j]:
                    tagsScore += 1
        tagsScoreNorm = tagsScore/len(tagsBooks)

        #genre preferences T_T
        #same as tags really...
        #genreAns = list(answers["genres"])
        #genreBooks = list(books[x]["genres"])
        #for i in range (len(genreAns)):
        #    for j in range (len(genreBooks)):
        #        if genreAns[i] == genreBooks[j]:
        #            rating += 1

                
        #length preference
        #answers["length"] = 'short', 'medium', 'long'
        #books["length"] = int page
        #short = 0-100; medium = 101-400; long = 401+
        lengthPref = 0
        bl = books[x]["length"]
        al = answers["length"]
        if bl <= 100 and al == 'short':
            lengthPref = 1
        elif bl > 100 and bl <= 400 and al == 'medium':
            lengthPref = 1
        elif bl > 400 and al == 'long':
            lengthPref = 1
        else: 
            lengthPref = 0
        #stfu bl isn't yaoi


        #era preference
        #answers["date"] = 'modern', 'renaissance', 'gothic', 'baroque', 'middle ages', 'antiquity', etc.
        #books["date"] = int date
        #source : wikipedia and history class in high school
        dateprefs = list(answers["date"])
        bd = books[x]["date"]
        eraPrefs = 0
        if bd < 476 and 'antiquity' in dateprefs:
            eraPrefs += 1
        if bd >= 476 and bd < 1492 and 'middle ages' in dateprefs:
            eraPrefs += 1
        if bd >= 1300 and bd < 1700 and 'renaissance' in dateprefs:
            eraPrefs += 1
        if bd >= 1150 and bd <= 1450 and 'gothic' in dateprefs:
            eraPrefs += 1
        if bd >= 1600 and bd <= 1750 and 'baroque' in dateprefs:
            eraPrefs += 1
        if bd >= 1492 and bd < 1793 and 'modern' in dateprefs:
            eraPrefs += 1
        if bd > 1793 and 'contemporary' in dateprefs:
            eraPrefs += 1
        
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
            languagePref = 1


        #final update of dict ratings
    
        totalAvg = (agepref + tagsScoreNorm + lengthPref + dateprefs + originPref + languagePref)/6
        ratings.update({x:totalAvg})

    def sort_index(lst, rev=True):
        index = range(len(lst))
        s = sorted(index, reverse = rev, key = lambda i: lst[i])
        return s

    #highest rated book(s)
    #def highest_value_titles(num):
    v = list(ratings.values())
    k = list(ratings.keys())
    s = sort_index(v)[:num]
    booklist = []
    for i in range(num):
            booklist = booklist.append(books[s[num]]["name"])

    return booklist
    #or return book ID ig...

    #h = k[v.index(max(v))]       (old code but could be useful if ever we revert)
    #return books[h]["name"]

