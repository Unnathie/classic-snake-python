from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.title("YOUR VERY OWN NOSTALGIC SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_over=Turtle()
game_over.hideturtle()

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.distance(snake.head)<20:
        food.creating_food()
        scoreboard.update_score()
        snake.extension()

    for segment in snake.turtle_list[1:]:  # skip the head
        if snake.head.distance(segment) < 10:
            game_on = False
            game_over.color("red")
            game_over.write("💀💀💀GAME OVER💀💀💀", align="center", font=("Papyrus", 20, "normal"))

    if snake.game_is_on():
        game_over.color("red")
        game_over.write("💀💀💀GAME OVER💀💀💀",align="center",font=("Papyrus",20,"normal"))
        game_on=False



screen.exitonclick()