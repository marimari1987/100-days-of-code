from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # festgelegter Datentyp QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Label
        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=FONT, fg="white")
        self.score.grid(row=0, column=1, padx=20, pady=20)
        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=FONT,
            fill=THEME_COLOR)  # width  macht automatische Zeilenumbrüche
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # buttons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.yes_button = Button(image=true_image, command=self.check_answer_true, bd=0)
        self.yes_button.grid(row=2, column=0, padx=20, pady=20)
        self.no_button = Button(image=false_image, command=self.check_answer_false, bd=0)
        self.no_button.grid(row=2, column=1, padx=20, pady=20)
        # initiale frage anzeigen
        self.get_next_question()
        # mainloop
        self.window.mainloop()

    def get_next_question(self):  # wenn man verscuht die Funktion direkt aus quizbrain aufzurufen,
        # fehlt ihm das self argument
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, right_answer: bool):
        if right_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
