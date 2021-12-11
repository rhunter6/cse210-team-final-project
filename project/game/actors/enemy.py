import arcade
import random
from game.actor import Actor
from game import constants

#class Enemy(arcade.SpriteSolidColor, Actor):
#    def __init__(self, width: int, height: int, color):
#        super().__init__(width, height, color)
#        self.set_hp(10)

class Enemy(arcade.Sprite, Actor):

    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture: str = None, angle: float = 0):
        
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle)

        self.set_hp(10)
        self.change_x = constants.ENEMY_SPEED * random.choice([-1, 1])

    def reverse_direction(self):
        self.change_x = -(self.change_x)