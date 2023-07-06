# This ones solves the bug appearing index out of range when one piece of news has no points given yet
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

all_anchor_tags = soup.find_all(name="a")

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
subtext = soup.select(selector="td .subtext")

point_list = []
for td in subtext:
    if "points" not in td.find(name="span").getText():
        point_list.append(0)
    else:
        #print(td.find(name="span").getText())
        content = str(td.find(name="span").getText())
        list_of_contents = content.split(" ")
        #print(list_of_contents[0])
        point_list.append(int(list_of_contents[0]))
print(point_list)

#Merge data with points data in a single list:
n = 0
for dict in data:
    dict["points"] = point_list[n]
    n += 1
#Find the points highest value and return its position as index
highest_value = max(point_list)
index = point_list.index(highest_value)
#Print the list element at index with the highest point value
print(data[index])
most_upvoted = data[index]["title"]
most_points = data[index]["points"]
print(f"The most upvoted piece of news is '{most_upvoted}' with {most_points} points")