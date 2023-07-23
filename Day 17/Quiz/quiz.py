#simple true or false
#let them know if correct or not and provide score
from question_model import Question
from data import question_data
import quiz_brain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_question:
  quiz.next_question()

print("You've completed the quiz!")
print(f"Your finals score was: {quiz.score}/{len(quiz.question_number)}")
