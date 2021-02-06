import turtle
import time

colors = ['#EEEB87', 'orange', '#87EE87', '#87D9EE', '#D687EE']
t = turtle.Pen()
t.pencolor('lime')
turtle.bgcolor('black')
t.speed(10000)

i = 0
while i < 36:
	t.pencolor(colors[i%5])
	t.forward(1)
	t.left(10)
	i = i + 1


t.circle(10)

time.sleep(200)
