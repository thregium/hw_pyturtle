

import turtle
import random
import math
s=turtle.Screen()


score = 0

airplane = turtle.Turtle()
airplane.color("blue")
airplane.shape("turtle")
airplane.penup()
airplane.speed(0)
airplane.goto(0,-200)
screen=airplane.getscreen()
shot=turtle.Turtle()
shot.pensize(10)
shot.color("white")
scoretext=turtle.Turtle()
scoretext.hideturtle()
scoretext.pencolor("red")
scoretext.penup()
scoretext.goto(200,200)
scoretext.write("점수:"+str(score))


asteroids=[]
for i in range(35):
    plant=turtle.Turtle()
    plant.color("yellow")
    plant.shape("circle")
    plant.penup()
    plant.speed(0)
    plant.goto(random.randint(-300,300),random.randint(-300,300))
    asteroids.append(plant)

def left():
    airplane.setheading(180)
    airplane.fd(10)
    
    
def right():
    airplane.setheading(0)
    airplane.fd(10)

def turnup():
    airplane.setheading(90)
    airplane.fd(10)

def turndown():
    airplane.setheading(270)
    airplane.fd(10)
    


    
def bullet():
    
    def bullethit():
        global score

        asteroids_to_remove = []
        for i in range(len(asteroids)):
            if shot.distance(asteroids[i].xcor(), asteroids[i].ycor()) < 15:
                score += 1
                asteroids_to_remove.append(i)

        for i in asteroids_to_remove:
            asteroids[i].ht()
            del asteroids[i]

        if len(asteroids_to_remove) != 0:
            scoretext.clear()
            scoretext.write("점수:"+str(score))
        return score

    
    shot.color("black")
    shot.shape("arrow")
    shot.penup()
    shot.speed(0)
    shot.goto(airplane.xcor(),airplane.ycor())
    shot.setheading(airplane.heading())
    for i in range(20):
        shot.fd(10)
        screen.ontimer(bullethit, 10)
    shot.clear()

    
screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")
screen.onkeypress(bullet,'space')
screen.onkeypress(turnup, "Up")
screen.onkeypress(turndown, "Down")
screen.listen()


x=-3000
y=-2999
      
def play():
       
    for plant in asteroids:
        plant.right(random.randint(-180,180))
        plant.forward(10)
        if shot.distance(plant)< 35:
             plant.goto(-3000,-2999)

              
            
    screen.ontimer(play,10)
screen.ontimer(play,10)



laser = turtle.Turtle()
laser.pensize(4)
laser.hideturtle()
laser.speed(0)

def turnleft():
    airplane.left(10) 
def turnright():
    airplane.right(10) 

def laserevent():
    def laserclear():
        laser.clear() 
    laser.penup()
    laser.goto(airplane.xcor(), airplane.ycor()) 
    laser.pendown()
    laser.setheading(airplane.heading()) 
    laser.forward(1000) 
    i = 0
    while True:
        if i >= len(asteroids): break
        if ((1 - asteroids[i].xcor() / 180 * math.pi) * math.sin(laser.heading() / 180 * math.pi) < 100):
            del asteroids[i]
        i += 1
    screen.ontimer(laserclear, 400)



