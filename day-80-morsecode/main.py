from morse import code_dict
from win32api import Beep as beep

# Get hold of the message to send and capitalize all letters
message = input("Write the message to send: ").upper()
# Split the string into a list containing all characters in the message, including spaces
message = list(message)
# Empty list that will contain the message encrypted as morse code
morse_code = []


def encode(message):
    """ The following function transforms the message into morse code and outputs it as a series of . and - """
    for character in message:
        try:
            cypher = code_dict[character]
            morse_code.append(cypher)
        except KeyError:  # When the character cannot be found as a key in the code_dict it raises an exception
            if character == " ":  # When the character is a space between words it is added to the morse_code list
                morse_code.append(character)
            elif character != " ":  # When the character is not a space it means it is not supported in morse code
                print(f"Character '{character}' is not supported in the morse code dictionary")
    return morse_code


def transmit(morse_code):
    """ The following function transforms the morse code into audible beeps and inaudible gaps"""
    for cypher in morse_code:
        if cypher == " ":  # When the cypher is a space
            beep(0, 7000)  # Seven time units (7000s) long silent gap, space between words
        else:  # Split the cypher into its individual components (. and -)
            beep(0, 3000)  # Three time units (3000s) Silent short gap in between letters
            cypher = list(cypher)
            for element in cypher:
                beep(0, 1000)  # One time unit (1000s) Silent gap in between elements within a cypher
                if element == ".":
                    beep(1500, 1000)  # One time unit (1000s) long
                elif element == "-":
                    beep(1500, 3000)  # Three time units (3000s) long


print(message)
transmission = encode(message)
print(morse_code)
transmit(transmission)
print("Transmission Ended")
