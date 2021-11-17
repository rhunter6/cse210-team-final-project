import arcade
from arcade.color import WHITE

# we need 6 rows
# we need 6 columns
rows = 6
columns = 6

#each grid location needs a width and height and margin
width = 100
height = 100

#margin sets space between each block and the edges of the screen thats seven margins
margin = 5


screen_width = 635 # maybe put these in a constants file
screen_height = 635 #these should be (width + height) * colum or row + margin
title = "Exploding Checkers"
class Board(arcade.Window):
    """ main board
        we need a two dimentional aray.  I think this makes cordinates? 

    """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.grid = []
        for row in range(rows):
            self.grid.append([]) #an empty aray that holds each cell in the row

        for column in range(columns):
            self.grid[row].append(0) #append to a cell, I don't know why this works. 
                                    #I didn't write this one.
        


        arcade.set_background_color(arcade.color.WHITE)

        self.grid_sprite_list = arcade.SpriteList()# used arcade academy for reference

        #make a list with colored sprites to rep each grid location
        for row in range(rows):
            for column in range(columns):
                #this is converting a two dimentional grid to a one dimentional sprite list
                #if you change it to a sprite list you can change things based on the list
                #not the coridinates. I think.. I'm not 100% clear yet.
                position = row * columns + column
                if self.grid[row][column].color == 0:
                    self.grid_sprite_list[position].color =arcade.color.WHITE
                else:
                    self.grid_sprite_list[position].color = arcade.color.BLACK

    def on_draw(self):
        """makes (renders) screen
        
        """
        arcade.start_render()

    def on_mouse_press():
        """ called when player presses a key up, down, left, right. 
        
        """
        pass
arcade.run()