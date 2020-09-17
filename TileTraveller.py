# Assignment 8 
# Tile Traveler
# Program that moves NORTH, SOUTH, WEST and EAST in a 3v3 tile plan.


#Function that gets your current loc and tells you what options you have

def tile_traveller(x,y):
    if (x == 1 and y == 1) or (x == 2 and y == 1):
        print("You can travel: (N)orth.")
    elif (x == 1 and y == 2 ) :
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif (x == 2 and y == 2) or (x == 3 and y == 3):
        print("You can travel: (S)outh or (W)est.")
    elif (x == 1 and y == 3 ) :
        print("You can travel: (E)ast or (S)outh.")
    elif (x == 2 and y == 3 ) :
        print("You can travel: (E)ast or (W)est.")
    elif (x == 3 and y == 2 ) :
        print("You can travel: (N)orth or (S)outh.")
    return x,y

#Function that gets current loc and wanted movement returns the resulting position

def wanted_movement(x,y,movement) :
    if (x == 1 and y == 1) or (x == 2 and y == 1):
        if movement == 'n' or movement == 'N' :
            y = y + 1
            return x , y          
    elif (x == 1 and y == 2 ) :
        if movement == 'n' or movement == 'N' :
            return x , y + 1
        if movement == 's' or movement == 'S' :
            return x , y - 1
        if movement == 'e' or movement == 'E' :
            return x + 1 , y
    elif (x == 2 and y == 2) or (x == 3 and y == 3):
        if movement == 'w' or movement == 'W' :
            return x - 1 , y
        if movement == 's' or movement == 'S' :
            return x , y - 1
    elif (x == 1 and y == 3 ) :
        if movement == 's' or movement == 'S' :
            return x , y - 1
        if movement == 'e' or movement == 'E' :
            return x + 1 , y
    elif (x == 2 and y == 3 ) :
        if movement == 'e' or movement == 'E' :
            return x + 1 , y
        if movement == 'w' or movement == 'W' :
            return x - 1 , y
    elif (x == 3 and y == 2 ) :
        if movement == 's' or movement == 'S' :
            return x , y - 1
        if movement == 'n' or movement == 'N' :
            return x , y + 1       
    print("Not a valid direction!")
    return x,y



# Main Program
x = 1
y = 1

while x != 3 or  y != 1 :
    x,y = tile_traveller(x,y)
    movement_str = input("Direction: ")
    x,y = wanted_movement(x,y, movement_str)

print("Victory!")


# Starts in 1,1

# while not winnging

# ask function where we are and get directions

# Tell program where you want to go

# function that performs action if possible and return the resulting position

