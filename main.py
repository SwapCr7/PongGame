import turtle
import winsound

# Window Screen
windown_screen = turtle.Screen()
windown_screen.title("Pong by Swapnil")
windown_screen.bgcolor("black")
windown_screen.setup(width=800, height=600)  # screen width and height
windown_screen.tracer(0)  # to speed up the game

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # this is the speed of the animation. It sets to the maximum speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)  # reshape the 20*20 pixel of the original square shape
paddle_a.penup()  # Turtle will move around the screen, but will not draw when its pen state is PENUP.
paddle_a.goto(-350, 0)  # position of the paddle A

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.8
ball.dy = 0.8

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)  # sets the animation
pen.color("white")
pen.penup()  # so that we don't see line when turtle move
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()  # get the y coordinate of the paddle_a
    y += 20
    paddle_a.sety(y)  # set the y coordinate to the new y


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keystroke listen
windown_screen.listen()
windown_screen.onkeypress(paddle_a_up, "w")
windown_screen.onkeypress(paddle_a_down, "s")
windown_screen.onkeypress(paddle_b_up, "Up")
windown_screen.onkeypress(paddle_b_down, "Down")

running = True
# Game Loop
while running:
    windown_screen.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # check the boundaries

    # top and bottom
    if ball.ycor() > 290:
        # set ball y coordinate to 290 and change the direction of the ball
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        # set ball y coordinate to 290 and change the direction of the ball
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # right and left
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
