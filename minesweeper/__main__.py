# from game.director import Director
import arcade
from game import constants
from game.menu_view import MenuView


def main():
    window = arcade.Window(constants.START_SCREEN_WIDTH, constants.START_SCREEN_HEIGHT, "Minesweeper")
    menu_view =  MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()