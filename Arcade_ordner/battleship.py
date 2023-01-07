from mInput import *
from random import randint
# single_mode : single player mode
# vs_mode: player vs computer mode


# battleship: game loop


def battleship_game():
    battle_ship_title()
    while True:
        print(CYAN + "1 " + WHITE + "Singele-player mode")
        print(CYAN + "2 " + WHITE + "Player vs. Computer ")
        choice = input(
            MAGENTA + "Choose a playing mode: " + WHITE)
        if choice.__eq__("1"):
            print(YELLOW +
                  "\n\n              Singelplayer mode" + WHITE)
            single_player_mode()
            choice_playing = ask_play_again(
                "Would you like to play another round(yes/no/...?")
            if not choice_playing:
                break
            else:
                continue
        if choice.__eq__("2"):
            print(YELLOW +
                  "\n\n              Player vs. Computer " + WHITE)
            vs_computer_mode()
            choice_playing = ask_play_again(
                "Would you like to play another round(yes/no/...?")
            if not choice_playing:
                break
            else:
                continue
        else:
            print(RED + "Choosen option does not exist!" + WHITE)

# displaying title of the game


def battle_ship_title():
    game_title = BLUE + f"""
/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\
/    {RED}  ____        __  __  __          ___\__               {BLUE }  \\
/  {RED}   / __ )____ _/ /_/ /_/ ___       |______\_____         {BLUE }  \\
/  {RED}  / __  / __ `/ __/ __/ / _ \_____/_______/_____\_______  {BLUE } \\
/ {RED}  / /_/ / /_/ / /_/ /_/ /  __|       > > >              /  {BLUE } \\
/ {RED} /_____/\__,_/\__/\__/_/\___/\_________________________/  {BLUE }  \\
/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\

"""
    print(game_title)

# single_mode : game loop


def single_player_mode():

    enemy_game_field_dict = {"A1": " ", "A2": " ", "A3": " ", "A4": " ", "A5": " ",
                             "B1": " ", "B2": " ", "B3": " ", "B4": " ", "B5": " ",
                             "C1": " ", "C2": " ", "C3": " ", "C4": " ", "C5": " ",
                             "D1": " ", "D2": " ", "D3": " ", "D4": " ", "D5": " ",
                             "E1": " ", "E2": " ", "E3": " ", "E4": " ", "E5": " "
                             }
    enemy = enemy_ship_placement()
    max_shots = 14
    game_state = True
    enemy_view_field(enemy_game_field_dict)
    while game_state:
        shot = hitting_enemy(enemy_game_field_dict)
        checked_enemy_game_field_dict = check_hit(
            enemy, shot, enemy_game_field_dict)
        game_state, shots_left, targets_left, shot_counter = check_win(
            enemy_game_field_dict, max_shots)
        enemy_view_field(enemy_game_field_dict)
        if not game_state:

            if targets_left == 1:
                print(BOLD + GREENBRIGHT +
                      f"Well done captain!!! WE won in {shot_counter} shots" + RESET)
            else:
                print(BOLD + RED +
                      f"we lost... {targets_left} targets left\n" + RESET)
            break

        print(f" Tries left   = {YELLOW}{shots_left:2}/14"+RESET)
        print(f" Targets left = {RED}{targets_left:2}/7"+RESET)


# player vs computer mode: game loop


def vs_computer_mode():
    enemy_game_field_dict = empty_field_dict()
    own_game_field_dict = empty_field_dict()
    enemy = enemy_ship_placement()
    own_ships = own_ship_placement()
    enemy_memory = empty_field_list()
    entire_field_view(own_game_field_dict, enemy_game_field_dict)
    while True:
        # your turn
        own_shot = hitting_enemy(enemy_game_field_dict)
        enemy_game_field_dict = check_hit(
            enemy, own_shot, enemy_game_field_dict)
        game_state, enemy_ships_left, own_shots_made = check_win_vs_mode(
            enemy_game_field_dict)
        if not game_state:
            entire_field_view(own_game_field_dict, enemy_game_field_dict)
            print(BOLD + GREENBRIGHT +
                  f"Well done captain!!! WE won in {own_shots_made} shots" + RESET)
            break
        # computer turn
        enemy_shot, enemy_memory = enemy_shooting(enemy_memory)
        own_game_field_dict = check_hit(
            own_ships, enemy_shot, own_game_field_dict)
        game_state, own_ships_left, enemy_shots_made = check_win_vs_mode(
            own_game_field_dict)
        if not game_state:
            entire_field_view(own_game_field_dict, enemy_game_field_dict)
            print(BOLD + RED +
                  f"WE LOST. WE ARE SINKING CAPTAIN!!! There are still {enemy_ships_left} targets left" + RESET)
            break
        # showing entire field
        entire_field_view(own_game_field_dict, enemy_game_field_dict)
        print(f"There are still {enemy_ships_left}/7 targets left")

# single_mode + vs_mode: determination of enemy ship positions


def enemy_ship_placement():
    # 3 SHIPS total: 1 with 3 space, 2 with 2 spaces
    # use random for decision of enemy
    enemy_decision = randrange(1, 5)
    # print(enemy_decision)
    enemy1 = {"A1": None, "A2": None, "A3": True, "A4": True, "A5": True,
              "B1": None, "B2": None, "B3": None, "B4": None, "B5": None,
              "C1": None, "C2": None, "C3": None, "C4": None, "C5": True,
              "D1": None, "D2": True, "D3": None, "D4": None, "D5": True,
              "E1": None, "E2": True, "E3": None, "E4": None, "E5": None
              }
    enemy2 = {"A1": None, "A2": None, "A3": None, "A4": None, "A5": None,
              "B1": True, "B2": None, "B3": True, "B4": True, "B5": True,
              "C1": True, "C2": None, "C3": None, "C4": None, "C5": None,
              "D1": None, "D2": None, "D3": None, "D4": None, "D5": True,
              "E1": None, "E2": None, "E3": None, "E4": None, "E5": True
              }
    enemy3 = {"A1": None, "A2": True, "A3": None, "A4": True, "A5": True,
              "B1": None, "B2": True, "B3": None, "B4": None, "B5": None,
              "C1": None, "C2": True, "C3": None, "C4": None, "C5": None,
              "D1": None, "D2": None, "D3": None, "D4": None, "D5": None,
              "E1": None, "E2": None, "E3": True, "E4": True, "E5": None
              }
    enemy4 = {"A1": True, "A2": True, "A3": None, "A4": None, "A5": None,
              "B1": True, "B2": True, "B3": True, "B4": None, "B5": None,
              "C1": None, "C2": None, "C3": None, "C4": None, "C5": None,
              "D1": None, "D2": None, "D3": None, "D4": None, "D5": None,
              "E1": True, "E2": True, "E3": None, "E4": None, "E5": None
              }
    if enemy_decision == 1:
        enemy = enemy1
    if enemy_decision == 2:
        enemy = enemy2
    if enemy_decision == 3:
        enemy = enemy3
    if enemy_decision == 4:
        enemy = enemy4

    return enemy

# single_mode+ vs_mode : demanding shot + checking if shot possible(optimizable)


def hitting_enemy(enemy_game_field_dict):
    possible_shots = empty_field_list()
    while True:
        guess = input(
            RED + "What are the coordinates we should shoot at?(A1,B2,...) \n" + WHITE)
        shot = guess.upper()
        for ele in possible_shots:
            ele_shot = ele
            if shot.__eq__(ele_shot):
                break
        if shot.__eq__(ele_shot):
            if enemy_game_field_dict[shot].__eq__(GREEN + "0" + BLUE) or enemy_game_field_dict[shot].__eq__(RED + "H" + BLUE):
                print(RED + "Perhaps another spot captain?!" + BLUE)
            else:
                break
        else:
            print(RED + "Impossible orders captain. Please try again captain!!!\n\n")

    return shot

# single_mode + vs_mode: checking if shot has hit or not


def check_hit(enemy, shot, enemy_game_field_dict):
    if enemy[shot]:
        enemy_game_field_dict[shot] = RED + "H" + BLUE
    else:
        enemy_game_field_dict[shot] = GREEN + "0" + BLUE

    return enemy_game_field_dict

# single_mode: checking win with max_shots


def check_win(enemy_game_field_dict, max_shots):
    ship_counter = 0
    shot_counter = 0
    game_state = True

    for key in enemy_game_field_dict:
        shots_left = max_shots - shot_counter
        ships_left = 7 - ship_counter
        if enemy_game_field_dict[key].__eq__(RED + "H" + BLUE):
            ship_counter += 1
            shot_counter += 1
        if enemy_game_field_dict[key].__eq__(GREEN + "0" + BLUE):
            shot_counter += 1
        if ship_counter == 7 or shot_counter == max_shots+1:
            game_state = False
            break

    return game_state, shots_left, ships_left, shot_counter

# single_mode: field view(5*5)


def enemy_view_field(enemy_game_field_dict):
    ew = WHITE+"Enemy waters"+BLUE
    field_view = f"""
     {ew}

        1        2        3        4        5
     _______  _______  _______  _______  _______
    |       ||       ||       ||       ||       |
  A |   {enemy_game_field_dict["A1"]}   ||   {enemy_game_field_dict["A2"]}   ||   {enemy_game_field_dict["A3"]}   ||   {enemy_game_field_dict["A4"]}   ||   {enemy_game_field_dict["A5"]}   |
    |_______||_______||_______||_______||_______|
     _______  _______  _______  _______  _______
    |       ||       ||       ||       ||       |
  B |   {enemy_game_field_dict["B1"]}   ||   {enemy_game_field_dict["B2"]}   ||   {enemy_game_field_dict["B3"]}   ||   {enemy_game_field_dict["B4"]}   ||   {enemy_game_field_dict["B5"]}   |
    |_______||_______||_______||_______||_______|
     _______  _______  _______  _______  _______
    |       ||       ||       ||       ||       |
  C |   {enemy_game_field_dict["C1"]}   ||   {enemy_game_field_dict["C2"]}   ||   {enemy_game_field_dict["C3"]}   ||   {enemy_game_field_dict["C4"]}   ||   {enemy_game_field_dict["C5"]}   |
    |_______||_______||_______||_______||_______|
     _______  _______  _______  _______  _______
    |       ||       ||       ||       ||       |
  D |   {enemy_game_field_dict["D1"]}   ||   {enemy_game_field_dict["D2"]}   ||   {enemy_game_field_dict["D3"]}   ||   {enemy_game_field_dict["D4"]}   ||   {enemy_game_field_dict["D5"]}   |
    |_______||_______||_______||_______||_______|
     _______  _______  _______  _______  _______
    |       ||       ||       ||       ||       |
  E |   {enemy_game_field_dict["E1"]}   ||   {enemy_game_field_dict["E2"]}   ||   {enemy_game_field_dict["E3"]}   ||   {enemy_game_field_dict["E4"]}   ||   {enemy_game_field_dict["E5"]}   |
    |_______||_______||_______||_______||_______|

    """
    print(BLUE + field_view+RED + "\n H " + WHITE + "= hit\n" +
          GREEN + " 0 " + WHITE+"= already hit/nothing found")

# single_mode + vs_mode: after game, check to re-enter loop or quit game


def ask_play_again(question):
    choice_playing = True
    answer = False
    possible_positive_answers = [
        "yes", "y", "yes, why not", "yes please", "yeah", "positive",]
    possible_negative_answers = ["no", "n", "absolutely not", "hell no"]
    while True:
        choice_play = input(
            question)

        for word in possible_positive_answers:
            if choice_play.__eq__(word):
                choice_playing = True
                answer = True
                break
        for word in possible_negative_answers:
            if choice_play.__eq__(word):
                choice_playing = False
                answer = True
                break

        if answer:
            break
        print(RED + "chosen option does not exist!" + RESET)
    return choice_playing

# vs_mode: view of the entire field(own+enemy) at once


def entire_field_view(own_game_field_dict, enemy_game_field_dict):
    ew = WHITE+"Enemy waters"+BLUE
    ow = WHITE+"Own waters"+BLUE
    field_view = f"""
    {ow}                                          {ew}

        1        2        3        4        5       |       1        2        3        4        5       
     _______  _______  _______  _______  _______    |    _______  _______  _______  _______  _______    
    |       ||       ||       ||       ||       |   |   |       ||       ||       ||       ||       |   
  A |   {own_game_field_dict["A1"]}   ||   {own_game_field_dict["A2"]}   ||   {own_game_field_dict["A3"]}   ||   {own_game_field_dict["A4"]}   ||   {own_game_field_dict["A5"]}   |   | A |   {enemy_game_field_dict["A1"]}   ||   {enemy_game_field_dict["A2"]}   ||   {enemy_game_field_dict["A3"]}   ||   {enemy_game_field_dict["A4"]}   ||   {enemy_game_field_dict["A5"]}   |
    |_______||_______||_______||_______||_______|   |   |_______||_______||_______||_______||_______|   
     _______  _______  _______  _______  _______    |    _______  _______  _______  _______  _______    
    |       ||       ||       ||       ||       |   |   |       ||       ||       ||       ||       |   
  B |   {own_game_field_dict["B1"]}   ||   {own_game_field_dict["B2"]}   ||   {own_game_field_dict["B3"]}   ||   {own_game_field_dict["B4"]}   ||   {own_game_field_dict["B5"]}   |   | B |   {enemy_game_field_dict["B1"]}   ||   {enemy_game_field_dict["B2"]}   ||   {enemy_game_field_dict["B3"]}   ||   {enemy_game_field_dict["B4"]}   ||   {enemy_game_field_dict["B5"]}   |   
    |_______||_______||_______||_______||_______|   |   |_______||_______||_______||_______||_______|   
     _______  _______  _______  _______  _______    |    _______  _______  _______  _______  _______    
    |       ||       ||       ||       ||       |   |   |       ||       ||       ||       ||       |   
  C |   {own_game_field_dict["C1"]}   ||   {own_game_field_dict["C2"]}   ||   {own_game_field_dict["C3"]}   ||   {own_game_field_dict["C4"]}   ||   {own_game_field_dict["C5"]}   |   | C |   {enemy_game_field_dict["C1"]}   ||   {enemy_game_field_dict["C2"]}   ||   {enemy_game_field_dict["C3"]}   ||   {enemy_game_field_dict["C4"]}   ||   {enemy_game_field_dict["C5"]}   |   
    |_______||_______||_______||_______||_______|   |   |_______||_______||_______||_______||_______|   
     _______  _______  _______  _______  _______    |    _______  _______  _______  _______  _______    
    |       ||       ||       ||       ||       |   |   |       ||       ||       ||       ||       |   
  D |   {own_game_field_dict["D1"]}   ||   {own_game_field_dict["D2"]}   ||   {own_game_field_dict["D3"]}   ||   {own_game_field_dict["D4"]}   ||   {own_game_field_dict["D5"]}   |   | D |   {enemy_game_field_dict["D1"]}   ||   {enemy_game_field_dict["D2"]}   ||   {enemy_game_field_dict["D3"]}   ||   {enemy_game_field_dict["D4"]}   ||   {enemy_game_field_dict["D5"]}   |   
    |_______||_______||_______||_______||_______|   |   |_______||_______||_______||_______||_______|   
     _______  _______  _______  _______  _______    |    _______  _______  _______  _______  _______    
    |       ||       ||       ||       ||       |   |   |       ||       ||       ||       ||       |   
  E |   {own_game_field_dict["E1"]}   ||   {own_game_field_dict["E2"]}   ||   {own_game_field_dict["E3"]}   ||   {own_game_field_dict["E4"]}   ||   {own_game_field_dict["E5"]}   |   | E |   {enemy_game_field_dict["E1"]}   ||   {enemy_game_field_dict["E2"]}   ||   {enemy_game_field_dict["E3"]}   ||   {enemy_game_field_dict["E4"]}   ||   {enemy_game_field_dict["E5"]}   |   
    |_______||_______||_______||_______||_______|   |   |_______||_______||_______||_______||_______|   

    """
    print(BLUE + field_view + RED + "\n H " + WHITE + "= hit\n" +
          GREEN + " 0 " + WHITE+"= already hit/nothing found")

# vs_mode: choosing from prepared shippositions


def own_ship_placement():
    own_ships = 0

    print(MAGENTA + " \nChoose a shipposition"+RESET)
    print(
        f"Every map has : 2* {GREEN}00 {WHITE}boats and 1* {GREEN}000 {WHITE}boat")
    own_ships1 = {"A1": None, "A2": None, "A3": True, "A4": True, "A5": True,
                  "B1": None, "B2": None, "B3": None, "B4": None, "B5": None,
                  "C1": None, "C2": None, "C3": None, "C4": None, "C5": True,
                  "D1": None, "D2": True, "D3": None, "D4": None, "D5": True,
                  "E1": None, "E2": True, "E3": None, "E4": None, "E5": None
                  }
    own_ships2 = {"A1": None, "A2": None, "A3": None, "A4": None, "A5": None,
                  "B1": None, "B2": None, "B3": None, "B4": None, "B5": None,
                  "C1": True, "C2": True, "C3": True, "C4": None, "C5": None,
                  "D1": None, "D2": None, "D3": True, "D4": True, "D5": None,
                  "E1": None, "E2": None, "E3": True, "E4": True, "E5": None
                  }
    own_ships3 = {"A1": True, "A2": None, "A3": None, "A4": None, "A5": None,
                  "B1": True, "B2": None, "B3": None, "B4": None, "B5": True,
                  "C1": True, "C2": None, "C3": None, "C4": None, "C5": True,
                  "D1": True, "D2": None, "D3": None, "D4": None, "D5": None,
                  "E1": True, "E2": None, "E3": None, "E4": None, "E5": None
                  }
    print("Choice: 1")
    show_mini_grid(own_ships1)
    print("Choice: 2")
    show_mini_grid(own_ships2)
    print("Choice: 2")
    show_mini_grid(own_ships3)
    while True:
        choice = input("Give me a choice: ")
        if choice.__eq__("1"):
            own_ships = own_ships1
            break
        elif choice.__eq__("2"):
            own_ships = own_ships2
            break
        elif choice.__eq__("3"):
            own_ships = own_ships3
            break
        else:
            print("Please use 1/2/3 to choose!")

    return own_ships

# vs_mode: visualisation of the own the possible placement of ships


def show_mini_grid(some_dict):
    grid_list = []
    for key in some_dict:
        if some_dict[key] == None:
            grid_list.append(WHITE + "0 " + RESET)
        if some_dict[key]:
            grid_list.append(GREEN + "0 " + RESET)

    mini_grid = f"""
        {grid_list[0]}{grid_list[1]}{grid_list[2]}{grid_list[3]}{grid_list[4]}
        {grid_list[5]}{grid_list[6]}{grid_list[7]}{grid_list[8]}{grid_list[9]}
        {grid_list[10]}{grid_list[11]}{grid_list[12]}{grid_list[13]}{grid_list[14]}
        {grid_list[15]}{grid_list[16]}{grid_list[17]}{grid_list[18]}{grid_list[19]}
        {grid_list[20]}{grid_list[21]}{grid_list[22]}{grid_list[23]}{grid_list[24]}
        """
    print(mini_grid)

# vs_mode: computer choosing a random shot(with memory)


def enemy_shooting(enemy_memory):
    # checking to shoot somewhere it hasn't shot yet. For now: only random
    spots_left = len(enemy_memory)
    random_index = randint(0, spots_left-1)
    random_shot = enemy_memory[random_index]
    enemy_memory.remove(random_shot)
    enemy_memory.sort()
    return random_shot, enemy_memory

# vs_mode: checking player/computer win with opponents ships left


def check_win_vs_mode(current_game_field_dict):
    game_state = True
    shot_counter = 0
    ship_counter = 0
    for key in current_game_field_dict:
        # print(current_game_field_dict[key])
        if current_game_field_dict[key].__eq__(RED + "H" + BLUE):
            ship_counter += 1
            shot_counter += 1
        if current_game_field_dict[key].__eq__(GREEN + "0" + BLUE):
            shot_counter += 1
            # print(shot_counter)
        if ship_counter == 7:
            game_state = False
            break
        # print(ship_counter)
    ships_left = 7 - ship_counter
    # print(ships_left)
    return game_state, ships_left, shot_counter


# function to create an empty battleship(5*5) list


def empty_field_list():
    some_list = []
    # How to make a list of a field if you are tired of constantly writing one
    num = 0
    short_alphabet = ["A", "B", "C", "D", "E"]
    for letter in short_alphabet:
        num += 1
        for chif in range(6):
            if chif == 0:
                continue
            some_list.append(letter+str(chif))
    return some_list

# function to create an empty battleship(5*5) dictionary


def empty_field_dict():
    some_dict = {}
    position = 0
    short_alphabet = ["A", "B", "C", "D", "E"]
    for letter in short_alphabet:
        for i in range(6):
            if i == 0:
                continue
            some_dict[letter+str(i)] = " "
            position += 1
    return some_dict
