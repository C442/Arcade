from mInput import *
from wordle import *
from hang_man import *
from battleship import *


def arcade_title():
    ORANGE = YELLOW + RED
    main_title = ORANGE + f"""
                                                        
     █████╗ ██████╗  ██████╗ █████╗ ██████╗ ███████╗    
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝    
    ███████║██████╔╝██║     ███████║██║  ██║█████╗     
    ██╔══██║██╔══██╗██║     ██╔══██║██║  ██║██╔══╝      
    ██║  ██║██║  ██║╚██████╗██║  ██║██████╔╝███████╗    
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚══════╝    

        {BOLD} {RED}by Lies Ben and Mayers Christophe{RESET}
"""
    print(main_title)
    print('WELCOME to the "Arcade".\nFeel free to choose a game you like to play.\n ')


def arcade_menu():
    arcade_title()
    while True:
        print(CYAN + "1 " + WHITE + "Battleship")
        print(CYAN + "2 " + WHITE + "Hangman")
        print(CYAN + "3 " + WHITE + "Tic Tac To")
        print(CYAN + "4 " + WHITE + "wordle")
        print(CYAN + "exit" + WHITE + " to quit the arcade")
        game_choice = input(
            MAGENTA + "What game would you like to play?: "+WHITE)
        if game_choice.__eq__("1"):
            battleship_game()
        if game_choice.__eq__("2"):
            hangman_game()
        if game_choice.__eq__("3"):
            pass
        if game_choice.__eq__("4"):
            wordle_game()
        if game_choice.__eq__("exit"):
            break


'''def ask_play_game(question):
    choice_state = True
    possible_positive_answers = [
        "yes", "y", "yes, why not", "yes please", "yeah", "positive",]
    possible_negative_answers = ["no", "n", "absolutely not", "hell no"]
    choice_play = input(
        question)

    for word in possible_positive_answers:
        if word.__eq__(choice_play):
            choice_playing = True
    for word in possible_negative_answers:
        if word.__eq__(choice_play):
            choice_playing = False
    return choice_play
'''

arcade_menu()
