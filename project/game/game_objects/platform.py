import arcade

class Platform(arcade.SpriteSolidColor):
    def __init__(self, width: int, height: int, color: "white"):
        super().__init__(width, height, color)