import turtle
import os

# screen setup
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invader')

# border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)

border_pen.hideturtle()

# player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#create invaders
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2

# bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

# bullet state
# ready to fire

# fire
bulletstate = 'Ready'

# move to right and left
def move_left():
	x = player.xcor() - playerspeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor() + playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == 'Ready':
		bulletstate = 'Fire'
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()


# create keyboard binding
turtle.Screen().listen()
turtle.Screen().onkey(move_left,'Left')
turtle.Screen().onkey(move_right,'Right')
turtle.Screen().onkey(fire_bullet, 'space')

# main game loop
while True:

	x = enemy.xcor() + enemyspeed
	enemy.setx(x)
	if enemy.xcor() > 280:
		enemyspeed *= -1
		y = enemy.ycor() - 40
		enemy.sety(y)
	if enemy.xcor() < -280:
		enemyspeed *= -1
		y = enemy.ycor() - 40
		enemy.sety(y)

# 	move bullet
	if bulletstate == 'Fire':
		y = bullet.ycor() + bulletspeed
		bullet.sety(y)

	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = 'Ready'

turtle.mainloop()
delay = raw_input('Press enter to quit game')
