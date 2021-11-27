from game.actor import Actor
from game import constants
import arcade

class Bullet(arcade.SpriteCircle, Actor):
    def __init__(self, radius =5, color="red", soft: bool = False):
        super().__init__(radius, color, soft=soft)

    def move(self):
        if self._orientation == "UP":
            self.change_y = constants.BULLET_SPEED
        elif self._orientation == "DOWN":
            self.change_y = -constants.BULLET_SPEED
        elif self._orientation == "LEFT":
            self.change_X = -constants.BULLET_SPEED
        elif self._orientation == "RIGHT":
            self.change_X = constants.BULLET_SPEED

    def set_orientation(self, orientation):
        self._orientation = orientation