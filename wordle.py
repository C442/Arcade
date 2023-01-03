from mInput import *

GREY = "\033[37m"
1


def wordle_title():
    print_title = CBLACKBG + GREEN + """
     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
    | ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
    | |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
    | |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
    | |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
    | |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
    | |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'     
     """
    print(print_title)


def interface_box(word_size, word_interface):
    box_print_top = CBLACKBG + GREY + TL + 3 * H + TR
    box_print_bot = BL + 3 * H + BR
    for size in range(word_size):
        for lig in range(3):
            for col in range(word_size):
                if lig == 0:
                    print(box_print_top, end="")
                elif lig == 1:
                    print(V + word_interface[size][col] + V, end="")
                elif lig == 2:
                    print(box_print_bot, end="")
            print()


def wordle_win_loose_detection(lig, word_size, word, guess):
    state = True
    if lig == word_size and not word == guess:
        print(RED + "You lost!")
        print(f"The word was: " + MAGENTA + word + RESET + CBLACKBG)
        state = False
    elif word == guess:
        print(GREEN + "You won!")
        state = False
    return state


def wordle_guessing(word, word_size, word_interface, more_letters, lig):
    guessing = True
    while guessing:
        guess = input(CBLACKBG + MAGENTA + "Enter your guess: ")
        guess = guess.upper()
        used_letters = []
        for index in range(word_size):
            if guess[index] not in used_letters:
                letter_count = word.count(guess[index])
                for _ in range(letter_count):
                    more_letters.append(guess[index])
                used_letters.append(guess[index])
            if word[index] == guess[index]:
                word_interface[lig][index] = CGREENBG + BLACK + \
                    " " + guess[index] + " " + GREY + CBLACKBG
                more_letters.remove(guess[index])
        for index1 in range(word_size):
            if guess[index1] in word and guess[index1] in more_letters and not word[index1] == guess[index1]:
                word_interface[lig][index1] = CYELLOWBG + BLACK + \
                    " " + guess[index1] + " " + GREY + CBLACKBG
                more_letters.remove(guess[index1])
            elif not word[index1] == guess[index1]:
                word_interface[lig][index1] = " " + guess[index1] + " "
        interface_box(word_size, word_interface)
        lig += 1
        guessing = wordle_win_loose_detection(lig, word_size, word, guess)


def wordle_word_size(language):
    user_input = 0
    words = []
    while not 3 <= int(user_input) <= 6:
        user_input = input(CBLACKBG + MAGENTA +
                           "Choose a word size (3 to 6): ")
        if 3 <= int(user_input) <= 6:
            if user_input == "3":
                if language == "German":
                    words = ["auf", "aus", "das", "ufo",
                             "ehe", "gab", "fee", "tee", "zug"]
                elif language == "English":
                    words = ["bit", "gap", "gas", "guy",
                             "bro", "dog", "cat", "hut", "mad"]
            elif user_input == "4":
                if language == "German":
                    words = ["bahn", "auto", "sehr", "fein",
                             "hund", "jahr", "jagd", "gans"]
                elif language == "English":
                    words = ["area", "army", "baby", "card",
                             "fish", "news", "wall", "bear"]
            elif user_input == "5":
                if language == "German":
                    words = ["hagel", "haase", "fahne",
                             "tiere", "haare", "sache", "fahrt"]
                elif language == "English":
                    words = ["anger", "apple", "beach",
                             "drink", "dress", "hotel", "steam"]
            elif user_input == "6":
                if language == "German":
                    words = ["abflug", "achsel", "zahlen",
                             "machen", "jaguar", "radler"]
                elif language == "English":
                    words = ["better", "bottle", "damage",
                             "eleven", "family", "garden"]
        else:
            print(RED + "Input not valid!" + RESET)
    return words


def wordle_word_list():
    print(CBLACKBG + GREEN + "1 " + WHITE + "German")
    print(CBLACKBG + GREEN + "2 " + WHITE + "English")
    user_input = 0
    words = []
    while user_input != 1 and user_input != 2:
        user_input = get_entier_naturel(
            CBLACKBG + "Please select a language: ")
        if user_input == 1:
            words = wordle_word_size("German")
        elif user_input == 2:
            words = wordle_word_size("English")
        else:
            print(RED + "Input not valid!")
    return words


def wordle_game():
    wordle_title()
    words = wordle_word_list()
    game = True
    while game:
        word = choice(words)
        words.remove(word)
        word = word.upper()
        word_size = len(word)
        word_interface = []
        for _ in range(word_size):
            word_interface.append(word_size * [3 * " "])
        lig = 0
        more_letters = []
        wordle_guessing(word, word_size, word_interface, more_letters, lig)
        again = ""
        while again != "y" and again != "n":
            print(
                BLUE + f"Wanna play again? {len(words)} words left to guess!")
            again = input("Type y/n: " + RESET)
            if again == "n":
                game = False
            elif again == "y":
                if not words:
                    print(RED + "No words left to guess!" + RESET)
                    words = wordle_word_list()
            else:
                print(RED + "Input npt valid!" + RESET)


# wordle_game()
