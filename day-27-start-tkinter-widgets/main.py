import tkinter
# tkinter.END = index 0
# Another option is using from tkinter import * (this imports evthg and you do not need to
# write tkinter."" in front of every object or function

FORMAT = ("Arial", 24, "italic")

def button_clicked():
    print("I got clicked")

def button_clicked_window():
    label["text"] = "Button Got Clicked"

def show_input():
    # Gets text in entry
    input_string = input.get()
    label["text"] = input_string

# Creating a GUI, changing its title and formatting the size
window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=600, height=300)

# Creating a label object and placing in on the window using the method .pack()
label = tkinter.Label(text="Hello!", font=FORMAT)
# label.pack(side="left")
label.pack()

# Different methods of updating object properties
# #https://docs.python.org/3/library/tkinter.html#handy-reference
label["text"] = "New text"
label.config (text="New text")

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Button2
button2 = tkinter.Button(text="Click Me 2", command=button_clicked_window)
button2.pack()

# Entry (inputting)
input = tkinter.Entry(width=30)
input.pack()
# Include a text to begin with in the entry field (i.e. descriptor)
input.insert(tkinter.END, string="Write your e-mail here.")


# Display on the label whatever input I write on the entry field
button3 = tkinter.Button(text="Show Input", command=show_input)
button3.pack()


# Text entry box for multiple lines of text
text = tkinter.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
text.pack()
print(text.get("1.0", tkinter.END))


# Spinbox that you can click as a counter (i.e. choosing birthdate)
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale is a slider to choose gradually from different values
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton can click on/off
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state (object from class IntVar() ), 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get() # I think this is not needed
checkbutton.pack()


# Radiobutton you can click different options
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

fruit_list = []
# List of options you can choose from (Listbox)
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
    # Store the options selected in a list and print them.
    fruit_list.append(listbox.get(listbox.curselection()))
    print(fruit_list)
    # Display the fruit_list on the GUI
    label["text"] = fruit_list

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



# Keeps the window open and listening for events (PLACE AT THE END OF THE FILE)
window.mainloop()

