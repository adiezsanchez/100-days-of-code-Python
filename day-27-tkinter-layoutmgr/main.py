from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Add padding around the widgets so they are not directly touching the edges of the window
window.config(padx=20, pady=20)


#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)
new_button.config(padx=10, pady=10)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)









window.mainloop()