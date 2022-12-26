from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position)
        self.updatescore()
        self.hideturtle()

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.updatescore()

    def updatescore(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)