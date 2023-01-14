import json


with open('answers.json') as answers:
    preferences = json.load(answers)

with open('books.json') as works:
    books = json.load(works)


ratings = {}

#probs easier if books were ID'd with a number instead of title
for x in books:
    rating = 0

    #age preference
    if answers["age"] <= books[x]["age"] - 2 and answers["age"] >= books[x]["age"] + 2:
        rating += 1
    
    #ratings.update({x:rating})

    #tags preference
    tagsAns = list(answers["tags"])
    tagsBooks = list(books[x]["tags"])
    for i in tagsAns:
        for j in tagsBooks:
            if tagsAns[i] == tagsBooks[j]:
                rating += 1

    #ratings.update({x:rating})
            
    #length preference
    #answers["length"] = 'short', 'medium', 'long'
    #books["length"] = int page
    #short = 0-100; medium = 101-400; long = 401+
    if books[x]["length"] <= 100 and answers["length"] == 'short':
        rating += 1
    elif books[x]["length"] > 100 and books[x]["length"] <= 400 and answers["length"] == 'medium':
        rating += 1
    elif books[x]["length"] > 400 and answers["length"] == 'long':
        rating += 1
    
    ratings.update({x:rating})

    #era preference
    #answers["date"] = 'modern', 'renaissance', 'gothic', 'baroque', 'middle ages', 'antiquity', etc.
    #books["date"] = int date
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
    if bd >= 1600 and bd <= 1750 and 'gothic' in dateprefs:
        rating += 1
    if bd >= 1492 and bd < 1793 and 'modern' in dateprefs:
        rating += 1
    if bd > 1793 and 'contemporary' in dateprefs:
        rating += 1
    
    #this cannot be efficient...



    #more shit if needed like subjects, time of release (era), author, etc.
    #also pls merge genres and tags in the json

    
#highest rating book
def highestValueTitle():
    v = list(ratings.values())
    k = list(ratings.keys())
    h = k[v.index(max(v))]
    return books[h]["name"]
    #or return book ID ig...

#also what if more than 1 book recommended




    