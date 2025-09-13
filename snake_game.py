
#                                                                           SNAKE  GAME

from turtle import  Turtle, Screen
import random
import time
# create the screen
screen=Screen()
screen.setup(width=700,height=700)
screen.bgcolor("black")
screen.title("My Snake Game Designed By Prantik Pal")
screen.tracer(0)

start_position=[(0,0),(-20,0),(-40,0)]
steps=20
class Snake:
    def __init__(self) :
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for i in start_position:
            self.add_segment(i)

    def add_segment(self,position):
        tim=Turtle(shape="square")
        tim.color("AliceBlue")
        tim.penup()
        tim.goto(position)
        self.segment.append(tim)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def move_snake(self):
        for i in range(len(self.segment)-1,0,-1):
            new_x=self.segment[i-1].xcor()
            new_y=self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.head.forward(steps)

    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() !=90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() !=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() !=0:
            self.head.setheading(180)


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.refresh()
    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.speed(0)
        self.goto(random_x,random_y)


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,330)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'Score : {self.score} ',align="center",font=("Arial",14,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f' Game Over \n Your Final Score is {self.score} \n Better Luck Next Time ',align="center",font=("Arial",24,"normal"))


snake=Snake()
food=Food()
scoreboard=Scoreboard()
# control key
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_race_on=True

while is_race_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect coloision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    # snake collision with wall
    if snake.head.xcor()>350 or snake.head.xcor()<-350 or snake.head.ycor()>350 or snake.head.ycor()<-350:
        is_race_on=False
        scoreboard.game_over()

    # snake collision with tail

    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            is_race_on=False
            scoreboard.game_over()

screen.exitonclick()
