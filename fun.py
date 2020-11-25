Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> s = turtle.Screen()
>>> s.bgcolor('black')
>>> t.pencolor('white')
>>> a=0
>>> b=0
>>> t.speed(0)
>>> t.penup()
>>> t.goto(0,200)
>>> t.pendown()
>>> while True:
	t.forward(a)
	t.right(b)
	a=a+3
	b= b+1
	if b==210:
		break
	t.hideturtle()

	
>>> turtle.done()
