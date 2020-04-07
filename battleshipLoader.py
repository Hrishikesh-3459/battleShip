from random import randint
import sys
import os
from ship import Ship

COL_SIZE = 10
ROW_SIZE = 10
NO_OF_SHIPS = 3
os.system('clear')
NO_OF_SHIPS = int(input("Enter the total number of ships (Max input limit 8): "))
SHIP_SIZE = 4
full_line = 190
chances = 0
grid = [[0] * COL_SIZE for j in range(ROW_SIZE)]
board = [["*"] * COL_SIZE for j in range(ROW_SIZE)]
   
def intro():
    st = "Welcome to battleship game"
    ste = st.center(full_line, "-")
    print(ste)
    # NO_OF_SHIPS = int(input("Enter the total number of ships  "))
    print("Number of ships = ", NO_OF_SHIPS)
    print("Ship Size = ", SHIP_SIZE)
    print(" '*' indicate unexplored coordinates")
    print(" 'H' indicates hits")
    print(" 'M' indicates misses")
    print("The ships are either horizontal or vertical,\nThey are not diagonal.")
    print("Sink Them All!")
    print("Good Luck!")
    print_board()

def print_board():
    border = 64
    pos_indicator = 10
    for i in range(full_line):
        print("-", end = "")
    print()
    for i in range(border):
        print("_", end = "")
    print()
    k = 0
    for i in range(pos_indicator): 
        print("   |" , i , end = "")
    print("   |")
    for i in range(ROW_SIZE):
        print(k, end="")
        for j in range(COL_SIZE):
            print("  |  " + board[i][j] , end = "")
        print("  |")
        k += 1
    for i in range(border):
        print("_", end = "")
    print()


def validate(input_cord):
    # max_hits = SHIP_SIZE * NO_OF_SHIPS
    FLAG = False
    for ship in ship_list:
        for i in range(ship.size):
            if((ship.coordinates[i]["row"] == input_cord['row']) and (ship.coordinates[i]["column"] == input_cord['column'])):
                board[input_cord["row"]][input_cord["column"]] = "H"
                print_board()
                print("HIT!!!") 
                FLAG = True
    if(FLAG == False):
        board[input_cord["row"]][input_cord["column"]] = "."
        print_board()
        print("MISS...")

def check_game_status(ship_list):
    GAME_OVER = True
    for ship in ship_list:
        if(ship.sunk == False):
            GAME_OVER = False    
    return GAME_OVER
    
def check_input(input_cord):
    if(board[input_cord["row"]][input_cord["column"]] !=  "*"):
        print("oops.. input already given. Enter new coordinates")
        return False
    else:
        return True
    
def get_input():
    while True:
        input_cord = {}
        inp_row = int(input("Enter the row coordinate:  "))
        input_cord["row"] = inp_row
        inp_col = int(input("Enter the column coordinate:  "))
        input_cord["column"] = inp_col
        if(check_input(input_cord)):
            return input_cord
        else:
            continue

def check_location(location, orientation):
    if(orientation == "Vertical"):
        for i in range(SHIP_SIZE):
            if(grid[location['row'] + i][location['column']] == 1):
                return False
    elif(orientation == "Horizontal"):
        for i in range(SHIP_SIZE):
            if(grid[location['row']][location['column'] + i] == 1):
                return False 
    return True


def get_location():
    while True:
        location = {}
        location['row'] = randint(0, ROW_SIZE - SHIP_SIZE)
        location['column'] = randint(0, COL_SIZE - SHIP_SIZE)
        orientation = "Vertical" if randint(0,1) == 0 else "Horizontal"
        result = check_location(location, orientation)
        if(result):
            return [location, orientation]
        else:
            continue


def fin(CHANCES):
    for i in range(full_line):
        print("-", end = "")
    print()
    print("Game Over")
    print("Total Number of chances = ", CHANCES)
    for i in range(full_line):
        print("-", end = "")
    print()
    sys.exit()


ship_list = []
CHANCES = 0
for ship in range(NO_OF_SHIPS):
    [location, orientation] = get_location()
    # print(location)
    # print(orientation)
    temp_ship = Ship(location, orientation, SHIP_SIZE)
    ship_list.append(temp_ship)
    for i in range(SHIP_SIZE):
        grid[temp_ship.coordinates[i]['row']][temp_ship.coordinates[i]['column']] = 1

intro()

# pos_indicator = 10
# for i in range(pos_indicator): 
#     print("   |" , i , end = "")
# print("   |")
# k = 0
# for i in range(ROW_SIZE):
#     print(k, end="")
#     for j in range(COL_SIZE):
#         print("  |  " + str(grid[i][j]) , end = "")
#     print("  |")
#     k += 1

while True:
    input_cord = get_input()
    os.system('clear')
    CHANCES += 1
    validate(input_cord)
    for temp_ship in ship_list:
        if(not temp_ship.sunk):
            temp_ship.change_health(input_cord)
            temp_ship.check_health()
    if(check_game_status(ship_list)):
        fin(CHANCES)
        