import arcade
from game.point import Point
from game.actor import Actor

class Platform(arcade.SpriteSolidColor, Actor):
    def __init__(self, width: int, height: int, color="red"):
        super().__init__(width, height, color)