#Fausta
#Grey mature sheep.
#Weights 250 pounds.
#Master of using a great sword and a master in dexterity.
import random

class main_character:
    a = 0
    hp = 20
    #starting items
    inventory = [a,hp]

    #append items here
    pickup = ["silver sword"]
    items = ["health_potion"]

    #def use_item()

#function to call attack...
    def attack():
        x = 0
        for x in range(len(main_character.pickup)):
            if main_character.pickup[x] == "silver sword":
                x = x + 1
                return random.randint(5,8)
        else:
            return random.randint(2,3)
#Function for player to heal themself on combat
    def heal():
        if use == "health_potion":
            health_potion = 5
            total = heal + health
            return total
        elif use == "food":
            food = 8
            return heal + health
#Function that adds armor top 
    #def arm():
