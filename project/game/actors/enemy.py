import arcade
from game.actor import Actor

class Enemy(arcade.SpriteCircle, Actor):
    def __init__(self, radius: int, color, soft: bool = False):
        super().__init__(radius, color, soft=soft)

        self._orientation = "RIGHT"
        
