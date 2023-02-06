class QuizBrain:
    def __init__(self,question_list):
        self.number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.number]
        self.number += 1
        user_answer = input(f"Q {self.number}: {current_question.text} True/False : ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_question(self):
        return self.number < len(self.question_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print ("you got it right")
            self.score += 1
        else:
            print ("it is wrong answer")
        print (f"the correct answer : {correct_answer}")
        print (f"You current score is {self.score} / {self.number}")
        print ("\n")