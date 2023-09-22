from turtle import Turtle
SCORE_BOARD_POSITION=(-300,260)
ALIGNMENT ="center"
FONT = "Comic Sans"
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(SCORE_BOARD_POSITION)
        self.level=0
        self.update()
    def level_up(self):
        self.clear()
        self.level+=1
        self.update()
    def update(self):
        self.write(f"Level : {self.level}",align=ALIGNMENT,font=(FONT,24,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("purple")
        self.write("GAME OVER !!",align=ALIGNMENT,font=(FONT,24,"normal"))