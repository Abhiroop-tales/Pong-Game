from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
left_score = Score((-150,270))
right_score = Score((150,270))

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    
    # Detect Collison with wall
    ball.move()
    
    # Detect Collison with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle)<50 and ball.xcor() < -330:
        ball.paddleCollison()
    
    # Detect the Collison miss
    if ball.distance(right_paddle) > 50 and ball.xcor() > 380:
        left_score.increase_score()
        ball.reset()

    if ball.distance(left_paddle) > 50 and ball.xcor() < -380:
        right_score.increase_score()
        ball.reset()


screen.exitonclick()