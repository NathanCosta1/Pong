import turtle 
import time # used in line 87
import winsound #using this to get sound

win = turtle.Screen()
win.title ("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) #Stops the window from updating, speeds up game


#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of animation, max possible speed
paddle_a.shape("square") #20 by 20 pixles as default
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #Not drawing a line? Default is to draw a line
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Speed of animation, max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #Not drawing a line? Default is to draw a line
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #Speed of animation, max possible speed
ball.shape("square")
ball.color("white")
ball.penup() #Not drawing a line? Default is to draw a line
ball.goto(0,0)
ball.dx = 2 #dx means change in x, delta x 
ball.dy = 2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {} \t\t\t Player 2: {}".format(score_a,score_b),align="center",font=("Consolas",16,"normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor() 
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() 
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -=20
    paddle_b.sety(y)


#Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


#Every game needs a "Main game loop"

while True:
        time.sleep(1/60) #makes the ball move at a constant rate

        win.update() #Every time the loop runs, this updates the screen

        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        

        #Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("C:/Users/82nat/OneDrive/Desktop/Programming/Python Projects/Pong/bounce.wav",winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("C:/Users/82nat/OneDrive/Desktop/Programming/Python Projects/Pong/bounce.wav",winsound.SND_ASYNC)


        if ball.xcor() >390: 
            ball.goto(0,0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player 1: {} \t\t\t Player 2: {}".format(score_a,score_b),align="center",font=("Consolas",16,"normal"))
            winsound.PlaySound("C:/Users/82nat/OneDrive/Desktop/Programming/Python Projects/Pong/bounce.wav",winsound.SND_ASYNC)


        if ball.xcor() <-390: 
            ball.goto(0,0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player 1: {} \t\t\t Player 2: {}".format(score_a,score_b),align="center",font=("Consolas",16,"normal"))
            winsound.PlaySound("C:/Users/82nat/OneDrive/Desktop/Programming/Python Projects/Pong/bounce.wav",winsound.SND_ASYNC)

        #Making the paddles not be able to go off the screen
        if  paddle_a.ycor() > 250:
            paddle_a.sety(250)

        if  paddle_a.ycor() < -250:
            paddle_a.sety(-250)

        if  paddle_b.ycor() > 250:
            paddle_b.sety(250)

        if  paddle_b.ycor() < -250:
            paddle_b.sety(-250)
        

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("C:/Users/82nat/OneDrive/Desktop/Programming/Python Projects/Pong/bounce.wav",winsound.SND_ASYNC)

        #Paddle and ball collisions

        if ball.xcor()> 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            ball.dx *= 1.03 #speeds game up slightly 
            ball.dy *= 1.03 #speeds game up slihgtly
            winsound.PlaySound("C:/Users/82nat/OneDrive/Desktop/Programming/Python Projects/Pong/bounce.wav",winsound.SND_ASYNC)
            
        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            ball.dx *= 1.03 #speeds up game slightly 
            ball.dy *= 1.03 #speeds up game slightly 
            winsound.PlaySound("C:/Users/82nat/OneDrive/Desktop/Programming/Python Projects/Pong/bounce.wav",winsound.SND_ASYNC)
