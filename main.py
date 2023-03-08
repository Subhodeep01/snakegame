from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

sn = Snake()
food = Food()
SB = ScoreBoard()
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
screen.onkey(sn.right, "Right")
screen.onkey(sn.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sn.snake_move()

    if sn.head.distance(food) < 15:
        food.refresh()
        SB.update()
        pos = sn.tail.position()
        sn.add_parts(pos)

    if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
        SB.highscore()
        sn.reset()
        # SB.gameover()

    for parts in sn.parts[1:]:
        if sn.head.distance(parts) < 10:
            SB.highscore()
            sn.reset()
            # SB.gameover()

screen.exitonclick()
