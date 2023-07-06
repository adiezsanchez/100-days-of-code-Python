# This star method imports all classes and constants but not modules of code
from tkinter import *
# This imports and specific module of code form tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # These list comprehensions substitute the for loops commented out below:

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    # Replace this commented section with the join method:
    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(0, f"{password}")
    # Load the password text into the clipboard
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_input.get()
    user = user_input.get()
    password = pass_input.get()

    if len(website) == 0 or password == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Are these the details you want to save? \nEmail: {user}"
                                                              f"\nPassword: {password}")
        if is_ok:
            with open("./Output/data_file.txt", mode="a") as data_file:
                data_file.write(f"{website},{user},{password}\n")
                # Alternative write to file method:
                # print(f"{website},{user},{password}\n", file=file)
                web_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Create the Tk window and assign a title
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg="white")

# Import the logo image into a variable
logo_img = PhotoImage(file="logo.png")

# Create the canvas and place the image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create labels
web_label = Label(text="Website:", bg="white")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", bg="white")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:", bg="white")
pass_label.grid(column=0, row=3)

# Create inputs
web_input = Entry(width=52)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

user_input = Entry(width=52)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "adiez.biotech@gmail.com")

pass_input = Entry(width=33)
pass_input.grid(column=1, row=3)

# Create buttons

gen_pass_button = Button(text="Generate Password", command=generate_pass)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
