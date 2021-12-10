import arcade
from game.director import Director
from game import constants

<<<<<<< HEAD

def main(screen):
    pass
=======
def main():
    """ Main function """
    window = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup()
    arcade.run()
>>>>>>> master

if __name__ == "__main__":
    main()  