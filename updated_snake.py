STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
from turtle import Turtle
class Snake:

    def __init__(self):
        self.turtle_list = []
        self.new_turtle()
        self.head=self.turtle_list[0]
    def new_turtle(self):
        for i in STARTING_POS:
            self.add_new_turtle(i)
    def add_new_turtle(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("green")
        new_turtle.penup()
        self.turtle_list.append(new_turtle)
        new_turtle.goto(position)

    def extension(self):
        tail_x = self.turtle_list[-1].xcor()
        tail_y = self.turtle_list[-1].ycor()
        self.add_new_turtle((tail_x, tail_y))
    def reset(self):
        for turt in self.turtle_list:
            turt.goto(-660,-660)
        self.turtle_list.clear()
        self.new_turtle()
        self.head=self.turtle_list[0]

    def up(self):
        if not (self.head.heading()==UP) :
            self.head.setheading(UP)
    def down(self):
        if not ( self.head.heading()==DOWN):
            self.head.setheading(DOWN)
    def left(self):
        if not (self.head.heading()==LEFT):
            self.head.setheading(LEFT)
    def right(self):
        if not (self.head.heading()==RIGHT):
            self.head.setheading(RIGHT)
    def move(self):
        for turt_number in range(len(self.turtle_list)-1,0,-1):
            new_x=self.turtle_list[turt_number-1].xcor()
            new_y = self.turtle_list[turt_number - 1].ycor()
            self.turtle_list[turt_number].goto(new_x,new_y)
        self.head.forward(MOVING_DISTANCE)
    def game_is_on(self):
        return (self.head.xcor()>=285 or self.head.xcor()<=-285 or
                self.head.ycor()>=285 or self.head.ycor()<=-285)
