import random
import arcade
from game import constants
from game.game_board import GameBoard 

class SetupBoard(arcade.View):

    '''
    
    Used to update constants that will be used for the game and create the game board screen
    
    '''
    def __init__(self, difficulty):
        super().__init__()
        
        if difficulty == "easy":
            constants.ROW_COUNT = 10
            constants.COLUMN_COUNT = 10
            constants.MINECOUNT = 10
            constants.FLAGS_REMAINING = 10
            constants.GRID_SIZE = constants.ROW_COUNT * constants.COLUMN_COUNT
            self.add_bombs(constants.MINECOUNT, constants.GRID_SIZE)
            self.create_minefield(constants.GRID_SIZE)
        
        if difficulty == "medium":
            constants.ROW_COUNT = 16
            constants.COLUMN_COUNT = 16
            constants.MINECOUNT = 40
            constants.FLAGS_REMAINING = 40
            constants.GRID_SIZE = constants.ROW_COUNT * constants.COLUMN_COUNT
            self.add_bombs(constants.MINECOUNT,constants.GRID_SIZE)
            self.create_minefield(constants.GRID_SIZE)

        if difficulty == "hard":
            constants.ROW_COUNT = 16
            constants.COLUMN_COUNT = 30
            constants.MINECOUNT = 99
            constants.FLAGS_REMAINING = 99
            constants.GRID_SIZE = constants.ROW_COUNT * constants.COLUMN_COUNT
            self.add_bombs(constants.MINECOUNT, constants.GRID_SIZE)
            self.create_minefield(constants.GRID_SIZE)

        self.start_game()

           
    def add_bombs(self,mine_count, grid_size):
        while mine_count > 0:
                bomb_number = random.randint(0,grid_size - 1)
                if bomb_number in constants.MINE_LOCATIONS:
                    continue
                else:
                    #variable called mine locations
                    constants.MINE_LOCATIONS.append(bomb_number)
                    mine_count -= 1

    def create_minefield(self, grid_size):
        print(f"Gridsize: {grid_size}")
        for i in range(grid_size):
            constants.MINE_FIELD.append("n")

    def start_game(self):
        game_board = GameBoard()
        game_board.on_draw()
        self.window.show_view(game_board)