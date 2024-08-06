import turtle as T
import random
tim=T.Turtle()
T.colormode(255)
tim.hideturtle()
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
tim.speed('fastest')
tim.pensize(2)
def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(5)
screen=T.Screen()
screen.exitonclick()
