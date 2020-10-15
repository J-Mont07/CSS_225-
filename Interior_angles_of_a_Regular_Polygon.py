#Juan Montoya

#Octobe 8, 2020

#Program that calculates the interior angle of the regular ploygon.
#Uses user input and calls a function that calculates the interior angle.


# asks the user for an input value
x = int (input ("How many sides: " ))

#Function to claculate interior angle
def num_sides (x):
    n = x - 2
    n = n * 180 / x
    return n 

#Prints the solution of the users input.
print (num_sides(x))
