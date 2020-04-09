import sys
import os

from battleShipUser import battleShipUser
from itertools import cycle

COL_SIZE = 10
ROW_SIZE = 10
os.system('clear')
NO_OF_SHIPS = 0

FULL_LINE = 190
# NO_OF_USERS = 0

grid = [[0] * COL_SIZE for j in range(ROW_SIZE)]
board = [["*"] * COL_SIZE for j in range(ROW_SIZE)]


def fin(chances, player):
    for i in range(FULL_LINE):
        print("-", end="")
    print()
    print("Game Over")
    print("Player '{0}' won!".format(player + 1))
    print("Total Number of chances: ", chances)
    for i in range(FULL_LINE):
        print("-", end="")
    print()
    # sys.exit()


global NO_OF_USERS


def intro():
    st = "Welcome to battleship game"
    ste = st.center(FULL_LINE, "-")
    print(ste)
    NO_OF_USERS = int(input("Enter number of players: "))
    NO_OF_SHIPS = int(
        input("Enter the total number of ships (Max input limit 8): "))
    # NO_OF_SHIPS = int(input("Enter the total number of ships  "))
    print("Number of ships = ", NO_OF_SHIPS)
    # print("Ship Size = ", SHIP_SIZE)
    print(" '*' indicate unexplored coordinates")
    print(" 'H' indicates hits")
    print(" 'M' indicates misses")
    print("The ships are either horizontal or vertical,\nThey are not diagonal.")
    print("Sink Them All!")
    print("Good Luck!")
    return [NO_OF_SHIPS, NO_OF_USERS]


# driver
ship_list = []
chances = 0
user_list = []
[NO_OF_SHIPS, NO_OF_USERS] = intro()

for user in range(NO_OF_USERS):
    user_list.append(battleShipUser(NO_OF_SHIPS))

# for dramu in range(NO_OF_USERS):
#     POS_INDICATOR = 10
#     for i in range(POS_INDICATOR):
#         print("   |", i, end="")
#     print("   |")
#     k = 0
#     for i in range(ROW_SIZE):
#         print(k, end="")
#         for j in range(COL_SIZE):
#             print("  |  " + str(user_list[dramu].grid[i][j]), end="")
#         print("  |")
#         k += 1


# POS_INDICATOR = 10
# for i in range(POS_INDICATOR):
#     print("   |", i, end="")
# print("   |")
# k = 0
# for i in range(ROW_SIZE):
#     print(k, end="")
#     for j in range(COL_SIZE):
#         print("  |  " + str(user_list[1].grid[i][j]), end="")
#     print("  |")
#     k += 1

# print(user_list[0].ship_list)
iterator = cycle(range(NO_OF_USERS))
player = next(iterator)
while True:
    print("Player {0}".format(int(player) + 1))
    input_cord = user_list[player].get_input()
    # os.system('clear')
    user_list[player].chances += 1
    user_list[player].validate(input_cord)
    for temp_ship in user_list[player].ship_list:
        if(not temp_ship.sunk):
            temp_ship.change_health(input_cord)
            user_list[player].sunk_ctr = temp_ship.check_health(
                user_list[player].sunk_ctr)
    if(user_list[player].check_game_status(user_list[player].ship_list)):
        fin(user_list[player].chances, player)
        break
    player = next(iterator)
