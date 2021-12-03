import arcade
import constants
import Assets
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Exploding Checkers"
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
MOVEMENT_SPEED = 5


class ExplodingCheckers(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.tile_list = arcade.SpriteList()
        self.token_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        img_list = ["./Assets/tile-green.png","./Assets/tile-blue.png","./Assets/tile-red.png","./Assets/tile-orange.png"]
        for row in range(30,600,60):
            for col in range(30,800,60):
                img = img_list[random.randint(0, len(img_list) - 1)]
                self.tile = arcade.Sprite(img,constants.Scaling)
                self.tile.center_y = row
                self.tile.center_x = col
                self.all_sprites.append(self.tile)
                
                
        self.player = arcade.Sprite("./Assets/token.png")
        self.player.center_y = SCREEN_HEIGHT / 2
        self.player.left = 0
        self.all_sprites.append(self.player)

    def on_draw(self):
        
        arcade.start_render()
        self.all_sprites.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.all_sprites.update()
        

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, key_modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    """ Main function """
    game = ExplodingCheckers(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


main()

        
        