from random import randint
# from ship import Ship
COL_SIZE = 10
ROW_SIZE = 10
NO_OF_SHIPS = 3
SHIP_SIZE = 4
h = [] # total number of hits
h.append(0)
c = [] # total number of chances
c.append(0)
st = "Welcome to battleship game"
ste = st.center(190, "-")
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


def print_board():
    symb = "*"
    for i in range(190):
        print("-", end = "")
    print()
    for i in range(41):
        print("_", end = "")
    print()
    k = 0
    l = 0
    for i in range(10): 
        print("   |" , i , end = "")
    print("   |")
    for i in range(len(board)):
        print(k, end="")
        for j in range(len(board)):
            print("  |  " + board[i][j] , end = "")
        print("  |")
        k += 1
    for i in range(41):
        print("_", end = "")
    print()


def check_input(a):
    c[0] += 1
    for i in range(len(grid)):
        if(grid[a[0]][a[1]] == 1):
            print("HIT!!!") 
            board[a[0]][a[1]] = "#"
            print_board()
            h[0] += 1
            break
        else:
            print("MISS...")
            board[a[0]][a[1]] = "."
            print_board()
            break
    if(h[0] == 12):
        fin()
    else:
        get_input()
    
    
def get_input():
    a = []
    print("Please enter coordinates  ")
    for q in range(2):
        b = int(input())
        a.append(b)
    check_input(a)


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
    for i in range(190):
        print("-", end = "")
    print()
    print("Game Over")
    print("Total Number of chances = ", c[0])
    for i in range(190):
        print("-", end = "")
    print()


# print_board()
# get_input()
ship_list = []
for ship in range(NO_OF_SHIPS):
    [location, orientation] = get_location()
    ship_list.append(Ship(location, orientation, SHIP_SIZE))
    # print(location['row'])
    # print(location['column'])
    # print(orientation)
# print_board()
print(grid)
print_board()
get_input()


