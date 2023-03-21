import turtle
import playsound

playsound.playsound('C:\Users\ELCOT\Desktop\2-player-pong-game\Dheera Dheera-[TamilDaDa.Info].mp3')


score_a = 0
score_b = 0


win=turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("2 player Pong Game")
win.tracer(0)


#left paddle as l_p

l_p=turtle.Turtle()
l_p.speed(0)
l_p.shape("square")
l_p.color("white")
l_p.shapesize(stretch_wid=5,stretch_len=1)
l_p.penup()
l_p.goto(-380,0)


# right paddle as r_p

r_p=turtle.Turtle()
r_p.speed(0)
r_p.shape("square")
r_p.color("white")
r_p.shapesize(stretch_wid=5,stretch_len=1)
r_p.penup()
r_p.goto(375,0)


# ball as b
b=turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("red")
b.penup()
b.dx=0.50
b.dy=0.50


# score
sc=turtle.Turtle()
sc.speed(0)
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Player A: 0   Player B: 0",align="center",font=("Ariel",22,"normal"))

# moving paddles
def l_p_up():
    l_p.sety(l_p.ycor()+20)

def l_p_down():
    l_p.sety(l_p.ycor()-20)

def r_p_up():
    r_p.sety(r_p.ycor()+20)

def r_p_down():
    r_p.sety(r_p.ycor()-20)



win.listen()
win.onkeypress(l_p_up,'w')
win.onkeypress(l_p_down,'s')
win.onkeypress(r_p_up,'Up')
win.onkeypress(r_p_down,'Down')




while True:
    win.update()

    # ball movement

    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)

    # ball -well collision
    # top wall
    if b.ycor()>290:
        b.sety(290)
        b.dy *=-1
    # bottom wall
    if b.ycor()<-290:
        b.sety(-290)
        b.dy *=-1
    # right wall
    if b.xcor()>390:
        b.setx(390)
        b.dx *=-1
        score_a +=1
        sc.clear()
        sc.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center",font=("Ariel",22,"normal"))
    # left_wall
    if b.xcor()<-390:
        b.setx(-390)
        b.dx *=-1
        score_b +=1
        sc.clear()
        sc.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center",font=("Ariel",22,"normal"))
        
    # collision with paddles
    if b.xcor() > 360 and r_p.ycor()-50<b.ycor()<r_p.ycor()+50:
        b.setx(360)
        b.dx *= -1
    if b.xcor() < -360 and l_p.ycor()-50<b.ycor()<l_p.ycor()+50:
        b.setx(-360)
        b.dx *= -1
