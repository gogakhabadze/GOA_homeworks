from turtle import *

speed(30)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#step 2 door (i guess)
begin_fill()
forward(70)
color("yellow")
left (90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#step thre roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#step3 windows ( this is super easy )
color("purple")
begin_fill()
left(30)
forward(100)
left(90)
color("blue")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

#step 4 window second
penup()
goto(200, 100)
pendown()

begin_fill()
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill() # this is the end of the second window 




#step 5 sun ( this is super easy ) 




exitonclick()

