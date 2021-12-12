import arcade
from game import constants

class ExplosionCheck:
    '''
    Checks to see if the grid box that was checked is a bomb
o	If it is not a bomb it will also check to see how many bombs are touching the square and return that number

    '''

    def check_right(location):
        
        if constants.MINE_FIELD[location] == "f":
            constants.MINE_FIELD[location] = "?" 
            constants.FLAGS_REMAINING += 1 
            print(f"TESTING location {location}") # FOR TESTING REMOVE
            return "?"

        if constants.MINE_FIELD[location] == "?":
            constants.MINE_FIELD[location] = "n" 
            print(f"TESTING location {location}") # FOR TESTING REMOVE
            return "n"
        
        while constants.FLAGS_REMAINING > 0:
            if constants.MINE_FIELD[location] == "n":
                constants.MINE_FIELD[location] = "f"
                constants.FLAGS_REMAINING -= 1 
                print(f"TESTING location {location}") # FOR TESTING REMOVE
                return "f"

    def check_left(location, row, column): 
        print (f"Location: {location}, Row: {row}, Column: {column}") # FOR TESTING REMOVE
        #is it a bomb?
        
        if constants.MINE_FIELD[location] == "f":
            return "flag"

        elif location in constants.MINE_LOCATIONS:
            return "bomb"

        else:
        
            lower_row = row - 1
            left_column = column -1       
            bombs_counted = ExplosionCheck.check_adjacent(location, lower_row, left_column)
            return str(bombs_counted)
            

    def check_adjacent(location, lower_row, left_column):
        #print(f"LR: {lower_row} LC: {left_column}")

        #set variables
        bombs_counted = 0

        for row in range(3):
            for column in range(3):
                #print(lower_row,left_column)
                
                # are we still on the board?
                if lower_row >= 0 and lower_row <= constants.ROW_COUNT -1 and left_column >= 0 and left_column <= constants.COLUMN_COUNT -1:
                    current_location = int((lower_row * constants.COLUMN_COUNT + left_column))
                    if current_location != location:
                        #print(f"Current: {current_location} Clicked: {location}")
                        if current_location in constants.MINE_LOCATIONS:
                            bombs_counted += 1
                    else:
                        pass
                else:
                    pass
                left_column += 1
            left_column = left_column -3
            lower_row += 1

        return bombs_counted

        #is location on the board?

        '''
        JUST IN CASE
         for row in range(3):
            for column in range(3):
                print(lower_row,left_column)
                left_column += 1
            left_column = left_column -3
            lower_row += 1
        '''
        

    
