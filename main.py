from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
scr = Screen()
scr.setup(600,600)
scr.bgcolor("black")
scr.title("Snake")
scr.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")
scr.onkey(snake.down,"Down")


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.point()
        snake.add_segment()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()


    if (snake.head.xcor() == 280) or (snake.head.xcor() == -280) or (snake.head.ycor() == 280) or (snake.head.ycor() == -280):
        score.reset()
        snake.reset()























scr.exitonclick()