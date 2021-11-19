import arcade
from arcade.color import RED
from game import constants
from arcade.draw_commands import draw_rectangle_filled
from arcade.text_pyglet import draw_text
'''
# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (constants.WIDTH + constants.MARGIN) * constants.COLUMN_COUNT + constants.MARGIN
SCREEN_HEIGHT = (constants.HEIGHT + constants.MARGIN) * constants.ROW_COUNT + constants.MARGIN + constants.HEADER
SCREEN_TITLE = "Lets play Minesweeper!"
'''
class GameView(arcade.View):
    """ Manage the 'game' view for our program. """

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        
        # One dimensional list of all sprites in the two-dimensional sprite list
        self.grid_sprite_list = arcade.SpriteList()

        # This will be a two-dimensional grid of sprites to mirror the two
        # dimensional grid of numbers. This points to the SAME sprites that are
        # in grid_sprite_list, just in a 2d manner.
        self.grid_sprites = []

        # Create a list of solid-color sprites to represent each grid location
        for row in range(constants.ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(constants.COLUMN_COUNT):
                x = column * (constants.WIDTH + constants.MARGIN) + (constants.WIDTH / 2 + constants.MARGIN)
                y = row * (constants.HEIGHT + constants.MARGIN) + (constants.HEIGHT / 2 + constants.MARGIN)
                #Use Arcade.sprite
                sprite = arcade.SpriteSolidColor(constants.WIDTH, constants.HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)# Create variables here

    def on_draw(self):
            """
            Render the screen.
            """

            # This command has to happen before we start drawing
            arcade.start_render()

            self.grid_sprite_list.draw()
            draw_rectangle_filled(constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT - (constants.HEADER / 2),constants.WIDTH * 4 ,constants.HEIGHT * 2,RED)
        
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (constants.WIDTH + constants.MARGIN))
        row = int(y // (constants.HEIGHT + constants.MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({column},{row})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        
        if row < constants.ROW_COUNT and column < constants.COLUMN_COUNT:
            
            if button == arcade.MOUSE_BUTTON_LEFT:
                # Flip the location between 1 and 0.
                if self.grid_sprites[row][column].color == arcade.color.WHITE:
                    self.grid_sprites[row][column].color = arcade.color.RED_DEVIL
                else:
                    self.grid_sprites[row][column].color = arcade.color.WHITE

            if button == arcade.MOUSE_BUTTON_RIGHT:

                # Flip the location between 1 and 0.
                if self.grid_sprites[row][column].color == arcade.color.WHITE:
                    self.grid_sprites[row][column].color = arcade.color.OLD_GOLD
                else:
                    self.grid_sprites[row][column].color = arcade.color.WHITE

 
 
 
 
    '''
    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_text("Game - press SPACE to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_WIDTH / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    '''
    '''
    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.SPACE:
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)
    '''