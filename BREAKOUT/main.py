import turtle

import time



# Setup the screen

screen = turtle.Screen()

screen.title("Breakout Game")

screen.bgcolor("black")

screen.setup(width=800, height=600)

screen.tracer(0)



# Paddle

paddle = turtle.Turtle()

paddle.shape("square")

paddle.color("white")

paddle.shapesize(stretch_wid=1, stretch_len=5)

paddle.penup()

paddle.goto(0, -250)



# Ball

ball = turtle.Turtle()

ball.shape("circle")

ball.color("red")

ball.penup()

ball.goto(0, -230)

ball.dx = 2

ball.dy = 2



# Bricks

bricks = []

colors = ["red", "orange", "yellow", "green", "blue"]

for i in range(5):

    for j in range(10):

        brick = turtle.Turtle()

        brick.shape("square")

        brick.color(colors[i])

        brick.shapesize(stretch_wid=1, stretch_len=2)

        brick.penup()

        brick.goto(-350 + j * 80, 250 - i * 30)

        bricks.append(brick)



# Score

score = 0

score_display = turtle.Turtle()

score_display.color("white")

score_display.penup()

score_display.hideturtle()

score_display.goto(0, 260)

score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))



# Functions

def paddle_left():

    x = paddle.xcor()

    if x > -350:

        paddle.setx(x - 20)



def paddle_right():

    x = paddle.xcor()

    if x < 350:

        paddle.setx(x + 20)



# Keyboard bindings

screen.listen()

screen.onkeypress(paddle_left, "Left")

screen.onkeypress(paddle_right, "Right")



# Game loop

while True:

    screen.update()



    # Move the ball

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)



    # Bounce off walls

    if ball.xcor() > 390 or ball.xcor() < -390:

        ball.dx *= -1



    if ball.ycor() > 290:

        ball.dy *= -1



    # Bounce off paddle

    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):

        ball.dy *= -1



    # Ball falls below the paddle

    if ball.ycor() < -290:

        score_display.clear()

        score_display.write("Game Over", align="center", font=("Courier", 24, "normal"))

        time.sleep(2)

        break



    # Ball hits bricks

    for brick in bricks:

        if brick.isvisible() and abs(ball.xcor() - brick.xcor()) < 40 and abs(ball.ycor() - brick.ycor()) < 15:

            brick.hideturtle()

            ball.dy *= -1

            score += 10

            score_display.clear()

            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))



    # Check if all bricks are broken

    if all(not brick.isvisible() for brick in bricks):

        score_display.clear()

        score_display.write("You Win!", align="center", font=("Courier", 24, "normal"))

        time.sleep(2)

        break



screen.mainloop()