import requests

c = requests.request("POST", "http://127.0.0.1:5000/add_book")
print(c.text)