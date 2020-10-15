#Juan Montoya

#October 8, 2020

#Program calculates the BMI of the user.

#Asks the input of the user's weight

w = int (input ("What is your weight in lbs?: "))

#Asks the input of the user's height

h = int (input ("What is your height in inches?: "))

#Function that calculates the BMI

def bmi_result (w,h):

    x = (h**2)
    x = (w / x * 703)
    return round (x,2)

#prints the result of the BMI
print (bmi_result(w,h))
    
