from ship import Ship
from random import randint

COL_SIZE = 10
ROW_SIZE = 10
SHIP_SIZE = 4


class battleShipUser:
    def __init__(self, NO_OF_SHIPS):
        self.input_cord = {}
        self.ship_list = []
        self.chances = 0
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
                self.grid[temp_ship.coordinates[i]['row']][temp_ship.coordinates[i]['column']] = 1

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
            orientation = "Vertical" if randint(0,1) == 0 else "Horizontal"
            result = self.check_location(location, orientation)
            if(result):
                return [location, orientation]
            else:
                continue