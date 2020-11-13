#Juan Montoya
#November 12, 2020
#Re-wrote Module 6 Lab activity problem one as a while loop.
#Prints 10 random numbers from 25 through 35 

import random

count = 0
while count < 10:
    count = count + 1
    print (random.randint(25, 35))
