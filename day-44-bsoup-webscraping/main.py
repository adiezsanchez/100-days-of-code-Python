from bs4 import BeautifulSoup

with open("./website.html", encoding="utf-8") as file:
    contents = file.read()

# Parser tells what particular type of parser we need (either for html or xml)
soup = BeautifulSoup(contents, "html.parser")
#Contents of the title
#print(soup.title.string)
#Name of the html tag
#print(soup.title.name)
#print(soup.prettify())

#Finding all list elements
all_list_elements = soup.find_all(name="li")
print(all_list_elements)

li_list = []
for li in all_list_elements:
    li_list.append(li.getText())
print(li_list)

#Finding all anchor tags
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

a_list = []
for a in all_anchor_tags:
    a_list.append(a.getText())
print(a_list)

#Finding all anchor tags and get links
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

link_list = []
for a in all_anchor_tags:
    #With get you get the value of any of the attributes
    link_list.append(a.get("href"))
print(link_list)

#Find a particular element searching by tag (name) and by attribute (class, id, etc)
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

#Use html or CSS selectors (html with p, a, h1, etc, CSS class with . , id with #)
#This uses a CSS selector to find all the <a> tags in a <p> tag.
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

class_heading = soup.select(selector=".heading")
print(class_heading)