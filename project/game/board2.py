""" array backed grid
from learn.arcade.academy tutorial

"""
import random
import arcade
import player

# sets how many rows and collumns
row_count = 6
column_count = 6

#set width and height of each grid square
width = 100
height = 100

#set margins between cells black lines
margin = 5

#math to make screen dimentions taking each square plus the margins up and down
screen_width = (width + margin) * column_count + margin
screen_height =(height + margin) * row_count + margin

class Game(arcade.Window):
    """ main application class
    
    """
    def __init__(self, width, height):
        """ sets up application
        
        """
        super().__init__(width, height)

        #create a two dimentional array.  that is a list of lists.
        self.grid = []
        for row in range(row_count):
            #add empty array that will hold each cell
            self.grid.append([])
            for column in range(column_count):
                self.grid[row].append(0) #append a cell
        arcade.set_background_color(arcade.color.BLACK)
        # self.all_sprites = arcade.SpriteList()
        # self.player = arcade.Sprite("flower.png")
        
        # self.player.sprite = arcade.SpriteList()
        # self.player = arcade.Sprite("flower.png") #we should change this picture
        # self.player.center_y = self.height / 2
        # self.player.left = 15
        # self.all_sprites.append(self.player)


    def on_draw(self):
        """ render screen"""

        #this must happen before you begin to draw
        arcade.start_render()
         #draw grid
        for row in range(row_count):
            for column in range(column_count):
                #what color is box
                # if self.grid[row][column] == 1:
                #     color = arcade.color.GREEN
                # if self.grid[row][column] == 2:
                #     color = arcade.color.PURPLE
                # else:
                #     color = arcade.color.WHITE
                if self.grid[row][column]== 0:
                    color = arcade.color.WHITE
                if self.grid[row][column]== 1:
                    color = arcade.color.GREEN
                if self.grid[row][column] == 2:
                    color = arcade.color.PURPLE    
                #math to figure out were box is
                y = (margin +width) * column + margin+width // 2
                x = (margin + height) * row + margin +height // 2

                #draw the box
                arcade.draw_rectangle_filled(x,y, width, height, color)


    def on_mouse_press(self, x,y, button, modifiers):
        """ called when user presses a mouse button
        
        """
        #change the  x/y screencoordinates to grid coordinates
        row =x // (width + margin)
        column = y // (height + margin)

        print(f"click coordinated: ({x}, {y},).grid coordinates : ({row}, {column})")

        #make sure you are on grid. It is possible to  click in the upper right
        #corner in the margin and go to a grid location that doesn't exist #fix that later
        if row < row_count and column < column_count:
            print("hello")
            self.grid[row][column] = random.choice([1,2])
            if self.grid[row][column] == 1:
                print("Safe, move again")
                self.grid[row][column] = 1
                #play again
            if self.grid[row][column] ==2:
                print("bang you're dead")
                self.grid[row][column] = 2
                arcade.close_window() 
        

        #     if on_mouse_press() == 1:
        #         print("safe, move again")  
        #     if on_mouse_press() == 2:
        #         arcade.close_window()
        #     print("game over")    
    
def main():

    window = Game(screen_height,screen_width)
    arcade.run()
if __name__ == "__main__":
    main()

    



