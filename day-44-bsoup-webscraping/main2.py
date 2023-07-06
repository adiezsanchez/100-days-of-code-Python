from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

all_anchor_tags = soup.find_all(name="a")

#The following lines of code are selecting the first instance of the data I am interested in
anchor_title = soup.select_one(selector="td .titleline a")
print(anchor_title.getText())
print(anchor_title.get("href"))

points = soup.select_one(selector="td .score")
print(points.getText())

#The following lines of code are selecting all the instances of the data I am interested in (title, link):
anchor_title_list = soup.select(selector="td .titleline a")
print(anchor_title_list)

data = []
for anchor in anchor_title_list:
    title = anchor.getText()
    link = anchor.get("href")
    dictionary = dict(title=title, link=link)
    data.append(dictionary)
print(data)

#Cleaning the list of dictionaries (data) of unwanted elements
for element in data:
    if "from?site" in element["link"]:
        data.remove(element)
print(data)
print(len(data))

#The following lines of code are selecting all the instances of the data I am interested in (points):
points_list = soup.select(selector="td .score")
points_data = []
for span in points_list:
    points = span.getText().split(" ")
    points_num_value = int(points[0])
    points_data.append(points_num_value)

print(points_data)
print(len(points_data))

#Merge data with points data in a single list:
n = 0
for dict in data:
    dict["points"] = points_data[n]
    n += 1
#Find the points highest value and return its position as index
highest_value = max(points_data)
index = points_data.index(highest_value)
#Print the list element at index with the highest point value
print(data[index])
most_upvoted = data[index]["title"]
most_points = data[index]["points"]
print(f"The most upvoted piece of news is '{most_upvoted}' with {most_points} points")