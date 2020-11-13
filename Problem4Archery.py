#Juan Montoya
#November 12, 2020
#This program is a mini archery game that uses the random import. 
import random

arrows = 10

player_score = 0

score_card = []

while  arrows != 0:
    target = random.randint(0,10)
    
    score_card.append(target)
    if target == 0:
        player_score = player_score
        arrows = arrows 

    elif target == 10:
        player_score = player_score + 20
        score_card.append(target)
        arrows = arrows - 1
    else:
        player_score = player_score + target
        arrows = arrows - 1 

print (player_score) 
print (score_card)
