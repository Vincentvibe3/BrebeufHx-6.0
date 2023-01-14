import json


with open('answers.json') as answers:
    preferences = json.load(answers)

with open('books.json') as works:
    books = json.load(works)


ratings = {}


for x in books:
    rating = 0

    #age preference
    if answers["age"] <= books["age"] - 2 and answers["age"] >= books["age"] + 2:
        rating += 1
    
    ratings.update({x:rating})

    #tags preference
    tagsAns = answers["tags"]
    tagsBooks = answers["tags"]
    for i in tagsAns:
        for j in tagsBooks:
            if tagsAns[i] == tagsBooks[j]:
                rating += 1

    ratings.update({x:rating})
            
    #length preference
    
