# Description:
# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# Tower block is represented as *
#
# Python: return a list;

def tower_builder(n_floors):
    tower = []
    tower_spaces = ""
    tower_center = "*"
    for first_floor in range(n_floors - 1):
        tower_spaces += " "
    tower.append(tower_spaces + tower_center + tower_spaces)
    for flor in range(1, n_floors):
        tower_spaces = tower_spaces[0:-1:1]
        tower_center += "**"
        tower.append(tower_spaces + tower_center + tower_spaces)
    return tower


print(tower_builder(4))
