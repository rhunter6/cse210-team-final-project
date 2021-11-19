import arcade
from game import constants
from game.actor import Actor
from game.point import Point
from game.__init__ import Game

def main(screen):
    arcade.Window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
