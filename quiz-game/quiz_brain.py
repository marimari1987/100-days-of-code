class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.list) # if statement kann man sich sparen, es gibt ja eh True oder False aus

    def next_question(self):
        question = self.list[self.question_number]  # der entsprechende Listeneintrag ist ja ein Objekt mit zwei Attributen
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")  # ich möchte das attribut text ausgeben
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Yor current score is: {self.score}/{self.question_number}")
        print("\n")


