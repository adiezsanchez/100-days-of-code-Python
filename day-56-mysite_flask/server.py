from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = f"<b>{function()}</b>"
        return text
    return wrapper_function

@app.route("/") #When under the homepage this is what it shows (only trigger the function when at homepage)
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)