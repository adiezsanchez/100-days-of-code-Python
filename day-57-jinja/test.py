import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
blog_data = blog_response.json()

print(blog_data[0])