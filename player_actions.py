#player_actions.py


def check_play_again(user_input):
    #Your code here
    if user_input == "Y":
        print ("Prepare yourself...\nLoading Game...")

    elif user_input == "N":
        print ("Better luck next time! \nGAMEOVER")

    else:
        print ("INVALID INPUT!")


check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
