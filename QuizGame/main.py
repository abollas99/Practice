from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for n in question_data:
    question_text = n["text"]
    question_answer = n["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

for n in range(0, len(question_bank)):
    quiz.next_question()

print(f"You have {quiz.correct} correct answers")