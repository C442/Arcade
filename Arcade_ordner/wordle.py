from mInput import *

GREY = "\033[37m"
BLACKBG = "\033[40m"


def wordle_title():
    print_title = BOLD + CYAN + """
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
     """ + RESET
    print(print_title)


def interface_box(word_size, word_interface):
    box_print_top = GREY + TL + 3 * H + TR
    box_print_bot = GREY + BL + 3 * H + BR
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


def wordle_win_loose_detection(lig, word_size, word, guess, word_interface):
    state = True
    if lig == word_size and not word == guess:
        interface_box(word_size, word_interface)
        print(RED + "You lost!")
        print(f"The word was: " + MAGENTA + word + RESET)
        state = False
    elif word == guess:
        interface_box(word_size, word_interface)
        print(GREEN + "You won!")
        state = False
    return state


def wordle_guessing(word, word_size, word_interface, more_letters, lig):
    guessing = True
    while guessing:
        interface_box(word_size, word_interface)
        guess = input(MAGENTA + "Enter your guess: ")
        guess = guess.upper()
        if len(guess) == len(word):
            used_letters = []
            for index in range(word_size):
                if guess[index] not in used_letters:
                    letter_count = word.count(guess[index])
                    for _ in range(letter_count):
                        more_letters.append(guess[index])
                    used_letters.append(guess[index])
                if word[index] == guess[index]:
                    word_interface[lig][index] = CGREENBG + \
                        BLACK + " " + guess[index] + " " + RESET + GREY
                    more_letters.remove(guess[index])
            for index1 in range(word_size):
                if guess[index1] in word and guess[index1] in more_letters and not word[index1] == guess[index1]:
                    word_interface[lig][index1] = CYELLOWBG + \
                        BLACK + " " + guess[index1] + " " + RESET + GREY
                    more_letters.remove(guess[index1])
                elif not word[index1] == guess[index1]:
                    word_interface[lig][index1] = GREY + \
                        " " + guess[index1] + " "
            lig += 1
            guessing = wordle_win_loose_detection(
                lig, word_size, word, guess, word_interface)
        else:
            print(YELLOW + f"Word length must be {len(word)} letters!" + RESET)


def wordle_word_size(language):
    words = []
    request = True
    while request:
        user_input = input(
            BLUE + "Select the number of letters in the word (3 to 6): ")
        try:
            user_input = int(user_input)
        except ValueError:
            print(RED + "Input has to be a number!")
        else:
            if 3 <= int(user_input) <= 6:
                if user_input == 3:
                    if language == "German":
                        words = ["auf", "aus", "das", "ufo",
                                 "ehe", "gab", "fee", "tee", "zug"]
                        break
                    elif language == "English":
                        words = ["bit", "gap", "gas", "guy",
                                 "bro", "dog", "cat", "hut", "mad"]
                        break
                elif user_input == 4:
                    if language == "German":
                        words = ["bahn", "auto", "sehr", "fein",
                                 "hund", "jahr", "jagd", "gans"]
                        break
                    elif language == "English":
                        words = ["area", "army", "baby", "card",
                                 "fish", "news", "wall", "bear"]
                        break
                elif user_input == 5:
                    if language == "German":
                        words = ["hagel", "haase", "fahne",
                                 "tiere", "haare", "sache", "fahrt"]
                        break
                    elif language == "English":
                        words = ["anger", "apple", "beach",
                                 "drink", "dress", "hotel", "steam"]
                        break
                elif user_input == 6:
                    if language == "German":
                        words = ["abflug", "achsel", "zahlen",
                                 "machen", "jaguar", "radler"]
                        break
                    elif language == "English":
                        words = ["better", "bottle", "damage",
                                 "eleven", "family", "garden"]
                        break
            else:
                print(RED + "Number of letters must be between 3 and 6!" + RESET)
    return words


def wordle_word_list():
    print(GREEN + "1 " + WHITE + "German")
    print(GREEN + "2 " + WHITE + "English")
    user_input = 0
    words = []
    while user_input != 1 and user_input != 2:
        user_input = input(
            MAGENTA + "Please select the language of the words: ")
        if user_input == "1":
            words = wordle_word_size("German")
            break
        elif user_input == "2":
            words = wordle_word_size("English")
            break
        else:
            print(RED + "This language doesn't exist!")
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
                print(RED + "Input not valid!" + RESET)


# main
if __name__ == "__main__":
    wordle_game()
