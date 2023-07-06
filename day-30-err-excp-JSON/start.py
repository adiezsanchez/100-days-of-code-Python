# try:
#     Something that might cause and exception
#     Treat it as an if
#
# except:
#     Do this if there was an exception
#
# else:
#     Do this if there were no exceptions
#
# finally:
#     Do this no matter what happens

try:
    file = open("a_file.txt")
    dictionary = {"key":"value"}
    print(dictionary["wrong_key"])

except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("File was created and written on")

except KeyError as error_message:
    print (f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("The file was closed")
