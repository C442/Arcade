from battleship import *
from random import randint
from mInput import *


def entire_field_view(own_game_field_dict, enemy_game_field_dict):
    ew = CBLACKBG+WHITE+"Enemy waters"+BLUE
    ow = CBLACKBG+WHITE+"Own waters"+BLUE
    field_view = CBLACKBG + f"""
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
    print(CBLACKBG+BLUE + field_view + RED + "\n H " + WHITE + "= hit\n" +
          GREEN + " 0 " + WHITE+"= already hit/nothing found")


def own_ship_placement():
    own_ships = 0
    # add mini grid for the position
    print(CBLACKBG + MAGENTA + " \nChoose a shipposition"+WHITE)
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
    print(CBLACKBG+"Choice: 1")
    show_mini_grid(own_ships1)
    print(CBLACKBG+"Choice: 2")
    show_mini_grid(own_ships2)
    print(CBLACKBG+"Choice: 2")
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


def show_mini_grid(some_dict):
    grid_list = []
    for key in some_dict:
        if some_dict[key] == None:
            grid_list.append(WHITE + "0 " + RESET)
        if some_dict[key]:
            grid_list.append(GREEN + "0 " + RESET)

    mini_grid = f"""{CBLACKBG}
        {grid_list[0]}{CBLACKBG}{grid_list[1]}{CBLACKBG}{grid_list[2]}{CBLACKBG}{grid_list[3]}{CBLACKBG}{grid_list[4]}{CBLACKBG}
        {grid_list[5]}{CBLACKBG}{grid_list[6]}{CBLACKBG}{grid_list[7]}{CBLACKBG}{grid_list[8]}{CBLACKBG}{grid_list[9]}{CBLACKBG}
        {grid_list[10]}{CBLACKBG}{grid_list[11]}{CBLACKBG}{grid_list[12]}{CBLACKBG}{grid_list[13]}{CBLACKBG}{grid_list[14]}{CBLACKBG}
        {grid_list[15]}{CBLACKBG}{grid_list[16]}{CBLACKBG}{grid_list[17]}{CBLACKBG}{grid_list[18]}{CBLACKBG}{grid_list[19]}{CBLACKBG}
        {grid_list[20]}{CBLACKBG}{grid_list[21]}{CBLACKBG}{grid_list[22]}{CBLACKBG}{grid_list[23]}{CBLACKBG}{grid_list[24]}{CBLACKBG}
        """
    print(mini_grid)


def enemy_shooting(enemy_memory):
    # checking to shoot somewhere it hasn't shot yet. For now: only random
    spots_left = len(enemy_memory)
    random_index = randint(0, spots_left-1)
    random_shot = enemy_memory[random_index]
    enemy_memory.remove(random_shot)
    enemy_memory.sort()
    return random_shot, enemy_memory


def check_own_win(enemy_game_field_dict):
    game_state = True
    shot_counter = 0
    ship_counter = 0
    for key in enemy_game_field_dict:
        if enemy_game_field_dict[key].__eq__(RED + "H" + BLUE):
            ship_counter += 1
            shot_counter += 1
        if enemy_game_field_dict[key].__eq__(GREEN + "0" + BLUE):
            shot_counter += 1
        if ship_counter == 7:
            print(BOLD + GREENBRIGHT +
                  f"{CBLACKBG}Well done captain!!! WE won in {shot_counter} shots" + RESET)
            game_state = False
            break
    return game_state


def enemy_check_hit(own_ships, enemy_shot, own_game_field_dict):
    # print(enemy_shot)
    if own_ships[enemy_shot]:
        own_game_field_dict[enemy_shot] = RED + "H" + BLUE
    else:
        own_game_field_dict[enemy_shot] = GREEN + "0" + BLUE
    # print(own_game_field_dict)

    return own_game_field_dict


def check_enemy_win(own_game_field_dict):
    game_state = True
    shot_counter = 0
    ship_counter = 0
    ships_left = 7 - ship_counter
    for key in own_game_field_dict:
        if own_game_field_dict[key].__eq__(RED + "H" + BLUE):
            ship_counter += 1
            shot_counter += 1
        if own_game_field_dict[key].__eq__(GREEN + "0" + BLUE):
            shot_counter += 1
        if ship_counter == 7:
            print(BOLD + RED +
                  f"{CBLACKBG}WE LOST. WE ARE SINKING CAPTAIN!!! {ships_left} " + CBLACKBG+WHITE)
            game_state = False
            break
    return game_state


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
        game_state = check_own_win(enemy_game_field_dict)
        if not game_state:
            break
        # computer turn
        enemy_shot, enemy_memory = enemy_shooting(enemy_memory)
        own_game_field_dict = enemy_check_hit(
            own_ships, enemy_shot, own_game_field_dict)
        game_state = check_enemy_win(own_game_field_dict)
        if not game_state:
            break
        # showing entire field
        entire_field_view(own_game_field_dict, enemy_game_field_dict)


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


def battleship_game():
    wordle_title()
    choice_playing = True
    while choice_playing:
        print(CBLACKBG + CYAN + "1 " + WHITE + "Singele-player mode")
        print(CBLACKBG + CYAN + "2 " + WHITE + "Player vs. Computer ")
        choice = input(
            CBLACKBG + MAGENTA + "Choose a playing mode: " + WHITE)
        if choice.__eq__("1"):
            print(YELLOW + CBLACKBG +
                  "\n\n              Singelplayer mode" + CBLACKBG+WHITE)
            single_player_mode()
            choice_playing = ask_play_again(choice_playing)
        if choice.__eq__("2"):
            print(YELLOW + CBLACKBG +
                  "\n\n              Player vs. Computer " + CBLACKBG+WHITE)
            vs_computer_mode()
            choice_playing = ask_play_again(choice_playing)
        else:
            print(CBLACKBG + RED + "Choosen option does not exist!" + WHITE)


# vs_computer_mode()
# show_mini_grid(own_ship_placement())
# battleship_game()
