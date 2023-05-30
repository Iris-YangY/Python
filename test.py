centralpoint=[(-50,150),(50,150),(150,150),
              (-50,50),(50,50),(150,50),
              (-50,-50),(50,-50),(150,-50)]
import turtle
def draw_X(pointx, pointy):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(pointx,pointy)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("red")
    turtle.left(45)
    turtle.forward(45)
    turtle.left(180)
    turtle.forward(90)
    turtle.left(180)
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)
    turtle.forward(90)

draw_X(centralpoint[2][0], centralpoint[2][1])

def draw_O(x,y):
    turtle.penup()
    turtle.goto(x-30,y-30)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("blue")
    turtle.circle(45)

draw_O(centralpoint[2][0], centralpoint[2][1])
