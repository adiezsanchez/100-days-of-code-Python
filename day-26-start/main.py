import random
import pandas as pd

# Create one list from another without using list comprehension

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(numbers)
print(new_list)

# Create one list from another using list comprehension
# new_list = [new_item for item in list]

new_list_2 = [n+1 for n in numbers]
print (new_list_2)

# Create lists from a string

name = "Angela"
new_list_3 = [letter for letter in name]
print(new_list_3)

# Create lists from a range

new_list_4 = [num*2 for num in range(1,5)]
print(new_list_4)

# Conditional list comprehension
# Add new item if the test passes
# new_list = [new_item for item in list if test]
# Add only the short names with 4 characters

names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Add only the long names with more than 4 characters and make them UPPERCASE
long_uppercase_names = [name.upper() for name in names if len(name) > 4]
print(long_uppercase_names)

# Dictionary comprehension based on the values of a list
# new_dict = {new_key:new_value for item in list if test}

names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]
random_scores = {student:random.randint(1,100) for student in names}
print(random_scores)


# Dictionary comprehension based on the values of a dict
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# Create a new dictionary with just the students that have a higher score than 60 (pass) using the random_scores dict
# as iterable

passed_students = {student:score for (student, score) in random_scores.items() if score >= 60}
print(passed_students)

# How to iterate over a Pandas dataframe
student_dict = {
    "student":["Angela", "James", "Lily"],
    "score":[56, 76, 98]
}

# Looping through a dict:
for (key, value) in student_dict.items():
    print(key)
    print(value)

# Create a dataframe and iterate over it:
student_df = pd.DataFrame(student_dict)
print(student_df)

# Loop through dataframe columns:
for (key, value) in student_df.items():
    print(key)
    print(value)

# Loop through dataframe rows (panda in-built method):
for (index, row) in student_df.iterrows():
    print(row) #Each of these rows is a panda series object
    print(row.student)
    print(row.score)

#Print a particular score from one of the students:
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)