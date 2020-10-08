import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'


def lever_fun(coins_input):
    lever_input = random.choice(['y', 'n'])
    print ('Pull a lever (y/n): {}'.format(lever_input))
    if lever_input.upper() == "Y":
        coins_input += 1
        print("You received 1 coin, your total is now {}.".format(str(coins_input)))
    return coins_input


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    


def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)


def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")


def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST      
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST     
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions


def play_one_move(col, row, valid_directions, coins,moves):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    direction = direction.lower()
    moves += 1
    print('Direction: {}'.format(direction))
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        if col == 1 and row == 2:
            coins = lever_fun(coins)
        elif col == 2 and row == 2:
            coins = lever_fun(coins)
        elif row == 3 and col == 2 :
            coins = lever_fun(coins)
        elif row == 2 and col == 3 :
            coins = lever_fun(coins)
        victory = is_victory(col, row)
    return victory, col, row, coins, moves


def play(coins,moves):
    victory = False
    row = 1
    col = 1

    seed = int(input('Input seed: '))
    random.seed(seed)

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, coins,moves = play_one_move(col, row, valid_directions, coins,moves)

    print("Victory! Total coins {}. Moves {}.".format(str(coins),str(moves)))

    
# Main programm

main = True
while main :

    coins = 0
    moves = 0
    play(coins,moves)
    answer = input("Play again (y/n): ")

    if answer.lower() == 'n':
        main = False

# Linkur á Github hjá okkur
# https://github.com/Davidsaemund/TileTraveller_Assign_8/commits/master
     