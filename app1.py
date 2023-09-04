from flask import Flask, jsonify,request
import  requests

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
]

param = {"page":1, "limit":10}
URL = "http://127.0.0.1:5000/api/books3"
res = requests.get(URL, params=param)



count = 1
for data in res.json():
    print({count}, data)
    count += 1





