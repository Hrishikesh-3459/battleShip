from random import randint
# from ship import Ship
COL_SIZE = 10
ROW_SIZE = 10
NO_OF_SHIPS = 5
SHIP_SIZE = 4
hits = [] # total number of hits
hits.append(0)
chances = [] # total number of chances
chances.append(0)
full_line = 190
st = "Welcome to battleship game"
ste = st.center(full_line, "-")
print(ste)
grid = [[0] * COL_SIZE for j in range(ROW_SIZE)]
board = [["*"] * COL_SIZE for j in range(ROW_SIZE)]


class Ship:
    
    def __init__(self, location, orientation, SHIP_SIZE):
        self.size = SHIP_SIZE
        self.orientation = orientation
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
        # print(grid)
        self.health = [["*"] * SHIP_SIZE]
    
    def change_health(self):
        pass

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


def check_input(input_cord):
    max_hits = SHIP_SIZE * NO_OF_SHIPS
    chances[0] += 1
    for ship in ship_list:
        for i in range(len(ship.size)):
            if((ship.coordinates[i]["row"] == input_cord['row']) and (ship.coordinates[i]["column"] == input_cord['column'])):
                print("HIT!!!") 
                board[input_cord["row"]][input_cord["column"]] = "#"
                print_board()
                hits[0] += 1
                break
        

        # if(grid[input_cord["row"]][input_cord["column"]] == 1):
        #     print("HIT!!!") 
        #     board[input_cord["row"]][input_cord["column"]] = "#"
        #     print_board()
        #     hits[0] += 1
        #     break
    print("MISS...")
    board[input_cord["row"]][input_cord["column"]] = "."
    print_board()
    break
    if(hits[0] == max_hits):
        fin()
    else:
        get_input()
    
    
def get_input():
    while True:
        input_cord = {}
        inp_row = int(input("Enter the row coordinate:  "))
        input_cord["row"] = inp_row
        inp_col = int(input("Enter the column coordinate:  "))
        input_cord["column"] = inp_col
        if(board[inp_row][inp_col] is not "*"):
            print("oops.. input already given. Enter new coordinates")
        else:
            check_input(input_cord)
            break


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


# print_board()
# get_input()
ship_list = []
for ship in range(NO_OF_SHIPS):
    [location, orientation] = get_location()
    ship_list.append(Ship(location, orientation, SHIP_SIZE))
    print(location['row'])
    print(location['column'])
    print(orientation)
# print_board()
print(grid)
print_board()
get_input()


