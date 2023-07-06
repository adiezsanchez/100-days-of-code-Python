from post import Post
import requests

# blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
# blog_response = requests.get(blog_url)
# blog_data = blog_response.json()

# print(blog_data)

# post_objects = []
# for post in blog_data:
#     post = Post(title=post["title"],
#                 subtitle=post["subtitle"],
#                 body=post["body"],
#                 id=post["id"])
#     post_objects.append(post)
    
# print(post_objects[1].id)

def get_blog(id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    
    for post in blog_data:
        if post["id"] == id:
            post_object = Post(title=post["title"],
                        subtitle=post["subtitle"],
                        body=post["body"],
                        id=post["id"])
            
            
    return post_object

post = get_blog(1)

print(type(post))
print(post.title)