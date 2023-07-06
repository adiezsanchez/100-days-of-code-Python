from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

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