from random import randint
import sys
COL_SIZE = 10
ROW_SIZE = 10
NO_OF_SHIPS = 3
NO_OF_SHIPS = int(input("Enter the total number of ships  "))
SHIP_SIZE = 4
hits = [] 
hits.append(0)
chances = [] 
chances.append(0)
full_line = 190
ship_no = []
ship_no.append(0)
grid = [[0] * COL_SIZE for j in range(ROW_SIZE)]
board = [["*"] * COL_SIZE for j in range(ROW_SIZE)]


class Ship:
    def __init__(self, location, orientation, SHIP_SIZE):
        self.size = SHIP_SIZE
        self.orientation = orientation
        self.numb = 1
        if(self.orientation == "Vertical"):
            self.coordinates = []
            for i in range(SHIP_SIZE):
                self.coordinates.append({'row': location['row'] + i, 'column': location['column']})
        if(self.orientation == "Horizontal"):
            self.coordinates = []
            for i in range(SHIP_SIZE):
                self.coordinates.append({'row': location['row'], 'column': location['column'] + i})
        for i in range(SHIP_SIZE):
            grid[self.coordinates[i]['row']][self.coordinates[i]['column']] = 1
        self.health = ["*"] * SHIP_SIZE
    
    # def check_health(self):
    #     if("*" not in self.health):
    #         print("Ship Sunk")
    
    def change_health(self, input_cord):
        for i in range(self.size):
            if((self.coordinates[i]["row"] == input_cord['row']) and (self.coordinates[i]["column"] == input_cord['column'])):
                self.health[i] = "H"
        if("*" not in self.health):
            print("Ship Sunk!!!")
            self.health = ["*"] * SHIP_SIZE
        # self.check_health()
    
    
def intro():
    st = "Welcome to battleship game"
    ste = st.center(full_line, "-")
    print(ste)
    # NO_OF_SHIPS = int(input("Enter the total number of ships  "))
    print("Number of ships = ", NO_OF_SHIPS)
    print("Ship Size = ", SHIP_SIZE, "x 1")
    print(" '*' indicate unexplored coordinates")
    print(" 'H' indicates hits")
    print(" 'M' indicates misses")
    print("The ships are either horizontal or vertical,\nThey are not diagonal.")
    print("Sink Them All!")
    print("Good Luck!")

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
    for i in range(len(board)):
        print(k, end="")
        for j in range(len(board)):
            print("  |  " + board[i][j] , end = "")
        print("  |")
        k += 1
    for i in range(border):
        print("_", end = "")
    print()


def validate(input_cord):
    To_avoid_error = 0
    max_hits = SHIP_SIZE * NO_OF_SHIPS
    chances[0] += 1
    for ship in ship_list:
        for i in range(ship.size):
            if((ship.coordinates[i]["row"] == input_cord['row']) and (ship.coordinates[i]["column"] == input_cord['column'])):
                print("HIT!!!") 
                board[input_cord["row"]][input_cord["column"]] = "H"
                print_board()
                hits[0] += 1
                for temp_ship in ship_list:
                    temp_ship.change_health(input_cord)
                To_avoid_error = 100
    if(To_avoid_error != 100):
        print("MISS...")
        board[input_cord["row"]][input_cord["column"]] = "M"
        print_board()
    
    if(hits[0] == max_hits):
        fin()
    else: 
        get_input()
    
    
def check_input(input_cord):
    if(board[input_cord["row"]][input_cord["column"]] !=  "*"):
            print("oops.. input already given. Enter new coordinates")
            get_input()
    else:
        validate(input_cord)
    
def get_input():
    while True:
        input_cord = {}
        inp_row = int(input("Enter the row coordinate:  "))
        input_cord["row"] = inp_row
        inp_col = int(input("Enter the column coordinate:  "))
        input_cord["column"] = inp_col
        check_input(input_cord)



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
        if(not result):
            continue
        else:
            return [location, orientation]


def fin():
    for i in range(full_line):
        print("-", end = "")
    print()
    print("Game Over")
    print("Total Number of chances = ", chances[0])
    for i in range(full_line):
        print("-", end = "")
    print()
    sys.exit()


ship_list = []
for ship in range(NO_OF_SHIPS):
    [location, orientation] = get_location()
    ship_list.append(Ship(location, orientation, SHIP_SIZE))
# print(grid)
intro()
print_board()
get_input()