#Create and account on https://deepnote.com/
from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Welcome to my Website"

app.run(host='0.0.0.0')