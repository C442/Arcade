# mInput.py

from random import randrange, choice

# constants for borders around text, see def title()
# https://www.w3schools.com/charsets/ref_utf_box.asp
TL = chr(9487)      # Top Left
TR = chr(9491)      # Top Right
BL = chr(9495)      # Bottom Left
BR = chr(9499)      # Bottom right
H = chr(9473)       # horizontal
V = chr(9475)       # vertical
C = chr(9547)       # Cross
SL = chr(9507)      # Splitter left
SR = chr(9515)      # Splitter right
ST = chr(9523)      # Splitter top
SB = chr(9531)      # Splitter bottom

# optional for 2B, but cool: color constants-> ANSI escape strings (https://en.wikipedia.org/wiki/ANSI_escape_code)
# 3 éléments: \033[ == ESC, <control sequence> interprétés par la console, m == terminator
# foreground colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
GREENBRIGHT = "\033[92m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[97m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
UNDERLINE = "\033[;4m"

# Background
CBLACKBG = '\33[40m'
CREDBG = '\33[41m'
CGREENBG = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG = '\33[46m'
CGRAYBG = '\33[100m'
CWHITEBG = '\33[47m'

# Mix == "\33[<foregroundcolor>;<background>m"
BLUEONGRAY = "\033[34;47m"
YELLOWONBLACK = "\033[93;40m"
WHITEONRED = "\033[97;41m"


def title(title):
    # "\n" forces line break above title
    print("\n" + BLUE + TL + H*len(title) + TR)
    print(V + title + V)
    print(BL + H*len(title) + BR + RESET + "\n")


def get_int(prompt="Saisissez un nombre entier: "):
    prompt = RESET + MAGENTA + prompt
    while True:
        try:
            userinput = input(prompt)
            n = int(userinput)          # try to convert to integer
            break                       # conversion OK -> jump out of loop
        except ValueError:
            print(BOLD + RED + f"{userinput} n'est pas un nombre entier!")
            continue                    # conversion fault -> reloop
    print(RESET, end="")
    return n


def get_entier_naturel(prompt="Saisissez un nombre entier naturel non nul: "):
    n = 0
    while n <= 0:
        n = get_int(prompt)             # function returns an Integer
        if n <= 0:
            print(RED + BOLD + f"{n} n'est pas un entier naturel non nul!")
    return n


def get_float(prompt="Saisissez un nombre réel: "):
    prompt = RESET + MAGENTA + prompt
    while True:
        try:
            userinput = input(prompt)
            n = float(userinput)            # try to convert to float
            break                           # conversion OK -> jump out of loop
        except ValueError:
            print(BOLD + RED + f"{userinput} n'est pas un nombre réel!")
            print(RESET, end="")
            continue                        # conversion fault -> reloop
    print(RESET, end="")
    return n


def liste_entiers_aleatoires(taille, min, max):
    li = []
    for i in range(taille):
        li.append(randrange(min, max+1))
    return li


def liste_car_aleatoires(taille=25, upper_lower = "ul"):
    # retourne une liste de lettres majuscules et/ou minuscules
    # param upper_lower == u: upper, ==l: lower,  ==ul: upper and lower letters
    uc = [chr(i) for i in range(65, 91)]  # Majuscules
    lc = [chr(i) for i in range(97, 123)] # minuscules
    all_chars = lc + uc
    l = []
    if upper_lower == "ul":
        for i in range(taille):
            l.append(choice(all_chars))
    elif upper_lower == "u":
        for i in range(taille):
            l.append(choice(uc))
    else:
        for i in range(taille):
            l.append(choice(lc))
    return l	


def print_table(table):    # table = list of lists,number of columns per line must be identical
    # first line
    sizes=[]   # sizes == table of cell sizes
    nbr_lines = len(table)
    nbr_cols = len(table[0])   # each line has same number of columns
    for lig in range(nbr_lines):
        l = []
        for col in range(nbr_cols):
            l.append(len(str(table[lig][col])))
        sizes.append(l)
    # find the maximum size of each column, add it to list: max_per_col
    max_per_col = []
    for col in range(nbr_cols):
        max = 0
        for lig in range(nbr_lines):
            if sizes[lig][col] > max:
                max = sizes[lig][col]
        max_per_col.append(max)

    #------- print 1st line of table --------
    firstline = TL
    for col in range(nbr_cols):
        firstline += H * max_per_col[col]
        firstline += ST
    firstline = firstline[:-1]
    firstline += TR
    print(firstline)

    # -------- print data ---------------------
    for lig in range(nbr_lines):
        print(V, end = "")
        for col in range(nbr_cols):
            text = str(table[lig][col])          # text to insert into cell
            spaces = max_per_col[col]-len(text)  # alignement: how many spaces before or after text
            if type(table[lig][col]) in (float, int):
                print(" " * spaces + BLUE + text  + RESET + V, end="")  # right aligned numbers/text
            else:
                print(BLUE + text + " " * spaces + RESET + V, end="")   # left aligned text
        print()
        # line between data
        line_between = SL
        for col in range(nbr_cols):
            line_between += H * max_per_col[col]
            line_between += C
        line_between = line_between[:-1]
        line_between += SR
        if lig < nbr_lines-1:   # only print if not last line of table
            print(line_between)

    # -------- print last line of table --------
    lastline = BL
    for col in range(nbr_cols):
        lastline += H * max_per_col[col]
        lastline += SB
    lastline = lastline[:-1]
    lastline += BR
    print(lastline)


# test code, not executed with an import
if __name__ == "__main__":
    title("Check whether input is of correct type")
    x = get_int("Integer value: ")
    y = get_float("And now a real number: ")
    n = get_entier_naturel("et maintenant un entier naturel non nul: ")
    print(RED + "\nen rouge " + BOLD + " en gras " + UNDERLINE + "souligné " + REVERSE + "inversé" + RESET)
    print(WHITEONRED + "blanc sur rouge" + RESET)
    title("listes aléatoires")
    print(f"liste aléatoire entre 50 et 100: {liste_entiers_aleatoires(10, 50, 100)}")
    print(f"liste aléatoire de lettres minuscules: {liste_car_aleatoires(10, 'l')}")                 # l = Lower
    print(f"liste aléatoire de lettres majuscules: {liste_car_aleatoires(10, 'u')}")                 # u = Upper
    print(f"liste aléatoire de lettres minuscules et majuscules: {liste_car_aleatoires(10, 'ul')}")  # ul = both
    title("print a matrix of size 2")
    text = "cell value"
    l = len(text)
    print(TL + H*l + ST + H*l + TR)
    print(V + text + V + text + V)
    print(SL + H*l + C + H*l + SR)
    print(V + text + V + text + V)
    print(BL + H*l + SB + H*l + BR)
    title("Print a table")
    l = [[100, 21, 30], [40, 5, 6], [7, 8, 9], [10, 11, 12], [12, 345, 2216]]
    print(f"list to print as table: {l}")
    print_table(l)
    l = [["numbers aligned right", "text aligned left"], [2.663, "abcd", "kukuk"]]
    print(f"list to print as table: {l}")
    print_table(l)

