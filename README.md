# Welcome to Battleship game

This is the version that uses SQL to keep log of the players

## Getting Started

Please make sure to do **all** of this before you run the code.

### Prerequisites

* Python 

* mySQL 

* mySQL Connector

* Tabulate package 

### Installing

##### mySQL:

Download [MySQL](https://dev.mysql.com/downloads/mysql/) and go through the setup process, and make sure to keep note of your host, username and password.

After installing MySQL, go to **dbConfig.py** and enter your host, username and password in the "init" function.

##### mySQL Connector

Paste 

```
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector
```

In your command line.

##### Tabulate Package

```
pip install tabulate
```

## Usage

The usage for this game is pretty straightforward and step-by-step instructions are provided **in game**.

In general

* You will have to select the number of players playing the game

* Select the numeber of ships you want to be on the grid (maximum 8)

* '*' indicate _unexplored_ coordinates.

  'H' indicates _hits_.
  
  '-' indicates _misses_.
  
* The ships are either horizontal or vertical, they are **not** diagonal. 

* You have to enter _row and column_ coordinates, whenever prompted and **sink** all of the ship!

* Once you have completed the game, you will be prompted to enter the name of the winner

* After entering the name, you will see the table of all the previous players and their scores.

## Screenshots

### Start

![Start](https://user-images.githubusercontent.com/51927760/86593210-6e125300-bfb2-11ea-9ec4-e38dd8257103.png)
