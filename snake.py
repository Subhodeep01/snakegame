from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (20, 0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        # self.sc1 = Screen()
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        self.tail = self.parts[len(self.parts)-1]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_parts(pos)

    def add_parts(self, pos):
        part = Turtle(shape="square")
        part.color("white")
        part.penup()
        part.goto(pos)
        self.parts.append(part)

    def reset(self):
        for part in self.parts:
            part.goto(1000, 1000)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]
        self.tail = self.parts[len(self.parts) - 1]

    # def screen(self):
    #     self.sc1.setup(height=600, width=600)
    #     self.sc1.bgcolor("black")
    #     self.sc1.title("Snake Game")
    #     self.sc1.tracer(0)
    #     self.sc1.exitonclick()

    def snake_move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            x = self.parts[i - 1].xcor()
            y = self.parts[i - 1].ycor()
            self.parts[i].goto(x, y)
        self.head.forward(MOVE)

    # def update(self):
    #     self.sc1.update()
    def up(self):
        x = self.head.heading()
        if x != DOWN:
            self.head.setheading(UP)

    def down(self):
        x = self.head.heading()
        if x != UP:
            self.head.setheading(DOWN)

    def right(self):
        x = self.head.heading()
        if x != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        x = self.head.heading()
        if x != RIGHT:
            self.head.setheading(LEFT)
