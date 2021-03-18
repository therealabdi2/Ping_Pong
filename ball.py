from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.track_x = 10
        self.track_y = 10
        self.mov_speed = 0.1

    def update_position(self):
        new_x = self.xcor() + self.track_x
        new_y = self.ycor() + self .track_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.track_y *= -1

    def bounce_x(self):
        self.track_x *= -1
        self.mov_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.mov_speed = 0.1
        self.bounce_x()


