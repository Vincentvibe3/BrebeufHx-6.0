import json


with open('answers.json') as answers:
    preferences = json.load(answers)

with open('books.json') as works:
    books = json.load(works)


ratings = {}


for x in books:
    rating = 0
    if answers["age"] <= books["age"] - 2 and answers["age"] >= books["age"] + 2:
        rating += 1
    
    ratings.update({x:rating})

    if answers["tags"]
    



#def AgeOrNot():
#   if answers["age"] <= books["age"] - 2 and answers["age"] >= books["age"] + 2:
#        return True
#    
#    else:
#        return False
