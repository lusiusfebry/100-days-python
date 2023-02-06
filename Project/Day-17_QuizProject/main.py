from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def main():
    question_bank = []
    for data in question_data:
        text = data["text"]
        answer = data["answer"]
        new_question = Question(text, answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_question():
        quiz.next_question()

    print ("You have completed the quiz")
    print (f"your finals score is {quiz.score} / {quiz.number}")



main()