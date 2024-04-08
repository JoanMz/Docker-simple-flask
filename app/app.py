from typing import List, Dict
from flask import Flask, request
import json

from models import Articles, get_data, add_data

app = Flask(__name__)

def my_articles():
    articles = get_data()
    return articles

@app.route('/')
def index() -> str:
    return my_articles()

@app.route('/add', methods=["POST"])
def add_registers():
    data = json.loads(request.data)
    add_data(data)
    return "Successful"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
