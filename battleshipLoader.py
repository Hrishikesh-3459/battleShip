from random import randint
# from ship import Ship
COL_SIZE = 9
ROW_SIZE = 9
NO_OF_SHIPS = 3
SHIP_SIZE = 4
        
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
        print(grid)

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



# print(grid)
ship_list = []
for ship in range(NO_OF_SHIPS):
    [location, orientation] = get_location()
    ship_list.append(Ship(location, orientation, SHIP_SIZE))
    print(location['row'])
    print(location['column'])
    print(orientation)
# print_board(grid)
# Welcome to battleship game
# ----------------------------------------
# _____________________________
# | * | * | * | * | * | * | * |
# | * | * 
# -----------------------------
