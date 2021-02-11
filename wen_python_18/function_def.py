import turtle

colors=['#C500FF', '#003CFF', '#42FF00']
t=turtle.Pen()

turtle.bgcolor('black')

i=121

def side():
	t.pencolor(colors[2])
	t.forward(100)
	t.left(i)

for x in range(0, 1000):
	side()

turtle.done()
