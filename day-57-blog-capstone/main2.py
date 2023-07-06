from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

# Fetch the json file containing the info from the api endpoint
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
blog_data = blog_response.json()

#Import the post class and create a list containing all blog posts
post_objects = [] #Empty list to add all objects
#Create object/instance from Post class and populate its attributes with the info from the json key:value pairs.
for post in blog_data:
    post = Post(title=post["title"],
                subtitle=post["subtitle"],
                body=post["body"],
                id=post["id"])
    post_objects.append(post)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/blog/<int:id>')
def get_blog(id):
    for post in post_objects:
        if post.id == id:
            post_object = post
    return render_template("post.html", post=post_object)

if __name__ == "__main__":
    app.run(debug=True)
