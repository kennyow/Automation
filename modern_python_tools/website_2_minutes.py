#Recommend to use this conde on Replt
from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Welcome to my Website"

app.run(host='0.0.0.0')