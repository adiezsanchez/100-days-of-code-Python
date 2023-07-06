from flask import Flask
from flask import render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        text = f"<b>{function()}</b>"
        return text

    return wrapper_function


@app.route("/")  # When under the homepage this is what it shows (only trigger the function when at homepage)
def home():
    today = dt.date.today()
    year = today.year
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, date=year) #Pass as **kwargs into the render_template

@app.route("/guess/<name>") #<>This parses the name from the url and passes it as a variable with same name
def api_requests(name):
    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    
    gender_response = requests.get(url=f"https://api.genderize.io/?name=p{name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    text = f"<h1>Hey {name.capitalize()},</h1>" \
            f"<h2>I think you are {gender},</h2>" \
            f"<h3>And maybe {age} years old</h3>"
            
    return text

@app.route("/guess_template/<name>") 
def api_template_requests(name):
    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    
    gender_response = requests.get(url=f"https://api.genderize.io/?name=p{name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    today = dt.date.today()
    year = today.year
            
    return render_template("index2.html",html_name=name, html_age=age, html_gender=gender, date=year) #Pass as **kwargs into the render_template

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
