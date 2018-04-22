import turtle
import os
import math
import random

# screen setup
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invader')
wn.bgpic('./images/bg.gif')

# register shape
turtle.register_shape('./images/invader.gif')
turtle.register_shape('./images/player.gif')
turtle.register_shape('./images/lazer.gif')

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

score = 0

# draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

# player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('./images/player.gif')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#  numbers of enemies
number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color('red')
	enemy.shape('./images/invader.gif')
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,200)
	y = random.randint(100,250)
	enemy.setposition(x,y)

enemyspeed = 2

# bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('./images/lazer.gif')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

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

#fire bullet
def fire_bullet():
	global bulletstate
	if bulletstate == 'Ready':
		os.system('afplay ./sounds/lasersound.wav&')
		bulletstate = 'Fire'
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()

#collision functions
def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

# create keyboard binding
turtle.Screen().listen()
turtle.Screen().onkey(move_left,'Left')
turtle.Screen().onkey(move_right,'Right')
turtle.Screen().onkey(fire_bullet, 'space')

# main game loop
while True:

	# loop through all enemies
	for enemy in enemies:
		x = enemy.xcor() + enemyspeed
		enemy.setx(x)
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor() - 40
				e.sety(y)
			enemyspeed *= -1
		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor() - 40
				e.sety(y)
			enemyspeed *= -1
		if isCollision(bullet,enemy):
			os.system('afplay ./sounds/ex.wav&')
			bullet.hideturtle()
			bulletstate = 'Ready'
			bullet.setposition(0,-400)
			x = random.randint(-200,200)
			y = random.randint(100,250)
			enemy.setposition(x,y)
			score += 10
			scorestring = "Score: {}".format(score)
			score_pen.clear()
			score_pen.write(scorestring,False,align='left',font=('Arial',14,'normal'))

		#if enemy hit player
		if isCollision(enemy,player):
			player.hideturtle()
			enemy.hideturtle()
			print('GAME OVER!!')
			break

# 	move bullet
	if bulletstate == 'Fire':
		y = bullet.ycor() + bulletspeed
		bullet.sety(y)

	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = 'Ready'

#make sure to keep game window open
turtle.mainloop()
delay = raw_input('Press enter to quit game')
