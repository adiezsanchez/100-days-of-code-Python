import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # If the try block produces an error it goes to except:, if no error it continues in else: block
        try:
            with open("password_db.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        # Line triggered on the first run where there is no .json file and no data inside the file
        except FileNotFoundError:
            data = new_data
        else:
            # Updating old data with new data (json.update method)
            data.update(new_data)

        finally:
            # Writing the updated data to file
            with open("password_db.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH JSON.DB ------------------------------- #
def find_password():
    search_website = website_entry.get()
    try:
        with open ("password_db.json", "r") as data_file:
            data = json.load(data_file)
            email = data[search_website]["email"]
            password = data[search_website]["password"]
    except KeyError:
        if search_website == "":
            messagebox.showwarning(title="Error", message=f"Please input a website to search for your credentials")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {search_website} exist")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message=f"No data file found")
    else:
        messagebox.showinfo(title=search_website, message=f"These are your credentials \nEmail: {email}"
                                                          f"\nPassword: {password}")

# ---------------------------- FIND PASSWORD ANGELA VERSION ------------------------------- #
def find_password_angela():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "adiez.biotech@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Create buttons

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()