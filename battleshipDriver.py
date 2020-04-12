from itertools import cycle
from battleShipUser import *
import sys
import os
import mysql.connector
import time

start_time = time.time()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="RamuSQL#123kaka",
    database="mydatabase"
)

mycursor = mydb.cursor()


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
    print("Total time taken  = ", (time.time() - start_time), " seconds")
    # for j in range(NO_OF_USERS):
    #     user_name.append(input("Enter name of user "))
    #     for user in user_name:
    #         sql = "INSERT INTO players (name,score) VALUES (%s)(%s)"
    #         val = [(user, chances)]
    #     mycursor.execute(sql, val)
    sql1 = "INSERT INTO players (score) VALUES (%s)"
    val1 = [(chances)]
    mycursor.execute(sql1, val1)
    mydb.commit()
    for i in range(FULL_LINE):
        print("-", end="")
    print()
    # sys.exit()


global NO_OF_USERS


def intro():
    # mycursor = mydb.cursor()
    # user_name = ""
    Board = [["*"] * COL_SIZE for j in range(ROW_SIZE)]
    st = "Welcome to battleship game"
    ste = st.center(FULL_LINE, "-")
    print(ste)
    while True:
        try:
            NO_OF_USERS = int(input("Enter number of players: "))
            break
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
    while True:
        try:
            NO_OF_SHIPS = int(
                input("Enter the total number of ships (Max input limit 8): "))
            break
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
    print("Number of ships = ", NO_OF_SHIPS)
    # print("Ship Size = ", SHIP_SIZE)
    print(" '*' indicate unexplored coordinates")
    print(" 'H' indicates hits")
    print(" '-' indicates misses")
    print("The ships are either horizontal or vertical,\nThey are not diagonal.")
    for j in range(NO_OF_USERS):
        user_name.append(input("Enter name of user "))
        for user in user_name:
            sql = "INSERT INTO players (name) VALUES (%s)"
            val = [(user)]
        mycursor.execute(sql, val)
    # mydb.commit()
    # mycursor.execute(sql, val)
    # mydb.commit()
    print("Sink Them All!")
    print("Good Luck!")
    print_board(Board)

    return [NO_OF_SHIPS, NO_OF_USERS]


# driver
ship_list = []
chances = 0
user_list = []
user_name = []
[NO_OF_SHIPS, NO_OF_USERS] = intro()

for user in range(NO_OF_USERS):
    user_list.append(battleShipUser(NO_OF_SHIPS))


# mycursor.execute(sql, val)
# mydb.commit()


for dramu in range(NO_OF_USERS):
    POS_INDICATOR = 10
    for i in range(POS_INDICATOR):
        print("   |", i, end="")
    print("   |")
    k = 0
    for i in range(ROW_SIZE):
        print(k, end="")
        for j in range(COL_SIZE):
            print("  |  " + str(user_list[dramu].grid[i][j]), end="")
        print("  |")
        k += 1


iterator = cycle(range(NO_OF_USERS))
player = next(iterator)
while True:
    print("Player {0}".format(int(player) + 1))
    input_cord = user_list[player].get_input()
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
