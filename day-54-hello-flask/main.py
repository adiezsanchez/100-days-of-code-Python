from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)

def make_bold(function):
    def wrapper_function():
        text = f"<b>{function()}</b>"
        return text
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        text = f"<em>{function()}</em>"
        return text
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        text = f"<u>{function()}</u>"
        return text
    return wrapper_function

@app.route("/") #When under the homepage this is what it shows (only trigger the function when at homepage)
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media1.giphy.com/media/AFPXxpkApjecMf8EDg/giphy.gif?cid=ecf05e47jobp9m5nm0vwtta3wiz0bobq4ihgfcaizmwnwp4w&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

@app.route("/loser") #When under the /loser this is what it shows
@make_bold
@make_emphasis
@make_underlined
def hello_loser():
    return "<p>Hello, Loser!</p>"

@app.route("/username/<name>/<int:age>") #When under the /loser this is what it shows
def greet(name, age):
    return f"<p>Hello there, {name}! You are {age} years old</p>"

if __name__ == "__main__":
    app.run(debug=True)
