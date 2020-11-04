#Juan Montoya
#
#October 29, 2020
#
#This program will print the numbers on \n
#I am not able to print the new list in the power of 2.
import math
#Example list
s = ["12","10","32","3","66"]
#function to **2 the numbers on the list
def square (n):
    return (n ** 2)

#for loop to print numbers on \n
for first_set in range(5):
    print (s[first_set])

print("")

#for loop to square numbers
for second_set in range(5):
    print(math.pow(s,[second_set]))
