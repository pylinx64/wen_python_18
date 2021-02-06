import turtle
import time

t = turtle.Pen()
colors = ['#2DE986', '#2DE7E9', '#E9D72D', '#DA70D1', '#70DA9B']
turtle.bgcolor('black')
t.speed(10)

text = turtle.textinput(' ', 'Введите текст: ')

for i in range(1000):
	t.pencolor(colors[i%5])
	t.penup()
	t.forward(i * 25)
	t.pendown()
	t.write(text, font=("Thintel", int((i + 4) / 4), "bold"))
	t.left(67)

time.sleep(50)

