import arcade
from game.actor import Actor

class Wall(arcade.SpriteSolidColor, Actor):
    def __init__(self, width: int, height: int, color: "white"):
        super().__init__(width, height, color)