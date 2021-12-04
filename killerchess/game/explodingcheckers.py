import arcade
from game.tiles import tile
import constants
import Assets
import random
import asyncio

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
        img_list = [constants.green_tile, constants.blue_tile, constants.red_tile, constants.orange_tile ]
        color_list = [arcade.color.GREEN, arcade.color.BLUE,arcade.color.RED,arcade.color.ORANGE]
        for row in range(30,600,60):
            for col in range(90,800,60):
                new_rand = random.randint(0, len(img_list) - 1)
                img = img_list[new_rand]
                colo = color_list[new_rand]
                self.tile = arcade.Sprite(img, constants.Scaling)
                self.tile._set_color(colo)
                self.tile.center_y = row
                self.tile.center_x = col
                self.tile_list.append(self.tile)
                
                
        self.player = arcade.Sprite("./killerchess/Assets/token.png")
        self.player.center_y = SCREEN_HEIGHT / 2
        self.player.center_x = 30
        self.player.boundary_bottom = self.player.center_y - 10
        self.player.boundary_top = self.player.center_y + 10
        self.player.boundary_left = self.player.center_x - 10
        self.player.boundary_right = self.player.center_x + 10
        self.all_sprites.append(self.player)

    def on_draw(self):
        
        arcade.start_render()
        self.tile_list.draw()
        self.player.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.player._get_center_x() >= SCREEN_WIDTH - 10:
            self.win_screen = arcade.Sprite("./killerchess/Assets/R.png")
            self.win_screen.set_position(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
            self.tile_list.append(self.win_screen)
  
        
        for i in range(0, len(self.tile_list) - 2):
            if arcade.check_for_collision(self.player, self.tile_list[i]) == True:
                self.check_tile(self.tile_list[i])
                
        self.player.update()
        self.tile_list.update()
        
    def check_tile(self,tile):
        if tile._get_color() == arcade.color.GREEN:
            self.lose_screen = arcade.Sprite("./killerchess/Assets/youdied.png")
            self.lose_screen.set_position(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
            self.tile_list.append(self.lose_screen)
            
            arcade.schedule(arcade.close_window, 3)
            

     
        

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

        
        