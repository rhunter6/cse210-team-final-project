from game.live_actor import LiveActor
from game import constants
import arcade

class Bullet(arcade.SpriteCircle, LiveActor):
    def __init__(self, direction, radius =5, color="red", soft: bool = False):
        super().__init__(radius, color, soft=soft)
        self.set_orientation(direction)

    def move(self):
        if self._orientation == "UP":
            self.change_y = constants.BULLET_SPEED
        elif self._orientation == "DOWN":
            self.change_y = -constants.BULLET_SPEED
        elif self._orientation == "LEFT":
            self.change_X = -constants.BULLET_SPEED
        elif self._orientation == "RIGHT":
            self.change_X = constants.BULLET_SPEED