
from turtle import Turtle
FONT=("Comic Sans MS",14,"normal")
ALIGN="Center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("pink")
        self.penup()
        self.goto(0,270)
        self.score=0
        with open("high_score.txt","r") as file:
            self.high_score= int(file.read())
        self.write(arg=f"SCORE: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("high_score.txt","w") as file:
                file.write(str(self.score))
        self.score=0
        self.update_score()

    def increase_score(self):
        self.score+=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)
