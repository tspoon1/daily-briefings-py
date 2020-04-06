#hello.py in root directory

from flask import Flask
app = Flask(__name__)

#route function names should be unique

#hello world
@app.route("/")
def hello_world():
    print("VISITED THE HELLO PAGE")
    return "Hello, World!"

#about
@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me"