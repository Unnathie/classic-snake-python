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
        self.write(arg=f"SCORE: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"SCORE: {self.score}", align=ALIGN, font=FONT)



