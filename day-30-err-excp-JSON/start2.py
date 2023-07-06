# Raise our own exceptions:
# raise TypeError("This is an error that I have made up")

height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

if height > 3:
    raise ValueError("Human height should not be over 3m")

bmi = weight / height ** 2

print(bmi)

# Facebook posts, some of the posts have no likes raising a KeyError

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0

print(total_likes)

# Fruit Pie

fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print ("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)