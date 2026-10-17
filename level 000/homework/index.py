from turtle import *

# we want to paint a house

# step 1: draw a square

width(7)
color("blue")
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# end of the square

# drawin a door

forward(70)

color("yellow")
begin_fill()
left(90)

forward(90)
right(90)

forward(70)
right(90)

fillcolor()

forward(90)
end_fill()
penup()

goto(200, 200)
pendown()

color("red")
begin_fill()

left(180)
left(50)
forward(130)

left(80)
forward(130)
end_fill()

color("blue")

left(50)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

left(90)
forward(60)
left(90)
forward(33)
left(90)
forward(60)

left(90)
forward(33)

left(90)
forward(30)
left(90)

forward(60)
penup()
goto(200, 200)
pendown()
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(32)
left(90)
forward(58)
left(90)
forward(32)
left(90)
forward(30)

left(90)
forward(60)
left(90)
forward(32)
left(90) 
forward(32)

exitonclick()
