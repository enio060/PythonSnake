from turtle import Turtle



class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            Snake = Turtle(shape="square")
            Snake.penup()
            Snake.color("white")
            Snake.goto(int(Snake.xcor()) - 20 * i, 0)
            self.segments.append(Snake)

    def move(self):
        for czesc in range(len(self.segments) - 1, 0, -1):
            x = self.segments[czesc - 1].xcor()
            y = self.segments[czesc - 1].ycor()
            self.segments[czesc].goto(x, y)
        self.segments[0].forward(20)

    def add_segment(self):
        Snake = Turtle(shape="square")
        Snake.color("white")
        Snake.penup()
        Snake.goto(int(self.segments[-1].xcor()) -20. , 0)
        self.segments.append(Snake)


    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() !=180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
