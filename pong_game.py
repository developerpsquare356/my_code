
#                                                                                PONG  GAME

from turtle import  Turtle, Screen
import random
import time
# create the screen
screen=Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
screen.title("My Pong Game Designed By Prantik Pal")
screen.listen()
screen.tracer(0)

class paddle(Turtle):
    def __init__(self,position) -> None:
        super().__init__()
        self.create(position)
        self.move_up()
        self.move_down()

    def create(self,position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(3,0.3)

    def move_down(self):
        new_cor=self.ycor() -20
        self.goto(self.xcor(),new_cor)
    def move_up(self):
        new_cor=self.ycor() +20
        self.goto(self.xcor(),new_cor)


class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8,0.8)
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.ymove*=-1

    def bounce_x(self):
        self.xmove*=-1
        self.move_speed*=0.9


    def reset_position(self):
        self.goto(0,0)

        self.bounce_x()



class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,280)
        self.write(f'Score : {self.l_score} ',align="center",font=("Arial",14,"normal"))
        self.goto(100,280)
        self.write(f'Score : {self.r_score} ',align="center",font=("Arial",14,"normal"))

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()

    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()




ball=Ball()

score=Scoreboard()

right_p=paddle((480,0))
left_p=paddle((-480,0))
screen.onkey(left_p.move_up,"Up")
screen.onkey(left_p.move_down,"Down")
screen.onkey(right_p.move_up,"a")
screen.onkey(right_p.move_down,"z")



is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detecte collition with wall
    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()
    #detecte collition with paddle
    if right_p.distance(ball)<20 and  ball.xcor()>460 or ball.xcor()<-460  and left_p.distance(ball)<20:
        ball.bounce_x()

    if ball.xcor()>480 :
        ball.reset_position()
        ball.move_speed=0.1
        score.l_point()
    if ball.xcor()<-480:
        ball.reset_position()
        ball.move_speed=0.1
        score.r_point()

    if score.l_score>5 or score.r_score>5:
        is_game_on=False

screen.exitonclick()
