from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start_position()
        self.increase_speed = False

    def start_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        y = self.ycor() + MOVE_DISTANCE
        x = self.xcor()
        self.goto(x, y)

    def finis_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
