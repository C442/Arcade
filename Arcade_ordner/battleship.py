from mInput import *
import random


def wordle_title():
    game_title = CBLACKBG + BLUE + f"""
/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\
/    {RED}  ____        __  __  __          ___\__               {BLUE+CBLACKBG}  \\
/  {RED}   / __ )____ _/ /_/ /_/ ___       |______\_____         {BLUE+CBLACKBG}  \\
/  {RED}  / __  / __ `/ __/ __/ / _ \_____/_______/_____\_______  {BLUE+CBLACKBG} \\
/ {RED}  / /_/ / /_/ / /_/ /_/ /  __|       > > >              /  {BLUE+CBLACKBG} \\
/ {RED} /_____/\__,_/\__/\__/_/\___/\_________________________/  {BLUE+CBLACKBG}  \\
/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\

"""
    print(game_title)


def single_player_mode():

    enemy_game_field_dict = {"A1": " ", "A2": " ", "A3": " ", "A4": " ", "A5": " ",
                             "B1": " ", "B2": " ", "B3": " ", "B4": " ", "B5": " ",
                             "C1": " ", "C2": " ", "C3": " ", "C4": " ", "C5": " ",
                             "D1": " ", "D2": " ", "D3": " ", "D4": " ", "D5": " ",
                             "E1": " ", "E2": " ", "E3": " ", "E4": " ", "E5": " "
                             }
    enemy = enemy_ship_placement()
    max_shots = 2
    game_state = True
    while game_state:
        enemy_view_field(enemy_game_field_dict)
        shot = hitting_enemy(enemy_game_field_dict)
        checked_enemy_game_field_dict = check_hit(
            enemy, shot, enemy_game_field_dict)
        game_state = check_win(
            enemy_game_field_dict, max_shots)


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


def hitting_enemy(enemy_game_field_dict):
    while True:
        guess = input(
            RED + "What are the coordinates we should shoot at?(A1,B2,...) \n" + WHITE)
        shot = guess.upper()
        if shot.__eq__("A1") or shot.__eq__("A2") or shot.__eq__("A3") or shot.__eq__("A4") or shot.__eq__("A5") or shot.__eq__("B1") or shot.__eq__("B2") or shot.__eq__("B3") or shot.__eq__("B4") or shot.__eq__("B5") or shot.__eq__("C1") or shot.__eq__("C2") or shot.__eq__("C3") or shot.__eq__("C4") or shot.__eq__("C5") or shot.__eq__("D1") or shot.__eq__("D2") or shot.__eq__("D3") or shot.__eq__("D4") or shot.__eq__("D5") or shot.__eq__("E1") or shot.__eq__("E2") or shot.__eq__("E3") or shot.__eq__("E4") or shot.__eq__("E5"):
            if enemy_game_field_dict[shot].__eq__(GREEN + "0" + BLUE) or enemy_game_field_dict[shot].__eq__(RED + "H" + BLUE):
                print(RED + "Perhaps another spot captain?!" + BLUE)
            else:
                break
        else:
            print(RED + "Impossible orders captain. Please try again captain!!!\n\n")
    return shot


def check_hit(enemy, shot, enemy_game_field_dict):
    if enemy[shot]:
        enemy_game_field_dict[shot] = RED + "H" + BLUE
    else:
        enemy_game_field_dict[shot] = GREEN + "0" + BLUE

    return enemy_game_field_dict


def check_win(enemy_game_field_dict, max_shots):
    ship_counter = 0
    shot_counter = 0
    game_state = True

    for key in enemy_game_field_dict:
        if enemy_game_field_dict[key].__eq__(RED + "H" + BLUE):
            ship_counter += 1
            shot_counter += 1
        if enemy_game_field_dict[key].__eq__(GREEN + "0" + BLUE):
            shot_counter += 1

        if ship_counter == 7:
            print(BOLD + GREENBRIGHT +
                  f"{CBLACKBG}Well done captain!!! WE won in {shot_counter} shots" + CBLACKBG+WHITE)
            game_state = False
            break
        if shot_counter == max_shots:
            print(BOLD + RED +
                  f"{CBLACKBG}we lost... {ships_left} targets left\n" + CBLACKBG+WHITE)
            game_state = False
            break
        shots_left = max_shots - shot_counter
        ships_left = 7 - ship_counter
        print(f" Tries left = {shots_left}")
    return game_state


def enemy_view_field(enemy_game_field_dict):
    ew = CBLACKBG+WHITE+"Enemy waters"+BLUE
    field_view = CBLACKBG + f"""
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
    print(CBLACKBG+BLUE + field_view+RED + "\n H " + WHITE + "= hit\n" +
          GREEN + " 0 " + WHITE+"= already hit/nothing found")


# problem with asking: choice doesn't check for wrong input
def ask_play_again(choice_playing):
    choice_state = True
    possible_positive_answers = [
        "yes", "y", "yes, why not", "yes please", "yeah", "positive",]
    possible_negative_answers = ["no", "n", "absolutely not", "hell no"]
    choice_play = input(
        "Would you like to play another round(yes/no/...)?")

    for word in possible_positive_answers:
        if word.__eq__(choice_play):
            choice_playing = True
    for word in possible_negative_answers:
        if word.__eq__(choice_play):
            choice_playing = False

    return choice_playing


# battleship_game()
