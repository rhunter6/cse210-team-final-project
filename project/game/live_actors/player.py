import arcade
from game.live_actor import LiveActor

class Player(arcade.SpriteCircle, LiveActor):
    def __init__(self, radius: int, color: "white", soft: bool = False):
        super().__init__(radius, color, soft=soft)
        
