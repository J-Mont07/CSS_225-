#Juan Montoya
#
#October 29,2020
#
#This program asks the user for input of user.

import turtle

t = turtle.Turtle()

#asks the user for input
s = int (input("Number of sides: "))

l = int (input("Length of side: "))

c = input ("color of line: ")

f = input ("Fill color: ")

#sets fill color from user input
t.fillcolor(f)

t.begin_fill()

#function for user input for polygon
for x in range(s):
    t.pencolor(c)
    t.left(l)
    t.forward(100)

#ends the color fill
t.end_fill()
    
