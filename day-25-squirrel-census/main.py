import pandas as pd
data = pd.read_csv("./2018_Central_Park_Squirrel_Census.csv")

fur_color_column = data["Primary Fur Color"] # Use the string method because there are spaces

# My solution: Iterate through a list and add to a variable everytime it encounters the colour

fur_color_list = fur_color_column.to_list()

gray_count = 0
black_count = 0
cinnamon_count = 0

for colors in fur_color_list:
    if colors == "Gray":
        gray_count += 1
    if colors == "Black":
        black_count += 1
    if colors == "Cinnamon":
        cinnamon_count += 1

fur_color_dict = {
    "fur colors":["Gray", "Black", "Cinnamon"],
    "counts":[gray_count, black_count, cinnamon_count]
    }

fur_color_dataframe = pd.DataFrame(fur_color_dict)
fur_color_dataframe.to_csv("./2018_Squirrel_Count.csv")

# Angela's solution:

gray_squirrels_count = len(data[fur_color_column == "Gray"])
black_squirrels_count = len(data[fur_color_column == "Black"])
cinnamon_squirrels_count = len(data[fur_color_column == "Cinnamon"])

fur_color_dict2 = {
    "fur colors":["Gray", "Black", "Cinnamon"],
    "counts":[gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
    }

fur_color_dataframe2 = pd.DataFrame(fur_color_dict2)
fur_color_dataframe2.to_csv("./2018_Squirrel_Count_Angelamethod.csv")

# Simply use a pandas method

colours_dataframe = data["Primary Fur Color"].value_counts()
colours_dataframe.to_csv("./2018_Squirrel_Count_pdmethod.csv")