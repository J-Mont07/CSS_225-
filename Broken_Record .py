#Juan Montoya

#October 8, 2020

#Programs skips throught tracks 0 through 11.

#Asks the user for current track number

t = int ( input ("What track is currently playing?: "))

#Asks the user how many tracks they would like to skipp

s = int ( input ("How many tracks would you like to skip?: "))

#Function of skipping tracks.

def track_num (t,s):
    
    x = t + s
    x = x % 12

    return x

#Prints the track that is going to play on the record player. 
print (track_num(t,s))
