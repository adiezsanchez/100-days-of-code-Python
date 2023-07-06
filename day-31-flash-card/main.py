import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# Data cleaning part to obtain a dataframe with the list of the 1000 most used Norwegian words from opensubtitles.org

# data = pd.read_csv("./data/norwegian_words.csv", encoding="ISO-8859-1")
# preprocessed_words_column = data["Norwegian"]
# preprocessed_words_list = preprocessed_words_column.to_list()
# processed_words = []
#
# for words in preprocessed_words_list:
#     split_words = words.split(" ")
#     processed_words.append(split_words[0])
#
# processed_words_df = pd.DataFrame(processed_words)
# print(processed_words_df)
#
# processed_words_df.to_csv("./data/norwegian_words_processed.csv")

# ------------------------------------------- GENERATE FLASH CARDS ----------------------------------------------------
try:
    df = pd.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    df = pd.read_csv("./data/norwegian_english_1000words.csv")

no_eng_dict_list = df.to_dict(orient="records")
print(len(no_eng_dict_list))

current_card = {}


# ------------------------------------------- BUTTON FUNCTIONALITY ------------------------------
def next_card(button_pressed):
    global current_card, flip_timer
    # This invalidates the timer every time we click the button
    window.after_cancel(flip_timer)
    # This variable initially was created within this function, so to make it available for the rest of the code
    # outside of the function we make it a global variable (first create it as an empty dict)
    current_card = random.choice(no_eng_dict_list)
    no_word = current_card["Norwegian"]
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="Norwegian", fill="black")
    canvas.itemconfig(card_word, text=no_word, fill="black")
    # Include know or unknown word functionality before the card flips:
    print(button_pressed)
    if button_pressed == "known":
        # Remove the current card from the list of 1000 words extracted from the original .csv
        no_eng_dict_list.remove(current_card)
        print(f"You have {len(no_eng_dict_list)} norwegian words left to learn")
        # Create a dataframe with all the list of dicts left and save it into a .csv
        no_eng_dict_list_data = pd.DataFrame(no_eng_dict_list)
        no_eng_dict_list_data.to_csv(f"./data/words_to_learn.csv", index=False)
    # After we set up this card the timer is restored, if we click the button again it stops the timer
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    eng_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=eng_word, fill="white")


# -------------------------------------------  TKINTER UI -------------------------------------------------------------

# Create the Tk window and assign a title
window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flashy")

# Associate the window.after method to a variable so we can access and modify it using window.after_cancel
flip_timer = window.after(3000, flip_card)

# Create buttons

cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, bg=BACKGROUND_COLOR, relief="flat",
                        command=lambda button_pressed="unknown": next_card(button_pressed))
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, bg=BACKGROUND_COLOR, relief="flat",
                      command=lambda button_pressed="known": next_card(button_pressed))
known_button.grid(column=1, row=1)

# Create canvas and place the images

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="")

next_card(button_pressed="")

window.mainloop()
