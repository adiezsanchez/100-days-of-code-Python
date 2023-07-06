from tkinter import *
import win32api
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark_string = ""
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checkmark_string
    global reps
    global timer

    window.after_cancel(timer)
    display.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

    checkmark_string = ""
    reps = 0
    timer = None

    checkmark_label.config(text=checkmark_string)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # Increase the reps everytime we click the Start Button
    # Access AND MODIFY a global scope variable within a function USING GLOBAL
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        display.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 0:
        win32api.Beep(300, 2500)
        count_down(short_break_secs)
        display.config(text="Short Break", fg=PINK)
    else:
        count_down(work_secs)
        display.config(text="Work Time", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# This functions calls itself after 1000ms of being triggered in main and inputs the initial count -1
def count_down(count):
    global checkmark_string

    # math.floor returns the largest floor number
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Solve the remainder 0 bug and the lack of 0 in front of the secs once they are below 10:
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # This method updates a particular argument/value within the timer_text object
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # After 1000ms, calls this function, and passes the count argument
        # To cancel this function when resetting I have to asign it to a variable, this is a local scope variable, so
        # in order to access it from another function I have to make it a global one
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_string += "✔"
            checkmark_label.config(text=checkmark_string)
            win32api.Beep(500, 2500)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Read the image and save it in a variable
tomato_img = PhotoImage(file="tomato.png")

# Display label
display = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
display.grid(column=1, row=0)

# Create the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="START", command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
start_button = Button(text="RESET", command=reset_timer)
start_button.grid(column=2, row=2)

# Check Mark label
checkmark_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
