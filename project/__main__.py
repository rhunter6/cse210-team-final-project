import arcade
from game.director import Director
from game import constants

def main():
    """ Main function """
    window = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()  