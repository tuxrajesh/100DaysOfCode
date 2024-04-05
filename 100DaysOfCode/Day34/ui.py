THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.initialize()
        
    def initialize(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, 
            text="Sample Question", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR,
            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        false_img = PhotoImage(file=".\\images\\false.png")
        true_img = PhotoImage(file=".\\images\\true.png")
        
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)
        
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)
        
        self.get_next_question()        
                
        self.window.mainloop()
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        return
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        return
        
    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
        
        return
        
    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
            
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)        
    