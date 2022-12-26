from turtle import Turtle

BALL_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = BALL_SPEED
    
    def move(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.ymove = self.ymove*(-1)       
        self.bounce()

    def bounce(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
    
    def paddleCollison(self):
        self.xmove = self.xmove*(-1)
        self.move_speed = self.move_speed*0.9
        self.bounce()

    def reset(self):
        self.goto(0,0)
        self.move_speed = BALL_SPEED
        self.xmove = self.xmove*(-1)

