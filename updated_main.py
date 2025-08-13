from turtle import Screen, Turtle
import time
from updated_snake import Snake
from food import Food
from updatedscore import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("YOUR VERY OWN NOSTALGIC SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)

updated_snake = Snake()
food = Food()
updated_score = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=updated_snake.up)
screen.onkey(key="Down", fun=updated_snake.down)
screen.onkey(key="Left", fun=updated_snake.left)
screen.onkey(key="Right", fun=updated_snake.right)

game_over = Turtle()
game_over.hideturtle()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    updated_snake.move()
    if food.distance(updated_snake.head) < 20:
        food.creating_food()
        updated_score.increase_score()
        updated_snake.extension()

    for segment in updated_snake.turtle_list[1:]:  # skip the head
        if updated_snake.head.distance(segment) < 10:
            updated_score.reset()
            updated_snake.reset()
    if updated_snake.game_is_on():
        updated_score.reset()
        updated_snake.reset()


screen.exitonclick()