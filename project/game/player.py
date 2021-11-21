import arcade

class Player(arcade.Window):

    """ this is the player it moves accross the gameboard from left to right
     the mouse clicks on a square and that square randomly chooses if you live or
     die. if you live you move forward. """

    def __init__(self):
        super().__init__(width, height, title)
        
        self.player.sprite = arcade.SpriteList()


    pass