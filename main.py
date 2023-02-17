from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Snake GAME by Miquel")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) <15:
        scoreboard.update_score()
        snake.extend()
        food.refresh()

    #Detect collision with edges.
    if snake.head.xcor() > 500 or snake.head.xcor() < -500 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # screen.clear()
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()
    #if head collides with any segment in the tails:
        #trigger game_over

screen.exitonclick()
