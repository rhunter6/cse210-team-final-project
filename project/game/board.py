import arcade
from arcade.color import *

# we need 6 rows
# we need 6 columns
row_count = 6 #changed names for clarity
column_count = 6 #changed names for clarity

#each grid location needs a width and height and margin
width = 100
height = 100

#margin sets space between each block and the edges of the screen thats seven margins
margin = 5


screen_width = (width + margin) * column_count + margin
screen_height =(height + margin) * row_count + margin
title = "Exploding Checkers"

class Board(arcade.Window):
    """ main board
        we need a two dimentional aray.  I think this makes cordinates? 

    """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.grid = []
        for row in range(row_count):
            self.grid.append([]) #an empty aray that holds each cell in the row

            for column in range(column_count):
                self.grid[row].append(0) #append to a cell, I don't know why this works. 
                                    #I didn't write this one.
        
        arcade.set_background_color(arcade.color.BLACK) #the white boxes will sit on the black

        self.grid_sprite_list = arcade.SpriteList()# used arcade academy for reference

        #make a list with colored sprites to rep each grid location
        for row in range(row_count):
            for column in range(column_count):
                #this is converting a two dimentional grid to a one dimentional sprite list
                #if you change it to a sprite list you can change things based on the list
                #not the coridinates. I think.. I'm not 100% clear yet.
                position = row * column_count + column
                if self.grid[row][column] == 1:
                    self.grid_sprite_list[position].color =arcade.color.PURPLE
                else:
                    self.grid_sprite_list[position].color = arcade.color.GREEN

    def on_draw(self):
        """ render screen"""

        #this must happen before you begin to draw
        arcade.start_render()

         #draw grid
         #this doesn't work the  way the way we need
        # for row in range(row_count):
        #     for column in range(column_count):
        #         #what color is box
        #         if self.grid[row][column] == 1:
        #             color = arcade.color.BLUE
        #         else:
        #             color = arcade.color.WHITE

                #draw the box
        arcade.draw_rectangle_filled( width, height, color)
        
#move to different class
    def on_mouse_press():
        """ called when player presses a key up, down, left, right. 
        
        """
        pass
def main():

    window = Board(screen_height,screen_width, title)
    arcade.run()
if __name__ == "__main__":
    main()
#I was trying this out in a different folder.