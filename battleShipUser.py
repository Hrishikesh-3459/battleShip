from ship import Ship
from random import randint


COL_SIZE = 10
ROW_SIZE = 10
SHIP_SIZE = 4
FULL_LINE = 190


class battleShipUser:

    def __init__(self, NO_OF_SHIPS):
        self.ship_list = []
        self.chances = 0
        self.sunk_ctr = 0
        self.grid = [[0] * COL_SIZE for j in range(ROW_SIZE)]
        self.board = [["*"] * COL_SIZE for j in range(ROW_SIZE)]
        self.create_ships(NO_OF_SHIPS)

    def create_ships(self, NO_OF_SHIPS):
        for ship in range(NO_OF_SHIPS):
            [location, orientation] = self.get_location()
            # print(location)
            # print(orientation)
            temp_ship = Ship(location, orientation, SHIP_SIZE)
            self.ship_list.append(temp_ship)
            for i in range(SHIP_SIZE):
                self.grid[temp_ship.coordinates[i]['row']
                          ][temp_ship.coordinates[i]['column']] = 1

    def check_location(self, location, orientation):
        if(orientation == "Vertical"):
            for i in range(SHIP_SIZE):
                if(self.grid[location['row'] + i][location['column']] == 1):
                    return False
        elif(orientation == "Horizontal"):
            for i in range(SHIP_SIZE):
                if(self.grid[location['row']][location['column'] + i] == 1):
                    return False
        return True

    def get_location(self):
        while True:
            location = {}
            location['row'] = randint(0, ROW_SIZE - SHIP_SIZE)
            location['column'] = randint(0, COL_SIZE - SHIP_SIZE)
            orientation = "Vertical" if randint(0, 1) == 0 else "Horizontal"
            result = self.check_location(location, orientation)
            if(result):
                return [location, orientation]
            else:
                continue

    def check_input(self, input_cord):
        if(self.board[input_cord["row"]][input_cord["column"]] != "*"):
            print("oops.. input already given. Enter new coordinates")
            return False
        else:
            return True

    def get_input(self):
        while True:
            try:
                input_cord = {}
                inp_row = int(input("Enter the row coordinate:  "))
                input_cord["row"] = inp_row
                inp_col = int(input("Enter the column coordinate:  "))
                input_cord["column"] = inp_col
                if(self.check_input(input_cord)):
                    return input_cord
                else:
                    continue
            except TypeError:
                print("\nPlease enter a number")

    def validate(self, input_cord):
        FLAG = False
        for ship in self.ship_list:
            for i in range(ship.size):
                if((ship.coordinates[i]["row"] == input_cord['row']) and (ship.coordinates[i]["column"] == input_cord['column'])):
                    self.board[input_cord["row"]][input_cord["column"]] = "H"
                    print_board(self.board)
                    print("HIT!!!")
                    FLAG = True
        if(FLAG == False):
            self.board[input_cord["row"]][input_cord["column"]] = "."
            print_board(self.board)
            print("MISS...")

    def check_game_status(self, ship_list):
        GAME_OVER = True
        for ship in self.ship_list:
            if(ship.sunk == False):
                GAME_OVER = False
        return GAME_OVER


def print_board(board):
    BORDER = 64
    POS_INDICATOR = 10
    for i in range(FULL_LINE):
        print("-", end="")
    print()
    for i in range(BORDER):
        print("_", end="")
    print()
    k = 0
    for i in range(POS_INDICATOR):
        print("   |", i, end="")
    print("   |")
    for i in range(ROW_SIZE):
        print(k, end="")
        for j in range(COL_SIZE):
            print("  |  " + board[i][j], end="")
        print("  |")
        k += 1
    for i in range(BORDER):
        print("_", end="")
    print()
