from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

"Loop using the range function."

# for dictionary in range(len(question_data)):
#     ind_q = question_data[dictionary]
#     new_question = Question(ind_q["text"], ind_q["answer"])
#     question_bank.append(new_question)

"Loop through each dictionary in a list"

for dictionary in question_data:
    new_question = Question(dictionary["text"], dictionary["answer"])
    question_bank.append(new_question)

"Access each object in the question_bank and print the text and answer attributes"

# for objects in question_bank:
#     print(objects.text)
#     print(objects.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score is: {quiz.score}/{len(question_bank)}")