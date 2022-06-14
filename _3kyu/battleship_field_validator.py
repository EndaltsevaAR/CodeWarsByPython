"""Description:
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a
valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the
array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing
several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship
occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we
will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1).
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner."""


MAX_SHIP_SIZE = 5


def validate_battlefield(field):
    ships_dict = dict()
    for size in range(1, MAX_SHIP_SIZE):  # ships initialization
        ships_dict[size] = MAX_SHIP_SIZE - size
    for y in range(len(field)):
        for x in range(len(field[0])):
            if is_start_of_ship(y, x, field):
                ship_data = find_ship(y, x, field)
                if ship_data[0] == -1 or ship_data[1] >= MAX_SHIP_SIZE or ships_dict[ship_data[1]] == 0 or has_neighbor(
                        y, x, ship_data, field):
                    return False
                else:
                    ships_dict[ship_data[1]] -= 1
    for ship_count in ships_dict.values():
        if ship_count > 0:
            return False
    return True


def is_start_of_ship(y, x, field):
    return (y == 0 or (y > 0 and field[y - 1][x] == 0)) and (x == 0 or (x > 0 and field[y][x - 1] == 0)) and field[y][
        x] == 1


def find_ship(y, x, field):
    size = 1
    direction = 0  # horizontal: 1, vertical: 2, one cell:0, different: -1
    while True:
        if direction == 0:
            if x <= len(field[0]) - 2 and field[y][x + 1] == 1:
                size += 1
                direction = 1
                x += 1
            elif y <= len(field) - 2 and field[y + 1][x] == 1:
                size += 1
                direction = 2
                y += 1
            else:
                return [direction, size]
        elif direction == 1:
            if x <= len(field[0]) - 2 and field[y][x + 1] == 1:
                size += 1
                x += 1
            else:
                return [direction, size]
        else:
            if y <= len(field) - 2 and field[y + 1][x] == 1:
                size += 1
                y += 1
            else:
                return [direction, size]


def has_neighbor(y, x, ship_data, field):
    y_min = max(0, y - 1)
    x_min = max(0, x - 1)
    if ship_data[0] == 1 or ship_data[0] == 0:
        y_max = min(len(field) - 1, y + 1)
        x_max = min(len(field[0]) - 1, x + ship_data[1])
    else:
        y_max = min(len(field) - 1, y + ship_data[1])
        x_max = min(len(field[0]) - 1, x + 1)
    for y_coord in range(y_min, y_max + 1):
        for x_coord in range(x_min, x_max + 1):
            if field[y_coord][x_coord] == 1:
                if (ship_data[0] == 1 or ship_data[0] == 0) and (  # for horizontal ship
                        y_coord != y or x_coord < x or x_coord >= x + ship_data[1]):  # except ship's cells
                    return True
                if ship_data[0] == 2 and (x_coord != x or y_coord < y or y_coord >= y + ship_data[1]):  # for vertical
                    return True  # except ship's cells
    return False
