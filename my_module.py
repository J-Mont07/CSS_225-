#Juan Montoya
#Novemeber 5, 2020
#this module implements functions

import random
import math

#For loop that prints random number ten times.
#From 25 through 35
def ten_ran():
    for n in range (10):
        print (random.randint(25, 35))

#prints a random element from list
def lst_ran():
    l = ["Stop","Go","Green","Red","Drive","Reverse"]
    x = random.choice(l)
    return x

#prints a random odd number
def odd_num():
   r = random.randint(0, 100)
   if r != 0:
       print (r)

#calculates the Pythagorean Theorme
def pyth_theor (a, b):
    a = math.pow(a,2)
    b = math.pow(a,2)
    t = a + b
    c = math.sqrt(t)

    return c

