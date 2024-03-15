from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(float(random.randint(-260,260)),float(random.randint(-260,260)))

    def refresh(self):
        self.goto(float(random.randint(-260,260)), float(random.randint(-260,260)))


