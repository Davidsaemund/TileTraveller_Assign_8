# Assignment 8 
# Tile Traveler
# Program that moves NORTH, SOUTH, WEST and EAST in a 3v3 tile plan.


#Function that gets your current loc and tells you what options you have

def tile_traveller(location):
    if location == 1.1 or location == 2.1:
        print("You can travel: (N)orth")
    elif location == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif location == 2.2 or location == 3.3:
        print("You can travel: (S)outh or (W)est.")
    elif location == 1.3:
        print("You can travel: (S)outh or (E)ast.")
    elif location == 2.3:
        print("You can travel: (E)ast or (W)est.")
    elif location == 3.2:
        print("You can travel: (N)orth or (S)outh")
    elif location == 3.1:
        print("Victory!")
    return location

#Function that gets current loc and wanted movement returns the resulting position



# Main Program

location = 1

while location!= 9:
    if 

# Starts in 1,1

# while not winnging

# ask function where we are and get directions

# Tell program where you want to go

# function that performs action if possible and return the resulting position

