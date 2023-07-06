from tkinter import *
# Importin the QuizBrain class to let the QuizInterface class we expect a QuizBrain "datatype" as input
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FORMAT = ("Arial", 15, "italic")
FORMAT_LABEL = ("Arial", 10, "bold")

class QuizInterface():
    # Letting the QuizInterface class know we expect a QuizBrain object as input
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0/10", bg=THEME_COLOR, fg="white", font=FORMAT_LABEL)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Example Question Text",
            fill=THEME_COLOR,
            font=FORMAT,
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_img, bg=THEME_COLOR, relief="flat", command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_img, bg=THEME_COLOR, relief="flat", command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    # Create two methods, add them as command to the buttons. Methods call check_answer() from quiz_brain and pass over
    # the string "True" or "False".

    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.reset_background)
        self.window.after(500, self.get_next_question)

    def reset_background(self):
        self.canvas.config(bg="white")