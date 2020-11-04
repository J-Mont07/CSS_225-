#Juan Montoya

#November 01,2020

#This program will be able to iterate the integers from 1 to 50.
#It will check if the integers are divisable by 3 or 5.
#It will also check if it is divisable by both!

for num in range(51):
    if num % 3 == 0:
        print (num)
        print ("Divisible by three")
    elif num % 5 == 0:
        print (num)
        print ("Divisable by five")
    if num % 3 == 0 and num % 5 == 0:
        print ("Divisable by both")
