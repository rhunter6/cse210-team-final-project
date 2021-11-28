from game.checkers import ExplodingCheckers
import constants
import arcade

class Director:

    def __init__(self):
        """
        """
        self._keep_playing = True
        self.cast = {}


    def StartGame(self):
        ExplodingCheckers(constants.MaxX,constants.MaxY,constants.ScreenTitle)
