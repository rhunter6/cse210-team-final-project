import arcade

class Platform(arcade.SpriteSolidColor):
    def __init__(self, width: int, height: int, color="red"):
        super().__init__(width, height, color)