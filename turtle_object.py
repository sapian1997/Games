from turtle import Turtle

STARTING_POSITION=(0, -280)
FINISH_LINE=280

class turtle_obj(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def is_finsih_line(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False
    def goto_start(self):
        self.goto(STARTING_POSITION)