from mInput import *


def hangman_title():
    screen_title = r""" 
 ___  ___  ________  ________   ________          _____ ______   ________  ________      
|\  \|\  \|\   __  \|\   ___  \|\   ____\        |\   _ \  _   \|\   __  \|\   ___  \    
\ \  \\\  \ \  \|\  \ \  \\ \  \ \  \___|        \ \  \\\__\ \  \ \  \|\  \ \  \\ \  \   
 \ \   __  \ \   __  \ \  \\ \  \ \  \  ___       \ \  \\|__| \  \ \   __  \ \  \\ \  \  
  \ \  \ \  \ \  \ \  \ \  \\ \  \ \  \|\  \       \ \  \    \ \  \ \  \ \  \ \  \\ \  \ 
   \ \__\ \__\ \__\ \__\ \__\\ \__\ \_______\       \ \__\    \ \__\ \__\ \__\ \__\\ \__\
    \|__|\|__|\|__|\|__|\|__| \|__|\|_______|        \|__|     \|__|\|__|\|__|\|__| \|__|                                 
    """
    print(GREENBRIGHT + screen_title)


def hangman_frames(wrong_answer):
    hangman_frame = ""
    if wrong_answer == 0:
        hangman_frame = r"""
        """
    elif wrong_answer == 1:
        hangman_frame = r"""
        ____
        |/   |
        |   
        |    
        |    
        |    
        |
        |_____
        """
    elif wrong_answer == 2:
        hangman_frame = r"""
         ____
        |/   |
        |   (_)
        |    
        |    
        |    
        |
        |_____
        """
    elif wrong_answer == 3:
        hangman_frame = r"""
         ____
        |/   |
        |   (_)
        |    |
        |    |    
        |    
        |
        |_____
        """
    elif wrong_answer == 4:
        hangman_frame = r"""
         ____
        |/   |
        |   (_)
        |   \|
        |    |
        |    
        |
        |_____
        """
    elif wrong_answer == 5:
        hangman_frame = r"""
         ____
        |/   |
        |   (_)
        |   \|/
        |    |
        |    
        |
        |_____
        """
    elif wrong_answer == 6:
        hangman_frame = r"""
         ____
        |/   | 
        |   (_)
        |   \|/
        |    |
        |   / 
        |
        |_____
        """
    elif wrong_answer == 7:
        hangman_frame = r"""
         ____
        |/   |
        |   (_)
        |   \|/
        |    |
        |   / \
        |
        |_____
        """
    elif wrong_answer == 8:
        hangman_frame = r"""
         ____
        |/   |
        |   (_)
        |   /|\
        |    |
        |   | |
        |
        |_____
        """
    return hangman_frame


def win_loose_detection(list1, list2, wrong_answer, round_counter, word):
    if wrong_answer == 8:
        print(BOLD + RED + "You lost!" + RESET)
        print(BOLD + RED + "The word was: " + RESET + MAGENTA + word.upper())
        gameState = False
    elif list1 == list2:
        print(BOLD + GREENBRIGHT +
              f"You won and needed {round_counter} guess(es)!" + RESET)
        gameState = False
    else:
        gameState = True
    return gameState


def induvidual_preset_words():
    words_preset = []
    word_count = 1
    action = True
    print(BLUE + "Fix a preset of words you want to guess! (When finished enter 0)" + RESET)
    while action:
        user_input = input(MAGENTA + f"Enter {word_count}. word: ")
        user_input = user_input.upper()
        if user_input not in words_preset and user_input != "" and " " not in user_input:
            words_preset.append(user_input.upper())
            word_count += 1
            if user_input == str(0):
                if words_preset == ["0"]:
                    print(RED + "You need to choose at least one word!" + RESET)
                    words_preset.remove(user_input)
                    word_count -= 1
                else:
                    words_preset = words_preset[:-1]
                    return words_preset
        else:
            print(RED + "Word already used or no valid input given!")


def preset_words():
    player_input = "0"
    word_set = []
    print(BLUE + "Which language do you prefer?" + RESET)
    print(GREEN + "1 " + RESET + "German")
    print(GREEN + "2 " + RESET + "English")
    while player_input != "1" and player_input != "2":
        player_input = input(MAGENTA + "Choose your language: " + RESET)
        if player_input == "1":
            word_set = ["katze", "hund", "berg", "felsen", "wasser", "feuer", "erde", "stier", "kuh", "auto", "zug",
                        "lastwagen", "baum", "elefant"]
        elif player_input == "2":
            word_set = ["cat", "dog", "mountain", "rock", "water", "fire", "earth", "taurus", "cow", "car", "train",
                        "truck", "tree", "elephant"]
        else:
            print(RED + "Language does not exist!" + RESET)
    return word_set


def hangman_guessing(wrong_answer, word, interface, round_counter, letters, used_letters):
    guessing = True
    printout_letters = ""
    print(YELLOW + "Game is starting...")
    while guessing:
        print(BOLD + CYAN + hangman_frames(wrong_answer))
        for i in range(len(word)):
            print(" ", end="")
            print(RED + interface[i], end="")
        print()
        print(GREEN + "Used letters: ", end="")
        if round_counter == 0:
            print("/", end="")
        print(printout_letters[:-2])
        guessing = win_loose_detection(
            interface, letters, wrong_answer, round_counter, word)
        if guessing:
            guess = input(MAGENTA + "Enter your guess: " + RESET)
            if len(guess) == 1 and " " not in guess:
                guess = guess.upper()
                if guess in used_letters:
                    print(YELLOW + "Letter already used!")
                else:
                    printout_letters += guess + ", "
                    used_letters.append(guess)
                    if guess in letters:
                        for index in range(len(letters)):
                            if letters[index] == guess:
                                interface[index] = guess
                    else:
                        wrong_answer += 1
                round_counter += 1
            else:
                print(RED + "Please enter one character!" + RESET)


def hangman_menu():
    user_input = "0"
    words = ""
    while user_input != "1" and user_input != "2":
        print(CYAN + "1 " + RESET + "Prefixed set of words")
        print(CYAN + "2 " + RESET + "Create your own set of words")
        user_input = input(MAGENTA + "Please choose an option: " + RESET)
        if user_input == "1":
            words = preset_words()
        elif user_input == "2":
            words = induvidual_preset_words()
        else:
            print(RED + "Choosen option does not exist!" + RESET)
    return words


def hangman_game():
    hangman_title()
    words = hangman_menu()
    game = True
    while game:
        word = choice(words)
        words.remove(word)
        wrong_answer = 0
        letters = []
        interface = len(word) * [H]
        used_letters = []
        round_counter = 0
        for letter in word:
            letters.append(letter.upper())
        hangman_guessing(wrong_answer, word, interface,
                         round_counter, letters, used_letters)
        again = ""
        while again != "n" and again != "y":
            print(
                BLUE + f"Wanna play again? {len(words)} words left to guess!")
            again = input("Press y/n: ")
            if again == "n":
                game = False
            elif again == "y":
                if not words:
                    print(RED + "No words left to guess!" + RESET)
                    words = hangman_menu()
            else:
                print(RED + "Input not valid!" + RESET)


# main
# hangman_game()
