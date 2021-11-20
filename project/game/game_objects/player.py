import arcade

class Player(arcade.SpriteCircle):
    def __init__(self, radius: int, color: "white", soft: bool = False):
        super().__init__(radius, color, soft=soft)