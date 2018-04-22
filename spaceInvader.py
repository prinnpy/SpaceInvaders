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

# create keyboard binding
turtle.Screen().listen()
turtle.Screen().onkey(move_left,'Left')
turtle.Screen().onkey(move_right,'Right')




turtle.mainloop()
delay = raw_input('Press enter to quit game')
