#combat section
import main_character as mc
import enemies as e
import random

#quick responses:
f = "Fausta:"
n = "Narrator:"

def rat():
    print(f,"Looks like we are fighting a",e.rat.name)
    print (f,"Looks weak, it has",e.rat.hp,"HP")
    print("....................................")
    print("Let the fighitng BEGIN")
    print ("You got to choose between two actions: ", "\nattack","\nblock")
    choose = input(e)
    while mc.main_character.hp >= 0 and e.rat.hp >=0:
        choose = input("What do you want to do?")
        if choose.lower() == "attack":
            e.rat.hp = e.rat.hp - mc.main_character.attack()
            print("Nice hit!!", e.rat.name,"HP left:",e.rat.hp)
            if e.rat.hp <= 0:
                print("You have slayed the enemy!!")
                return
            print("Now its",e.rat.name,"turn")
            mc.main_character.hp = mc.main_character.hp - e.rat.attack
            print("you got hit","HP left:",mc.main_character.hp)
        if choose.lower() == "block":
            print("You took no damage")
            print("HP left:",mc.main_character.hp)
            #Checks inventory
        if choose.lower() == "inventory":
            x = 0
            for x in range(len(mc.main_character.items)):
                print ("Here is what you have so far")
                print (mc.main_character.items[x])
        if choose.lower() == "health":
            
print (rat())
