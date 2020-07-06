from random import randint
import sys
import os

COL_SIZE = 10
ROW_SIZE = 10
SHIP_SIZE = 4


class Ship:
    def __init__(self, location, orientation, SHIP_SIZE):
        self.size = SHIP_SIZE
        self.orientation = orientation
        self.sunk = False
        
        if(self.orientation == "Vertical"):
            self.coordinates = []
            for i in range(SHIP_SIZE):
                self.coordinates.append(
                    {'row': location['row'] + i, 'column': location['column']})
                
        if(self.orientation == "Horizontal"):
            self.coordinates = []
            for i in range(SHIP_SIZE):
                self.coordinates.append(
                    {'row': location['row'], 'column': location['column'] + i})
        self.health = ["*"] * SHIP_SIZE

    # Function to check the status of each ship
    def check_health(self, sunk_ctr):
        if("*" not in self.health):
            sunk_ctr += 1
            print("Ship no. {0} sunk!".format(sunk_ctr))
            self.sunk = True
        return sunk_ctr
    
    # Function to update the status of each ship
    def change_health(self, input_cord):
        for i in range(self.size):
            if((self.coordinates[i]["row"] == input_cord['row']) and (self.coordinates[i]["column"] == input_cord['column'])):
                self.health[i] = "H"
