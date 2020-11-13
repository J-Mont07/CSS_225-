#Juan Montoya
#November 12, 2020
#Takes user input. Uses a while toop to check vaild input.

user_input = input("Type either one of these letters" + "\nA" +"\nB" + "\nC" +"\n")
option = 'A','B','C'

while user_input.upper() != 'A' and user_input.upper() != 'B'and user_input.upper() != 'C':
        print("Invalid input" + "\n")
        user_input = input ("Type either one of these letters" + "\nA" +"\nB" + "\nC" +"\n")
