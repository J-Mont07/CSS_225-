#Juan Montoya
#
#Novemeber 01,2020
#
#Bonus: Create a drawing in a turtle shell...

import turtle

t = turtle.Turtle()

for v in range(50):
    t.left(90)
    t.forward(100)
    t.left(55)

for g in range(51):
    t.pencolor("Red")
    t.right(90)
    t.forward(100)
    t.right(55)
t.right(90)
t.forward(100)
t.left(90)
t.pencolor("Black")


