PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    name_list = file.readlines()
    # Alternative method file.splitlines() offers a list of names without the \n
    # Also a list comprehension works (less readability): invited_names = [name.strip() for name in file.readlines()]

processed_names = []

for names in name_list:
    clean_name = names.strip()
    # Alternative to strip names.replace("\n", "")
    processed_names.append(clean_name)

with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

for names in processed_names:
    letter_ready = starting_letter.replace(PLACEHOLDER, names)
    with open(f"./Output/ReadyToSend/letter_for_{names}.doc", mode="w") as file:
        file.write(letter_ready)

# Alternatives:

# with open("./Input/Names/invited_names.txt") as invited_names:
#     names = invited_names.read().splitlines()
#
# with open("./Input/Letters/starting_letter.txt") as starting_letter:
#     contents = starting_letter.read()
#
# for name in names:
#     with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_letter:
#         output_letter.write(contents.replace("[name]", name))


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp