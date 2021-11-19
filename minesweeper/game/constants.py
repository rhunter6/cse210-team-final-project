#Screen size

START_SCREEN_WIDTH = 800
START_SCREEN_HEIGHT = 600

# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 20
HEADER = 75
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

SCREEN_WIDTH = int((WIDTH + MARGIN) * COLUMN_COUNT + MARGIN)
SCREEN_HEIGHT = int((HEIGHT + MARGIN) * ROW_COUNT + MARGIN + HEADER)
SCREEN_TITLE = "Array Backed Grid Buffered Example"