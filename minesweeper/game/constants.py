import arcade
import os
#Screen size

START_SCREEN_WIDTH = 1055
START_SCREEN_HEIGHT = 650

# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 20
GRID_SIZE = 400
HEADER = 100

#number of mines
MINECOUNT = 0

#mine Locations
MINE_LOCATIONS = []

# Minefeild
MINE_FIELD = []

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

SCREEN_WIDTH = int((WIDTH + MARGIN) * COLUMN_COUNT + MARGIN)
SCREEN_HEIGHT = int((HEIGHT + MARGIN) * ROW_COUNT + MARGIN + HEADER)
SCREEN_TITLE = "Array Backed Grid Buffered Example"

PATH = os.path.dirname(os.path.abspath(__file__))

#Sprites 

default_sprite = arcade.Sprite (PATH+"/icons/default.png", image_height= HEIGHT - (MARGIN/2),image_width= WIDTH - (MARGIN/2))