# with open ("./weather_data.csv") as file:
#     weather_data = [weather.strip() for weather in file.readlines()]

# in-built functions to read csv (limit functionality). Get temperatures and create a list with them.

# import csv
# with open ("./weather_data.csv") as file:
#     weather_data = csv.reader(file)
#     temperatures = []
#     for row in weather_data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))


# Import pandas to read a .csv file
import pandas as pd
data = pd.read_csv("./weather_data.csv")

def convert_to_celsius(temp):
    return temp * 1.8 + 32

# Transform data into a dictionary
data_dict = data.to_dict()
print(data_dict)

# Get hold of the columns either with a function or using attributes:
print(data["condition"]) # Treating it like a dictionary getting hold of the key
print(data.condition) # Treating it like an attribute from an object

# Calculate the average temperature of the week (manually)
temp_list = data["temp"].to_list()
print(temp_list)
avg_temp = (sum(temp_list)/len(temp_list))
print(avg_temp)

# Calculate the average temperature of the week (pandas)
avg_temp_pd = data["temp"].mean()
print(f"The average temp is: {avg_temp_pd}")

# Get the max temperature of the week (pandas)
max_temp_pd = data["temp"].max()
print(f"The max temp is: {max_temp_pd}")

# Get data in row
print(data[data.day == "Monday"])

# Print the row of data which had the highest temperature
# Which row inside our column of temps has the highest value
print(data[data.temp == data.temp.max()])

# Get a particular value within a particular row
monday = data[data.day == "Monday"]
print(monday.condition)

# Get Monday's temp in Fahrenheit
# Need to convert data type to integer to get rid of all the extra indexes and numbers around
monday_temp = int(monday.temp)
print(f"Monday's temp: {convert_to_celsius(monday_temp)}F")

# Create a dataframe from scratch(dictionary) and save it as a .csv
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "grades": [60, 70, 99]
}

grades_data = pd.DataFrame(data_dict)
grades_data.to_csv("./grades_data.csv")



















